## Introduction to Docker for CTFs

*“Docker is a software platform that allows you to build, test, and deploy applications quickly. It is an open platform for developing, shipping, and running applications.”*

*“A container is an isolated environment for your code. This means that a container has no knowledge of your operating system, or your files. It runs on the environment provided to you by Docker Desktop. This is why a container usually has everything that your code needs in order to run, down to a base operating system.”*

These are like Virtual Machines but not VMs. *A virtual machine (VM) is a virtual environment that functions as a virtual computer system with its own CPU, memory, network interface, and storage, created on a physical hardware system (located off- or on-premises)*

For CTFs, these are good because we can focus on searching for the vulnerability, instead of dealing with setups. Also, if an exploit works locally, it should work on challenge servers as the organisers likely use the same.

It’s easy and comfortable.

We can also setup our CTF play environment with it.

You basically use docker like a linux server where you ssh into. You have a shell and tools installed. (No graphical user interface). It is used for running command-line tools and execute scripts that we write during CTFs.

Set up: Docker runs on linux, so if you are using it on Windows or Mac then Docker is kind of using a hidden virtual machine. Besides docker might want to install docker-compose as well. Docker compose uses docker to give you some commands to launch multiple containers describing a whole setup with multiple systems.

He then proceeds to explain how to set docker as a challenge host or as a ctf solver.
