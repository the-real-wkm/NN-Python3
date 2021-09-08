def planet_mass(grav, r):
    mass = (grav*r**2) / (6.67*10**-11)
    return mass

def planet_vol(r):
    vol = (4*3.142*r**2) / 3
    return vol