import math
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
def power(num1, num2):
    return num1 ** num2
def sqrt_num(num1):
    return math.sqrt(num1)
def save_record(text):
    f = open("calc_history.txt", "a", encoding="utf-8")
    f.write(text + "\n")
    f.close()
def read_record():
    try:
        f = open("calc_history.txt", "r", encoding="utf-8")
        content = f.read()
        f.close()
        print("\n=====历史计算记录=====")
        print(content)
    except:
        print("还没有任何计算记录，文件不存在")
while True:
    print("\n====简易计算器系统====")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    print("5.幂运算")
    print("6.开平方")
    print("7.查看历史记录")
    print("0.退出程序")
    try:
        choice = int(input("请输入功能序号："))
        if 1 <= choice <=5:
            n1 = float(input("请输入第一个数字："))
            n2 = float(input("请输入第二个数字："))
            result = 0
            _str = ""
            if choice == 1:
                result = add(n1, n2)
                _str = "%s+%s=%s" % (n1, n2, result)
            elif choice == 2:
                result = sub(n1, n2)
                _str = "%s+%s=%s" % (n1, n2, result)
            elif choice == 3:
                result = mul(n1, n2)
                _str = "%s+%s=%s" % (n1, n2, result)
            elif choice == 4:
                if n2 == 0:
                    print("错误：除数不能为0！")
                    continue
                result = div(n1, n2)
                _str = "%s+%s=%s" % (n1, n2, result)
            elif choice == 5:
                result = power(n1, n2)
                _str = "%s+%s=%s" % (n1, n2, result)
            print("计算结果：", result)
            save_record(_str)
        elif choice == 6:
            n = float(input("请输入要开方的数字："))
            if n < 0:
                print("错误：负数无法开平方！")
                continue
            res = sqrt_num(n)
            print("开方结果：", res)
            save_record("√%s=%s" % (n, res))
        elif choice ==7:
            read_record()
        elif choice ==0:
            print("程序结束，再见！")
            break
        else:
            print("输入序号超出范围，请重新选择！")
    except ValueError:
        print("输入错误！你必须输入数字，不能输入文字符号")
