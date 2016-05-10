# -*- coding: utf-8 -*-
# class MyClass(GeneratedClass):
def __init__(self):
    GeneratedClass.__init__(self)

def onLoad(self):
    self.baseurl = "http://cms.e-harp.jp/json/"
    pass

def onUnload(self):
    #put clean-up code here
    pass
'''
def onInput_onStart(self, p):
    import requests
    from datetime import datetime
    url = self.baseurl + p
    res = requests.get(url)
    if res.text == "There is no data. Please check QR code number.":
        cont = "データがありません。ちょっと、受付の人に確認してみてくださいね？"
    else:
        res = res.json()
        # content = "ID" + str(res["id"]) + "の"
        # content += "QRコードは" + str(res["qr"])
        # "\RSPD=70\\VCT=100\ふむふむ、、\pau=1000\\rspd=100\\vct=160\あー\VCT=180\ー？、、\VCT=160\札幌から来た、佐藤さんですねえええ？"
        cont = "\RSPD=70\ふむふむ、、\pau=200\\rspd=100\\vct=120\あ\VCT=180\あーーーーーー！"
        cont += "\VCT=160\札幌から来た、" + str(res["name"].encode('utf8')) + "ですねえええ？"
        cont += "ここまで来てくれたお礼に、僕からのプレゼントがあるよーーー？"
        cont += "アンケートも一緒に答えてね"
        cont += "、母国語は" + str(res["lang"])
        cont += "、母国語は" + str(res["lang"])
        cont += "、メモは" + str(res["memo"])
        cont += "、出発時刻は" + str(res["start"])
        cont += "です。"
    self.onStopped(cont)
    pass
'''
def onInput_onStart():
    import requests
    from datetime import datetime
    url = baseurl + "123"
    res = requests.get(url)
    if res.text == "There is no data. Please check QR code number.":
        cont = "データがありません。ちょっと、受付の人に確認してみてくださいね？"
    else:
        res = res.json()
        # content = "ID" + str(res["id"]) + "の"
        # content += "QRコードは" + str(res["qr"])
        # "\RSPD=70\\VCT=100\ふむふむ、、\pau=1000\\rspd=100\\vct=160\あー\VCT=180\ー？、、\VCT=160\札幌から来た、佐藤さんですねえええ？"
        cont = "\RSPD=70\ふむふむ、、\pau=200\\rspd=100\\vct=120\あ\VCT=180\あーーーーーー！"
        cont += "\VCT=160\札幌から来た、" + str(res["name"].encode('utf8')) + "ですねえええ？"
        cont += "ここまで来てくれたお礼に、僕からのプレゼントがあるよーーー？"
        cont += "アンケートも一緒に答えてね"
        cont += "、母国語は" + str(res["lang"])
        cont += "、母国語は" + str(res["lang"])
        cont += "、メモは" + str(res["memo"])
        cont += "、出発時刻は" + str(res["start"])
        cont += "です。"
    print cont
    pass

def onInput_onStop(self):
    self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
    self.onStopped() #activate the output of the box

baseurl = "http://cms.e-harp.jp/json/"
onInput_onStart()
