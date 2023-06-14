# import format
# import audio
# from chatGPT import Request

# # file = 'in.wav'

# # format.WAV2MP3(file)
# # format.MP32PCM(file)
# # ar = audio.Audio_Recog(file)
# # ar.run()
# r = "太空旅行又进一步，我国可重复使用试验航天器成功着陆"
# # while len(r) == 0:
# #         r = ar.result
# # print(r)

# request = Request()


# response = request.getResponse()
# print(response)
# request.setMessage(r)

# response = request.getResponse()
# print(response)
from db_insert import *

def test():
    question = 'hi'
    answer = 'hi'
    insert_user_data(question, answer)
    
test()

