"""
阻塞等待
"""
from threading import Thread, Event

msg = None
e = Event()


def 杨子荣():
    print("杨子荣来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set()


t = Thread(target=杨子荣)
t.start()

print("说对口令才是自己人")
e.wait()
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神你是对的人")
else:
    print("打死他 无情啊 哥哥...")
