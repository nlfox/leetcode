import requests

rT = requests.get("http://192.168.1.200/decoder_control.cgi?command=6&user=admin&pwd=").text
print rT
