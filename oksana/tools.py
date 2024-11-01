from datetime import datetime, timedelta
import pytz
import json

def load_json(name):
  with open(f'data/{name}.json', mode='r', encoding="utf8") as jFile:
      jdata = json.load(jFile)
#  print(f'[{name}.json] 讀取！')
  jFile.close()
  return jdata

def write_js(name,data):
  jsdata = json.dumps(data,ensure_ascii=False)
  with open(f'data/{name}.json', mode='w', encoding="utf8") as jFile:
    jFile.write(jsdata)
    jFile.close()
#    print(f'[{name}.json] 寫入！')

def get_time():
    """
    獲取當前時間(Taiwan, GMT+8)
    回傳：以「年/月/日,時：分」為格式的字串
    """
    tz_taiwan = pytz.timezone('Asia/Taipei')
    now = datetime.now(tz_taiwan)
    return now.strftime("%Y/%m/%d,%H:%M")

import requests
from typing import Literal

TOKEN = "CWA-BE6F63DA-EA21-4D19-AF90-14D41AB5C975"
time_type = Literal["d","w"]
name_type = Literal[
    "宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣",
    "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市",
    "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣",
    "雲林縣", "嘉義縣", "嘉義市", "屏東縣"
]

def get_weather(time:time_type, locationName:name_type):
    """
    回傳未來的天氣
    參數:
      time: 想要看到的時間，請傳入d或w。
        d代表今、明天36小時的氣象報告
        w代表未來一週的氣象預報
      locationName: 傳入縣市名稱，允許的參數如下：
        [宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣]
    """
    url1 = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={TOKEN}&locationName={locationName}"
    url2 = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization={TOKEN}&locationName={locationName}"
    url = {"d":url1, "w":url2}.get(time)
    res = requests.get(url)
    return res.json()["records"]
