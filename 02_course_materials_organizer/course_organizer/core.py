from pathlib import Path
import shutil
from course_organizer.rules import HOMEWORK_KEYWORDS, SUFFIX_RULES, OTHER_FOLDER


def get_target_folder(file_name: str, suffix: str) -> str:
    """判断单个文件应该分到哪个文件夹"""
    # 优先判断作业关键词
    for keyword in HOMEWORK_KEYWORDS:
        if keyword in file_name:
            return "homework"
    # 再按后缀匹配
    return SUFFIX_RULES.get(suffix.lower(), OTHER_FOLDER)


def get_unique_path(dest_dir: Path, file_name: str) -> Path:
    """目标文件存在时，自动重命名：a.txt → a_1.txt → a_2.txt"""
    dest_path = dest_dir / file_name
    if not dest_path.exists():
        return dest_path

    stem = dest_path.stem
    suffix = dest_path.suffix
    count = 1
    while True:
        new_name = f"{stem}_{count}{suffix}"
        new_path = dest_dir / new_name
        if not new_path.exists():
            return new_path
        count += 1


def plan_files(source: Path) -> list:
    """扫描源文件夹，生成整理计划（只规划，不操作文件）"""
    plan = []
    # 只遍历一级文件，不递归子文件夹
    for file in source.iterdir():
        if file.is_file():
            suffix = file.suffix.lower()
            target_dir_name = get_target_folder(file.name, suffix)
            plan.append({
                "source_path": file,
                "target_dir_name": target_dir_name,
                "file_name": file.name
            })
    return plan


def execute_organize(source: Path, target: Path, dry_run: bool = False):
    """执行整理，dry_run=True只打印计划，不创建文件"""
    plan = plan_files(source)
    record_list = []
    folder_counter = {}

    if dry_run:
        print("===== 【预览整理计划】dry-run模式，不会改动任何文件 =====")
        for item in plan:
            print(f"{item['source_path']}  -->  {target / item['target_dir_name'] / item['file_name']}")
        return

    # 真实执行复制流程
    print("===== 开始执行文件复制 =====")
    for item in plan:
        target_sub_dir = target / item["target_dir_name"]
        target_sub_dir.mkdir(exist_ok=True, parents=True)
        final_dest = get_unique_path(target_sub_dir, item["file_name"])

        # 复制文件（不删除原文件）
        shutil.copy2(item["source_path"], final_dest)
        print(f"已复制: {item['source_path'].name} → {final_dest}")

        # 记录日志，用于生成报告
        record_list.append((item["source_path"], final_dest))
        folder_counter[item["target_dir_name"]] = folder_counter.get(item["target_dir_name"], 0) + 1

    # 生成整理报告.txt
    report_path = target / "整理报告.txt"
    total_files = len(record_list)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=== 课程资料整理报告 ===\n")
        f.write("执行模式：复制文件（原始文件保留）\n")
        f.write(f"总共整理文件数量：{total_files}\n\n")

        f.write("文件迁移明细：\n")
        for src, dst in record_list:
            f.write(f"{src}  >>>  {dst}\n")

        f.write("\n各文件夹文件统计：\n")
        for folder, count in folder_counter.items():
            f.write(f"{folder} : {count} 个\n")

    print(f"\n✅ 整理完成，报告已生成：{report_path}")