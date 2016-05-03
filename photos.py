from PIL import Image
import glob
import time

for fp in glob.iglob(r'E:\迅雷下载\1\**\*.jpg', recursive=True):

    im = Image.open(fp)
    try:
        im.show()
        time.sleep(0.01)
    except Exception:
        pass