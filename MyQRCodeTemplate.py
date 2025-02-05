from QRCodeGenerator import generate_qr_code

# File settings
url = "gameswithstyle.com"      # The link the qr code to sends users to
qr_code_name = "MyQRCode"       # The name of the image generated

# Resolution and padding
box_size = 15                   # How many pixels go in one box
border = 3                      # How many boxes of padding it contain out the edges

# Colors                        Acceptable inputs
light_color = (255, 255, 255)   # RGB tuple: (000, 123, 255)
dark_color = "#000000"          # HEX string: "#123456" or "123456"
                                # Or any valid python color names: "white", "darkblue", etc.
# Center image
image_name = "GWS.png"          # Include directory and file type (Ex: "Logos/MyPicture.png")
img_size = 3                    # How large is the center image?
correction = 4                  # 1 has the least correction and 4 has the most

generate_qr_code(url, qr_code_name, box_size, border, light_color, dark_color, image_name, img_size, correction)