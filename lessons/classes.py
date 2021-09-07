
class Planet:

    # Class Variable
    shape = 'Spherical'

    # Class method, accessible by all instances/objects and by the class itself
    @classmethod
    def commons(cls):
        return f'Planets are a {cls.shape} shape due to gravity.'

    # A method that only takes the provided input and does not assign it. Consistent across all instances. Callable on class level.
    @staticmethod
    def spin(speed = '[Speed Unknown]'):
        return f'The Planet spins at a speed of: {speed}'

    # The init funtion is similar to a constructor
    def __init__(self, name, radius="Unknown", gravity="Unknown", system="Unknown"):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return(f'{self.name} is orbiting in the {self.system}')

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
