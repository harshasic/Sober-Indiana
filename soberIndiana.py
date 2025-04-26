from bs4 import BeautifulSoup
import requests
import json
import time
import os

data = {}
def postData(webhook, text):
    obj = {"text": text}
    # Send POST request with JSON data using the json parameter
    response = requests.post(webhook, json=obj)
    # Print the response
    print(response)


def findNextSoberRide():
    url = "https://soberrideindiana.com/redeem"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    #ele = soup.find_all("a", class_="x-el x-el-a c1-3h c1-3i c1-1s c1-5g c1-5h c1-11 c1-1e c1-1d c1-1p c1-1f c1-1q c1-q c1-1x c1-4 c1-5i c1-5j c1-r c1-s c1-5k c1-5l c1-5m c1-3 c1-b c1-5n c1-5o c1-3k c1-5p c1-5q c1-3o c1-3p c1-3q c1-3r")
    ele = soup.find_all(attrs={"data-ux":"ButtonPrimary"})
    rides = [i.text.split("-")[-1].strip("th").lower().strip() for i in ele]
    firstRide = rides[0]
    return firstRide

    

if 'data.json' not in os.listdir():
    with open('data.json', 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)

with open('data.json', 'r') as fp:
    data = json.load(fp)

    # Post updates on Sober Indiana rides
    nextSoberRide = findNextSoberRide()
    try:
        if data["nextSoberRide"] != nextSoberRide:
            postData('https://hooks.slack.com/services/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', 'Sober Indiana ride update: ' + nextSoberRide)
            data["nextSoberRide"] = nextSoberRide
            data["soberRideLastPosted"] = int(time.time())
            with open('data.json', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
    except:
        postData('https://hooks.slack.com/services/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', 'Sober Indiana ride update: ' + nextSoberRide)
        data["nextSoberRide"] = nextSoberRide
        data["soberRideLastPosted"] = int(time.time())
        with open('data.json', 'w') as fp:
            json.dump(data, fp, sort_keys=True, indent=4)
