from chatGPT import Request

request = Request()

for i in range(10):
  response = request.getResponse().encode('GBK')
  print(response)
  data = None
  while data is None:
    pass
  request.setMessage(data)

