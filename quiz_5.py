class fishbread:
    def __init__(self,ingredient,price):
        self.ingredient = ingredient
        self.price = price
        self.total = 0
    def sell(self):
        print(self.ingredient + '을 ' + str(self.price) + '원에 판매했습니다.')
        self.total=self.total+self.price
    def eat(self):
        print(self.ingredient + '을 먹었습니다.')

redbeen_bread = fishbread('팥 붕어빵',1000)
cream_bread = fishbread('슈크림 붕어빵',900)

cream_bread.eat()
redbeen_bread.sell()
redbeen_bread.sell()
redbeen_bread.sell()
redbeen_bread.sell()
redbeen_bread.sell()

print(redbeen_bread.total)
