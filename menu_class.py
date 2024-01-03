from main import Restaurant

class Menu(Restaurant):
    def __init__(self) -> None:
        
        self.food_menu = {}
        self.drinks_menu = {}
        self.dessert_menu = {}

    def add_item(self, item: str, price: float) -> None:
        
        self.food_menu[item] = price
        self.drinks_menu[item] = price
        self.dessert_menu[item] = price

    def remove_item(self, item: str):
        if item in self.food_menu:
            del self.food_menu[item]
        elif item in self.drinks_menu:
            del self.drinks_menu[item]
        elif item in self.dessert_menu:
            del self.dessert_menu[item]

  
    def display_menu(self):
        for item, price in self.food_menu.items():
            print(f"Food menu: {item}: {price}€")
        for item, price in self.drinks_menu.items():
            print(f"Drinks menu: {item}: {price} €")
        for item, price in self.dessert_menu.items():
            print(f"Dessert menu: {item}: {price} €")
        



food_menu = Menu()
drinks_menu = Menu()
dessert_menu = Menu()


food_menu.add_item("Burger", 10.50)
food_menu.add_item("Pizza", 12.00)
food_menu.add_item("Salad", 8.00)
drinks_menu.add_item("Beer", 4.50)
drinks_menu.add_item("Water", 2.00)
drinks_menu.add_item("Juice", 3.00)
dessert_menu.add_item("Ice creame", 4.50)
dessert_menu.add_item("Apple pie", 3.90)
dessert_menu.add_item("Cake", 4.20)


food_menu.display_menu()
# drinks_menu.display_menu()
# dessert_menu.display_menu()





