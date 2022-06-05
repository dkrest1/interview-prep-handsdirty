def make_pizza(size=20, **toppings):
    print("hello this is a module {}".format(str(size)))
    for topping in toppings:
        print(topping)
