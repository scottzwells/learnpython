import random
remain = 10000
for n in range(1,21):
    perf = random.randint(1,10)
    if (perf < 5):
        print(f"员工{n}，绩效分{perf}，低于5，不发工资，下一位")
    else:
        remain-=1000
        print(f"向员工{n}发放工资1000元，账户余额还剩余{remain}")
    if remain <= 0:
        break
print("工资发完了，下个月领取吧")

def hello(msg):
    """

    :param msg:hh
    :return: s
    """
    print("hello"+msg)
    return 1

hello("Ayin")