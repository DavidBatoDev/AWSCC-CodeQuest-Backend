class Student:
    def __init__(self, name='', age=0, gender='Not specified', is_enrolled=False, classes=[], offenses=[]):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses

    def add_class(self, new_class):
        self.classes.append(new_class)


student1 = Student('David')

