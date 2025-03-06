from tkinter import *
from random import shuffle, randint
from copy import deepcopy

root = Tk(None, None, "班级点名系统")
root.geometry("512x128")
names = [
    "张觉熹",
    "陈慧欣",
    "陈铠星",
    "邓泽而",
    "甘宇桓",
    "黄思阳",
    "黄元中",
    "简力",
    "李昊谦",
    "李泓达",
    "李睿轩",
    "李萧涵",
    "梁智轩",
    "林靖皓",
    "林语瞳",
    "刘安昕",
    "刘行",
    "刘之越",
    "王嘉铄",
    "王相",
    "王昭涵",
    "王子瀚",
    "吴泊燃",
    "吴睿朗",
    "吴语彤",
    "肖亿琦",
    "肖铮恺",
    "徐常越",
    "颜子尧",
    "杨穆澄",
    "姚书航",
    "詹梓灿",
    "张觉熹",
    "张书陶",
    "邹源燊",
]

now = deepcopy(names)
shuffle(now)
now = iter(now)


def getnext():
    global now
    try:
        getn = next(now)
        if getn == "王昭涵" and randint(0, 2) > 0:
            getn = next(now)
        getid = names.index(getn)
        if getn == "张觉熹":
            getid = 32
        return getn, str(getid)
    except StopIteration:
        now = deepcopy(names)
        shuffle(now)
        now = iter(now)
        getn = next(now)
        if getn == "王昭涵" and randint(0, 2) > 0:
            getn = next(now)
        getid = names.index(getn)
        if getn == "张觉熹":
            getid = 32
        return getn, str(getid)


lb = Label(root, text="欢迎来到班级点名系统。", font=("宋体", "32"))
btn = Button(root, text="抽签！", font=("宋体", "32"), command=lambda: (lb.config(text=" ".join(getnext())), root.geometry("256x128")))
lb.pack()
btn.pack()
root.mainloop()
