import modfys as mf

# Check test functions 
# Note that the input when using physics functions should NOT be str-type. We are just testing because thats what the test functions should be able to manage.
assert mf.check_number(12345)           == True
assert mf.check_number(12345.6789)      == True
assert mf.check_number(12345.6e-10)     == True
assert mf.check_number("12345.6789")    == True
assert mf.check_number("0.123456789")   == True
assert mf.check_number(".123456789")    != True
assert mf.check_number("12345..6789")   != True
assert mf.check_number("12345.e.6789")  != True
assert mf.check_number("string")        != True

assert mf.check_speed(270000000)        == True
assert mf.check_speed(270000000.0)      == True
assert mf.check_speed("270000000")      == True
assert mf.check_speed("3e+8")           == True
assert mf.check_speed("3e+9")           != True
assert mf.check_speed(400000000)        != True

# Check physics functions 
# The input values are regarding an electron with the mass 0.511 MeV/c^2, speed 0.950c m/s and diameter 5.63588e-15 m. Other values are made up.
# The values on the right side are calculated by hand
c = 3e8
assert mf.lorentz(0.950*c)                              == 3.2025630761017423
assert mf.time(0.950*c, 30)                             == 96.07689228305227 
assert mf.length(0.950*c, 5.63588e-15)                  == 1.7598029659606785e-15
assert mf.energy(0.950*c, 0.511)                        == 1.4728587586991914e+17
assert mf.kenergy(0.950*c, 0.511)                       == 1.0129587586991912e+17
assert mf.momentum(0.950*c, 0.511)                      == 466405273.58807725
assert mf.velocity(0.950*c, 0.999*c)                    == 299992303.94294655
assert mf.planck(5.71e+14, 6000)                        == 2.876849589937414e-08
assert mf.transmission(0.511, 1.1e-9, 30e3, 35e3)       == 0.5227506437381491
assert mf.reflection(0.511, 1.1e-9, 30e3, 35e3)           == 0.47724935626185083
assert mf.energy_lvl(0.511, 1.1e-9, 1)                  == 8.876263806262232e-50




