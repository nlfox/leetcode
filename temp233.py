import requests
from pyquery import PyQuery as pq

r = requests.get("https://leetcode.com/problemset/algorithms/").text
locked = 0
for i in pq(r).find("#problemList").find("tr"):
    if pq(i).find(".fa-lock"):
        print "---------locked----------"
        locked += 1
    print pq(i).text()
print locked