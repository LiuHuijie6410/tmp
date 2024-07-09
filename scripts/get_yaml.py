# -*- coding: utf-8 -*-

import os
import yaml
import pandas as pd

# 定义路径
excel_path = 'ucf/ucf_prompt.xlsx'  # 请确保文件路径正确
template_yaml_path = 'configs/config_multi_videos_tmp.yaml'
video_dir = 'ucf/ucf_action'
output_dir = 'ucf/ucf_action_outputs'
output_yaml_dir = 'ucf/ucf_yaml'  # 输出yaml文件的目录
os.makedirs(output_dir,exist_ok=True)
try:
    # 创建输出yaml文件的目录
    os.makedirs(output_yaml_dir, exist_ok=True)

    # 读取Excel文件
    excel_data = pd.read_excel(excel_path, header=None, names=['folder', 'prompt'], engine='openpyxl')

    # 读取模板yaml文件
    with open(template_yaml_path, 'r') as file:
        template_yaml = yaml.safe_load(file)

    # 获取视频存储文件夹和输出文件夹中的子文件夹路径
    video_subfolders = {name: os.path.join(video_dir, name) for name in os.listdir(video_dir) if os.path.isdir(os.path.join(video_dir, name))}
    output_subfolders = {name: output_dir for name in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, name))}
    # import pdb;pdb.set_trace()
    # 遍历Excel数据，根据文件夹名生成对应的yaml文件
    for index, row in excel_data.iterrows():
        folder_name = row['folder']
        prompt = row['prompt']

        if folder_name in video_subfolders and folder_name in output_subfolders:
            # 更新模板yaml文件中的相应字段
            
            config = template_yaml.copy()
            # import pdb;pdb.set_trace()
            config['train_data']['path'] = video_subfolders[folder_name]
            config['train_data']['fallback_prompt'] = prompt
            config['output_dir'] = output_subfolders[folder_name]
            config['validation_steps'] = 5000  # 修改validation_steps为5000
            
            # 写入新的yaml文件
            yaml_output_path = os.path.join(output_yaml_dir, f"{folder_name}.yaml")
            with open(yaml_output_path, 'w') as yaml_file:
                yaml.dump(config, yaml_file, default_flow_style=False, allow_unicode=True)

    print(f"生成的yaml文件存储在目录: {output_yaml_dir}")

except Exception as e:
    print(f"执行过程中出现错误: {e}")
