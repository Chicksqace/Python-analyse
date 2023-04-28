#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/11 16:09
# @File : 图像的手绘效果.py
# 图像读取
# from PIL import Image
# import numpy as np
# im=np.array(Image.open("img.jpg"))
# print(im.shape,im.dtype)
# 图像变换
# from PIL import Image
# import numpy as np
# im=np.array(Image.open("img.jpg"))
# print(im.shape,im.dtype)
# b=[255,255,255]-im
# im=Image.fromarray(b.astype('uint8'))
# im.save("img2.jpg")
# 2
# from PIL import Image
# import numpy as np
# im=np.array(Image.open("img.jpg").convert('L'))
# b=255-im
# im=Image.fromarray(b.astype('uint8'))
# im.save("img3.jpg")
# 4
# from PIL import Image
# import numpy as np
# im=np.array(Image.open("img.jpg").convert('L'))
# b=(100/255)*im+150
# im=Image.fromarray(b.astype('uint8'))
# im.save("img4.jpg")
# 5
# from PIL import Image
# import numpy as np
# im=np.array(Image.open("img.jpg").convert('L'))
# b=255*(im/255)**2
# im=Image.fromarray(b.astype('uint8'))
# im.save("img5.jpg")