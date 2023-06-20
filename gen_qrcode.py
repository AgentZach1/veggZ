import qrcode
from PIL import Image

def create_qr_code(url, filename):
    # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    # Add data
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save it somewhere, change the extension as needed:
    img.save(filename)

# Test the function
url = "https://docs.google.com/forms/d/e/1FAIpQLSeRJPeMVwo67oMxe-6Hn-hMKZYGZvCznrcgnbxtZsq4BE83Xg/viewform?usp=sf_link"
create_qr_code(url, "opinion_of_town_qrcode.png")