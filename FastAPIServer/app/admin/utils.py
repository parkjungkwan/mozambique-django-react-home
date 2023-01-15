import string
from datetime import datetime
import pytz
import uuid
import shortuuid


def current_time():
    tz = pytz.timezone('Asia/Seoul')
    cur_time = datetime.now(tz)
    current_time = cur_time.strftime("%H:%M:%S")
    return f"{current_time}"

def utc_seoul():
    return datetime.now(pytz.timezone('Asia/Seoul'))

def myuuid():
    alphabet = string.ascii_lowercase + string.digits
    su = shortuuid.ShortUUID(alphabet=alphabet)
    return su.random(length=8)


if __name__ == '__main__':
    alphabet = string.ascii_lowercase + string.digits
    su = shortuuid.ShortUUID(alphabet=alphabet)
    print(" > "+su.random(length=8))