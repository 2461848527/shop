#encoding: utf-8
from django.http import JsonResponse

#重构Restful.API的实现
# eg.8

class HttpCode(object):
    ok = 200
    # 参数错误
    paramserror = 400
    # 没有授权
    unauth = 401
    # 请求方法错误
    methoderror = 405
    # 服务器内部错误
    servererror = 500

# {"code":400,"message":"","data":{}}
def result(code=HttpCode.ok,message="",data=None,kwargs=None):
    """返回restful的结果"""
    json_dict = {"code":code,"message":message,"data":data}

    # 判断是否是字典类型并且有值
    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        # 有添加
        json_dict.update(kwargs)

    return JsonResponse(json_dict)


def ok():
    return result()


def params_error(message="",data=None):
    return result(code=HttpCode.paramserror,message=message,data=data)

def unauth(message="",data=None):
    return result(code=HttpCode.unauth,message=message,data=data)

def method_error(message='',data=None):
    return result(code=HttpCode.methoderror,message=message,data=data)

def server_error(message='',data=None):
    return result(code=HttpCode.servererror,message=message,data=data)

