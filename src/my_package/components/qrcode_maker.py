#type: ignore
import qrcode
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap

def create_qrcode(url:str) -> QPixmap:
    #Gera o qr code
    generic_qrcode = qrcode.make(url) 
    #Convert pil.PilImage em image.image
    img = generic_qrcode.get_image()
    #Converte o qr code em QImage
    qimage = ImageQt(img)
    #Retorna o QImage como QPixmap
    return QPixmap.fromImage(qimage) 

url = "https://www.youtube.com"
print(create_qrcode(url))
    