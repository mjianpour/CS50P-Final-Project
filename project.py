import math
import csv
import sys
import re
import urllib.request

url = "https://drive.google.com/uc?export=download&id=1uYbagysew2XvpOPIxcM5_dLZkrDiWeZi"
local_filename = "data.csv"
urllib.request.urlretrieve(url, local_filename)


class Data:
    def __init__(self, initangle, initv, gravity):
        angle_radians = math.radians(float(initangle))

        self.initangle = float(angle_radians)
        self.initv = float(initv)
        self.gravity = float(gravity)

    def __str__(self):
        return f"{round(self.cal_t(), 2)},{round(self.cal_r() , 2)},{round(self.max_altitude(), 2)}"

    def cal_t(self):
        t = (2 * self.initv * math.sin(self.initangle)) / self.gravity
        return t

    def cal_r(self):
        r = ((self.initv**2) * math.sin(2 * self.initangle)) / self.gravity
        return r

    def f(self, x):
        y = (math.tan(self.initangle)) * x - (
            (self.gravity * (x**2)) / (2 * (self.initv * math.cos(self.initangle)) ** 2)
        )
        return y

    def max_altitude(self):
        return self.f(self.cal_r() / 2)


def main():
    name = input("Enter a csv file or Data. ")
    file = check_input(name)
    if ".csv" in file:
        numbers = read_data(f"{file}")

        output_of_data(numbers)

    else:
        print(single(file))


def check_input(name):

    if ".csv" in name:
        try:
            with open(f"{name.strip()}", "r"):
                return name.strip()
        except:
            sys.exit("File does not exist.")
    elif re.search(
        r"^[0-9]+(.[0-9]+)? *, *[0-9]+(.[0-9]+)? *, *[0-9]+(.[0-9]+)?$", name.strip()
    ):
        return name.strip()
    else:
        sys.exit("Invalid input")


def single(x):
    data = []
    k = x.split(",")
    for i in k:
        data.append(i.strip())
    output = str(Data(*data))
    x, y, z = output.split(",")
    return f"Duration: {x}s\nRange of the motion: {y}m\nMax altitude: {z}m"


def read_data(file):
    data = []
    with open(f"{file}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append([row["initangle"], row["initv"], row["gravity"]])
    return data


def output_of_data(data):
    with open("output.csv", "w") as file:
        file.write("duration(s),range(m),max_altitude(m)\n")
    with open("output.csv", "a") as file:
        for d in data:
            file.write(f"{Data(*d)}\n")


if __name__ == "__main__":
    main()
