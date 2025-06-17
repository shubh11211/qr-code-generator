import qrcode
data="https://postimg.cc/TyD8sRD0"
qr=qrcode.QRCode(version=1,
                 box_size=10,
                 border=6,)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="White")
img.save("my qr.png")
print("QR code gnerated and saved as", 'my qr.png')