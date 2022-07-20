#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <time.h>
#include <unistd.h>
#include <sys/wait.h>

#define BIN_SEM   0
#define BUFFER_EMPTY 1
#define BUFFER_FULL  2

#define DEC -1
#define INC 1

#define PRODUCERS_COUNT 3
#define CONSUMERS_COUNT 3

#define PRODUCERS_DELAY 3
#define CONSUMERS_DELAY 2

#define N 26 /*'Z' - 'A' */

#define PERMS S_IRWXU | S_IRWXG | S_IRWXO

struct 

int semId = -1;
int shmId = -1;

int *shm = NULL;
int *shm_producer_count = NULL;
int *shm_consumer_count = NULL;
int *shm_symbol_now = NULL;


int randint(int a, int b) 
{
	return a + rand() % (b - a + 1);
}

void v(int semId, int semnum)
{
	struct sembuf vbuf;
	vbuf.sem_num = semnum;
	vbuf.sem_op = INC;
	vbuf.sem_flg=SEM_UNDO;
	if (semop(semId,&vbuf,1)==-1) 
	{
		perror("semop"); 
		exit(1);
	}
}

void p(int semId, int semnum)
{
	struct sembuf pbuf;
	pbuf.sem_num = semnum;
	pbuf.sem_op = DEC;
	pbuf.sem_flg = SEM_UNDO;
	if (semop(semId, &pbuf, 1) == -1) 
	{
		perror("semop"); 
		exit(1);
	}
}

int semrel(int semId)
{
	return semctl(semId, 0, IPC_RMID, 0);
}

int shmrel(int semId)
{
    return shmctl(shmId, IPC_RMID, NULL);
}

void forkChildren(const int n, void (*func)(const int)) 
{
    for (int i = 0; i < n; ++i) 
    {
        const pid_t pid = fork();
        if (pid == -1) 
        {
            perror("Err: fork");
            exit(1);
        } 
        else if (pid == 0) 
        {
            if (func) 
                func(i);
            exit(1);
        }
    }
}

void waitChildren(const int n) 
{
    for (int i = 0; i < n; ++i) 
    {
        int status;
        const pid_t child_pid = wait(&status);
        if (child_pid == -1) 
        {
            perror("wait");
            exit(1);
        }
        if (WIFEXITED(status)) 
            printf("Process %d returns %d\n", child_pid, WEXITSTATUS(status));
        else if (WIFSIGNALED(status)) 
            printf("Process %d terminated with signal %d\n", child_pid, WTERMSIG(status));
        else if (WIFSTOPPED(status)) 
            printf("Process %d stopped due signal %d\n", child_pid, WSTOPSIG(status));
    }
}

void producer(const int id) 
{
    while(1) 
    {
        sleep(randint(0, PRODUCERS_DELAY));
        /* производит единичный объект*/
        /*ждет, когда освободится хотя бы одна ячейка буфера*/
        p(semId, BUFFER_EMPTY);
        /*ждет, когда или другой производитель или потребитель выйдет из критической секции*/
        p(semId, BIN_SEM);
        /* положить в буфер */
        int symbol = 'A' + *shm_producer_count % ('Z' - 'A');
        *(shm + *shm_producer_count) = symbol;
        printf("Producer-%d (pid %d) produces %c\n", id, getpid(), symbol);
        (*shm_producer_count)++;

        /* освобождение критической секции*/
        v(semId, BIN_SEM);
        /* инкремент количества заполненных ячеек */
        v(semId, BUFFER_FULL);
        
    }
}

void consumer(const int id) 
{
    while(1) 
    {
        sleep(randint(0, CONSUMERS_DELAY));
        /* выбирает из буфера единичный объект*/
        /*ждет, когда будет заполнена хотя бы одна ячейка буфера*/
        p(semId, BUFFER_FULL);
        /*ждет, когда или потребитель, или другой производитель выйдет из критической секции*/
        p(semId, BIN_SEM);
        /* взять из буфера */
        printf("\t\t\t\t\tConsumer %d (pid %d) consumes %c\n", id, getpid(), *(shm + *shm_consumer_count));
        (*shm_consumer_count)++;
        
        /* освобождение критической секции*/
        v(semId, BIN_SEM);
        /* инкремент количества пустых ячеек */
        v(semId, BUFFER_EMPTY);
    }
}

void initSemaphore() 
{
    /* два считающих семафора + один бинарный */
    semId = semget(IPC_PRIVATE, 3, IPC_CREAT | PERMS);
    
    if (semId == -1) 
    {
        perror("Err: semget");
        exit(1);
    }
    /*количество заполненных ячеек равно 0*/
    /*Все ячейки буфера изначально пусты */
    if (semctl(semId, BIN_SEM,   SETVAL, 1) == -1 ||
        semctl(semId, BUFFER_EMPTY, SETVAL, N) == -1 ||
        semctl(semId, BUFFER_FULL,  SETVAL, 0) == -1) 
    {
        perror("Err: semctl");
        exit(1);
    }
}

void createSharedMemory() 
{
    // (N + 3) * sizeof(int) - kích thước
    //IPC_PRIVATE - tạo seg mới
    shmId = shmget(IPC_PRIVATE, (N + 2) * sizeof(int), IPC_CREAT | PERMS);
    if (shmId == -1) 
    {
        perror("Err: shmget");
        exit(1);
    }
    shm = shmat(shmId, 0, 0);
    if (shm == (void *) -1) 
    {
        perror("Err: shmat");
        exit(1);
    }
    shm_producer_count = shm;
    shm_consumer_count = shm + 1;
    *shm_producer_count = 0;
    *shm_consumer_count = 0;
    shm = shm + 2;
}

int main() 
{
    initSemaphore();
    createSharedMemory();

    forkChildren(PRODUCERS_COUNT, producer);
    forkChildren(CONSUMERS_COUNT, consumer);

    waitChildren(PRODUCERS_COUNT + CONSUMERS_COUNT);

    shmrel(semId);
    semrel(semId);
}

