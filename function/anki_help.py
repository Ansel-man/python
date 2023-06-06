import re

'''
此程序在为anki模版添加答案时使用

将文本b.txt中的内容插入到pp.txt符合条件的行之后
正则表达式在匹配文本中具有很大的作用
处理文本之前对文本的格式进行浏览

处理文本的工具
1.vscode 编辑器自带的替换功能
2.linux下的grep.sed.awk等软件
3.python中的re模块
'''

if __name__ == "__main__" :
    with open('/Users/ansel/Documents/workdir/pp.txt',mode='r+') as f:
        with open('/Users/ansel/Documents/workdir/b.txt',mode="r+") as m:
            pp = f.readlines()
            b = m.readlines()
            i = 0
            n = 0
            res = re.compile(r'^\*[^\*]*\n$',flags=0)
            for index in range(len(pp)):
                if res.match(pp[index]) != None:
                    pp[index]=re.sub(r'\n',b[i]+'\n',pp[index])
                    i = i+1
                    print(pp[index])
        with open('/Users/ansel/Documents/workdir/a.txt',mode='w+') as p:
            for line in pp:
                p.write(line)

'''

代码过程中的要点:

注意: 处理索引的过程中,不要越界

mode = 'w+' 会直接重写文本

'''