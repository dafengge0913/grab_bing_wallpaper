from urllib.request import urlopen
from urllib.request import urlretrieve
import re

html = urlopen("http://cn.bing.com").read().decode('utf-8')
matchs = re.findall(r"http://s.cn.bing.net/az/hprichbg/rb/.*.jpg", html)
str = matchs[0].split(",")[0]
img_url = str[:-1]
print(img_url)
file_name = img_url.split("/")[-1]
urlretrieve(img_url, r"C:\Users\wangjf\Desktop\other\壁纸\\"+file_name)
