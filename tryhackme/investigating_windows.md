# Investigating Windows

A windows machine has been hacked, its your job to go investigate this windows machine and find clues to what the hacker might have done.

<hr>
<pre>
This is a challenge that is exactly what is says on the tin, there are a few challenges around investigating a windows machine that has been previously compromised.

Connect to the machine using RDP. The credentials the machine are as follows:

Username: Administrator
Password: letmein123!
</pre>
<hr>

#### Q1. Whats the version and year of the windows machine?

Simply open the powershell, and use systeminfo to get all the required information about the machine.

```
PS C:\Windows\system32> systeminfo

Host Name:                 EC2AMAZ-I8UHO76
OS Name:                   Microsoft Windows Server 2016 Datacenter
OS Version:                10.0.14393 N/A Build 14393 
..
.
.

```

Here , windows machine is of ```Windows Server 2016```
<hr>

#### Q2. Which user logged in last?

net user command can be used to check the users in machine. We can check one by one which user has what last logon they had , it will show up at the end as Last logon, but there must be a quicker way for it so I searched and found...
```
PS C:\Windows\system32> Get-LocalUser | Select-Object Name, LastLogon
Name           LastLogon
----           ---------
Administrator  10/27/2023 10:08:33 AM
DefaultAccount
Guest                                                                                       
Jenny
John           3/2/2019 5:48:32 PM  
```

Here we can see ```Administrator``` had the last login.
<hr>

#### Q3. When did John log onto the system last?

Answer format: MM/DD/YYYY H:MM:SS AM/PM

From above we can see John logged in at ```03/02/2019 05:48:32 PM```
<hr>

#### Q4. What IP does the system connect to when it first starts?

![0000](https://github.com/YouGuess21/RepOffs/assets/125740625/ce7a2117-5f0d-41a6-b133-1b52c51e4ee6)

IP it connects to is ```10.34.2.3```

<hr>

#### Q4 What two accounts had administrative privileges (other than the Administrator user)?

Similar to Q2 this can be done by checking each user using net user commmand but I didn't find any quicker way for this so I just checked for all one by one, they show up as
```
Local Group Memberships      *Administrators 
```
Accounts having Administrators memberships are Administrator, Jenny and Guest.

So answer is ```Jenny, Guest```

<hr>

#### Q5. Whats the name of the scheduled task that is malicous.

I was stuck here for a while, then I just used GUI to open ```Task Scheduler```, in which I opened ```Task Scheduler Library```

Here,

![0001](https://github.com/YouGuess21/RepOffs/assets/125740625/2f740f3d-f54d-4407-91ac-c80be2906462)

under actions tab we could see what each of these is doing.

Here, ```GameOver``` having action ```C:\TMP\mim.exe sekurlsa::LogonPasswords > C:\TMP\o.txt```
and  ```Clean file system``` having action ```C:\TMP\nc.ps1 -l 1348```
seem highly sus.

From answer format, we can figure out that required task is indeed ```Clean file system```.

<hr>







