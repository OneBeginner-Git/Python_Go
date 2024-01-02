# %%
class Dog(object):

    def __init__(self, name, age):  # 默认方法
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")


dog1 = Dog("ada", 1)
print("My dog name is " + dog1.name.title() + ".")
print("My dog is " + str(dog1.age) + " year(s) old.")

dog1.sit()
dog1.roll_over()

dog2 = Dog("bob", 3)
print("My dog name is " + dog2.name.title() + ".")


# %%
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.waiters_num: int = 2
    def describe_restaurant(self):
        print("Restaurant name is {}.".format(self.restaurant_name))
        print("Cuisine type is {}.".format(self.cuisine_type))
        print("There are {:d} waiters here.".format(self.waiters_num))

    def open_restaurant(self):
        print("Restaurant {} is opening now!".format(self.restaurant_name))

    def employ_new_waiters(self, new_number:int):
        print("We hired {:d} new waiters here.".format(new_number))
        self.waiters_num += new_number
    def get_waiters_num(self):
        print("We have {:d} waiters now!".format(self.waiters_num))


restaurant1 = Restaurant("KFC", "Fried Chicken")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.employ_new_waiters(10)
restaurant1.get_waiters_num()
restaurant1.get_waiters_num()
restaurant1.get_waiters_num()



# %%

# %%
