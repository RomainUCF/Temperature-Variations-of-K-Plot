########################################
# @AUTHOR TAYLOR ROMAIN                #
# @DATE 3-6-2021                       #
# __main__.py                #
########################################

import matplotlib.pyplot as plt
import math
import numpy as np

from math import log10, floor
from tabulate import tabulate

headers = ['Temperature (K)', "1/T", "Volume of HCL",
           "Moles of H+", "Moles of Borax",
           "Molarity of Borax", "Natural Log of Borax",
           "3 Natural Log of Borax",
           "Natural Log of Equilibrium Expression"]

# List's to store data.
OneOverT = []
Celsius_To_Kelvin = []
Ln_K = []
Volume_Of_HCL_Used = []
MOLES_H_PLUS = []
MOLES_BORAX = []
MOLARITY_OF_BORAX = []
NATURAL_LOG_OF_BORAX = []
THREE_NATURAL_LOG_OF_BORAX = []
NATURAL_LOG_EQUILIBRIUM_EXPRESION = []

# Constants.
MOLARITY_OF_HCL = 0.4680


def main():
    print("Press x to stop entering data.")
    while True:
        #Take in input from the console.
        temperature = input(
            "Temperature in Celsius of Sample #".__add__(str(OneOverT.__len__() + 1)))
        try:
            temperature = float(temperature)

            # Celsius to Kelvin Conversion
            CelsiusToKelvin = (temperature + 273)
            #1/T Calculation
            Divided_Temperature = 1 / CelsiusToKelvin
            # Add the data to the lists declared above.
            OneOverT.append(Divided_Temperature)
            Celsius_To_Kelvin.append(CelsiusToKelvin)
        except ValueError:
            #Check if the input is equal to the termination value 'x',
            # if so break the loop.
            if temperature == "x":
                break
            else:
                print("Only Int & Float values are accepted. Try again.")

    print("Press x to stop entering data.")
    while True:
        buret_readings = input(
            "(Final Burette Reading in mL) insert ',' (Initial Burette Reading in mL) for Sample #".__add__(
                str(Volume_Of_HCL_Used.__len__() + 1))).split(',')

        try:
            final_reading = buret_readings[0]
            initial_reading = buret_readings[1]
            Volume_Of_HCL_Used_L = (float(final_reading) - float(initial_reading)) / 1000
            Volume_Of_HCL_Used.append(Volume_Of_HCL_Used_L)
        except ValueError:
            if temperature == "x":
                break
            else:
                print("Only Int & Float values are accepted. Try again.")
        except IndexError:
            break;
    calculate()


def calculate():
    for i in range(0, Volume_Of_HCL_Used.__len__()):
        MOLES_H_PLUS.append(float((Volume_Of_HCL_Used[i]) * MOLARITY_OF_HCL))
    for i in range(0, MOLES_H_PLUS.__len__()):
        MOLES_BORAX.append(float((MOLES_H_PLUS[i]) / 2))
    for i in range(0, MOLES_BORAX.__len__()):
        MOLARITY_OF_BORAX.append(float((MOLES_BORAX[i]) / 0.00500))
    for i in range(0, MOLES_BORAX.__len__()):
        NATURAL_LOG_OF_BORAX.append(float(np.log(MOLARITY_OF_BORAX[i])))
    for i in range(0, NATURAL_LOG_OF_BORAX.__len__()):
        THREE_NATURAL_LOG_OF_BORAX.append(float((3 * np.log(MOLARITY_OF_BORAX[i]))))
    for i in range(0, THREE_NATURAL_LOG_OF_BORAX.__len__()):
        NATURAL_LOG_EQUILIBRIUM_EXPRESION.append(float(math.log(4) + THREE_NATURAL_LOG_OF_BORAX[i]))
    printDataShowGraph()


def printDataShowGraph():
    plt.scatter(OneOverT, NATURAL_LOG_EQUILIBRIUM_EXPRESION)

    x = np.array(OneOverT)
    y = np.array(NATURAL_LOG_EQUILIBRIUM_EXPRESION)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, x * m + b)
    print("y=",m,"x+",b)
    plt.xlim(min(OneOverT) - 0.0001, max(OneOverT) + 0.0001)
    plt.ylim(min(NATURAL_LOG_EQUILIBRIUM_EXPRESION) - 1, max(NATURAL_LOG_EQUILIBRIUM_EXPRESION) + 1)
    plt.xlabel("1/T (Kelvin)")
    plt.ylabel("Ln K")
    plt.title("Change in Equilibrium Constant with Temperature")
    plt.show()
    data = zip(Celsius_To_Kelvin, OneOverT, Volume_Of_HCL_Used, MOLES_H_PLUS, MOLES_BORAX, MOLARITY_OF_BORAX,
               NATURAL_LOG_OF_BORAX, THREE_NATURAL_LOG_OF_BORAX, NATURAL_LOG_EQUILIBRIUM_EXPRESION)
    print("\n")
    print(tabulate(data, headers=headers, floatfmt=".5f"))


main()
