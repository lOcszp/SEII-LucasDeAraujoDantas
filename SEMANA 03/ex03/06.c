int main ()
{
    int child_status;

    char* arg_list[] = {
        "ls",
        "-l",
        "/",
        NULL
    };

    spawn("ls", arg_list);

    if (WIFEXITED(child_status))
        printf("the child process exited normally, with the exit code %d\n", WEXITSTATUS (child_status));

    else
        printf("the child process exited abnormally\n");

    return 0;
}
