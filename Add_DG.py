# this code provides function that adds distributed generator at specified bus number with specified rating
import py_dss_interface
import math

def add_generator(dss, bus, rating_in_kw):
    dg_bus = bus    # Bus to which the wind generator is connected
    generator_name = "DG"+f"{dg_bus}" # define a custom DG name by adding bus name in suffix
    transformer_name = 'Transformer' + f"{dg_bus}"
    
    dss.circuit.set_active_bus(dg_bus) # activating the required bus
    
    bus_base_voltage = dss.bus.kv_base*math.sqrt(3) # getting the base kV of the required bus
   
    print("adding the DG to Bus ",dg_bus)

    dss.text(f"new generator.{generator_name} bus1 = DG_bus kv = 0.69 kw = {rating_in_kw} pf = 0.85 model = 1") # Assuming 0.69 kV output of the DG, as in case of Siemens wind turbines
    
    dss.text(f"new transformer.{transformer_name} buses = (DG_bus {dg_bus}) conns = (wye wye) kvs = (0.69 {bus_base_voltage}) kvas = ({rating_in_kw/0.7} {rating_in_kw/0.7})" )
    
    pass
