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

.bash_logout .bashrc .bash_profile

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
