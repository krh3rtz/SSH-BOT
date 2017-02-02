 -------
# SSH-BOT
 -------
SSH-BOT is an application intended to be used as a manager for
Secure Shell connections. It has been built to help system administrators while
managing several servers at the same time.

This tool handles connections in three different ways. The first one is 
accomplished by using custom threaded SSH connections. This type of shells are for mere
visualization purposes (verify port status, check non privileged required files). The second
one is by pure SSH system shells. The main function of these connections, is to 
procede with actions that need su/sudo/root commands (modify files, verify specific
tasks in each one of the systems, etc). The last type, is similar to the second one. The
main difference is that all connections made with this third option need to be created
at the moment.

The way sessions are created (regarding the first way to connect hosts) is by using a credentials 
file (-F credentials_file). SSH-BOT will read the credentials from this file and will atempt to establish 
a custom threaded SSH connection with the remote servers. If everything goes well, this status will be added to the
log file as well as if anything goes wrong, providing the host (in dotted decimal notation)
and the credentials used while atempting log-in. 

The structure of this file is:

	eg.  127.0.0.1|ssh_user|pass

NOTE: The seclusion is accomplished by the '|' (pipe) symbol with no spaces in between each parameter. 
	It is recomended to use vi to edit this file. Optionally, you can use the last version of 
	PASS-CRYPT to crypt your credentials before and after using SSH-BOT.


[+] To start the application:

	sudo ./ssh_botnet.py -F credentials_file.txt


# [*] OPTIONS [*]

	The menu has 7 options:

 # 1) Single or multi bot interaction:

	This is the first type of connection above specified. If you type 'exit' or 'back',
	the sessions will not be closed but you will rather be forwarded to main menu. Every
	command send though this interface, will show the output of every host provided.

	If you want to interact with one host, simply provide the ID. Otherwise, if the interaction
	is with several hosts, you would provide a list of IDs separated by a comma:

	eg. 0,1,2,3

	NOTE: To choose all bots at the same time, type the handicap 'all'.

 # 2) Disconnect bot:

	This options recieves the ID corresponding to the bot you wish to disconnect.
	There will be register of this in the log file.

 # 3) Add single bot:
	
	With a host (in dotted decimal notation), user and password, you can add a new host (bot) 
	to the list. This connection will be saved in the log file.
	
	eg. 192.168.1.50,ssh_user,passwd
	
	NOTE: separate them with a comma. There will be register of this in the log file.

 # 4) Win server connection:

	A pure SSH connection is established. In contrast with the last option, you just need 
	to provide host (in dotted decimal notation) and user. Once in the newly open
	terminal, you enter the password. A peculiar thing is that you need to provide a OS 
	version	(Win os version). If provided, an algorithm will detect the version of the 
	remote os. This information will be logged.

	eg. 127.0.0.1,ssh_user
	Password: XXXXX

	For the version:

	eg.
	[*] Give me the version: 1.2.345

# 5) Specific actions -> used for actions that need su/sudo:
	
	This is similar to the last option, the difference is that ID(s) need to be provided.
	This means that a pure SSH will be established using the credentials of the already 
	connected hosts. This interaction is done when su/sudo commands are to be used.
	Connections will also be logged.

	eg. 0,1,2,3

	For all bots:

	eg. all
	
# 6) Refresh botlist:

	Refreshes the hosts list. The main task is to show the administrator host, including
	the automatic detection of the remote OS and some kernel information. This part of the
	interface, has all the IDs used to interact with all hosts.

# 7) Check log file:
	
	A quick view to the current logfile.


 NOTE:  In order to exit the application, typing 'exit' will help.


# MORE INFORMATION:

[+] All the log files are saved after exiting SSH-BOT. They are held under 'os_admin/' folder.
    There are two types of log files: log and sys_list. The first one keeps all the information
    regarding connections. The second one contains the last hosts list before exiting SSH-BOT. 
    Although they are different, they are tagged with date and time of disconnection from the platform.

	eg.  logs_01-02-2017_06:26:56  sys_list_01-02-2017_02:16:31


   NOTE: In case you need to verify connections made on certain date, yet there are many log files,
	 there is a bash script that will simply ask you for a filter and will automatically give you
	 all logs with that filter. This simplifies the way to visualize log files. This script is under
	 'filtered/'.

[+] To avoid problems with this application, make sure you are on a linux machine and that
    you have installed sshpass. In Debian like systems simply:

	apt-get install sshpass

    This has been developed on Python 3.4. For this reason you need to have installed the library pexpect.
    A simple way to install it is by using 'pip3'. Simply:
	
	pip3 install pexpect

   The parsing of options is done by using argparse. You also need it installed:

	pip3 install argparse 


	Created by: 

==================================================================
| ##   ## ######## ##   ##   ###### ########  ######## ########   |
| ##  ##  ##    ## ##   ##       #  ##    ##     ##          #    |
| ## ##   ##    ## ##   ##      ##  ##    ##     ##         #     |
| ## ##   ######   #######        # ######       ##       #       |
| ##  ##  ##   ##  ##   ##        # ##   ##      ##     #         |
| ##   ## ##    ## ##   ##   #####  ##    ##     ##    ########   |
|                                                                 |
|     Exploiting vulnerabilities, creating new ways through...    |
==================================================================	
	
Happy hacking.
