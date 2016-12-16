import urllib.request

url = 'http://zipcloud.ibsnet.co.jp/api/search?zipcode=7080824'
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
# jsonfile = json.loads(html.read().decode('utf-8'))
# decoded_data = data.decode('shift_jis')
print (data)
