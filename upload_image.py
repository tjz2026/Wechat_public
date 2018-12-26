import requests
from get_access_token import Get_access_token
from os.path import sep, getsize

def uploadImage( Mfile):
    _type = 'image'
    AccessToken = Get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token='+AccessToken+str('&type=')+str(_type)
    f = open(Mfile, 'rb')
    suf = f.name.split('.')[-1].lower()
    if suf <> 'jpg' and suf <> 'png':
        return 'Not a image file!'
    elif getsize(Mfile) > 2097152L:
        return 'Image file too large!'
    else:
        files = {'file': (f.name.split(sep)[-1], f)}
        r = requests.post(url, files=files)
        f.close()
    if 'media_id' in r.json():
        return r.json()['media_id']
    else:
        return 'errcode: {}, errmsg: {}'.format(r.json()['errcode'], r.json()['errmsg'])

if __name__ == '__main__':
    Mfile = './Levis_logo-4-e1544707494140.jpg'
    media_id = uploadImage(Mfile)
    print media_id
