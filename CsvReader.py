import csv
import matplotlib.pyplot as plt


class CsvReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stress_data = []

    def read_csv(self):
        self.stress_data = []
        with open(self.file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            i = 0
            for row in csv_reader:
                index = i
                stress = row['Main Data']
                i += 1
                self.stress_data.append({"index": index, "stress": stress})
                # print("index: {}, value: {}".format(index, stress))
        print("End of reading CSV file")

    def draw_stress(self):
        index = []
        stress = []
        for data in self.stress_data:
            index.append(data["index"])
            stress.append(data["stress"])
        # print(index)
        # print(stress)
        plt.scatter(index, stress, color="blue")
        plt.show()
        print("End of plot")
