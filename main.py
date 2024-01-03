class Restaurant:
    def __init__(self, name: str, address: str, phone_number:str, menu: dict, about: str) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.about = about
        self.menu = menu

    def get_info(self) -> str:
        return f"Restaurant info: {self.name}, {self.address}, {self.phone_number}"
    
    def get_about(self) -> str:
        with open("about.txt", 'r', encoding='utf-8') as failas:
            return failas.read()
        
    def get_menu(self) -> str:
        return 
    



        
    
history = []


while True:
        print("Welcome to our restaurant. Please choose one of the options below:")
        if 1 in history:
            print("1. Reustaurant info [checked]")
        else:
            print("1. Reustaurant info")
        if 2 in history:
            print("2. Restaurant menu [checked]")
        else:
            print("2. Restaurant menu")
        if 3 in history:
            print("3. Table reservation [checked]")
        else:
            print("3. Table reservation")
        print("4. Exit")
        
        choice = input("Choose an option (1, 2, 3 etc.): ")

        if choice == '1':
 
            history.append(1)
        elif choice == '2':
        
            history.append(2)
        elif choice == '3':
         
            history.append(3)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option (1, 2, 3 etc.)")