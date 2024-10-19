import qrcode


url=input("Enter a url: ").strip()
filename=input("Enter a filename: ").strip()

qr= qrcode.QRCode(box_size=10, border=4)
qr.add_data(url)
image= qr.make_image(fill='black', back_color='white')
image.save(filename)
print(f"QR code saved as {filename}")