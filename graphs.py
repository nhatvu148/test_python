import matplotlib.pyplot as plt
import numpy as np
import csv


def multiple_plot():
    years = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    company = np.array([23, 45, 67, 89, 100, 210, 300, 340, 450, 600])
    company2 = list(map(lambda x: x*1.5, company))
    company3 = list(map(lambda x: x*2.5, company))
    # plt.xkcd()
    plt.style.use("grayscale")
    plt.plot(years, company, color="red", linestyle='dashed', marker='o')
    plt.plot(years - 0.5, company2, color="green",
             linestyle='dashed', marker='o')
    plt.bar(years, company3, color="blue")
    plt.title("This is my plot")
    plt.xlabel("Year")
    plt.ylabel("Profit")
    plt.legend(["Company A", "Company B", "Company C"])
    plt.savefig("myplots.png")
    # plt.grid(True)
    # print(plt.style.available)
    plt.show()


def read_csv():
    stress_data = []
    with open("stress.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        i = 0
        for row in csv_reader:
            index = i
            stress = row['Main Data']
            i += 1
            stress_data.append({"index": index, "stress": stress})
            # print("index: {}, value: {}".format(index, stress))
    print("End of reading CSV file")
    return stress_data


def draw_stress(stress_data):
    index = []
    stress = []
    for data in stress_data:
        index.append(data["index"])
        stress.append(data["stress"])
    # print(index)
    # print(stress)
    plt.plot(index, stress, color="blue")
    plt.show()
    print("End")


def draw_pie():
    percents = [9.4, 10.8, 11.3, 12.4, 24.8, 31.3]
    languages = ["C++", "C#", "JavaScript", "PHP", "Python", "Java"]
    explode = [0, 0.1, 0, 0, 0, 0]
    plt.pie(percents, labels=languages, autopct="%1.2f%%", explode=explode)
    plt.show()
