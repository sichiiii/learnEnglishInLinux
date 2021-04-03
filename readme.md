**#this script opens window with english word that u have to translate to russian** 

# run script every 5 minutes
*/5 * * * *   myuser  python3 /path/to/main.py

# run script after system (re)boot
@reboot       myuser  python3 /path/to/main.py
