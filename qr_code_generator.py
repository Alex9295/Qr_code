import qrcode

# Data to encode (ensure this is a full URL)
data = input('Enter the URL (including https:// or http://): ')

# QR code configuration
version = int(input('Enter the version (complexity, 1-40): '))
box_size = int(input('Enter the box size: '))
border = int(input('Enter the border size: '))

# Check if the version is within a valid range
if version < 1 or version > 40:
    print('Version must be between 1 and 40.')
else:
    # Creating an instance of QRCode class
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=box_size,
        border=border
    )

    # Adding data to the instance of Qrcode class 
    qr.add_data(data)

    # Making the QR code fit to size
    qr.make(fit=True)

    # Creating the image
    img = qr.make_image(fill_color='black', back_color='white')

    # Saving the image of the QR code
    file_name = input('Name it as: ')
    img.save(f'{file_name}.png')

    # Showing the image
    img.show()

    # Printing a message to inform the user that the QR code has been generated and saved
    print('QR code generated and saved in the gallery')
