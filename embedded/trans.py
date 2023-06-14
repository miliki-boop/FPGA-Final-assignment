import serial
import serial.tools.list_ports
import wave
import format
import audio
from chatGPT import Request
import time
class Communication(object):
    def __init__(self) -> None:
        self.port = 'COM3'
        self.bps = 115200      #波特率
        self.timeout = 5
        self.record = 0
        # 打开串口，并得到串口对象
        self.main_engine = serial.Serial(
            self.port, self.bps, timeout=self.timeout)
    
    def recv(self):
        if (self.main_engine.is_open):   # 判断是否打开成功
            frames = []
            while True:
                if self.main_engine.in_waiting:
                    str = self.main_engine.read(self.main_engine.in_waiting)
                    print(str)
                    if str == 'Start Recording...'.encode():
                        self.record = 1
                        continue
                    if str == 'Recording Done'.encode():
                        self.record = 0
                        dest = "./tmp/in.wav"
                        with wave.open(dest, 'wb') as wf:
                            wf.setnchannels(1)
                            wf.setsampwidth(2)
                            wf.setframerate(16000)
                            wf.writeframes(b''.join(frames))
                            wf.close()
                            
                        format.WAV2MP3(dest)
                        format.MP32PCM(dest)
                        ar = audio.Audio_Recog(dest)
                        ar.run()
                        r = ""
                        while len(r) == 0:
                            r = ar.result
                        print(r)
                        
                        # r = r + ' '
                                             
                        
                        request = Request()
                        request.setMessage(r)
                        response = request.getResponse()
                        print(response)
                        
                        # response = response + ' '
                        response = 'c' + response
                        res = r + '\n' + response
                        print(res)
                        
                        time.sleep(10)
                        self.main_engine.write(res.encode('utf-8'))    
                        print("已传输")    
                         
                    if self.record == 1:
                        frames.append(str)


if __name__ == '__main__':
    Cs= Communication()
    Cs.recv()