class Parent(object):

    def overide(self):
        print("PARENT overide()")

class Child(Parent):

    def overide(self):
        print("CHILD overide()")

dad = Parent()
son = Child()

dad.overide()
son.overide()
