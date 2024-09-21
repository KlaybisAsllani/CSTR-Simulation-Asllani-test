# Simple simulation of a first order Continuous Stirred Tank Reactor (CSTR) 
- Includes response to various types of concentration input stimuli (step changes, ramp inputs, and sinusoidal inputs)
- Incorporation of PID controller to maintain concentration set point 
- Simulates the response of an MPC controller for a heat exchanger model
- Represents a first-order heat exchanger model using Euler's method for discrete-time simulation

#### Description of the System
A liquid stream enters the reactor at a volumetric flow rate **F** and contains reactant **A**. Reactant A decomposes in the reactor according to the irreversible chemical reaction (**A→B**), proceeding at a rate of **r=k*C<sub>a</sub>**

The reactor is modeled with a time constant **𝜏** and a gain **K**. The purpose of the control system is to maintain the concentration of A leaving the reactor at a desired value despite variations in the inlet concentration **C<sub>a</sub><sub>0</sub>**

#### Reactor Formulas
V $\frac{dc}{dt}$ = F*C<sub>a</sub><sub>0</sub> - (F+kv)*C<sub>a</sub>

and

𝜏 $\frac{dc}{dt}$ + C<sub>a</sub> = K*C<sub>a</sub><sub>0</sub> 

where:
- 𝜏 = $\frac{V}{F+kV}$
- K = $\frac{1}{kV/F}$

At steady state, $\frac{dc}{dt}$ = 0, so the equation becomes:
c= K*C<sub>a</sub><sub>0</sub>


#### Reference
Coughanowr, D. R., & LeBlanc, S. E. (2009). *Process Systems Analysis and Control* (3rd ed.). McGraw-Hill Education. Pages 123-124.
