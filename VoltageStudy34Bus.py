#this is code for the voltage study

import py_dss_interface
import Add_DG as DG

dss = py_dss_interface.DSS() # creating the DSS object

#dss_file = r"D:\OpenDSS\Project\34Bus\ieee34Mod2.dss" #define the path to the dss files here
dss_file = r".\ieee34Mod2.dss" #define the path to the dss files here

dg_bus = '848'

dss.text("compile {}".format(dss_file)) #compiling the selected dss file

dss.circuit.set_active_class("Line")
# adding energy meter to line 1
dss.text(f"New Energymeter.M1  Line.{dss.active_class.names[0]}  1")

dss.text("set maxcontroliter=300")


dss.text("New Capacitor.C890      Bus1=890        Phases=3        kVAR=300        kV=4.16") # adding capacitor to bus 890 to bring voltage within required limit

DG.add_generator(dss,dg_bus,1000)

dss.text("calcv")
dss.solution.solve()
dss.text("plot profile phases = all")

