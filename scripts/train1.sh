CUDA_VISIBLE_DEVICES=6 python MotionDirector_train.py --config ucf/ucf_yaml/Riding-Horse.yaml
CUDA_VISIBLE_DEVICES=4 python MotionDirector_train.py --config ucf/ucf_yaml/Golf-Swing-Side.yaml
CUDA_VISIBLE_DEVICES=4 python MotionDirector_train.py --config ucf/ucf_yaml/Run-Side.yaml
CUDA_VISIBLE_DEVICES=4 python MotionDirector_train.py --config ucf/ucf_yaml/Swing-SideAngle.yaml
CUDA_VISIBLE_DEVICES=4 python MotionDirector_train.py --config ucf/ucf_yaml/Diving-Side.yaml
CUDA_VISIBLE_DEVICES=4 python MotionDirector_train.py --config ucf/ucf_yaml/Kicking-Side.yaml
chmod +x ./scripts/infer_temp1.sh && ./scripts/infer_temp1.sh
./scripts/concat_videos.sh




