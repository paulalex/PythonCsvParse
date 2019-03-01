import csv
from multiprocessing import Pool


def process_row(row):
    print(str(row))


class CsvReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.row_count = 0
        self.chunk_size = 10000

    def get_row_count(self):
        with open(self.file_name) as f:
            for i, l in enumerate(f):
                pass
        self.row_count = i

    def select_chunk_size(self):
        if self.row_count > 10000000:
            self.chunk_size = 100000
            return
        if self.row_count > 5000000:
            self.chunk_size = 50000
            return

        return

    def process_rows(self):
        print("Processing rows..")
        p = Pool(4)
        rows_for_processing = []

        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows_for_processing.append(row)
                if len(rows_for_processing) == self.chunk_size:
                    p.map(process_row, rows_for_processing)
                    del rows_for_processing[:]

    def start_process(self):
        self.get_row_count()
        self.select_chunk_size()
        self.process_rows()







