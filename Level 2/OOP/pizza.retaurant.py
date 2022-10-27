class PizzaRestaurant:
    def __init__(self, ingrediente, gramaj, volum):
        self.ingrediente = ingrediente
        self.gramaj = gramaj
        self.volum = volum
    def printIt(pizza):
        print("PizzaRestaurant", pizza.ingrediente, pizza.gramaj, pizza.volum)
        
       
pizza_michael = PizzaRestaurant("ciuperci", 100, "grame")
pizza_marry   = PizzaRestaurant("Brinza", 50, "grame")
pizza_john    = PizzaRestaurant("Rosii", 10, "grame")

PizzaRestaurant.printIt(pizza_michael)
PizzaRestaurant.printIt(pizza_marry)
PizzaRestaurant.printIt(pizza_john)
