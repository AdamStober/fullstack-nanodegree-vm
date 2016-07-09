# P2_FullStackWebDev

## P2 - Adam’s Tournament Results
This program will pair players in a tournament according to a Swiss algorithm.
Players are paired based on having the same number of wins.

## What's included?
Tournament Project
-tournament.sql
-tournament.py
-tournament_test.py

### tournament.sql
This sets up a tournament database schema with tables like
Players and Matches, and Views that include Wins per player,
matches per player, and standings.

### tournament.py
This python file contains methods to connect to the tournament
database, add and delete players, add matches, and pair players.

### tournament_test.py
This python file contains scripts that test the methods implemented in tournament.py .

## Configuration:
Install Vagrant and VirtualBox.
Then, launch the Vagrant VM.

Instructions on configuring a vagrant virtual environment are at
https://www.udacity.com/wiki/ud197/install-vagrant

### Operating
Run a test suite to verify your code (tournament_test.py).
To execute your tests, launch your Vagrant Virtual machine with the command "vagrant up".
Log in to the virtual machine with the command "vagrant ssh".
Navigate to the tournament project folder.
Run "python tournament_test.py".
If all tests pass, the tournament.py program is running successfully!


#### Copyright and licensing information
All the files are belong to me, Adam

#### Known bugs
[None]

#### Troubleshooting
Good luck!

#### Credits and acknowledgements
Thanks Udacity, Udacity Andy, and Disqus Christian !

##### Changelog
N/A: V1.0, created June 15, 2016
V1.1, created June 22, 2016 - updated README
V1.2, created July 7, 2016 - updated README and tournament.py