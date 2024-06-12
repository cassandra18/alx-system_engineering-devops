alx-system_engineering-devops
=============================

1.  ### Introduction to basic shell commands, e.g.,

    a. Command to list files or directories:

    `ls`

    b. Command to go back home:

    `cd ~`

2.  ### Introduction to shell permissions, e.g.,

    a.  Command that prints the username of the current user:

    `whoami`

    b.  Script that creates an empty file called `hello`:

     ```
        #!/usr/bin/bash
        touch hello
     ```

3. ### Input/Output redirection

The commands mentioned earlir print their output on the display. By using special notations, we can redirect the output of many commands to files, devices and even output of other commands. <bold> Example <bold>

    a. To redirect standard output to a file, the ">" character is used like this:
       
       `ls > file_list.txt`

   b. Each time the command above is repeated, file_list.txt is overwritten from the beginning with the output of the command ls. To have the new results appended to the file instead, we use ">>" like this:
   
       `ls >> file_list.txt`

   c.  To redirect standard input from a file instead of the keyboard, the "<" character is used like this:
   
       `sort < file_list.txt`

   d. The most useful and powerful thing we can do with I/O redirection is to connect multiple commands together to form what are called pipelines.
    With pipelines, the standard output of one command is fed into the standard input of another. Here is a very useful example:
    
         ` ls -l | less`
