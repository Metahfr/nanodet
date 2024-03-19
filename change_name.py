import os

def rename_files(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') and ' (' in filename and ')' in filename:
            # 提取文件名中的yy(x).jpg部分
            parts = filename.split(' (')
            prefix = parts[0]
            suffix = parts[1].split(')')[0]
            # 构造新的文件名
            new_filename = f"{prefix}_{suffix}.jpg"
            # 构造完整的文件路径
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")

# 要处理的文件夹路径
folder_path = './coco/val2020'
# 调用函数重命名文件
rename_files(folder_path)
