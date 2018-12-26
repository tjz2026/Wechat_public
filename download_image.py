import urllib2
import json
from get_access_token import Get_access_token

def download_imag( accessToken, mediaId):
    postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
    urlResp = urllib2.urlopen(postUrl)
    headers = urlResp.info().__dict__['headers']
    if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
        jsonDict = json.loads(urlResp.read())
        print jsonDict
    else:
        buffer = urlResp.read() 
        mediaFile = file(str(mediaId) + '.jpg', "wb")
        mediaFile.write(buffer)
        print "get successful"
    return
if __name__ == '__main__':
    accessToken = Get_access_token()
    mediaId = '5v2thI3EkP7OB9BFrRlMdRpsvs-iZ2dx5Z2EIpOm0o2X00ayTmX0VCcZ1U55k0Ip'
    download_imag(accessToken, mediaId)
