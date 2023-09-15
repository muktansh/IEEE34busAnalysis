
#This code if for conducting the loss studies
import py_dss_interface
import Add_DG as DG
import pandas as pd
import matplotlib.pyplot as plt

dss = py_dss_interface.DSS() # creating the DSS object
dg_bus = '890'
x_axis = []
y_axis = []
for ratings in range(1,2500,10): # change the ranges here to check the range of DG values

    dss.text("clear")

    #dss_file = r"D:\OpenDSS\Project\34Bus\ieee34Mod2.dss" #define the path to the dss files here
    dss_file = r".\ieee34Mod2.dss" #define the path to the dss files here

    dss.text("compile {}".format(dss_file)) #compiling the selected dss file

    # adding energy meter to line 1
    dss.text("New Energymeter.M1  Line.L1  1")
    # dss.text("New Energymeter.M1  bus.sourcebus  1")
    dss.text("set maxcontroliter=300")


    dss.text("New Capacitor.C890      Bus1=890        Phases=3        kVAR=300        kV=4.16") # adding capacitor to bus 890 to bring voltage within required limit

    DG.add_generator(dss,dg_bus,ratings)

    dss.text("calcv")
    dss.solution.solve()
    print(dss.circuit.losses[0])
    y_axis.append(dss.circuit.losses[0])
    x_axis.append(ratings)
plt.xlabel(f'Generator Rating in kW at bus {dg_bus}')
plt.ylabel('Total losses in the network in Watts')
plt.plot(x_axis,y_axis)

plt.show()



