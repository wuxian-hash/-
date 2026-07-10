# 1. 作业类关键词，命中就归入 homework 文件夹
HOMEWORK_KEYWORDS = {"作业", "练习", "实验", "任务"}

# 2. 后缀对应文件夹规则
SUFFIX_RULES = {
    # 课件
    ".ppt": "slides",
    ".pptx": "slides",
    ".key": "slides",
    # 代码
    ".py": "code",
    ".ipynb": "code",
    ".c": "code",
    ".cpp": "code",
    ".java": "code",
    # 数据文件
    ".csv": "data",
    ".xlsx": "data",
    ".json": "data",
    # 文本文档
    ".pdf": "documents",
    ".doc": "documents",
    ".docx": "documents",
    ".txt": "documents",
    ".md": "documents",
    # 图片
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",
}

# 兜底未知文件
OTHER_FOLDER = "others"