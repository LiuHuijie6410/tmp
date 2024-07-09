import argparse
import os
from omegaconf import OmegaConf


def get_all_filenames(base_path):
    # 用于存储所有文件名的字典
    all_filenames = {}

    # 获取所有一级子文件夹
    subfolders = [f.path for f in os.scandir(base_path) if f.is_dir()]

    # 遍历每个子文件夹
    for subfolder in subfolders:
        subfolder_name = os.path.basename(subfolder)
        all_filenames[subfolder_name] = []

        # 获取子文件夹中的所有文件名
        for file in os.listdir(subfolder):
            file_path = os.path.join(subfolder, file)
            if os.path.isfile(file_path):
                all_filenames[subfolder_name].append(file)
    
    return all_filenames


noise_prior = 0.
seed = 0
CUDA = 2
model = '/cephfs/huijie/proj/MotionDirector_classifier/models/zeroscope_v2_576w'
current_file_path = os.path.dirname(os.path.abspath(__file__))
sh_name = ['scripts/infer1_test.sh','scripts/infer2_test.sh']
base_path = 'ucf/ucf_action_outputs'
output_dir_base = 'ucf/inference/temp_lora'
parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, default='/cephfs/huijie/proj/qkv/qkv_one_shot_datasets/ucf/inference_prompt_test.yaml')
args = parser.parse_args()
# prompts = args.config
prompts = OmegaConf.load(args.config)
# 使用示例

all_filenames = get_all_filenames(base_path)
commands1 = []
commands2 = []
commands3 = []
commands4 = []
commands5 = []
commands6 = []
commands7 = []
commands8 = []
# commands = [commands1, commands2, commands3, commands4, commands5, commands6, commands7, commands8]
commands = [commands1, commands2]
for filename in all_filenames:
    checkpoint_folder = base_path + '/' + filename
    
    for prompt in prompts[filename]:
        for i in range(2):

            for seed in range(20*i,20*(i+1),1):
                output_dir = output_dir_base + f'/{filename}'
                # import pdb;pdb.set_trace()
                command = f"CUDA_VISIBLE_DEVICES={i} python MotionDirector_inference.py --model {model} --prompt '{prompt}' --checkpoint_folder {checkpoint_folder} --checkpoint_index 500 --noise_prior {noise_prior} --seed {seed} --output_dir {output_dir}"
                commands[i].append(command)
                echo_command = f"echo '{command}'"
                commands[i].append(echo_command)            

for i in range(2):
    with open(sh_name[i], 'w') as file:
        # 将列表中的每个字符串写入文件，每个字符串占一行
        for command in commands[i]:
            file.write("%s\n" % command)
    print(f'save to {sh_name[i]}')
    os.chmod(sh_name[i],0o755)
# print(f'num = {(len(commands8)+len(commands7)+len(commands6)+len(commands5)+len(commands4)+len(commands3) + len(commands2)+len(commands1))/2}')




# for i in range(8):
#     with open(sh_name[i], 'w') as file:
#         # 将列表中的每个字符串写入文件，每个字符串占一行
#         for command in commands[i]:
#             file.write("%s\n" % command)
#     print(f'save to {sh_name[i]}')
#     os.chmod(sh_name[i],0o755)
# print(f'num = {(len(commands8)+len(commands7)+len(commands6)+len(commands5)+len(commands4)+len(commands3) + len(commands2)+len(commands1))/2}')




