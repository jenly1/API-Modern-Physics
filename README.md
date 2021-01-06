# Modern Physics

This physics API enables one to compute frequently used equations in the physics course "SH1014 Modern Fysik" (see formulary) and receive basic information about the elementary particles in the Standard Model and its four fundamental forces.  

The module will cover the following areas:

- *Special Relativity:* Lorentz factor, time dilation, length contraction, relativistic energy, relativistic kinetic energy, relativistic momentum, relative velocity

- *Quantum Mechanics:* Planck's law, energy levels and transmission- and reflection probability

- *Particle Physics:* Information about the elementary particles and its interactions in the Standard Model 

## Usage

The functions (equations) and its arguments:

- *Special Relativity:*

lorentz(v)

time(v, t0)

length(v, l0)

energy(v, m)

kenergy(v, m)

momentum(v, m)

velocity(v, u)

- *Quantum Mechanics:*

planck(f, T)

transmission(m, a, U0, E)

reflection(m, a, U0, E)

energy_lvl(m, a, n)

- *Particle Physics:*

model(choice)

For every function except "model", the arguments must be an intenger or a float. It is possible to use *e* to indicate “times 10 to the power of”. 
For the “model” function, the argument must be a string. Different choices:

- To recieve all particle symbols, use model("particles").

- To recieve all interactions names, use model("interactions")

- To recieve information about a specific particle or interaction, type in its particle symbol or interaction name.

## Example

**Definition:** 
````
>>> import modfys as mf
>>> mf.lorentz(27e7)
>>> mf.model("e")
````

**Response:**
```
2.29415733871
```

```json
{ 
    "particle":"electron",
    "symbol":"e",
    "mass": "510.10 keV/c^2 ≈ 9.11e-31 kg",
    "electric charge":"≈ -1.60e-19 C",
    "spin": "1/2",
    "particle type":"fermion",
    "main class":"lepton",
    "antinparticle":"positron",
    "interactions":"strong, weak, electromagnetic, gravity",    
}
```

## Installation

1. You will need to install [python](https://www.python.org/downloads/)
2. You will need to download the files: modfys.py and data.py.

