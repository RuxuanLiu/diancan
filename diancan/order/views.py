import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from wechatpy import parse_message,create_reply
# Create your views here


@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        #接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        #服务器配置中的token
        token = 'liuruxuan'
        #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print('[token, timestamp, nonce]', hashlist)
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')
        print('hashstr befor sha1', hashstr)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print("handle/GET func: hashcode, signature: ", hashstr, signature)
        if hashstr == signature:
          return HttpResponse(echostr)
        else:
          return HttpResponse("field")
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)


@csrf_exempt
def autoreply(request):
    msg = parse_message(request.body)
    print(msg)
    reply = create_reply('你已点好', message=msg)
    xml = reply.render()
    return HttpResponse(xml)
