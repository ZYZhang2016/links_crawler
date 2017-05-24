from urllib.parse import urlparse


#Get domain name(example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2]+'.'+results[-1]
    except:
        return ''

#Get sub domain name(name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

#print(get_domain_name('http://www.mobile.email.weibo.com/u/6067950253/home?wvr=5&c=spr_web_sq_firefox_weibo_t001#1495602253356'))
