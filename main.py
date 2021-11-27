import pytesseract
import sys

class TesseratReader:
    def __init__(self):
        self.config = r'--oem 3 --psm 6 -l ukr'
        #there shuold be path to teseract cmd on your pc (only for windows)
        if (sys.platform=='win32'):
            pytesseract.pytesseract.tesseract_cmd = 'G:\\teseract\\tesseract.exe'

    def read(self,picturePath):

        text = pytesseract.image_to_string(picturePath,config=self.config)
        return text





