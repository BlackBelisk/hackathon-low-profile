import pytesseract
from PIL import Image
def procesarATexto(AUTH, image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    threshold = 140
    bw_image = grayscale_image.point(lambda x: 0 if x < threshold else 255, '1')
    texto_original = pytesseract.image_to_string(bw_image)
 
    # if(AUTH.lower() not in texto_original.lower()):
    #     angulo = 0
    #     k = 0
    #     rotar = True
    #     while (rotar) and (k < 20):
    #         imagen_rotada = bw_image.rotate(angulo, expand = True)
    #         texto_original = pytesseract.image_to_string(imagen_rotada)

    #         if AUTH.lower() in texto_original.lower():
    #             rotar = False
    #         else:
    #             k+=1
    #             angulo+=5

    #     if k >= 360:
    #         return False

    # Procesado normal
    texto_original = [line for line in texto_original.split('\n') if line.strip()]
    result = ''
    for value in texto_original:
        if AUTH.lower() == value.lower():
            result = texto_original[texto_original.index(AUTH) + 1]

    result = result.split(' ')
    result = ''.join(filter(str.isdigit, result))
    return result

# imagen = 'intentoDificil.jpg'
# nom = "OSE"
# print(procesarATexto(nom, imagen))