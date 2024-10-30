from datetime import datetime, timedelta
import pytz

def get_time():
    """
    獲取台灣（GMT+8）的當前時間
    回傳：以「年/月/日 ; 時：分」為格式的字串
    """
    tz_taiwan = pytz.timezone('Asia/Taipei')
    now = datetime.now(tz_taiwan)
    return now.strftime("%Y/%m/%d ; %H:%M")

