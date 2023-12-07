#!/usr/bin/env python3

# import modules
import qrcode, sys, getopt
from PIL import Image

def help():
    help_str = """create_qr.py
generate the qr code of a link with a logo in the middle

Example usage:
    ./create_qr.py  -l www.google.com -o test.png

Required options:
    -o / --output - output path
    -l / --link   - link for the qr code

Optional options (hehe):
    -c / --colour - colour of the qr code (default #17365c)
    -p / --picture - colour of the qr code (default DOI_logo_white.png)
    """
    print(help_str)


def defaults():
    return {"picture": "DOI_logo_white.png", "colour": "#17365c", "base_width": 100}


def generate(options):
    # taking image which user wants
    # in the QR code center
    logo = Image.open(options["picture"])

    # taking base width
    basewidth = options["base_width"]

    # adjust image size
    wpercent = basewidth / float(logo.size[0])
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.BICUBIC)
    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # taking url or text
    url = options["link"]

    # adding URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = options["colour"]

    # adding color to QR code
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert("RGB")

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    QRimg.save(options["output"])


if __name__ == "__main__":
    options = defaults()
    opts, args = getopt.getopt(
        sys.argv[1:], "hc:p:l:o:", ["picture=", "link=", "colour=", "output="]
    )

    for opt, arg in opts:
        if opt == "-h":
            help()
            sys.exit()
        elif opt in ("-c", "--colour"):
            options["colour"] = arg
        elif opt in ("-p", "--picture"):
            options["picture"] = arg
        elif opt in ("-l", "--link"):
            options["link"] = arg
        elif opt in ("-o", "--otuput"):
            options["output"] = arg

    generate(options)
    print("QR code generated!")
