# -*- coding: utf-8 -*-

from flask import Flask,send_file
import datetime
import json
app=Flask(__name__)



@app.route('/servers')
def get_time():
    today = datetime.date.today()
    data = {"list":[today.month],"max":today.day}
    return json.dumps(data, ensure_ascii=False).encode().decode('utf8')



@app.route('/global_notice.html')
def gnotice():
    return "오늘의 날짜는.."



@app.route('/favicon.ico')
def favicon():
    return send_file('favicon.ico','image/x-icon')



@app.route('/')
def root():
    return main()



@app.route('/kkutu')
def kkutu():
    return main()



def main():
    return "<p>이 페이지는 끄투가 아닌, 달력입니다. 뭘 바라셨어요?</p>"+("<br />"*100)+"""<div id="Bottom" style="width: 1032px;"><div class="bottom-legal"><div style="color: #666;">그냥 달력 Copyright (C) 2018 CrowZ(preta@crowz.r-e.kr)<br>이 프로그램은 제품에 대한 어떠한 형태의 보증도 제공되지 않습니다.<br>이 프로그램은 자유 소프트웨어이며 배포 규정을 만족시키는 조건 아래 자유롭게 재배포할 수 있습니다.<br>이에 대한 자세한 사항은 본 프로그램의 구현을 담은 다음 레포지토리에서 확인하십시오:<a target="_blank" href="https://github.com/Preta-Crowz/Date">https://github.com/Preta-Crowz/Date</a>"""



app.run(host='114.204.175.211',port=2018);