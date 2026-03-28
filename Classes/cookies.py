class Cookies:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color



# Application:

cookie_one = Cookies('green')
cookie_two = Cookies('blue')

print('cookie one is', cookie_one.get_color())
print('cookie two is', cookie_two.get_color())
print('\n')

cookie_one.set_color('red')
# print('\n')

print('cookie one is', cookie_one.get_color())
print('cookie two is', cookie_two.get_color())