import serial
import serial.tools.list_ports
from threading import Thread
import wave
import song_recognition
import format
import audio

class Communication():

    def __init__(self):
        self.port = 'COM3'
        self.bps = 115200
        self.timeout = 5
        self.record = 0
            # 打开串口，并得到串口对象
        self.main_engine = serial.Serial(
            self.port, self.bps, timeout=self.timeout)
        # 判断是否打开成功
        if (self.main_engine.is_open):
            frames = []
            flag  = 0
            while True:
                if self.main_engine.in_waiting:
                    str = self.main_engine.read(self.main_engine.in_waiting)
                    print(str)
                    if str == 'Start Recording...'.encode():
                        self.record = 1
                        continue
                    if str == 'Recording Done'.encode():
                        self.record = 0
                        if flag == 0:
                            dest = "./song/in.wav"
                        else:
                            dest = "./song/search/in_re.wav"
                        with wave.open(dest, 'wb') as wf:
                            wf.setnchannels(1)
                            wf.setsampwidth(2)
                            wf.setframerate(16000)
                            wf.writeframes(b''.join(frames))
                            wf.close()
                            if flag == 0:
                                a = song_recognition.audio()
                                ordr = a.recog("in.wav")
                                print(ordr)
                                if ordr == "search":
                                    flag = 1
                                    continue
                                od = song_recognition.order(ordr)
                                result = od.process()

                                serial2 = serial.Serial('COM4', 115200, timeout=2)
                                if serial2.isOpen():
                                    print('串口已打开') 
                                    data = result[0].encode('utf-8') # 发送的数据
                                    if result == "error.mp3":
                                        data = "9".encode("utf-8")
                                    serial2.write(data)  # 串口写数据
                                    print('You Send Data:', data)

                                    data = serial2.read(100)  # 串口读20位数据

                                    print('receive data is :', data)

                                else:
                                    print('串口未打开')

                                # 关闭串口
                                serial2.close()

                                if serial2.isOpen():
                                    print('串口未关闭')
                                else:
                                    print('串口已关闭')
                                
                                print(result)
                            else:
                                od = song_recognition.order(ordr)
                                result = od.process()
                                serial2 = serial.Serial('COM4', 115200, timeout=2)
                                if serial2.isOpen():
                                    print('串口已打开') 
                                    data = result.encode('utf-8') # 发送的数据
                                    serial2.write(data)  # 串口写数据
                                    print('You Send Data:', data)

                                    data = serial2.read(100)  # 串口读20位数据

                                    print('receive data is :', data)

                                else:
                                    print('串口未打开')

                                # 关闭串口
                                serial2.close()

                                if serial2.isOpen():
                                    print('串口未关闭')
                                else:
                                    print('串口已关闭')
                                print(result)
                                flag = 0
                            #break
                        frames = []
                        self.record = 0
                    if self.record == 1:
                        frames.append(str)
                
                


    def get_msg(self):
        frames = []
        flag  = 0
        while True:
            if self.main_engine.in_waiting:
                str = self.main_engine.read(self.main_engine.in_waiting)
                print(str)
                if str == 'Start Recording...'.encode():
                    self.record = 1
                    continue
                if str == 'Recording Done'.encode():
                    self.record = 0
                    if flag == 0:
                        dest = "./song/in.wav"
                    else:
                        dest = "./song/search/in_re.wav"
                    with wave.open(dest, 'wb') as wf:
                        wf.setnchannels(1)
                        wf.setsampwidth(2)
                        wf.setframerate(16000)
                        wf.writeframes(b''.join(frames))
                        wf.close()
                        if flag == 0:
                            a = song_recognition.audio()
                            ordr = a.recog("in.wav")
                            print(ordr)
                            if ordr == "search":
                                flag = 1
                                continue
                            od = song_recognition.order(ordr)
                            result = od.process()
                            print(result)
                        else:
                            od = song_recognition.order(ordr)
                            result = od.process()
                            print(result)
                            flag = 0
                        #break
                    frames = []
                    self.record = 0
                if self.record == 1:
                    frames.append(str)


if __name__ == '__main__':
    Communication()