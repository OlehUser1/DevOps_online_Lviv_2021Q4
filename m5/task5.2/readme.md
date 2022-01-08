1) Analyze the structure of the /etc/passwd and /etc/group file, what fields are
present in it, what users exist on the system? Specify several pseudo-users, how
to define them?

/etc/passwd Username/Placeholder character for password/UID/GID/Description/Home directory/Login shell
/etx/group group_name/password/GID/group List
pseudo-users uid/gid 1-999

![image](https://user-images.githubusercontent.com/46942305/148612745-8654fddb-3f83-4bd6-a834-8cc52045cbdf.png)

2) What are the uid ranges? 

0-65535, 0- root, 1-999- pseudo-users, 1000+ - regular users

  What is UID?
 
user identifier

  How to define it?
 
UIDs are stored in the /etc/passwd file

3) What is GID? 

group identifier

  How to define it?

GIDs are stored in the /etc/groups file

4) How to determine belonging of user to the specific group?

command groups

5) What are the commands for adding a user to the system? 

commands useradd and adduser

What are the basic parameters required to create a user?

password, home directory, uid, gid and etc

6) How do I change the name (account name) of an existing user?

usermod -l newusername oldusername

7) What is skell_dir? What is its structure?

Skel_dir is a special directory that contain all necessary files and directories which will be copied to new user's home directory.

.bash_logout .bashrc .profile

8) How to remove a user from the system (including his mailbox)?

userdel -r username

9) What commands and keys should be used to lock and unlock a user account?

passwd - l to lock, passwd -u to unlock

10) How to remove a user's password and provide him with a password-free login for subsequent password change?

passwd -d

11) Display the extended format of information about the directory, tell about the information columns displayed on the terminal.

![image](https://user-images.githubusercontent.com/46942305/148616701-b4d1a40b-094e-4227-b967-346134daca3a.png)

access rights/number of links per file/owner/group/size/created time/name

12) What access rights exist and for whom (i. e., describe the main roles)? Briefly describe the acronym for access rights.

-r read(4), -w write(2), -x execute(1) 

owner, group, other

13) What is the sequence of defining the relationship between the file and the user?

all information about the file can be found with the command ls -l

14) What commands are used to change the owner of a file (directory), as well
as the mode of access to the file? Give examples, demonstrate on the terminal.

![image](https://user-images.githubusercontent.com/46942305/148618943-52ba391b-f530-4aed-b5db-9a7cee4bba28.png)

15) What is an example of octal representation of access rights? Describe the
umask command.

777 - full access for everyone (4 read, 2 write, 1 execute: 4+2+1=7)

umask command sets the mask of rights for new files and directories

![image](https://user-images.githubusercontent.com/46942305/148620546-30e442c2-5592-4f62-8230-3e539d7410e3.png)

16) Give definitions of sticky bits and mechanism of identifier substitution. Give
an example of files and directories with these attributes.

Sticky bit is special attribute that affects user access rights.(only the file owner, folder owner, or root can rename or delete the file)

![image](https://user-images.githubusercontent.com/46942305/148621663-348a83a5-6af4-4f3c-a946-6d2a3e233fcd.png)

17) What file attributes should be present in the command script?

-x execute 
