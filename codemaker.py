
import sys, os
import numpy as np

from PIL import Image, ImageDraw, ImageFont
import cv2



def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image

def mosaic(img, alpha):
    h, w, ch = img.shape
    img = cv2.resize(img,(int(w*alpha), int(h*alpha)))
    img = cv2.resize(img,(w, h), interpolation=cv2.INTER_NEAREST)
    return img

# 生成したいテキストを入力
text = "剣"

# ファイルを読み込む場合
# read_file = 'wide_thumbnail_normal.jpg'  

fontname = "~/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
fontsize = 280
canvasSize = (300, 300)
backgroundRGB = (255, 255, 255)
textRGB = (0, 0, 0)

img = Image.new('RGB', canvasSize, backgroundRGB)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(fontname, fontsize)
draw.text((10, 10), text, fill=textRGB, font=font)

img.save(os.path.join('img', text + '.jpg'))

cv2_img = pil2cv(img)

# cv2_img = cv2.imread(os.path.join('img', read_file))
dst = mosaic(cv2_img, 0.1)
# cv2.imwrite(os.path.join('img', 'dot_' + read_file), dst)
cv2.imwrite(os.path.join('img', 'dot_' + text + '.jpg'), dst)