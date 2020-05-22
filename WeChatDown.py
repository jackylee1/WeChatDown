import itchat
import time
'''
----- 使用说明 -----
1.第12-17行选择登录方式（可选）。
2.将第20行的*******改为对方的备注、微信号或者昵称。
3.可按照37-38行自定义自动回复（可选）。
[!] 聊天记录会保存在程序所在目录下的ChatRecords.log里，图片、语音会保存在程序所在目录。
[!] 本程序仅仅是itchat项目的应用，itchat项目地址：https://itchat.readthedocs.io/zh/latest/
'''

itchat.auto_login()
# 通过如下命令登陆，即使程序关闭，一定时间内重新开启也可以不用重新扫码。
#itchat.auto_login(hotReload=True)
# 命令行二维码登录。部分的linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2。
#itchat.auto_login(hotReload=True,enableCmdQR=True)
#itchat.auto_login(hotReload=True,enableCmdQR=2)

myUserName = itchat.search_friends().UserName
herUserName = itchat.search_friends(name='**********')[0].UserName

# 文字
@itchat.msg_register(itchat.content.TEXT)
def text(msg):
    # 我发给她的消息
    if msg.FromUserName == myUserName and msg.ToUserName == herUserName:
        fo = open(r"./ChatRecords.log", "a")
        fo.write(time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()) + ' Boy:' + msg.Text + '\n')
        fo.close()
    # 她发给我的消息
    if msg.FromUserName == herUserName and msg.ToUserName == myUserName:
        fo = open(r"./ChatRecords.log", "a")
        fo.write(time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()) + ' Girl:' + msg.Text + '\n')
        fo.close()

        # 自动回复：接收到'我爱你'则自动回复'我也爱你'。
        if msg.TEXT == '我爱你':
            itchat.send('我也爱你', toUserName=herUserName)

# 语音
@itchat.msg_register(itchat.content.RECORDING)
def picture(msg):
    nowTime = time.time()
    fileNameAndTime = str(nowTime) + '-' + msg.fileName # 防止同时发送多个图片，图片名相同导致覆盖前一张图片。
    if msg.FromUserName == myUserName and msg.ToUserName == herUserName:
        fo = open(r"./ChatRecords.log", "a")
        fo.write(time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()) + ' Boy:[RECORDING-' + fileNameAndTime + ']' + '\n')
        fo.close()
        msg.download(fileNameAndTime)
    if msg.FromUserName == herUserName and msg.ToUserName == myUserName:
        fo = open(r"./ChatRecords.log", "a")
        fo.write(time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()) + ' Girl:[RECORDING-' + fileNameAndTime + ']' + '\n')
        fo.close()
        msg.download(fileNameAndTime)

# 图片
@itchat.msg_register(itchat.content.PICTURE)
def picture(msg):
    nowTime = time.time()
    fileNameAndTime = str(nowTime) + '-' + msg.fileName
    if msg.FromUserName == myUserName and msg.ToUserName == herUserName:
        fo = open(r"./ChatRecords.log", "a")
        fo.write(time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()) + ' Boy:[PICTURE-' + fileNameAndTime + ']' + '\n')
        fo.close()
        msg.download(fileNameAndTime)
    if msg.FromUserName == herUserName and msg.ToUserName == myUserName:
        fo = open(r"./ChatRecords.log", "a")
        fo.write(time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()) + ' Girl:[PICTURE-' + fileNameAndTime + ']' + '\n')
        fo.close()
        msg.download(fileNameAndTime)

itchat.run(debug=True)