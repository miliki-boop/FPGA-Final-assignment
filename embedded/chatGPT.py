import openai
import threading

openai.api_key = "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"


class Request:
  def __init__(self):
    self.message = [
      {"role": "system", "content": "你是一个乐于助人、有创造性、聪明友善的人工智能助手。今天是5月12日，星期五。"}]
    self.response = "我是一个乐于助人、有创造性、聪明友善的人工智能助手，你需要我提供什么帮助吗？"

  def getResponse(self):
    print(self.message)
    while 1:
      try:
        self.timeout()
        return self.response + '\r\n'
      except openai.error.APIConnectionError as errC:
        print(errC)
        print("正在尝试重新连接")
        continue
      except TimeoutError as errT:
        print(errT)
        print("正在尝试重新连接")
        continue

  def setMessage(self, question):
    message = {
      "role": "user",
      "content": question
    }
    self.message.append(message)

  def timeout(self):

    def target():
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.message
      ).choices[0].message['content']
      self.message.append({
        "role": "assistant",
        "content": response
      })
      self.response = response

    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout=15)
    if thread.is_alive():
      raise TimeoutError('connection timeout')


if __name__ == "__main__":
  # completion = openai.ChatCompletion.create(
  #   model="text-davinci-003",
  #   messages=[
  #     {"role": "system", "content": "你是一个乐于助人、有创造性、聪明友善的人工智能助手。"}]
  # ).choices[0].message['content']

  messages = [
    {"role": "system", "content": "你是一个乐于助人、有创造性、聪明友善的人工智能助手。"}]
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  ).choices[0].message['content']

  print(response)
  # text = get_text()
  # promt = "你是一个"
  # response = openai.Completion.create(
  #   model="text-davinci-003",
  #   prompt=promt,
  #   temperature=0.9,
  #   max_tokens=1900,
  #   top_p=1,
  #   frequency_penalty=0.0,
  #   presence_penalty=0.6,
  #   stop=[" Human:", " AI:"]
  # )
  # print(response['choices'][0]['text'])
