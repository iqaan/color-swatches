import cv2
from matplotlib import ticker
from matplotlib import pyplot as plt

def display(image, dpi=180, cmap=None, vmin=None, vmax=None):
    plt.figure(dpi=dpi)
    disp = plt.imshow(image, cmap=cmap, vmin=vmin, vmax=vmax)
    disp.axes.get_xaxis().set_visible(False)
    disp.axes.get_yaxis().set_visible(False)

def compare(images, labels=None, cmap=None):
    if labels is None:
        labels = [None] * len(images)
    plt.figure()
    f, sub = plt.subplots(1,len(images))
    f.set_dpi(180)
    for i in range(0, len(images)):
        disp = sub[i].imshow(images[i], cmap=cmap)
        sub[i].set_title(labels[i] or "", fontsize=5)
        disp.axes.get_xaxis().set_visible(False)
        disp.axes.get_yaxis().set_visible(False)

def hls2rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_HLS2RGB)

def read_image_hls(img_path):
    image = cv2.imread(img_path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2HLS)


