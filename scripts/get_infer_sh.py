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
sh_name = 'scripts/infer.sh'
base_path = 'ucf/ucf_action_outputs'
output_dir_base = 'ucf/inference/temp_lora'
parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, default='/cephfs/huijie/proj/exp4_to_out/ucf/inference_prompt.yaml')
args = parser.parse_args()
# prompts = args.config
prompts = OmegaConf.load(args.config)
# 使用示例

all_filenames = get_all_filenames(base_path)
commands = []
for filename in all_filenames:
    checkpoint_folder = base_path + '/' + filename
    # import pdb;pdb.set_trace()
    for prompt in prompts[filename]:
        for idx in range(100,3001,100):
            output_dir = output_dir_base + f'/{filename}'
            command = f"CUDA_VISIBLE_DEVICES={CUDA} python MotionDirector_inference.py --model {model} --prompt '{prompt}' --checkpoint_folder {checkpoint_folder} --checkpoint_index {idx} --noise_prior {noise_prior} --seed {seed} --output_dir {output_dir}"
            commands.append(command)
            echo_command = f"echo '{command}'"
            commands.append(echo_command)

with open(sh_name, 'w') as file:
    # 将列表中的每个字符串写入文件，每个字符串占一行
    for command in commands:
        file.write("%s\n" % command)
print(f'save to {sh_name}')
os.chmod(sh_name,0o755)





