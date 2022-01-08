1. How many states could has a process in Linux?

Running, Sleeping, Uninterruptable sleep, Stopped, Zombie

2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.

![image](https://user-images.githubusercontent.com/46942305/148648681-e07975ef-2b05-462a-b584-1798989c04fd.png)

3. What is a proc file system?

Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down.
It contains useful information about the processes that are currently running, it is regarded as control and information center for kernel.

4. Print information about the processor (its type, supported technologies, etc.).

![image](https://user-images.githubusercontent.com/46942305/148649169-ad639906-258a-49c8-892f-e97e428f81e1.png)

5. Use the ps command to get information about the process. The information should be as
follows: the owner of the process, the arguments with which the process was launched for
execution, the group owner of this process, etc.

![image](https://user-images.githubusercontent.com/46942305/148649970-94e8482a-5cdd-4f88-a315-035d5f0b0fb3.png)

6. How to define kernel processes and user processes?

processes started by the user are user processes, all other are kernel processes

7. Print the list of processes to the terminal. Briefly describe the statuses of the processes.
What condition are they in, or can they be arriving in?

![image](https://user-images.githubusercontent.com/46942305/148651427-3be1ac52-e32f-455e-8bb4-a1decd7157a7.png)

 S  --  Process Status
           The status of the task which can be one of:
               D = uninterruptible sleep
               I = idle
               R = running
               S = sleeping
               T = stopped by job control signal
               t = stopped by debugger during trace
               Z = zombie
               
8. Display only the processes of a specific user.

![image](https://user-images.githubusercontent.com/46942305/148651707-b6c1d9af-6256-4066-934d-af4140d7aff2.png)

9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?

ps, top, htop

10. What information does top command display?

![image](https://user-images.githubusercontent.com/46942305/148651673-c5121d05-5a9c-4a69-97a3-dd59da6a774d.png)

11. Display the processes of the specific user using the top command.

![image](https://user-images.githubusercontent.com/46942305/148651808-5232f327-b366-479c-92ad-a7216ed07394.png)

12. What interactive commands can be used to control the top command? Give a couple of examples.

<Shift>+<N> — sort by PID;
<Shift>+<P> — sort by CPU usage;
<Shift>+<M> — sort by Memory usage;
<Shift>+<T> — sort by Time usage;
<Shift>+<Z> — change colors;
<c> - display absolute path of command;
 
13. Sort the contents of the processes window using various parameters (for example, the
amount of processor time taken up, etc.)

![image](https://user-images.githubusercontent.com/46942305/148651920-717d5364-5656-4e2e-af09-757312ccc961.png)

14. Concept of priority, what commands are used to set priority?
  
nice, renice

15. Can I change the priority of a process using the top command? If so, how?

Once given top command, press r. Give PID value of the process you want to change the process value. Give renice value (from -20 to +19)
Nice value of -20 means highest priority value and +19 means lowest priority value. 0 is by default value.
  
16. Examine the kill command. How to send with the kill command process control signal? Give an example of commonly used signals
