# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > mkdir <directory name> - makes new directory
> > mv <original file name> <new file name> -
> > grep "<text>" <file> - output occurrences of text inside file
> > touch <filename> - create new file
> > cd .. - change directory to parent level
> > rm <filename> - delete file
> > head <filename> - show first 10 lines of file
> > tail -F <filename> - live output last 10 lines of file
> > !! - repeat last command
> > find . -name "<text>" - find files by text in current directory
> > !find - run last executed find command
> > ls - list files
> > cp <file> <directory> - copy file to directory
> > curl -0 <url> - download file via http or ftp
> > ping - ping host and display status
> > less <file> - output contents of file (supports pagination)
> > chmod 755 <file> - change file permissions to 755

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls - no options, list files in bare format. no details provided
> > ls -a - list all files including hidden files
> > ls -l - shows file/directory size, modified date and time, file/folder name, owner of file and permission
> > ls -lh - similar to -l, but with human-readable file sizes
> > ls -lah - combination of -a and -lh
> > ls -t - shows latest modification date as last
> > ls -Glp - G adds color and p adds a slash (/) if a file is a directory

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -r - reverse output order
> > ls -F - same effect as -p
> > ls -R - also displays subdirectories
> > ls -u - show by file access time
> > ls -C - display in columnar format

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes a big list or arguments and divides it into a smaller list
> > received from a standard input. For example, find . -name "*bash*" | xargs
> > in the etc/ folder will return the multiline output into a single line.
> > ./bash.bashrc
> > ./bash.bash_logout
> > ./defaults/etc/bash.bashrc
> > ./defaults/etc/bash.bash_logout

> > ./bash.bashrc ./bash.bash_logout ./defaults/etc/bash.bashrc ./defaults/etc/bash.bash_logout
