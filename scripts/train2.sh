CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/Lifting.yaml
CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/Golf-Swing-Back.yaml
CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/Golf-Swing-Front.yaml
CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/SkateBoarding-Front.yaml
CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/Walk-Front.yaml
CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/Kicking-Front.yaml
CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/Swing-Bench.yaml
chmod +x ./scripts/infer_temp2.sh && ./scripts/infer_temp2.sh
./scripts/concat_videos.sh
