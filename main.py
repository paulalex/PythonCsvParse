import datetime
from PythonCsvParse.csv_reader import CsvReader
from PythonCsvParse.zip_utils import ZipUtils


class Main:

    if __name__ == "__main__":
        print("Running")
        start_time = datetime.datetime.now()
        zip_utils = ZipUtils()
        csv_path = zip_utils.unzip_file()
        csv_reader = CsvReader(csv_path)
        csv_reader.start_process()
        end_time = datetime.datetime.now()
        print(end_time - start_time)



