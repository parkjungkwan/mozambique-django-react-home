from datetime import datetime, timedelta
if __name__ == '__main__':
    kr = datetime.utcnow() + timedelta(hours=9)
    a = kr.strftime("%Y-%m-%d %H:%M:%S")
    print(a)