# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')


    student_list = []
    while True:
        print("学生成绩管理系统")
        print("1.录入学生信息")
        print("2.查询学生信息")
        print("3.成绩统计")
        print("4.退出系统")
        choice = input("请输入你要选择的数字：")
        if choice == "1":
            name = input("请输入学生姓名：")
            id_num = input("请输入学生学号：")
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
            student_dict = {
                "姓名": name,
                "学号": id_num,
                "语文": chinese,
                "数学": math,
                "英语": english
            }
            student_list.append(student_dict)
            print("学生信息录入成功！")
        elif choice == "2":
            search_name = input("请输入要查找的学生姓名：")
            find_flag = 0
            for stu in student_list:
                if stu["姓名"] == search_name:
                    print("查到该学生信息")
                    print("姓名：", stu["姓名"])
                    print("学号：", stu["学号"])
                    print("语文：", stu["语文"])
                    print("数学：", stu["数学"])
                    print("英语：", stu["英语"])
                    find_flag = 1
                    break
            if find_flag == 0:
                print("没有找到这个学生")
        elif choice == "3":
            if len(student_list) == 0:
                print("还没有录入任何学生数据，无法统计")
            else:
                all_score = []
                for stu in student_list:
                    all_score.append(stu["语文"])
                    all_score.append(stu["数学"])
                    all_score.append(stu["英语"])
                total = 0
                for s in all_score:
                    total = total + s
                avg = total / len(all_score)
                max_score = max(all_score)
                min_score = min(all_score)
                print("全部科目平均分：", avg)
                print("全部科目最高分：", max_score)
                print("全部科目最低分：", min_score, "\n")
        elif choice == "4":
            print("程序结束")
            break
        else:
            print("输入数字不对，请重新选择！")







