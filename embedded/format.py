import os
import base64

def M4A2WAV(audiofile):
    cmd = 'ffmpeg -loglevel quiet -y -i ' + audiofile + ' ' + audiofile[:-4] + '.wav'
    os.system(cmd)
    
def MP32PCM(audiofile):
    cmd = 'ffmpeg -loglevel quiet -y -i ' + audiofile + ' -acodec pcm_s16le ' + '-f' + ' s16le' + ' -ac' + ' 1' + ' -ar' + ' 16000 '+audiofile[:-4] + '.pcm'
    os.system(cmd)

def M4A2MP3(audiofile):
    cmd = 'ffmpeg -loglevel quiet -y -i ' + audiofile + ' ' + audiofile[:-4] + '.mp3'
    os.system(cmd)
    
def WAV2MP3(audiofile):
    cmd = 'ffmpeg -loglevel quiet -y -i ' + audiofile + ' ' + audiofile[:-4] + '.mp3'
    os.system(cmd)    

def base64decode(s):
    return str(base64.b64decode(s), "utf-8")
    
