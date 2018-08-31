# nanopool-watcher
Watches your rig and sends an sms and email when it stops hashing, and when it starts hashing again.

# Initial setup 
1) To run this script you will need python3
2) Clone this repo to a local folder in your computer
3) Open a terminal in the same folder from step 2
4) Install the required modules:
  pip install -r requirements.txt --user
5) Run the script for the first time so it creates a config file you can set:
  python3 pool_watcher.py
6) Open a twilio account and write down your account sid and token
7) Press Ctrl+C to stop the script, and open the file pool_watcher.cfg
8) Enter all the configuration values needed in the config file
