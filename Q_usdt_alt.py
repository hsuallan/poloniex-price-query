import json
import os
import msvcrt
from urllib.request import urlopen
s = 1
while s:
    os.system("cls")
    print("Which currency you want search in poloniex?")
    print("1.XMR\t2.ETH\t3.ETC\t4.BTC\t5.BCH\t6.Close the program")
    choose_content = {"1":"XMR", "2":"ETH", "3":'ETC', "4":'BTC', "5":'BCH', "6":"close"}
    cin = msvcrt.getch()
    cin = str(ord(cin) - 48)
    x = cin in choose_content
    if x == 6:
        break
    elif x:
        polo = urlopen("https://poloniex.com/public?command=returnTicker").read()
        content = json.loads(polo)
        os.system("cls")
        print("---------------------------------------------------")
        print("Current " + choose_content[cin] + " price is $" + content["USDT_" + choose_content[cin]]["last"])
        os.system("pause")
        os.system("cls")
