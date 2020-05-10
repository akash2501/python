import json
import urllib.request, urllib.parse, urllib.error
url = "https://api.covid19india.org/data.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Data Retrived")
js = json.loads(data)
tdate = js["cases_time_series"]

print("1.Total Cases")
print("2.Total Recovered")
print("3.Total Active Cases")
print("4.Total Dead")
print("5.Total Overview")
print("6.State Data")
print("7.New Cases in India")
print("8.Cases on date")
print("9.Exit")
while True:
    op = input("what you want to do >>")

    if op == "1":
        y = js["statewise"][0]["confirmed"]
        print("Total Cases >>",y)
    elif op == "2":
        m = js["statewise"][0]["recovered"]
        print("Total Recovered >>",m)
    elif op == "3":
        k = js["statewise"][0]["active"]
        print("Total Active >>",k)
    elif op == "4":
       l = js["statewise"][0]["deaths"]
       print("Total Deaths >>",l)
    elif op == "5":
        confirm = js["statewise"][0]["confirmed"]
        re = js["statewise"][0]["recovered"]
        acti = js["statewise"][0]["active"]
        dead = js["statewise"][0]["deaths"]
        print("Total Confirmed >>",confirm)
        print("Total Recovered >>",re)
        print("Total Active >>",acti)
        print("Total Dead >>",dead)

    elif op == "6":
        name = input("Enter the name of the state code>>")
        for i in range(38):
            state = js["statewise"][i]["statecode"]
            if (state == name):
                confirm = js["statewise"][i]["confirmed"]
                re = js["statewise"][i]["recovered"]
                acti = js["statewise"][i]["active"]
                dead = js["statewise"][i]["deaths"]
                print(state)
                print("Total Confirmed >>", confirm)
                print("Total Recovered >>", re)
                print("Total Active >>", acti)
                print("Total Dead >>", dead)
                print("........................................")
                print("........................................")
    elif op == "7":
        confirm = js["statewise"][0]["deltaconfirmed"]
        re = js["statewise"][0]["deltarecovered"]
        dead = js["statewise"][0]["deltadeaths"]
        lastup = js["statewise"][0]["lastupdatedtime"]
        print("New Confirmed >>", confirm)
        print("New Recovered >>", re)
        print("New Deaths >>", dead)
        print("Last updated at>>",lastup)
        print("........................................")
        print("........................................")
    elif op == "8":
        date = input("Enter the date in format DD MMMMM")
        for i in range(len(tdate)):
            odate = js["cases_time_series"][i]["date"]
            odate = odate.rstrip()
            if date == odate:
                dconfirm = js["cases_time_series"][i]["dailyconfirmed"]
                tconfirm = js["cases_time_series"][i]["totalconfirmed"]
                dre = js["cases_time_series"][i]["dailyrecovered"]
                tre = js["cases_time_series"][i]["totalrecovered"]
                ddead = js["cases_time_series"][i]["dailydeceased"]
                tdead = js["cases_time_series"][i]["totaldeceased"]
                print(odate)
                print("Confirmed on that day>>", dconfirm)
                print("Recovered on that day>>", dre)
                print("Deaths on that day>>", ddead)
                print("Total Confirmed >>", tconfirm)
                print("Total Recovered >>", tre)
                print("Total Deaths >>", tdead)
                print("........................................")
                print("........................................")

    elif op == "9":
        print("Thank You!!")
        break
    else:
        print("PLease give proper operation!")