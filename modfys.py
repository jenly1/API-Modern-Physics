"""
A physics API.

This module is a library consisting of the most frequently used equations in the physics course "SH1014 Modern Fysik", especially from the areas: 
Special Relativity, Quantum Mechanics and Particle Physics. Beside calculating different values, one will also be able to get information about the Standard Model. 

The module will cover:
Special Relativity: Lorentz factor, time dilation, length contration, relativistic energy, relativistic kinetic energy, relativistic momentum, relative velocity
Quantum Mechanics: Planck's law, energy levels and transmission- and reflection probability
Particle Physics: Information about the elementary particles and its interactions in the Standard Model 
"""

# Import nescessary modules
import math         # Math operations
import re           # Regular expression for testing input
import json         # File format

# Import data
from data import particle_symbols, particles, interactions_names, interactions

# Constants
c = 3e8             # Speed of light in vacuum
h = 6.62618e-34     # Planck's constant 
k = 1.38065e-23     # Boltzmann's constant

# -------------------------------------------------------- TEST FUNCTIONS -------------------------------------------------------------------
def check_number(n):
    """ Controls input with regex.

    The function controls that input is either an intenger or a float by using regular expression to match character combinations.

    Args:
        n (int or float): arbitrary number 

    Returns:
        n if successful input, error otherwise.
    """

    # If correct input, return True.
    # Else, return False.
    match = re.match('^\d+\.?\d+(e[\-\+]\d+)?$', str(n))
    if match:
        return True
    else:
        print("Tried to enter something else than a number.")
        return False

def check_speed(v):
    """ Controls input.

    The function controls that the velocity (input) doesn't exceed the speed of light.

    Args:
        v (int or float): velocity

    Returns: 
        v if successful input, error otherwise.
    """

    # Check if input is a number
    check_number(v)

    # If velocity is higher than the speed of light, return False.
    # Else, return True.
    if float(v) > c:
        print("Tried to enter a velocity higher than the speed of light.")
        return False
    else:
        return True

# -------------------------------------------------------- PHYSICS FUNCTIONS ----------------------------------------------------------------

def lorentz(v): 
    """ Calculates the Lorentz factor.

    The Lorentz factor is the factor by which time, length, and relativistic mass change for an object while that object is moving.

    Args:
        v (int or float): velocity of system S'
    """

    check_speed(v)
    if v == c:
        print("Tried to divide by 0.")
    return math.sqrt(1/(1-(v)**2/(c)**2))

def time(v, t0):
    """ Calculates the time dilation t.

    Args:
        v (int or float): velocity of system S'
        t0 (int or float): the time in system S
    """

    check_speed(v)
    check_number(t0)
    gamma = lorentz(v)
    return t0*gamma

def length(v, l0):
    """ Calculates the length contraction.

    Args:
        v (int or float): velocity of system S'
        l0 (int or float): the length of the object in system S
    """

    check_speed(v)
    check_number(l0)
    gamma = lorentz(v)
    return l0/gamma

def energy(v, m):
    """ Calculates the relativistic energy.

    Args:
        v (int or float): velocity of system S'
        m (int or float): mass of the particle
    """

    check_speed(v)
    check_number(m)
    gamma = lorentz(v)
    return gamma*m*c**2

def kenergy(v, m):
    """ Calculates the relativistic kinetic energy.

    Args:
        v (int or float): velocity of system S'
        m (int or float): mass of the particle
    """

    check_speed(v)
    check_number(m)
    gamma = lorentz(v)
    return (gamma-1)*m*c**2

def momentum(v, m):
    """ Calculates the relativistic momentum.

    Args:
        v (int or float): velocity of system S'
        m (int or float): mass of the particle
    """

    check_speed(v)
    check_number(m)
    gamma = lorentz(v)
    return gamma*m*v

def velocity(v, u):
    """ Calculates the relative velocity 

    Args:
        v (int or float): velocity of system S'
        u (int or float): velocity of system S
    """

    check_speed(v)
    check_number(u)
    return (u+v)/(1+(u*v)/c**2)

def planck(f, T):
    """ Calculates Planck's law I. 

    Planck's law I describes the spectral density of electromagnetic radiation emitted by a black body in thermal equilibrium at a given frequency f and temperature T. 

    Args:
        f (int or float): freauency 
        T (int or float): temperature
    
    Returns: 
        I (int or float) 
    """

    # Checks if arguments are numbers
    for arg in [f, T]:
        check_number(arg)
    return (2*h*f**3)/(c**2*((math.e)**((h*f)/(k*T))-1))

def transmission(m, a, U0, E):
    """ Calculates the transmission coefficient T.

    The transmission coefficient T describes the amplitude, intensity, or total power of a transmitted wave relative to an incident wave.

    Args:
        m (int or float): mass of the particle
        a (int or float): distance
        U0 (int or float): barrier height
        E (int or float): incoming particle energy

    Returns: 
        T (int or float) 
    """

    # Checks if arguments are numbers
    for arg in [m, a, U0, E]:
        check_number(arg)

    # Different criterias
    if E > U0:
        numerator = math.sin(math.sqrt(2*m*(E-U0))*(2*math.pi*a/h))**2
        denominator = numerator+(4*E*(E/U0-1))/U0
        T = numerator/denominator
        return T
    else:
        numerator = math.sinh(math.sqrt(2*m*(U0-E))*(2*math.pi*a/h))**2
        denominator = numerator+(4*E*(1-E/U0))/U0
        T = numerator/denominator
        return T

def reflection(m, a, U0, E):
    """ Calculates the emission coefficient.

    The reflection coefficient R describes how much of a wave is reflected by an impedance discontinuity in the transmission medium. 

    Args:
        m (int or float): mass of the particle
        a (int or float): distance
        U0 (int or float): barrier height
        E (int or float): incoming particle energy

    Returns: 
        R (int or float) 
    """

    # Checks if arguments are numbers
    for arg in [m, a, U0, E]:
        check_number(arg)
    
    # Different criterias
    if E > U0:
        numerator = (4*E*(E/U0-1))/U0
        denominator = math.sin(math.sqrt(2*m*(E-U0))*(2*math.pi*a/h))**2+(4*E*(E/U0-1))/U0
        R = numerator/denominator
        return R
    else:
        numerator = (4*E*(1-E/U0))/U0
        denominator = math.sinh(math.sqrt(2*m*(U0-E))*(2*math.pi*a/h))**2+(4*E*(1-E/U0))/U0
        R = numerator/denominator
        return R

def energy_lvl(m, a, n):
    """ Calculates the energy levels within a particle.

    A quantum mechanical system or particle that is bound can only take on certain discrete values of energy defined by n=1,2,3..., called energy levels.

    Args:
        m (int or float): mass of the particle
        a (int or float): distance
        n (int): n=1,2,3... (level)

    Returns:
        Energy level n (int or float)
    """

    # Checks if arguments are numbers.
    for arg in [m, a]:
        check_number(arg)

    # Checks if n is a positive intenger with regex.
    # Will otherwise throw a error message.
    match = re.match('^[1-9]+', str(n))
    if match:
        return (n*h)**2/(8*m*(a**2))
    else:
        return "n can only be a positive intenger."

# -------------------------------------------------------- PHYSICS INFORMATION ---------------------------------------------------------------

def model(choice):
    """ Displays information from the Standard Model.

    Args:
        choice (str): choice of name that you want to display information about.

    Returns:
        Desired information in json-format.
    """

    # If intput=particles, display the particle symbols. 
    if choice == "particles":
        return particle_symbols

    # If input=interactions, display the interactions' names.
    elif choice == "interactions":
        return interactions_names
    
    # Otherwise, check and display if given input is a particle or a interaction.
    else:
        for particle in particles:
            if particle['symbol'] == choice:
                return json.dumps(particle, indent=2)
        for interaction in interactions:
            if interaction['interaction'] == choice:
                return json.dumps(interaction, indent=2)
    
    # If input cannot be found.
    return "The requested name was not found. If you entered the name manually please check your spelling and try again."
        
