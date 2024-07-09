
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array

# 文件路径
video_dir = "./outputs/inference"

# 视频文件名模板
templates = [
    "A_man_is_playing_golf_in_front_of_the_White_House_0_{}.mp4",
    "A_monkey_is_playing_golf_on_a_field_full_of_flowers_0_{}.mp4",
    "A_panda_is_riding_a_bicycle_in_a_garden_0_{}.mp4"
]

# 数字范围
ranges = [
    range(100, 1600, 100),
    range(1600, 3100, 100)
]

# 合并视频函数
def merge_videos(video_files, output_file):
    clips = [VideoFileClip(os.path.join(video_dir, video)) for video in video_files]
    # 按照3行5列布局
    final_clip = clips_array([
        [clips[i] for i in range(5)], 
        [clips[i] for i in range(5, 10)],
        [clips[i] for i in range(10, 15)]
    ])
    final_clip.write_videofile(output_file)

# 处理每一类视频
for template in templates:
    for i, r in enumerate(ranges):
        video_files = [template.format(num) for num in r]
        os.makedirs("./concat_output",exist_ok=True)

        output_file = f"./concat_output/merged_{template.split('_')[1]}_{i+1}.mp4"
        merge_videos(video_files, output_file)
