#this code is for fault level study

import py_dss_interface
import Add_DG as DG
import pandas as pd
import matplotlib.pyplot as plt
import Get_index_by_Bus as GI

dss = py_dss_interface.DSS() # creating the DSS object

#dss_file = r"D:\OpenDSS\Project\34Bus\ieee34Mod2.dss" #define the path to the dss files here
dss_file = r".\ieee34Mod2.dss" #define the path to the dss files here

dg_bus = '888'
x_axis=[]
y_axis = []

for ratings in range(1,2000,400):
    
    dss.text("clear")
    dss.text("compile {}".format(dss_file)) #compiling the selected dss file
    DG.add_generator(dss,dg_bus,ratings)
    dss.text("Buscoords IEEE34_BusXY.csv")
    dss.text("New Capacitor.C890      Bus1=890        Phases=3        kVAR=300        kV=4.16") # adding capacitor to bus 890 to bring voltage within required limit

    dss.text("calcv")
    dss.solution.solve()

    dss.text("set mode = faultstudy")
    dss.solution.solve()
    dss.text("Export fault")
    df= pd.read_csv('ieee34-2_EXP_FAULTS.CSV')
    df.to_string()
    # print(df)
    fault_at_DGBUS = df['  3-Phase'][GI.get_index(dg_bus)]
    #print(df)
    # print(ratings," ", fault_at_671)
    x_axis.append(ratings)
    y_axis.append(fault_at_DGBUS)

# print([x for x in zip(x_axis,y_axis)])

plt.xlabel('Generator Ratings kW')
plt.ylabel(f'Fault Level at the Generator bus {dg_bus}: Amperes')
plt.plot(x_axis,y_axis)

plt.show()


