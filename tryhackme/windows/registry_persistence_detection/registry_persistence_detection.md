![0000](https://github.com/YouGuess21/RepOffs/assets/125740625/993431a4-077f-4c32-8504-77a40f7812d8)# Registry Persistence Detection
```
Learn to use the AutoRuns PowerShell module to detect persistence mechanisms that use the Registry.

One crucial step that malware does upon successful execution on a target machine is to ensure that it can stay there even after a reboot or removal attempt. This is possible using various techniques, collectively called "malware persistence mechanisms".

This room will give you an overview of these techniques and introduce a tool that can help detect them and aid in removal.
```
Interesting.


<hr>

## Task 2 Intro to Malware Persistence Mechanisms 
```The term "malware persistence" can be defined as:

"Behaviors that enable malware to remain on a system regardless of system events, such as reboots."

```
How?
```
In Windows, the most common and easiest-to-implement technique is the abuse of Windows Registry Run keys.

The Windows Registry is a database of low-level operating systems and application settings. The Run keys are specific keys within the Registry that contain a path that runs every time a user logs on, and they are listed below:

    * HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run - Run path when the current user logs in
    * HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run - Run path when any user logs in
    * HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce - Run path when the current user logs in, then delete
    * HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce - Run path when any user logs in, then delete
```


```
If you want to view the value for one of the Run keys, expand the folders and their subfolders until you reach the key you are looking for. For example:

    HKEY_LOCAL_MACHINE > Software > Microsoft > Windows > CurrentVersion > Run
```

Time to go on that path.

![0000](https://github.com/YouGuess21/RepOffs/assets/125740625/1cabb0d6-024e-4331-b48d-a258f6c9164a)


 #### What is the value "Name" of the suspicious registry entry that runs during startup? Include the parenthesis. 

 I wonder what has parenthesis here, (Default) but also clearly data of ```(Default)``` is weird.

 #### What is the value "Data" of the suspicious registry entry that runs during startup?

 ```C:\Users\Administrator\AppData\Local\bd84\24d9.bat```

 #### What string is displayed on the console when the suspicious file runs?

Runs it.

![0001](https://github.com/YouGuess21/RepOffs/assets/125740625/f8afa68b-7148-42eb-a780-9fb888ead377)


```pleaseletmepersist```

<hr>

###  Task 3 Intro to the AutoRuns PowerShell Module 

```
Some other registry keys can be used to establish persistence, and they are not as obvious, making them harder to find. 
A widely-used tool from Microsoft called [AutoRuns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)  checks all possible locations where a program can automatically run on start-up or when a user logs in. This tool does what we need, but it is not the one we'll be using for this room (If you still want to check it out, try the SysInternals room).
```
Before we start, just to use with Get-Help 
```
PS C:\Users\Administrator> Get-Command -Module AutoRuns                                                                                                                 CommandType     Name                                               Version    Source
-----------     ----                                               -------    ----- 
Function        Compare-AutoRunsBaseLine                           14.0       Au... 
Function        Get-PSAutorun                                      14.0       Au... 
Function        New-AutoRunsBaseLine                               14.0       Au...                                            
```

