import hashlib
import sys
import time
from modules import globalVar as gl
def col(str,col):
    if col == "green":
        return "\033[1;32;40m{}\033[0m".format(str)
    elif col == "red":
        return "\033[1;31;40m{}\033[0m".format(str)
    elif col == "yellow":
        return "\033[1;33;40m{}\033[0m".format(str)
    elif col == "cyan":
        return "\033[1;36;40m{}\033[0m".format(str)

def times():
    return col("["+time.strftime("%H:%M:%S", time.localtime())+"] ","cyan")

def Url_init(url):
    if url.endswith('/'):
        return url.rstrip('/')
    else:
        return url

def Path_init(path):
    if not path.startswith('/'):
        return '/'+path
    else:
        return path

def Get_Md5(str):
    my_md5 = hashlib.md5()  # 获取一个MD5的加密算法对象
    my_md5.update(str)  # 得到MD5消息摘要
    my_md5_Digest = my_md5.hexdigest()  # 以16进制返回消息摘要，32位
    return my_md5_Digest


def headers_init(head):
    str = ''
    keys = head.keys()
    for i in keys:
        str += i+":"+head[i]+"\n"
    return str

def save_init(path):
    open(path,"w",encoding="utf-8").close()


def save(url,path,str,name):
    if gl.get_value("save_path") != None:
        file = open(gl.get_value("save_path"),"a",encoding="utf-8")
        file.write(str+": "+url+": "+path+": "+name+"\n")
        file.close()

def proxies_init(str):
    if str != None:
        xieyi, daili = str.split('://')
        if gl.get_value("url").startswith("https"):
            return {"https":daili}
        else:
            return {"http":daili}
    else:
        return str
# def Progress_bar(name,geshu):
#     for i in tqdm(range(geshu), desc=name, ncols=80):
#         if name == 'md5':
#             while True:
#                 if gl.get_value('md5_int'):

if __name__ == '__main__':
    print(times())