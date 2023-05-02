# Solution of Question 2 of Variable Analog Voltage 

#import required libraries 
import ltpy

#create a simulation environment
sim = ltpy.Simulation("draft4.asc")

#set up pulse source,resistor and capacitor
pulse = ltpy.VoltageSource("V1", "in", "0", 0, 5, delay_time="10u", rise_time="1u", fall_time="1u", pulse_width="1u", period="10u") 
R1 = ltpy.Resistor("R1", "in", "out", 10e3) 
C1 = ltpy.Capacitor("C1", "out", "0", 0.1e-6)

## Note: pulse_width = ton in LTspice simulator.
#This creates a pulse source named "V1" with a 1 kHz frequency, 10 kΩ resistor named "R1", and a 0.1 µF capacitor named "C1".

#un the simulation:
sim.run_sim()

#change the pulse width parameter to either 25,50,75 and 100% as 
pulse.param["pulse_width"] = "7.5u"

#run the new simulation with new duty cycles.
sim.run_sim()

