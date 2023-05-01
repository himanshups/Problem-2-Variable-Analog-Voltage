# Problem-2-Variable-Analog-Voltage
This is the submission task for Problem 2 of Stretch-a-bit: Embedded Systems Engineer (Round 2)

The steps to create simulation of variable voltage source is as follows:

## Step1: Using LTspice simulator: 

1. Open LTSpice and create a new schematic.

2. From the "Component" tab, select the following components and place them on the schematic page:
   - Voltage source (Vpulse)
   - Resistor (R)
   - Capacitor (C)

3. Connect the components as follows:

   - Connect the positive (+) terminal of the voltage source to one end of the resistor.
   - Connect the other end of the resistor to one end of the capacitor.
   - Connect the other end of the capacitor to the negative (-) terminal of the voltage source.

4. Double-click on the voltage source component to open its properties dialog box. In the "Value" field, enter "0 5 pulse(0 1 0 0.5m 0.5m 1k)". This command will give you a 1kHz square wave signal that varies between 0V and 5V with a 50% duty cycle.

5. Double-click on the resistor component to open its properties dialog box. In the "Value" field, enter "10k". This sets the resistance value to 10 kohm.

6. Double-click on the capacitor component to open its properties dialog box. In the "Value" field, enter "0.1u". This sets the capacitance value to 0.1uF.

7. Save your schematic and run the simulation by clicking the "Simulate" button located at the top of the screen.

Note: I have attached the screenshots depicting the output of every duty cycles for 25,50,75,100% in the code folder, please check it.

## Step2: Run LTspice simulations with help of ltspice library.

1. Import the necessary libraries: To communicate with LTspice from Python, you'll need to use the ltpy library. You can import it using the following code:

      import ltpy
   

2. Create a simulation environment: To simulate a circuit in LTspice, you'll need to create a simulation environment. You can do this using the ltpy.Simulation class. Here's an example:

      sim = ltpy.Simulation("example.cir")
   

   Replace "example.cir" with the name of your LTspice circuit file.

3. Set up the pulse source and resistor: You can use the ltpy.VoltageSource and ltpy.Resistor classes to create a pulse source and a resistor. Here's an example:

      pulse = ltpy.VoltageSource("V1", "in", "0", 0, 5, delay_time="10u", rise_time="1u", fall_time="1u", pulse_width="1u", period="10u")
   r = ltpy.Resistor("R1", "in", "out", 10e3)
   c = ltpy.Capacitor("C1", "out", "0", 0.1e-6)
   
   Note: pulse_width = ton in LTspice simulator.

   This creates a pulse source named "V1" with a 1 kHz frequency, 10 kΩ resistor named "R1", and a 0.1 µF capacitor named "C1".

4. Run the simulation: Call the ltpy.run_sim() function to run the simulation. Here's an example:

      sim.run_sim()
   

5. Change the duty cycle: Once the simulation has run, you can change the duty cycle of the pulse source by setting the pulse_width parameter in the pulse object. For example, to change the duty cycle to 75%, you can do the following:

      pulse.param["pulse_width"] = "7.5u"
   

   This sets the pulse_width parameter to 7.5 µs, which is 75% of the period.

6. Run the simulation with the new duty cycle: Call ltpy.run_sim() again to run the simulation with the new duty cycle:

      sim.run_sim()
   

7. Repeat steps 5 and 6 as desired: You can repeat steps 5 and 6 to change the duty cycle as many times as you'd like.

The output and all necessary files have been attached in the folder structure in the given repository, please check it out.

