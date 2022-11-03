# wav-audio-hidden Ver 1.0
# Powered by poisk-ls
# Secret Message Extractor
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
af = args.audiofile
arged = False
if af:
    arged = True
def cls():
  os.system("clear")
def help():
  print ("")
  print ("\033[1;92mHide Your Secret Message in Audio Wave File.\033[0m")
  print ("")
  print ('''usage: wav-audio-hidden.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]
optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File
  -m SECRETMSG  Enter your message
  -o OUTPUTFILE Your output file path and name

  * Extract Secret Information from Audio file
                     ↓
  Ex: python3 glydehide.py -f anyname.wav
''')

def banner():
    print ('''

       ___  ___    ___ | /    |     ___
      |__| |  | | |__  |/ __  |    |__
      |    |__| | ___| |\     |__  ___|
                       | \ 


                      v1.0
\033[1;91m______________________________________________________________________
\033[1;91m
\033[1;92m Follow me on Github:    \033[1;91m https://poisk-ls\033[0m
\033[1;92m DM me for more info:    \033[1;91m https://m.me/speedy.mmsc80.thugs\033[0m
\033[1;92m My Discord:             \033[1;91m https://discord.gg/jade-posk-ls\033[0m
\033[1;92m Follow me on Instagram: \033[1;91m https://instagram.com/buhayanjade\033[0m
\033[1;92m My Telegram:            \033[1;91m https://t.me/poisLs\033[0m
\033[1;91m______________________________________________________________________

\033[1;93mHide your text message in wave audio file like poisk-ls\033[0m''')


def ex_msg(af):
    if not arged:
      help()
    else:
        print ("")
        print (" \033[1;91mPlease wait in sec...\033[0m")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        msg = string.split("###")[0]
        print ("")
        print ("Your Secret Message is: \033[1;94m"+msg+"\033[0m")
        print ("")
        waveaudio.close()
cls()
banner()
try:
  ex_msg(af)
except:
  print ("Something went wrong!! try again")
  quit('')
