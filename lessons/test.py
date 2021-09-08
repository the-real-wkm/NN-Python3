from classes import Planet

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
naboo = Planet('Naboo', 300000, 8, 'Naboo System')

print(f'''\nName: {hoth.name}
Radius: {hoth.radius}
Gravity: {hoth.gravity}

{hoth.orbit()}

-----

Name: {naboo.name}
Radius: {naboo.radius}
Gravity: {naboo.gravity}

{naboo.orbit()}

-----

{Planet.commons()}
{Planet.spin(2000)}\n''')
