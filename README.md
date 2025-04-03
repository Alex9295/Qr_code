# QR Code Generator in Python 

A simple Python script to generate customizable QR codes from URLs or text. Perfect for beginners learning Python or QR code basics!

## Features ✨
- **Customizable QR Codes**: Adjust version (complexity), box size, and border.
- **Error Correction**: Built-in error correction (`ERROR_CORRECT_L`).
- **Save & Preview**: Generates a `.png` file and opens the image automatically.
- **User-Friendly**: Interactive input prompts guide the user.

## How It Works ⚙️
1. Enter a **URL** (e.g., `https://www.youtube.com).
2. Set QR code parameters:
   - **Version**: 1 (smallest) to 40 (largest, high complexity).
   - **Box Size**: Pixel size of each QR "box".
   - **Border**: White space around the QR code.
3. The script generates and saves the QR code as a `.png` file.


## Run the script:
python qr_code_generator.py

# Example Inputs:
1.- Enter the URL (including https:// or http://): https://youtube.com
2.- Enter the version (complexity, 1-40): 15
3.- Enter the box size: 8
4.- Enter the border size: 4
5.- Name it as: youtube



