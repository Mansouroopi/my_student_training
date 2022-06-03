class decorator_showname_class(object):
    def __init__(self, myfunc):
        self.myfunc = myfunc

    def __call__(self, *args, **kwargs):
        print("I am going to execute: ", self.myfunc.__name__)
        return self.myfunc(*args, **kwargs)





@decorator_showname_class
def hypotenuse3(a, b):
    return round(float((a*a) + (b*b))**0.5, 2)

print(hypotenuse3(1,2))