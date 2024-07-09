
# -*- coding: utf-8 -*-


import os
import shutil

def move_files_and_remove_subfolders(root_folder):
    # 遍历文件夹A中的所有子文件夹B
    for subfolder_b_name in os.listdir(root_folder):
        subfolder_b_path = os.path.join(root_folder, subfolder_b_name)
        if os.path.isdir(subfolder_b_path):
            # 遍历子文件夹B中的所有子文件夹C
            for subfolder_c_name in os.listdir(subfolder_b_path):
                subfolder_c_path = os.path.join(subfolder_b_path, subfolder_c_name)
                if os.path.isdir(subfolder_c_path):
                    # 移动子文件夹C中的文件D到子文件夹B
                    for file_name in os.listdir(subfolder_c_path):
                        file_path = os.path.join(subfolder_c_path, file_name)
                        if os.path.isfile(file_path):
                            shutil.move(file_path, subfolder_b_path)
                    # 删除子文件夹C
                    os.rmdir(subfolder_c_path)

# 调用函数并传入文件夹A的路径
root_folder = '/mnt/dolphinfs/hdd_pool/docker/user/hadoop-imagen/liuhuijie03/school/PartialAttn/ucf_action'
move_files_and_remove_subfolders(root_folder)
