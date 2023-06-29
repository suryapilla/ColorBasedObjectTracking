# Image-Processing
> Create conda environment:
1. conda create -n env_objDet python=3.10.6
2. conda activate env_objDet
3. pip install -r requirements.txt

> Update the config.yml with required setting
1. Specify the input type you need to process
2. Specify the path of image and video

> To run the inference on video or image:
1. python objectTracking.py -i "input_type" -p "path to input type"
2. Ex for image/video python objectTracking.py -i image -p ./testData/img.png
3. Ex for webcam: python objectTracking.py -i webcam

> Adjust the tracker to track various colored objects