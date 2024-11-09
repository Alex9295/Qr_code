# incoding data into quick response and Importing the qrcode library to the Python script.
import qrcode

#data to encode 
data  = input('enter the Data: ')

version=int(input('Enter the version(complexity): ')) # the size and amount of information that the code can store max 15
box_size = int(input('Enter the Box size: '))

# Creating an instance of Qr code class
qr = qrcode.QRCode(version, box_size, border=5)

# adding data to the instance of Qrcode class 
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'black', black_color = 'white') # give the colors you want

f=input("name it as: ")

img.show() 
# Saving the image of the QR code to the user-specified file name
img.save(f'{f}.png')
# Printing a message to inform the user that the QR code has been generated and saved in the gallery
print('qr code generated and saved in the gallery')