from flask import Flask, request, render_template
from threading import Thread
import webbrowser

app = Flask(__name__)
from copy import deepcopy
from random import shuffle

names = [
    "李泓达",
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
    "张觉熹",
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


def regen():
    global now
    now = deepcopy(names)
    shuffle(now)
    now.append("王昭涵")
    now = iter(now)


def getnext():
    global now
    try:
        getn = next(now)
        if getn == "王昭涵":
            return getn, 20
        if getn == "李泓达":
            return getn, 9
        if getn == "张觉熹":
            return getn, 32
        return getn, names.index(getn)
    except StopIteration:
        regen()
        getn = next(now)
        if getn == "王昭涵":
            return getn, 20
        if getn == "李泓达":
            return getn, 9
        if getn == "张觉熹":
            return getn, 32
        return getn, names.index(getn)


regen()


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        getn, getid = getnext()
        return render_template("index.html", name=getn, id=getid)
    return render_template("index.html", name="", id=0)


if __name__ == "__main__":
    Thread(target=app.run).start()
    webbrowser.open("http://localhost:5000")
