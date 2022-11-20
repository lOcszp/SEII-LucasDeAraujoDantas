#include <stdio.h>
#include <unistd.h>

int main ()
{
    printf("O ID de processo eh %d\n", (int) getpid());
    printf("O processo pai ID eh %d\n", (int) getppid());


    return 0;
}
