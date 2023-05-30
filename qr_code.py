# # Simple QRCode

# # import qrcode as qr 

# # # this import is used to import qrcode module. - alias petname

# # img= qr.make("https://www.youtube.com/results?search_query=wscube+tech") # Yeh function hume QR code bnane mein help karta hain. "" - String banayenge

# # img.save("wscubetech.png") 

# # # This function is used to save qrcode in img format. "png" saves img in a png extention.

# # QRCode with Color Fills

# import qrcode

# from PIL import Image 

# # PIL is used to formating image, here I am importing Image from PIL.

# qr= qrcode.QRCode(version=1,
#                   error_correction=qrcode.constants.ERROR_CORRECT_H,
#                   box_size=20,border=4,)

# # While reading PIL module, I have a function "QRCode" which helps me to change given qrcode functionality.

# qr.add_data("https://www.wscubetech.com/")

# # Adding link URL.

# qr.make(fit=True)

# img= qr.make_image(fill_color="black", back_color="white")

# # Above function make_image sets the fill color and background color for qrcode.

# img.save("website.png")

# Hii i added a new code here