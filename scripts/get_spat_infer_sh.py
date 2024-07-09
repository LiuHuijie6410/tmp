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
CUDA = 6
model = '/cephfs/huijie/proj/MotionDirector_classifier/models/zeroscope_v2_576w'
current_file_path = os.path.dirname(os.path.abspath(__file__))
sh_name = 'scripts/infer_spat.sh'
base_path = 'ucf/ucf_action_outputs'
save_path_base = 'ucf/inference/spat_lora'
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
        for temp_idx in range(250,3001,250):
            temporal_path_folder = checkpoint_folder + f'/checkpoint-{temp_idx}/temporal/lora/'
            for spat_idx in range(200,1401,300):
                save_path = save_path_base + f'/{filename}'
                spatial_path_folder = 'appearce/outputs/config_multi_images' + f'/checkpoint-{spat_idx}/spatial/lora'
                command = f"CUDA_VISIBLE_DEVICES={CUDA} python MotionDirector_inference_multi.py --model {model} --prompt '{prompt}' --spatial_path_folder {spatial_path_folder} --temporal_path_folder {temporal_path_folder} --noise_prior {noise_prior} --seed {seed} --output_dir {save_path}"
                commands.append(command)
                command = f"echo '{command}'"
                commands.append(command)

with open(sh_name, 'w') as file:
    # 将列表中的每个字符串写入文件，每个字符串占一行
    for command in commands:
        file.write("%s\n" % command)
os.chmod(sh_name,0o755)





