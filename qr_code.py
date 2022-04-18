from ensurepip import version
from turtle import back
import qr_code
import image
qr = qrcode.QRCode(
    version = 15,#version of qrcode
    box_size =10,#size of qrcode
    border =5

)

data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"
#the link above will be converted into qrcode
qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")