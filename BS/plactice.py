# 《Python爬虫开发与项目实战》 page：30
from multiprocessing.context import Process
import os
import pickle as pickle
from multiprocessing import process

txtName = "test.txt"
# print(fileName)


def printFile(txtName):
    try:
        file = open(txtName, 'r')  # 打开文件
        # 'r'读模式、'w'写模式、'a'追加模式、'b'二进制模式（处理媒体文件等）、'+'读/写模式
        print(txtName + '当前内容为：' + file.read())
    finally:
        if file:
            file.close()
# 同样写法
# with open(r'D:\111.txt') as fileReader:
#     print(fileReader.read())


def writeFile(txtName):
    printFile(txtName)
    with open(txtName, 'w') as f:
        f.write('qqq')
    printFile(txtName)
# writeFile(txtName) # 写文件


# # 序列化与反序列化:
# d = dict(url='www.baidu.com', title='首页', content='首页')
# f = open(r'test.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open(r'test.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# a = os.getcwd()  # 获取当前路径 other：os.remove('') remove/removedirs/path.exists等等
# print(a)

# multiprocessing模块创建多进程 （类似的fork方法则用于Unix/inux）
def run_proc(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=str(i), )
        print('Process will start')
        p.start()
    p.join()
    print('Process end.')


# try：
#   code    #需要判断是否会抛出异常的代码，如果没有异常处理，python会直接停止执行程序
# except:  #这里会捕捉到上面代码中的异常，并根据异常抛出异常处理信息
# #except ExceptionName，args：    #同时也可以接受异常名称和参数，针对不同形式的异常做处理
#   code  #这里执行异常处理的相关代码，打印输出等
# else：  #如果没有异常则执行else
#   code  #try部分被正常执行后执行的代码
# finally：
#   code  #退出try语句块总会执行的程序

# VSCode插件：
# Bracket Pair Colorizer 2
# Chinese (Simplified) Language Pack for Visual Studio Code
# fun-comment
# Jupyter
# Pylance
# Python Docstring Generator
# vscode-icons
