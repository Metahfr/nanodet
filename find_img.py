import os

def find_images_with_special_characters(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是图片文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # 检查文件名是否包含点号或空格，但不包含在扩展名前面的情况
            parts = filename.rsplit('.', 1)  # 按照最后一个点号分割文件名
            if len(parts) > 1:
                name, extension = parts
                if '.' in name or ' ' in name:
                    print(f"Found image with special characters: {filename}")

# 要查询的文件夹路径
folder_path = './coco/val2020'
# 调用函数查询包含特殊字符的图片文件
find_images_with_special_characters(folder_path)
