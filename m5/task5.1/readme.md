PART1
1) Log in to the system as root. 

![image](https://user-images.githubusercontent.com/46942305/148602554-43fe6081-46b0-4bfe-b14a-d2b9dee59c37.png)

2) Use the passwd command to change the password. Examine the basic parameters of the command. 

![image](https://user-images.githubusercontent.com/46942305/148602664-4cfd9901-44e2-4975-ae0b-b172c2217a34.png)

What system file does it change?
/etc/shadow

3) Determine the users registered in the system, as well as what commands they execute. 

![image](https://user-images.githubusercontent.com/46942305/148602823-3c0b8805-8a2e-40fe-bb13-584390951c9d.png)

What additional information can be gleaned from the command execution?
IP, login time

4) Change personal information about yourself.

![image](https://user-images.githubusercontent.com/46942305/148603092-1c4d1b43-8e6d-4dff-b7cf-7e392b0c55d2.png)

5) Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two
keys for these commands. Give examples.

command chfn with -f key change user's full name and with -h key change user's home phone number

6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.

![image](https://user-images.githubusercontent.com/46942305/148603476-0c358d0b-e682-48c9-b5c4-90af1a0bf0f8.png)

![image](https://user-images.githubusercontent.com/46942305/148603596-019df012-0352-482e-9dd1-238071772dcd.png)

7) Describe in plans that you are working on laboratory work 1. Tip: You should
read the documentation for the finger command.

![image](https://user-images.githubusercontent.com/46942305/148603709-818e6970-c665-42cb-b43a-15814b44edf9.png)

8) List the contents of the home directory using the ls command, define its files
and directories.

![image](https://user-images.githubusercontent.com/46942305/148603847-9e94dda4-8bf4-4396-b63c-568f2e4788ec.png)

PART2

1) Examine the tree command. Master the technique of applying a template, for
example, display all files that contain a character c, or files that contain a
specific sequence of characters. List subdirectories of the root directory up to
and including the second nesting level.

![image](https://user-images.githubusercontent.com/46942305/148604308-db9b0870-d2fa-4fd1-b6c7-d4c6404c5071.png)

![image](https://user-images.githubusercontent.com/46942305/148604379-53df71a0-f9ba-4fb6-8857-ab8ccb365a4c.png)

2) What command can be used to determine the type of file (for example, text or binary)?

![image](https://user-images.githubusercontent.com/46942305/148604502-65f6d879-e614-47a5-8be9-7ba74e58adca.png)

3) Master the skills of navigating the file system using relative and absolute paths.

![image](https://user-images.githubusercontent.com/46942305/148604858-baa40bd7-563a-4481-a910-e81193a61531.png)

How can you go back to your home directory from anywhere in the filesystem?
cd ~

4) Become familiar with the various options for the ls command. Give examples
of listing directories using different keys. 

![image](https://user-images.githubusercontent.com/46942305/148604972-76b42581-abf8-4cb1-b221-f6ce503088c4.png)

Explain the information displayed on the terminal using the -l and -a switches.

access rights/number of links per file/owner/group/size/created time/name

5) Perform the following sequence of operations:
- create a subdirectory in the home directory;
- in this subdirectory create a file containing information about directories
located in the root directory (using I/O redirection operations);
- view the created file;
- copy the created file to your home directory using relative and absolute
addressing.
- delete the previously created subdirectory with the file requesting removal;
- delete the file copied to the home directory.

![image](https://user-images.githubusercontent.com/46942305/148605980-b231735c-cead-49ed-aab0-8453773416b2.png)

6) Perform the following sequence of operations:
- create a subdirectory test in the home directory;
- copy the .bash_history file to this directory while changing its name to
labwork2;
- create a hard and soft link to the labwork2 file in the test subdirectory;
- how to define soft and hard link, what do these
concepts;
- change the data by opening a symbolic link. What changes will happen and
why
- rename the hard link file to hard_lnk_labwork2;
- rename the soft link file to symb_lnk_labwork2 file;
- then delete the labwork2. What changes have occurred and why?

![image](https://user-images.githubusercontent.com/46942305/148606673-5a93bade-d242-4438-85e3-a90f8d1895a0.png)

7) Using the locate utility, find all files that contain the squid and traceroute sequence.

![image](https://user-images.githubusercontent.com/46942305/148606800-ee1d96b2-ec21-4c90-8a91-43fa6820cdd8.png)

8) Determine which partitions are mounted in the system, as well as the types of these partitions.

fdisk -l

9) Count the number of lines containing a given sequence of characters in a given file.

![image](https://user-images.githubusercontent.com/46942305/148607703-aa28f011-5dc1-4332-908c-266e7b56f03a.png)

10) Using the find command, find all files in the /etc directory containing the
host character sequence

![image](https://user-images.githubusercontent.com/46942305/148608053-2de0f8cd-3fa6-49a8-9c02-4aecfcc21690.png)

11) List all objects in /etc that contain the ss character sequence. 
![image](https://user-images.githubusercontent.com/46942305/148608613-f4de9ed5-e14e-4e1d-a143-45470f9841de.png)

12) Organize a screen-by-screen print of the contents of the /etc directory. Hint:
You must use stream redirection operations.

![image](https://user-images.githubusercontent.com/46942305/148610067-f4fc0573-0807-4bbf-b5da-ea78c7ea5b7b.png)

13) What are the types of devices and how to determine the type of device? Give
examples.

Character Device, Block Device, Pipe Device, Socket Device

14) How to determine the type of file in the system

command file

what types of files are there?

simple files for storing information, special files for devices and tunnels, directories

15) List the first 5 directory files that were recently accessed in the /etc directory.

![image](https://user-images.githubusercontent.com/46942305/148611113-b3376cba-1429-463a-b491-a1d999f35102.png)


