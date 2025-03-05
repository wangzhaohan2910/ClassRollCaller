from flask import Flask, request, render_template
from random import shuffle, randint
from copy import deepcopy
from threading import Thread
import webbrowser

app = Flask(__name__)
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
    "张觉熹",
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
        return getn, getid
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
        return getn, getid


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        getn, getid = getnext()
        return render_template("index.html", name=getn, id=getid)
    return render_template("index.html", name="", id=0)


def runserver():
    app.run()


if __name__ == "__main__":
    Thread(target=runserver).start()
    webbrowser.open("http://localhost:5000")
