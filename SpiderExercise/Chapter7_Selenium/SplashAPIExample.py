import requests

# render.html
# it will wait 5 sec to get google
url = 'http://localhost:8050/render.html?url=https://www.google.com&wait=5'
response = requests.get(url)
print(response.text)


# render.png
# render.jpeg
# get the screen shot of the site
url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('taobao.png', 'wb') as f:
    f.write(response.content)

# render.json
# return interface's all function
# http://localhost:8050/render.json?url=https://www.jd.com&html=1&har=1