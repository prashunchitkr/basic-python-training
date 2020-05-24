import operator

print(dir(operator))


# CLASS, OBJECTS, METHODS, ATTRIBUTES, OPERATOR OVERLOADING

class Person:
    '''
    This class describes a person
    The self argement is compulsory in class methods except static methods
    Operator overloading is done through dunder methods or magic functions
    '''
    name = 'adad'

    def __init__(self, name, age):
        '''This is a constructor that takes two argument'''
        self.name = name
        self.age = age

    def describe(self):
        print(f'{self.name} {self.age}')

    def speak(self, to_speak):
        '''Takes an argument and prints following'''
        print(f'{self.name} says {to_speak}')

    def __add__(self, other):
        '''This is an example of operator overloading that overrides + operator'''
        return self.age + other.age

    def __sub__(self, other):
        return abs(self.age - other.age)

    @staticmethod
    def change_name(new_name):
        '''This is a static method that can change static variables'''
        Person.name = new_name


# THE COMMENTED CODE BELOW IS FOR ONE WITHOUT CONSTRUCTOR THAT WAS SHOWN IN CLASS

# p1 = Person()
# print(type(p1))
# p1.describe()

# p1.name = 'John'
# p1.age = 18

# p1.describe()
p1 = Person('John', 18)
print(type(p1))
p1.describe()
p1.speak('Hello')

print(p1.name)
print(p1.age)

p2 = Person('Testing', 20)
p2.describe()

p1.name = 'Apple'
p1.age = 20

print(p1.name)
print(p1.age)

print(Person.__doc__)


# After operator overloading
print(p1+p2)
print(p2-p1)


# INHERITANCE

class Student(Person):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level

    def describe(self):
        super().describe()
        print(f'{self.name} is {self.age} years old and is in {self.level}')


class Worker(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def describe(self):
        super().describe()
        print(f'{self.name} is {self.age} years old and earns {self.salary}')


class Teacher(Worker):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age, salary)
        self.subject = subject

    def describe(self):
        super().describe()
        print(
            f'{self.name} is {self.age} years old and earns {self.salary} and teaches {self.subject}')

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary


s1 = Student('John', 10, 6)
s1.speak('Testing')
s1.describe()

w1 = Worker('Testing', 30, 20000)
w1.describe()

t1 = Teacher('Testing2', 40, 30000, 'CS')
t2 = Teacher('Testing3', 20, 40000, 'CS')

t1.describe()

print(t1 < t2)
print(t1 <= t2)
print(t1 == t2)
print(t1 >= t2)
print(t1 > t2)


# Person -> Worker -> Teacher


# Creating a custom complex class

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def abs_value(self):
        return (self.real**2 + self.imag**2)**0.5

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)

    def __sub__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)

    def __str__(self):
        return '{}+{}i'.format(self.real, self.imag)


c1 = Complex(1, 2)
c2 = Complex(2, 3)
print(abs(c1))


print(c1)
c3 = c1+c2
print(type(c3))
print(c3)
