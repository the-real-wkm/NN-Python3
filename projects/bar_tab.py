class Tab:

    menu = {
        'Wine': 5,
        'Beer': 3,
        'Soda': 2,
        'Shot': 5,
        'Pepperoni Pizza': 12,
        'Cheese Pizza': 10,
        'Meats Pizza': 15,
        'Veggie Pizza': 15,
        'Ice Cream': 4
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_total(self, tax_rate, tip_prcnt):
        tax = (tax_rate/100) * self.total
        tip = (tip_prcnt/100) * self.total
        total = self.total + tax + tip

        print('\nRECIEPT\n\n------------------\n')

        for item in self.items:
            print(f'{item:16} | ${self.menu[item]:.2f}')

        print(f'''
------------------
        
{f'Tax ({tax_rate}%): ':13} ${tax:.2f}
{f'Tip ({tip_prcnt}%): ':13} ${tip:.2f}
{"Total:":13} ${total:.2f}''')

