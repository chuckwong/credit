#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib

class STUCredit:

    # 类的初始化
    def __init__(self):
        # URL
        self.loginURL = 'http://credit.stu.edu.cn/portal/stulogin.aspx'
        self.mainURL = 'http://credit.stu.edu.cn/portal/STUMainPage.aspx'
        # CookieJar对象
        self.cookies = cookielib.CookieJar()
        # POST Data
        self.postDataDict = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKMTM1MzI1Njg5N2Rkgl08wbsYqyvisOP2702B+mD2kog=',
            '__EVENTVALIDATION': '/wEWBAK77NOfDwLT8dy8BQLG8eCkDwKk07qFCeLFbY7oqztt9HeypEghIXEFkJRK',
            'txtUserID': '14jhwang',
            'txtUserPwd': 'diaonilaomao',
        }
        # headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
            'Referer': 'http://credit.stu.edu.cn/portal/stulogin.aspx',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        # Opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        # Combine POST Data
        data = urllib.urlencode(self.postDataDict)
        self.postData = data + '&btnLogon=%B5%C7%C2%BC'
        print self.postData
    # login方法构建
    def login(self):
        req = urllib2.Request(self.loginURL, self.postData, self.headers)
        try:
            response = self.opener.open(req)
            responseStr = response.read().decode('gbk')
            print responseStr
        except urllib2.HTTPError, e:
            print e.code
            print e.reason
        except urllib2.URLError, e:
            print e.reason

credit = STUCredit()
credit.login()
