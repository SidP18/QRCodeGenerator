# install all the necessary libraries using pip qrcode Image
import qrcode


# create a function that collects text and converts it to a qrcode using the documentation
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # save the qrcode as an image that can be viewed on the local device or within the folder
    img.save("qrimg.png")


# run the function and ask the user to input a valid url
url = input("Please enter the url you would like to convert to a qrcode: ")
generate_qrcode(url)
