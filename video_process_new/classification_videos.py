
import os
import shutil

# 定义文件夹A的路径
folder_A = 'ucf/inference/temp_lora'  # 修改为实际路径

# 遍历文件夹A中的所有子文件夹B
for folder_B in os.listdir(folder_A):
    path_B = os.path.join(folder_A, folder_B)
    if os.path.isdir(path_B):
        # 获取所有的mp4文件
        mp4_files = [f for f in os.listdir(path_B) if f.endswith('.mp4')]
        
        # 创建一个字典来存储各个字符串对应的文件列表
        file_dict = {}
        
        for file in mp4_files:
            # 解析文件名以提取字符串部分
            string_part = '_'.join(file.split('_')[:-2])
            
            if string_part not in file_dict:
                file_dict[string_part] = []
            file_dict[string_part].append(file)
        
        # 为每个字符串创建一个子文件夹C，并将对应的文件移动到子文件夹C中
        for string_part, files in file_dict.items():
            folder_C = os.path.join(path_B, string_part)
            os.makedirs(folder_C, exist_ok=True)
            
            for file in files:
                src_path = os.path.join(path_B, file)
                dest_path = os.path.join(folder_C, file)
                shutil.move(src_path, dest_path)

print("视频文件分类完成。")