import modfys as mf

# Compute the lorentz factor
print(mf.lorentz(27e7))
# Output: 2.29415733871 

# Display information about the electron
print(mf.model("e"))
# Output:
#{
#  "main class": "lepton", 
#  "antiparticle": "positron", 
#  "mass": "510.10 keV/c^2 = 9.11e-31 kg", 
#  "particle": "electron", 
#  "particle type": "fermion", 
#  "electric charge": "-1.60e-19 C", 
#  "symbol": "e", 
#  "interactions": "strong, weak, electromagnetic, gravity", 
#  "spin": "1/2"
#}