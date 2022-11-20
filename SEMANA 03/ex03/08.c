#include <signal.h>
#include <string.h>
#include <sys/sys/types.h>
#include <sys/wait.h>

sig_atomic_t child_exit_status;

void clean_up_child_process (int signal_number)
{
    int status;
    wait (&status);
    child_exit_status = status;
}

int main()
{
   struct sigaction sigchild_action;
   memset (&sigchld_action, 0, sizeof(sigchld_action));
   sigchld_action.sa_handler = &clean_up_child_process;
   sigaction (SIGCHLD, &sigchld_action, NULL);

    return 0;
}
