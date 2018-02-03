# CCR-data-collection

Procedure:
Start the camera node :  rosrun libuvc_camera camera_node 
Check that the image_raw topic is there :  rostopic list
rosbag record image_raw -O images
To actually view the video live : rosrun image_view image_view image:=image_raw
To save bag into npz: python image_reader.py bagName saveName
sample size:  images, 12:18s, 9.5GB, 11082 msgs    15hz
                              joints,     11:36s, 27.5 MB, 69682 msgs 100hz

