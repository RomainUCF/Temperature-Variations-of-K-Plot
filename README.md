# Temperature Variations of K

The purpose of this demo is to calculate and plot variations of K lab data using [matplotlib](https://matplotlib.org/). This project is on going development.

## Disclaimer
[There is a low systematic error in the calculation of y=mx+b](https://github.com/RomainUCF/Temperature-Variations-of-K-Plot/issues/1).

Output data is calculated to the hundred-thousandths place (.5f) with the exclusion of Temperature (K).

K = 273.15 (Celsius to Kelvin Conversion)

## Checking Python Version

Press the Windows Key.

Search for Windows Powershell, open Windows Powershell.

Type 'python -V'

![python](https://user-images.githubusercontent.com/63273069/110226992-9f387f80-7ec1-11eb-87bb-348c5ed86ca2.png)

If Python isnt't installed continue.

## Python3 Interpreter Installation

Install the latest version of [Python](https://www.python.org/downloads/)

Complete the installation setup for Python3.

## PyCharm Installation 

Install [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) Community or Professional Edition.
![py](https://user-images.githubusercontent.com/63273069/110227607-1bce5c80-7ec8-11eb-8bfc-78011e451a21.png)

## Matplotlib, NumPy, Tabulate Installation Through PyCharm Terminal
Run and install missing dependecies if applicable. 
![term](https://user-images.githubusercontent.com/63273069/110227765-a9f71280-7ec9-11eb-8579-52febae33a5b.png)

```bash
pip install matplotlib
pip install numpy
pip install tabulate 
```

## Run with PyCharm

Download the project.

![install](https://user-images.githubusercontent.com/63273069/110227859-81bbe380-7eca-11eb-8bb8-177f94170276.png)


Save it in a folder. Remember this location.

Start PyCharm.

![configure pycharm2 091120](https://user-images.githubusercontent.com/63273069/110227672-dfe7c700-7ec8-11eb-8bae-b7c8715a49d2.png)

Open the project from the directory you saved it in or use Version Control to import from 'https://github.com/RomainUCF/Temperature-Variations-of-K-Plot.git'.

![image](https://user-images.githubusercontent.com/63273069/110227791-dd39a180-7ec9-11eb-9228-4098fdd3ef08.png)


*let PyCharm update any missing dependencies. 

## Usage 


Insert temperature test tube values in Celsius. Press enter to submit a data point, press x to stop entering temperature values and continue.
```bash
Temperature in Celsius of Sample #1: 61.3
-enter-
Temperature in Celsius of Sample #2: 54.9
-enter-
Temperature in Celsius of Sample #3: 43.2
-enter-
Temperature in Celsius of Sample #4: 30.6
-enter-
Temperature in Celsius of Sample #5: 23.2
-enter-
Temperature in Celsius of Sample #6: x
-enter-
```
Insert the final burette reading of HCL (mL) separated by a comma (',') followed by the initial burette reading of HCL (mL) and press enter, press x to stop entering burette data and continue. 

```bash
(Final Burette Reading in mL) insert ',' (Initial Burette Reading in mL) for Sample #1: 25.40,3.20
-enter-
(Final Burette Reading in mL) insert ',' (Initial Burette Reading in mL) for Sample #1: 21.8,1.30
-enter-
(Final Burette Reading in mL) insert ',' (Initial Burette Reading in mL) for Sample #3: 18.20,8.90
-enter-
(Final Burette Reading in mL) insert ',' (Initial Burette Reading in mL) for Sample #4: 13.80,4.30
-enter-
(Final Burette Reading in mL) insert ',' (Initial Burette Reading in mL) for Sample #5: 16.42,13.60
-enter-
(Final Burette Reading in mL) insert ',' (Initial Burette Reading in mL) for Sample #6: x
-enter-
```
## Example Output

Data taken from Lab Notebook:

Temp(C): 61.3 |54.9 | 43.2 | 30.6 | 23.2

Burrette Readings (Final (mL) - Initial (mL) ): 25.40,3.20 | 21.80,1.30 | 18.20, 8.90 | 13.80, 4.30 | 16.42, 13.60
```bash
y= -14291.738115291102 x+ 44.55578285619493
  Temperature (K)      1/T    Volume of HCL    Moles of H+    Moles of Borax    Molarity of Borax    Natural Log of Borax    3 Natural Log of Borax    Natural Log of Equilibrium Expression
-----------------  -------  ---------------  -------------  ----------------  -------------------  ----------------------  ------------------------  ---------------------------------------
        334.30000  0.00299          0.02220        0.01039           0.00519              1.03896                 0.03822                   0.11466                                  1.50095
        327.90000  0.00305          0.02050        0.00959           0.00480              0.95940                -0.04145                  -0.12434                                  1.26195
        316.20000  0.00316          0.00930        0.00435           0.00218              0.43524                -0.83186                  -2.49557                                 -1.10928
        303.60000  0.00329          0.00950        0.00445           0.00222              0.44460                -0.81058                  -2.43174                                 -1.04545
        296.20000  0.00338          0.00282        0.00132           0.00066              0.13198                -2.02514                  -6.07541                                 -4.68911

```
![779cd17e078130e2a3aafffc77f9b47a](https://user-images.githubusercontent.com/63273069/110224542-9a1c0600-7eaa-11eb-9336-0a03ca6e3f98.png)

## Excel Version
![ex](https://user-images.githubusercontent.com/63273069/110224769-85d90880-7eac-11eb-9771-e639bf82df5f.png)




