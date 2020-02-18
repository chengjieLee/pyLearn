import requests, json, smtplib
data = {
    'link': 'https://api.tryto.cn/saylove/text',
    'link1': 'http://open.iciba.com/dsapi/',
    'link2': 'http://wthrcdn.etouch.cn/weather_mini?city=',
    'city': '南京',
    'first': '亲！！\r\n',
    'last': '\r\n'
}
def getWhether(city, link):
    url = link + city
    r = requests.get(url).json()
    msg = '\r\n 今天'+ data['city'] +'的天气是'+r['data']['forecast'][0]['type'] + '\r\n最低温度:'+r['data']['forecast'][0]['low']+ '--最高温度：' + r['data']['forecast'][0]['high'] +\
    '\r\n 祝你今天有个好心情'
    return str(msg)

def getWord(link):
    r = requests.get(link).json()
    msg = '\r\n\r\n 来点每日英语：\t'+ r['content'] + '\r\n' + r['note']
    return str(msg)

def getTWQH(link):
    r = requests.get(link).json()
    msg = '\r\n\r\n来点土味情话： \t' + r['data']['content']
    return str(msg)

msg = data['first'] + getWhether(data['city'], data['link2']) + getWord(data['link1']) + data['last'] + getTWQH(data['link'])

massage = '''From: From Person <爸爸>
To: To Person <沙雕>
Subject: 注意查收！
''' + msg

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
smtp.login('1105963651@qq.com', 'ntbvqdpwhrigggdi')
smtp.sendmail('1105963651@qq.com', '2685819826@qq.com', massage.encode('utf-8'))
smtp.quit()

print('Done !')