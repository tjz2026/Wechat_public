# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import reply
import receive
import web
import csv
from random import randint
import reader
from download_image import download_imag
from get_access_token import Get_access_token

class Handle(object):
    user_lists_history = []
    media_lists_history = []
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "hello2018"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        webData = web.data()
        print "Handle Post webdata is ", webData
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg):
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            Handle.user_lists_history.append(toUser)
            if recMsg.MsgType == 'text':
                times = Handle.user_lists_history.count(toUser)
                content = "收到您的留言：" + recMsg.Content + '\n'
                if recMsg.Content == 'figs':
                    content += 'There are ' + str(len(Handle.media_lists_history)) + ' figures stored\n' 
                if recMsg.Content == 'show_last_fig':
                    mediaId = Handle.media_lists_history[-1]
                    replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                    yield  replyMsg.send()
                if times ==1:
                    content += "   嗨，很高兴收到您的首次消息，您有什么需要的请留言！"
                content += "公众号测试阶段，欢迎微信联系" + "  tangtang_dream" + " Thank you! " + str(toUser)
                quotes = reader.get_quotes()
                content += "送给亲一条名句 \n" + quotes[1] + '\n By ' + quotes[0]
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                #yield  replyMsg.send()
                yield  replyMsg.send()
            if recMsg.MsgType == 'image':
                #quotes = reader.get_quotes()
                #print quotes
                #content += "送给亲一条名句 \n" + quotes[1] + '\n By ' + quotes[0]
                #replyMsg = reply.TextMsg(toUser, fromUser, content)
                #yield  replyMsg.send()
                mediaId = recMsg.MediaId
                accessToken = Get_access_token()
                download_imag(accessToken, mediaId)
                Handle.media_lists_history.append(mediaId)
                replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                yield  replyMsg.send()
        else:
            print "暂且不处理"
            yield "success"
        return 
    def get_quotes():
        with open("quotes.csv") as f:
            reader = csv.reader(f)
            next(reader) # skip header
            data = []
            for row in reader:
                data.append(row)
        num = len(data)
        select = randint(0,num)
    #print num, select
    #print data[select]
        return data[select]

