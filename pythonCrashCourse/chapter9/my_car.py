from electric_car import ElectricCar
    
my_tesla = ElectricCar('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.battery_size = 100
my_tesla.battery.get_range()
