

import random #导入随机函数

randnum = random.randint(0, 101)  #生成随机数
i = 0 #定义循环变量
list = []
while i < 1:
    pnum = int(input("您好，请输入您猜的数字哦："))
    if pnum > randnum:
        print("真遗憾，您猜大了，请重新猜哦")
        list = list + ['   '+str(pnum)+'     呀！猜小啦' ]
    elif pnum < randnum:
        print("真的令人难过，您猜小了哟，请重新猜吧")
        list = list + ['   '+str(pnum)+'     真遗憾，猜大啦' ]
    else:
        print("wow，恭喜💐您，答对啦，45你真棒👍！")
        list = list + ['   '+str(pnum) + '      💐答对啦💐']
        i += 1
        break

print(" *猜数字* | *结果* ")
print("-----------------------")
for name in list:
    print(str(name))

