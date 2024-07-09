# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

def delete_non_avi_files_and_empty_folders(root_folder):
    for subdir_b in os.listdir(root_folder):
        subdir_b_path = os.path.join(root_folder, subdir_b)
        
        if os.path.isdir(subdir_b_path):
            contains_avi = False
            
            for root, dirs, files in os.walk(subdir_b_path, topdown=False):
                for file in files:
                    if file.endswith('.avi'):
                        contains_avi = True
                    else:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        os.rmdir(dir_path)
                    except OSError:
                        pass

            if not contains_avi:
                shutil.rmtree(subdir_b_path)

def convert_avi_to_mp4(root_folder):
    for subdir_b in os.listdir(root_folder):
        subdir_b_path = os.path.join(root_folder, subdir_b)
        
        if os.path.isdir(subdir_b_path):
            for root, dirs, files in os.walk(subdir_b_path):
                for file in files:
                    if file.endswith('.avi'):
                        avi_file_path = os.path.join(root, file)
                        mp4_file_path = os.path.splitext(avi_file_path)[0] + '.mp4'
                        
                        try:
                            subprocess.call(['ffmpeg', '-i', avi_file_path, mp4_file_path])
                        except Exception as e:
                            pass
                        
                        os.remove(avi_file_path)

def move_mp4_files_to_subdir_b(root_folder):
    for subdir_b in os.listdir(root_folder):
        subdir_b_path = os.path.join(root_folder, subdir_b)
        
        if os.path.isdir(subdir_b_path):
            for root, dirs, files in os.walk(subdir_b_path):
                for file in files:
                    if file.endswith('.mp4'):
                        src_file_path = os.path.join(root, file)
                        dst_file_path = os.path.join(subdir_b_path, file)
                        
                        if src_file_path != dst_file_path:
                            shutil.move(src_file_path, dst_file_path)
                
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    shutil.rmtree(dir_path, ignore_errors=True)

# 使用示例
root_folder = '/mnt/dolphinfs/hdd_pool/docker/user/hadoop-imagen/liuhuijie03/school/PartialAttn/ucf_action_outputs'
delete_non_avi_files_and_empty_folders(root_folder)
convert_avi_to_mp4(root_folder)
move_mp4_files_to_subdir_b(root_folder)
