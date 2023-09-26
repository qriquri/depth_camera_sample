# デプスカメラの距離情報で色分けして表示する
# First import the library
import pyrealsense2 as rs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a context object. This object owns the handles to all connected realsense devices
pipeline = rs.pipeline()
pipeline.start()

N = 50

fig, ax = plt.subplots()

count = 0


def update(i):
    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    if not depth:return

    depth_data = depth.as_frame().get_data()
    np_image = np.asanyarray(depth_data)

    np_color_map = np.zeros([np_image.shape[0], np_image.shape[1], 3])

    idx = np.where(np_image > 50)
    np_color_map[idx] = [1., 1., 1.]
    
    idx = np.where(np_image > 500)
    np_color_map[idx] = [1., 1., 0.]
    
    idx = np.where(np_image > 1000)
    np_color_map[idx] = [1., 0., 0.]
    
    idx = np.where(np_image > 1500)
    np_color_map[idx] = [0., 0., 1.]

    idx = np.where(np_image > 2000)
    np_color_map[idx] = [0., 1., 0.]
        
    plt.clf()
    plt.imshow(np_color_map)

try:
    anime = animation.FuncAnimation(fig, update, np.arange(1,  N), interval=25)
    plt.show()

finally:
    pipeline.stop()
    exit()