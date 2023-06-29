# Image-Processing
> Update the config.yml with required setting
1. Specify the input type you need to process
2. Specify the path of image and video

> To run the inference on video or image:
1. python objectTracking.py -i "input_type" -p "path to input type"
2. Ex for image/video python objectTracking.py -i image -p ./testData/img.png
3. Ex for webcam: python objectTracking.py -i webcam

> Adjust the tracker to track various colored objects