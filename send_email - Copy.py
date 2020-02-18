import requests, json, smtplib #requests 发送请求   json 处理数据格式  smtplib 邮件
data = {
    'link': 'https://api.tryto.cn/saylove/text', # 情话接口
    'link1': 'http://open.iciba.com/dsapi/',    # 英语 每日一句
    'link2': 'http://wthrcdn.etouch.cn/weather_mini?city=', # 城市天气
    'city': '合肥', #城市
    'first': '亲！！\r\n',
    'last': '\r\n'
}
def getWhether(city, link):
    url = link + city
    r = requests.get(url).json()
    print(r['data']['forecast'][0])
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

smtp = smtplib.SMTP() #开启邮件
smtp.connect('smtp.qq.com',25) # 链接qq邮箱服务
smtp.login('****@qq.com', 'ntbvqdpwh*******') #前面是账号  后面是smtp服务密码 需要在qq邮箱里面申请
smtp.sendmail('*******@qq.com', '******6@qq.com', massage.encode('utf-8')) # 前面是发送人  后面是接收人 第三位是消息
smtp.quit() #关闭邮箱

print('Done !')