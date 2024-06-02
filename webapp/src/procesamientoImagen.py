import pytesseract
from PIL import Image

def procesarAtexto(AUTH, image_path):
    image = Image.open(image_path)

    grayscale_image = image.convert('L')
    threshold = 140
    bw_image = grayscale_image.point(lambda x: 0 if x < threshold else 255, '1')
    text = pytesseract.image_to_string(bw_image)
    text = [line for line in text.split('\n') if line.strip()]

    for idx, value in enumerate(text):
        if AUTH.lower() in value.lower():
            result = text[idx+1]

    result = result.split(' ')
    result = ''.join(result)
    return result
