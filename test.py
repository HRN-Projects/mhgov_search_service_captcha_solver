import io
from PIL import Image                                                           
import pytesseract
import cv2

# Please install tessaract windows setup even if you have the "pytessaract" module installed
# Setting the the "tessaract_cmd" Path is necessary as shown below.
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# List of image file names which need to be converted to text.
files = ['Handler.png', 'Handler_1.png']

# Setting custom config for tessaract.
custom_config = r' --oem 3 --psm 6'

# Loop on all files
for file in files:
	
	# Passing image file in 'image' variable
	image = cv2.imread(file)

	# Extracting the captcha letters out of image.
	text = pytesseract.image_to_string(image, config=custom_config)
	print("Captcha text from \"{}\" is : {}".format(file, text))