import zipfile
import os


class ZipUtils:
    def unzip_file(self):
        zip_ref = zipfile.ZipFile("./import.zip", 'r')
        extracted = zip_ref.namelist()
        zip_ref.extractall(".")
        zip_ref.close()
        extracted_file = os.path.join(".", extracted[0])

        return extracted_file
