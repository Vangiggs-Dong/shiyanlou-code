##逢7就跳小游戏，在实验楼首试Python！By Vangiggs in2020/05/09/04:59 in maoming.
a=0
for i in range(1,101):
    if i%7==0:#7倍数
        continue
    elif i%10==7:#7结尾
        continue
    elif i//10==7:#7在十份位
        continue
    print(i)
    a+=1

print('共有{}人'.format(a))##此自另加的功能
