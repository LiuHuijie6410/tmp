import os
import re
from moviepy.editor import VideoFileClip, clips_array

# 定义输入和输出路径
input_dir = "ucf/inference/temp_lora"
output_dir = "ucf/inference/temp_lora_concat"

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 用于从文件名中提取数字的正则表达式
number_pattern = re.compile(r'_(\d+)\.mp4$')

def get_sorted_video_files(folder):
    files = [f for f in os.listdir(folder) if f.endswith(".mp4")]
    files.sort(key=lambda x: int(number_pattern.search(x).group(1)))
    return files

def concatenate_videos(folder, video_files, output_file):
    clips = [VideoFileClip(os.path.join(folder, f)) for f in video_files]
    # 将视频按3行4列排列
    if len(video_files) == 30:
        concatenated_clip = clips_array([[clips[0], clips[1], clips[2], clips[3],clips[4],clips[5]],
                                        [clips[6], clips[7], clips[8], clips[9],clips[10],clips[11]],
                                        [clips[12], clips[13], clips[14], clips[15],clips[16],clips[17]],
                                        [clips[18], clips[19], clips[20], clips[21],clips[22],clips[23]],
                                        [clips[24], clips[25], clips[26], clips[27],clips[28],clips[29]]])
    if len(video_files) == 20:
        concatenated_clip = clips_array([[clips[0], clips[1], clips[2], clips[3],clips[4]],
                                        [clips[5], clips[6], clips[7], clips[8],clips[9]],
                                        [clips[10], clips[11], clips[12], clips[13],clips[14]],
                                        [clips[15], clips[16], clips[17], clips[18],clips[19]],
                                        [clips[20], clips[21], clips[22], clips[23],clips[24]],])  

    concatenated_clip.write_videofile(output_file)

# 遍历文件夹结构
for root, dirs, files in os.walk(input_dir):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
        for subdir in subdirs:
            subdir_path = os.path.join(dir_path, subdir)
            video_files = get_sorted_video_files(subdir_path)
            if len(video_files) == 30 or len(video_files) == 20:
          
                output_mp4name = f'{dir_name}_' + subdir
                output_file = os.path.join(output_dir, f"{output_mp4name}.mp4")
                concatenate_videos(subdir_path, video_files, output_file)
            else:
                print(f"Warning: {subdir_path} does not contain exactly 12 video files.")

print("Video concatenation complete.")