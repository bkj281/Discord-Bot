# Welcome to Discord Bot
# Bhavesh K. Kothari
## A featured bot for Discord Servers

App Name : Python_BKJ

**About this file**  
The purpose of this file is to provide overview, setup instructions and background information of the project. If you have joined this project as a part of the development team, please ensure this file is up to date.  
  
**Note : All developers must ensure that the instructions mentioned in this file are sufficient to enable a new developer to obtain a executable copy of the lastest code in this repository, without involvement from any other human assistance.**

---

**Tools and Hardware Requirements Declaration**

I) Software requirements
>1) Latest version of discord.py library
>2) VS Code (or Sublime or any other code editor)
>3) FFmpeg

---

**Project Technical Specifications**

* This project is a Python based project which uses discord.py library for its working.
* Terminal is used to start a server.
* This bot provides various features to discord server.

---

**Setup Instructions**  
As mentioned earlier , this is a Python project,  
The below mentioned steps may vary significantly across various operating systems, please follow them accordingly.

These instructions are aimed at a developer who has been added to the project team, after the project development has already been initiated,

Therefore the aim is to get the code from the git repository to run on the developer's system, so as to allow him / her to continue with further development.

---

**Firstly Fork the Git Repository**
**Clone the repository from GitHub :**  

```git clone https://github.com/<username>/Discord-Bot```

( This will create a folder titled Discord-Bot )

**Checking out the latest development branch**

As of writing this guide the main branch used for development is : master  
To switch to this branch run : 

```git checkout master```

**Installing dependencies**  
This project requires pip modules for running,
You can install it by following the steps below:

**Change current working directory to Project directory**

```cd Discord-Bot```

**Install all the pip modules.**

```pip install discord```
```pip install youtube-search-python```
```pip install youtube-dl```
```pip install python-dotenv```

**Create an .env file for storing environment variable.**
**Enter the following environment variables into .env file**
```DISCORD_TOKEN = <your token>```

Please ensure this file is updated incase any package is added / removed.

**Start the server for bot :**  

**Go to the Project Directory using Command Line or Terminal**

**To start Server change working directory to server**

```py bot.py```

---

**Note for future developers**
Can add Music queue.
