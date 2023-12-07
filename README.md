# qrcode-doi
Generate a QR code with the doi logo in the middle. 

Example:
![Oreology paper](./oreology.png)

Usage:
```
create_qr.py
generate the qr code of a link with a logo in the middle

Example usage:
    ./create_qr.py  -l www.google.com -o test.png

Required options:
    -o / --output - output path
    -l / --link   - link for the qr code

Optional options (hehe):
    -c / --colour - colour of the qr code (default #17365c)
    -p / --picture - colour of the qr code (default DOI_logo_white.png)
```
    
