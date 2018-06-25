import requests

url = "http://img1.mm131.me/pic/980/2.jpg"

headers = {
    'accept': "image/webp,image/*,*/*;q=0.8",
    'connection': "keep-alive",
    'accept-encoding': "gzip, deflate, sdch",
    'referer': "http://www.mm131.com/qipao/980_2.html",
    'accept-language': "zh-CN,zh;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400",
    'cache-control': "no-cache",
    'postman-token': "6eb76e77-4f11-513b-56e5-124ee2fd1814"
    }

response = requests.request("GET", url, headers=headers)
sz = open('./logo.jpg', 'wb').write(response.content)
# print(response.text)