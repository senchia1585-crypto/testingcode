from selenium import webdriver #webdriver 是 selenium 的一个模块，提供了一个接口来驱动浏览器进行自动化测试 像remote control 一样 control web browser
from selenium.webdriver.chrome.options import Options #options 是 selenium 的一个模块，提供了一个接口来设置浏览器的选项 身份验证，
# 隐身模式，禁用扩展程序等像身份牌
from selenium.webdriver.common.by import By 
#By 是 selenium 的一个模块，提供了一个接口来定位元素 通过id name class name tag name css selector xpath等方式定位元素 叫代码找东西以什么方式找
from selenium.webdriver.support.ui import WebDriverWait 
#WebDriverWait 是 selenium 的一个模块，提供了一个接口来等待某个条件成立 直到超时或者条件成立才继续执行 叫等一下 等到有东西出现了才继续执行
from selenium.webdriver.support import expected_conditions as EC
#expected_conditions 是 selenium 的一个模块，提供了一些预定义的条件 用于 WebDriverWait 来等待某个条件成立 例如元素可见 可点击 存在等 叫条件判断
#等到元素可见了才继续执行
import time #time 是 python 的一个模块，提供了一些函数来处理时间 例如 sleep() 函数可以让程序暂停一段时间 叫等一下 等到时间到了才继续执行卜
#时机到才继续执行
c_options=Options() #创建一个 Options 对象来设置浏览器选项
# c_options.add_argument("--headless") #添加一个参数来让浏览器以无头模式运行 无头模式就是没有界面 叫隐身模式
ip={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}
c_options.add_argument("--disable-blink-features=AutomationControlled") #添加一个参数来禁用浏览器的自动化控制特征 叫隐藏身份
c_options.add_argument("--no-sandbox") #添加一个参数来禁用浏览器的沙盒模式 叫隐藏身份
c_options.add_argument("--disable-dev-shm-usage") #添加一个参数来禁用浏览器的 dev-shm 使用 叫隐藏身份
c_options.add_argument(f"--user-agent={ip['User-Agent']}") #添加一个参数来设置浏览器的 User-Agent 叫身份验证
d= webdriver.Chrome(options=c_options) #创建一个 Chrome 浏览器实例
url="https://wutheringwaves.kurogames.com/zh-tw/main/news"
d.get(url) #让浏览器打开指定的 URL
final_titles=[] #创建一个空列表来存储最终的标题
try:
    print("Waiting for the page to load...")
    d.get(url) #让浏览器打开指定的 URL
    print("Page loaded. Finding announcements...")
    w=WebDriverWait(d, 15) #创建一个 WebDriverWait 对象，设置最大等待时间为 15 秒
    news=EC.presence_of_element_located((By.CLASS_NAME,"news-item-title")) #定义一个条件，等待 class name 为 "news-item-title" 的元素出现
    w.until(news) #等待条件成立，即等待 class name 为 "news-item-title" 的元素出现   
    all_t=d.find_elements(By.CLASS_NAME,"news-item-title") #通过标签名找到所有的 h2 元素
    for e in all_t:
        text = e.text.strip() #获取每个 h2 元素的文本内容，并去除多余的空白字符
        if text:
             final_titles.append(text) 
             print(f"Found news title: {text}")
             #如果文本内容不为空，则将其添加到 final_titles 列表中
        #print(f"Found news title: {text}") #打印每个 h2 元素的文本内容，并去除多余的空白字符
    #count=len(all_t) #计算找到的 h2 元素的数量
    # print(f"\nTotal titles tags found: {count}") #打印找到的 h2 元素的数量
   #  print("-" * 30) #打印分隔线 
    #t=d.find_element(By.TAG_NAME,"h2") #通过标签名找到第一个 h2 元素
    #element=d.find_element(By.XPATH,"//*[contains(text(),'announcement') or contains(text(),'latest announcement')]") #通过 XPath 找到第一个 h2 元素
    # for i, item in enumerate(all_t,1): #通过标签名找到所有的 h2 元素，并且使用 enumerate 来获取索引和元素
          #  print(f"{i}. {item.text.strip()}") #打印每个 h2 元素的文本内容，并去除多余的空白字符
except Exception as e:
    print(f"Error loading page: {e}")
finally:
    time.sleep(10) #等待 10 秒钟 checking time
    d.quit()
    print("\nALL done. You did it bro!")
    if final_titles:
         with open("news of wutheringwaves.txt","w",encoding="utf-8") as f:
              for i, item in enumerate(final_titles,1):
                    f.write(f"{i}. {item}\n")
                    print(f"Writing news {i} to file...")
                    time.sleep(1) # Simulate time taken to write each news item
         print("All news items have been written to file.")
    else:
         print("NOTHING FOUND.")
#with open("news of wutheringwaves.txt","w",encoding="utf-8") as f: #打开一个文件，准备写入文本数据
     #for i, item in enumerate(all_t,1): #通过标签名找到所有的 h2 元素，并且使用 enumerate 来获取索引和元素
           # f.write(f"{i}. {item.text.strip()}\n") #将每个 h2 元素的文本内容写入文件，并去除多余的空白字符，每个标题占一行
     










