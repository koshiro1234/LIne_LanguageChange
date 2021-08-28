import requests

url = "https://notify-api.line.me/api/notify"
access_token = '2il2IuZX3GcTzFfYBS7Xk2AVCVPzWDZLWa6R5CURIjt'
headers = {'Authorization':'Bearer ' + access_token}

message = 'Write your message'
payload = {'message':message}
r = requests.post(url,headers=headers,data=payload,)
print(r)