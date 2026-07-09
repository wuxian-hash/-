import numpy as np

student_names = []
student_scores = []

def show_menu():
    print("=" * 50)
    print("        成绩分析系统")
    print("=" * 50)
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")
    print("=" * 50)

def input_scores():
    global student_names, student_scores
    student_names.clear()
    student_scores.clear()

    try:
        count=int(input("请输入学生人数："))
        if count <= 0:
            print("人数必须是正整数！")
            return
        for i in range(count):
            name=input(f"请输入第{i+1}个学生姓名：")
            score=float(input("请输入成绩："))
            if 0 <= score <= 100:
                student_names.append(name)
                student_scores.append(score)
            else:
                print("成绩必须在0~100之间，本条数据作废")
        print(" 数据录入完成！")
    except ValueError:
        print("输入格式错误，请输入数字！")

def stat_analysis():
    if not student_scores:
        print(" 请先录入学生成绩！")
        return
    arr=np.array(student_scores)
    print("\n===== 成绩统计结果 =====")
    print(f"总人数：{len(arr)}")
    print(f"总分：{np.sum(arr):.2f}")
    print(f"平均分：{np.mean(arr):.2f}")
    print(f"最高分：{np.max(arr):.2f}")
    print(f"最低分：{np.min(arr):.2f}")
    print(f"方差：{np.var(arr):.2f}")
    print(f"标准差：{np.std(arr):.2f}")

def sort_rank():
    if not student_scores:
        print(" 请先录入学生成绩！")
        return
    combine=list(zip(student_names, student_scores))
    combine.sort(key=lambda x: x[1], reverse=True)
    print("\n===== 成绩排名（由高到低） =====")
    print(f"{'名次':<5}{'姓名':<8}{'成绩':<6}")
    for idx, (name, score) in enumerate(combine, start=1):
        print(f"{idx:<5}{name:<8}{score:<6.1f}")

def score_distribute():
    if not student_scores:
        print("请先录入学生成绩！")
        return
    arr=np.array(student_scores)
    level_a=arr[(arr >= 90) & (arr <= 100)]
    level_b=arr[(arr >= 80) & (arr < 90)]
    level_c=arr[(arr >= 60) & (arr < 80)]
    level_d=arr[arr < 60]

    print("\n===== 成绩等级分布 =====")
    print(f"优秀(90~100分)：{len(level_a)} 人")
    print(f"良好(80~89分)：{len(level_b)} 人")
    print(f"及格(60~79分)：{len(level_c)} 人")
    print(f"不及格(0~59分)：{len(level_d)} 人")

def search_student():
    if not student_names:
        print(" 请先录入学生成绩！")
        return
    target=input("请输入要查询的学生姓名：")
    if target in student_names:
        idx=student_names.index(target)
        print(f" {target} 的成绩为：{student_scores[idx]}")
    else:
        print(" 未找到该学生")

def main():
    while True:
        show_menu()
        choice=input("请选择：")
        if choice=="1":
            input_scores()
        elif choice=="2":
            stat_analysis()
        elif choice=="3":
            sort_rank()
        elif choice=="4":
            score_distribute()
        elif choice=="5":
            search_student()
        elif choice=="6":
            print("系统退出")
            break
        else:
            print("6 输入错误，请选择1~6之间的数字！")
        input("\n按下回车键返回菜单...")

if __name__ == "__main__":
    main()