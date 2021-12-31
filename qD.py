# import qr library
import qrcode

# define a variable and assign to it the location of the qrcode redirect 
site = 'https://opensea.io/revareaze'

# create a qr code object and define attributes
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 2,
)

# load the redirect location into the qrcode object
# and make it fit 
qr.add_data(site)
qr.make(fit=True)

# output an image from the qr code generation
codeImage = qr.make_image(fill_color = '#DC143C', back_color = '#191970')
codeImage.save('sprq`rrOSqr.png')