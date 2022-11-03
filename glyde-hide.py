# wav-audio-hidden ver 1.0
# Powered by poisk-ls
# Hide your secret text in wave audio file.
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')
parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
args = parser.parse_args()
af = args.audiofile
string = args.secretmsg
output = args.outputfile
arged = False
if af and string and output:
    arged = True
def cls():
  os.system("clear")
def help():
  print("\033[1;92mHide Your Secret Message in Audio Wave File.\033[0m")
  print ('''usage: wav-audio-hidden.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]
optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File
  -m SECRETMSG  Enter your message
  -o OUTPUTFILE Your output file path and name

  * Hide Secret Information in Wav Audio file*
                      ↓
  Ex: python3 wav-audio-hidden.py -f 'Rauf Faik - колыбельная.wav' -m "Secret Msg" -o anyname.wav
''')

def banner():
    print ('''

       ___  ___    ___ | /    |     ___
      |__| |  | | |__  |/ __  |    |__
      |    |__| | ___| |\     |__  ___|
                       | \  


                      v1.0
\033[1;91m----------------------------------------------------------------------
\033[1;92m Follow me on Github:    \033[1;91m https://poisk-ls\033[0m
\033[1;92m DM me for more info:    \033[1;91m https://m.me/speedy.mmsc80.thugs\033[0m
\033[1;92m My Discord:             \033[1;91m https://discord.gg/jade-posk-ls\033[0m
\033[1;92m Follow me on Instagram: \033[1;91m https://instagram.com/buhayanjade\033[0m
\033[1;92m My Telegram:            \033[1;91m https://t.me/poisLs\033[0m
\033[1;91m----------------------------------------------------------------------

\033[93mHide your text message in wave audio file like poisk-ls\033[0m''')

def em_audio(af, string, output):
    if not arged:
      help()
    else:
      print ("")
      print (" \033[1;91mPlease wait in sec...\033[0m")
      waveaudio = wave.open(af, mode='rb')
      frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
      string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
      waveaudio.close()
      print ("")
      print ("Done...")
      print ("")
cls()
banner()
try:
  em_audio(af, string, output)
except:
  print ("Something went wrong!! try again")
  quit('')
