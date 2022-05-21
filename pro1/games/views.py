from django.shortcuts import render
import pymongo
from pymongo import MongoClient

# Create your views here.
global p1
p1 = ""
py = MongoClient('mongodb://localhost:27017/')
db = py['sriram21']
col = db['sri']


def home(request):
    global p1
    u1 = "games/error.html"
    p1 = request.POST.get("p1").upper()
    ps1 = request.POST.get("ps1")
    o1 = request.POST.get("o1")
    o3 = request.POST.get("o3")
    p2 = col.find_one({"name": p1})
    ps2 = col.find_one({"name": p1, "password": ps1})
    if (p2 and (o1 == "1")):
        print("old")
        if ps2:
            u1 = "games/home.html"
        else:
            u1 = "games/error.html"
    elif (p1 and (o3 == "2")):
        p11 = {"name": p1, "password": ps1, "hs": 0, "hs1": 0, "hs4": 0, "hs5": 0, "hs6": 0}
        print(col.insert_one(p11))
        u1 = "games/home.html"

    return render(request, u1, {"p1": p1})


def player(request):
    global p1

    return render(request, "games/player.html", {"p1": p1})


def snake(request):
    global p1
    hs = 0
    hs2 = col.find_one({"name": p1})
    hs3 = hs2["hs"]
    f1 = col.find({}, {"name": 1, "hs": 1})
    # print(f1[1])
    if request.method == 'GET':
        hs = request.GET.get("hs")
        print(hs)
        print(type(hs))
        if hs != None:
            hs1 = {"name": p1}
            so = col.update_one(hs1, {"$set": {"hs": hs}})
            print(so)
    return render(request, "games/snake.html", {"p1": p1, "hs3": hs3, "f1": f1})


def handc(request):
    global p1

    hs4 = 0
    hs2 = col.find_one({"name": p1})
    hs3 = hs2["hs4"]
    f1 = col.find({}, {"name": 1, "hs4": 1})
    if request.method == 'GET':
        hs4 = request.GET.get("hs4")
        print(hs4)
        if hs4 != None:
            hs11 = {"name": p1}
            so = col.update_one(hs11, {"$set": {"hs4": hs4}})
            print(so)

    return render(request, "games/handc.html", {"p1": p1, "hs3": hs3, "f1": f1})


def ttt(request):
    global p1

    hs6 = 0
    hs2 = col.find_one({"name": p1})
    hs3 = hs2["hs6"]
    f1 = col.find({}, {"name": 1, "hs6": 1})
    if request.method == 'GET':
        hs6 = request.GET.get("hs6")
        print(hs6)
        if hs6 != None:
            hs11 = {"name": p1}
            so = col.update_one(hs11, {"$set": {"hs6": hs6}})
            print(so)

    return render(request, "games/ttt.html", {"p1": p1, "hs3": hs3, "f1": f1})


def flyingb(request):
    global p1

    hs5 = 0
    hs2 = col.find_one({"name": p1})
    hs3 = hs2["hs5"]
    f1 = col.find({}, {"name": 1, "hs5": 1})
    if request.method == 'GET':
        hs5 = request.GET.get("hs5")
        print(hs5)
        if hs5 != None:
            hs11 = {"name": p1}
            so = col.update_one(hs11, {"$set": {"hs5": hs5}})
            print(so)

    return render(request, "games/flyingb.html", {"p1": p1, "hs3": hs3, "f1": f1})


def car(request):
    global p1

    hs1 = 0
    hs2 = col.find_one({"name": p1})
    hs3 = hs2["hs1"]
    f1 = col.find({}, {"name": 1, "hs1": 1})
    if request.method == 'GET':
        hs1 = request.GET.get("hs1")
        print(hs1)
        if hs1 != None:
            hs11 = {"name": p1}
            so = col.update_one(hs11, {"$set": {"hs1": hs1}})
            print(so)
    return render(request, "games/car.html", {"p1": p1, "hs3": hs3, "f1": f1})
