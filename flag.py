import qrcode
from PIL import image 
# The data you want to encode in the QR code
data = "https://twitter.com/clcoding"
#Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, boder=5)
qr.add_data(data)
qr.make(fit=True)
#Create an image from the QR code
image = qr.make_image(fill="black", back_color="white")
#Save the image
image.save("qr_code.png")
image.open("qr_code.png")