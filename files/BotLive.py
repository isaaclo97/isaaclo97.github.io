import urllib.request
import time
from shutil import copyfilep
import os
from subprocess import call
testfile = urllib.request.URLopener()
testfile.retrieve("http://ajedrezlaroda.com/retransmision/games.pgn", "games.txt")
copyfile('games.txt','D:/GitHub/live.github.io/files/games.txt')
os.chdir('D:/GitHub/live.github.io/')
#Commit Message
commit_message = "refresh game"
#Stage the file
call('git add .', shell = True)
# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)
#Push the new or update files
call('git push origin master', shell = True)