import requests
url="https://fastcdn.hoyoverse.com/content-v2/hkrpg/163118/3dc92660fc87730376952fbb62e48c43_9152923416788276017.png"
res = requests.get(url)
with open("hoikai star character picture.png", "wb") as f: #with open (name,mode="wb") as f: #打开一个文件，准备写入二进制数据
    # "hoikai star character picture.png" 是文件名，"wb" 表示以二进制写入模式打开文件，as f 将文件对象赋值给变量f
    f.write(res.content) #write 方法将res.content（图片的二进制数据）写入文件中