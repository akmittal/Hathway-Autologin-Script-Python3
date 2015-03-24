Hathway-Autologin-Script-Python3
================================

A Python 3 script to login automatically

##How to run script

```python AutHathwayLogin.py username@hathway.com password timeout```

Timeout is time interval after it will check whether connection is alive. it is in seconds. Just keep is 30 if you don't know what to do.

##Auto start script in windows
create a batch file in same directory as script(like startup.bat). 
write ```start python AutohathwayLogin.py```
create a shortcut link to .bat file in location: ```C:\Users\[username]\AppData\Roaming\Microsoft\Windows\Start Menu```

