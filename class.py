# class Student:
#     name=None
#     def say_hi(self):
#         print(f"Hi大家好，我是{self.name}")
#     def say_hi2(self,msg):
#         print(f"Hi大家好，{msg}")
#     def __init__(self,name: str,age: int) :
#         self.name=name
#         self.age=age
#     def __str__(self) -> str:
#         return f"我是一个学生，名字叫{self.name}，年龄是{self.age}"
#     def __lt__(self, other):
#         return self.age>other.age
#     def __le__(self, other):
#         return self.age>=other.age
#
#
# class StudentPlus(Student):
#     addr=None
#     def say_hi(self):
#         print("这是子类的打招呼")
#         Student.say_hi(self)
#
# student1:StudentPlus =StudentPlus("A",13)
# print(student1)
# student2 =StudentPlus("B",13)
# print(student2)
# print(student1 >= student2)
# student2.say_hi()
# x=9     # type: int


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def makenoise(animal: Animal):
    animal.speak()

dog=Dog()
cat=Cat()
makenoise(dog)
makenoise(cat)

