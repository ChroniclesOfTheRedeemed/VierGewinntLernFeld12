# Connect Four Server

Created: /n 16.07.23  
Last Updated: 06.08.23

### Goal

The goal of this project is to provide a deployable Four Connect API to fellow developers to develop other projects to.
This includes but not limits to client applications in form of UIs or automated players.

### Current State

#### API Overview (TODO with second screen)

| Command    | Parameters                                     | Return Type | Description | 
|------------|------------------------------------------------|-------------|-------------| 
| git status | List all new or modified files                 |             |             | 
| git diff   | Show file differences that haven't been staged |             |             |

#### things left to do

 - add tests for game results
 - put some deployment commands into the readme
   - build/run
   - tests
   - test coverage
 - logging strategy?
### How to run the application

Setup (TODO when setting up project on new machine)
install python version ???  (dunno)
--> link setup page

- `pip install requests`
- `pip install flask-cors`
- `pip install bcrypt`

install Bcrypt install flask

Once setup is complete you can:

(TODO I have no idea with what command you can execute the main file D; have to look into basicuser pythonanywhere
account how it's deployed there)

### On the subject of testing

There are no tests (jkjk)

#### how to execute all tests

`python3.8 -m unittest discover tests`

### Known Issues

gameResult always returns player1 wins, this bug majestically evaded tests SOMEHOW

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from src.constants import Api
ImportError: No module named src.constants
```

There is no solution for this issue yet  
Last time setup was done on a fresh Pi the preinstalled Python command worked  
It is likely a path issue when the python has been messed with a lot

### First time Setup Assistance of machines for general usage

Connecting to a machine via ssh

- have a valid username and password for the machine
- enable ssh on said machine
- find out local ip with e.g. `ifconfig`
- connect remotely with `ssh username@ip`
    - e.g. `ssh raspberry@192.168.1.45`

Use screen

- `sudo apt install screen`
- `screen -v`
- `screen -ls`
- `screen -S new-screen`
- deattach: CRTL-a d
- reattach: `screen -r screen-id`

For ChroniclesOfTheRedeemed Projects:

- use `git config --global credential.helper store` to store credentials in next push request
    - a new access token get be taken from here https://github.com/settings/tokens
- you need to use http request to clone, or set up ssh keys and connect it with github
    - there are no ssh keys setup in GitHub yet