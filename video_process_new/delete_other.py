# -*- coding: utf-8 -*-

import os
import shutil

def delete_non_avi_files_and_empty_folders(root_folder):
    # 遍历文件夹A中的所有子文件夹B
    for subdir_b in os.listdir(root_folder):
        subdir_b_path = os.path.join(root_folder, subdir_b)
        
        # 检查是否是文件夹
        if os.path.isdir(subdir_b_path):
            contains_avi = False
            
            # 遍历子文件夹B中的所有文件和文件夹
            for root, dirs, files in os.walk(subdir_b_path, topdown=False):
                for file in files:
                    if file.endswith('.avi'):
                        contains_avi = True
                    else:
                        # 删除非.avi文件
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                
                for dir in dirs:
                    # 尝试删除空文件夹
                    dir_path = os.path.join(root, dir)
                    try:
                        os.rmdir(dir_path)
                    except OSError:
                        pass

            # 如果子文件夹B中不包含.avi文件，删除整个子文件夹B
            if not contains_avi:
                shutil.rmtree(subdir_b_path)



# 使用示例
root_folder = '/mnt/dolphinfs/hdd_pool/docker/user/hadoop-imagen/liuhuijie03/school/PartialAttn/ucf_action'
delete_non_avi_files_and_empty_folders(root_folder)
