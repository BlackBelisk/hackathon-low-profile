import pytesseract
from PIL import Image
import re

def procesar():
    DEFAULT_AUTH = "twitter"
    image_path = 'webapp/screen.png'
    image = Image.open(image_path)
    #image.show()
    grayscale_image = image.convert('L')
    threshold = 140
    bw_image = grayscale_image.point(lambda x: 0 if x < threshold else 255, '1')
    #bw_image.show()
    #custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    #text = pytesseract.image_to_string(bw_image, config = custom_config)
    text = pytesseract.image_to_string(bw_image)
    text = [line for line in text.split('\n') if line.strip()]

    for idx, value in enumerate(text):
        if DEFAULT_AUTH in value.lower():
            result = text[idx+1]

    result = result.split(' ')
    result = ''.join(result)
    
    with open('webapp/token.txt', 'w') as archivo:
        archivo.write(result)

    #numbers = ''.join(filter(str.isdigit, text))

    #output_file_path = 'numeros.txt'
    #with open(output_file_path, 'w') as file:
    #    file.write(numbers)
