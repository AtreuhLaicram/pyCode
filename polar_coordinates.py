import cmath  # Imports the complex math module to handle complex numbers

s = input() # Obtains from STDIN a complex number format string type 1+2j
phi = cmath.phase(complex(s)) # Computes the modulus phi angle in radians
r = abs(complex(s)) # Computes the modulus r

print("{:.3f}".format(r)) # Sends  to STDOUT the modulus r up to three decimals
print("{:.3f}".format(phi)) # Sends to STDOUT the angle phi up to three decimals

