import qrcode
import os

# Create QR code for the local server URL
url = "http://192.168.1.8:8000"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print(f"QR code generated successfully!")
print(f"URL: {url}")
print(f"QR code saved as: qr_code.png")
