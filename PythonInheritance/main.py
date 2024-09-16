class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

# child class
class Rabbit(Animal):
    # define a run method
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")



rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# through inheritance
#print(rabbit.alive)
#ish.eat()
#awk.sleep()

rabbit.run()
hawk.fly()
fish.swim()


