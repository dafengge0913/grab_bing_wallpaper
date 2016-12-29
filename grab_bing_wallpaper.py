import json
from urllib.request import urlopen, urlretrieve

import time

try:
    idx = int(input("How many days ago do you want to get? \n\
eg: if you want to get the yesterday's please input 1, \n\
Enter directly or input 0 for the today's: "))

except ValueError:
    idx = 0

base_url = "http://cn.bing.com"

time_stamp = int(round(time.time() * 1000))
url_pattern = base_url + "/HPImageArchive.aspx?format=js&idx={idx}&n=1&nc={time_stamp}&pid=hp&video=0"
url = url_pattern.format(idx=idx, time_stamp=time_stamp)
data = urlopen(url).read().decode('utf-8')
json_str = json.loads(data)

try:
    img_url = json_str["images"][0]["url"]
except TypeError:
    print("can not found url, maybe it is too early")
    exit()

img_url = base_url + img_url
print("download", img_url)
file_name = img_url.split("/")[-1]
urlretrieve(img_url, r"C:\Users\wangjf\Desktop\other\壁纸\\" + file_name)
