import argparse
from pathlib import Path
from course_organizer.core import execute_organize

def main():
    parser = argparse.ArgumentParser(description="课程资料自动整理器")
    parser.add_argument("--source", required=True, help="原始资料文件夹路径")
    parser.add_argument("--target", required=True, help="整理后输出文件夹路径")
    parser.add_argument("--dry-run", action="store_true", help="仅预览计划，不实际复制文件")

    args = parser.parse_args()
    source_dir = Path(args.source)
    target_dir = Path(args.target)

    if not source_dir.exists():
        print(f"错误：源文件夹 {source_dir} 不存在！")
        return

    execute_organize(source_dir, target_dir, dry_run=args.dry_run)

if __name__ == "__main__":
    main()