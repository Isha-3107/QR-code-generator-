#Simple way to create QRCode
# **First "pip install qrcode"

# import qrcode as qr
# img = qr.make("https://www.linkedin.com/in/isha-khutale-5b5a22249/")
# img.save("myqrcode.png") 


#Creating modern QRCode
import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10,
                   border = 4)

qr.add_data("https://www.linkedin.com/in/isha-khutale-5b5a22249/")

qr.make(fit = True)

img = qr.make_image(fill_color = "white",
                    back_color = "black")

img.save("newImage.png")