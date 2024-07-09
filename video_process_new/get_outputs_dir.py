# -*- coding: utf-8 -*-
import os
import shutil

# 定义目标目录路径
target_directory = "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-imagen/liuhuijie03/school/PartialAttn/ucf_action_outputs"

def clear_subdirectories(directory):
    # 遍历目标目录中的所有项目
    for root, dirs, files in os.walk(directory):
        # 忽略根目录本身，只处理其子目录
        if root == directory:
            continue

        # 删除子目录中的所有文件
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print("Deleted file: {}".format(file_path))
            except Exception as e:
                print("Failed to delete file: {}. Reason: {}".format(file_path, e))

        # 删除子目录中的所有子目录
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            try:
                shutil.rmtree(subdir_path)
                print("Deleted directory: {}".format(subdir_path))
            except Exception as e:
                print("Failed to delete directory: {}. Reason: {}".format(subdir_path, e))

if __name__ == "__main__":
    clear_subdirectories(target_directory)
    print("All subdirectory contents have been deleted.")
