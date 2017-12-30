"""
This is a bit advanced stuff..
Here is code that have 2 superclasses and 1 subclass 
which inherits both superclasses. IOW, it’s multiple inheritance.
Now advanced stuff:
There are 3 pairs of print statements at bottom. In each pair, 
1st statement is what end users type, 2nd statement is what 
Python might come up with internally after resolving class tree. 
I wrote 2nd print statements digging deep into Python class semantics.
"""


class sup1:
    """
    class: sup1
    """
    x = ("sup1", 10)
    y = ("sup1", 10)
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return self.data

class sup2:
    """
    class: sup2
    """
    y = ("sup2", 10)
    z = ("sup2", 10)
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return self.data

class sub(sup1, sup2):
    """
    class: sub
    super class: sup1, sup2
    """
    y = ("sub", 10)

I1 = sup1("sup1 class")
I2 = sup2("sup2 class")
I3 = sub("sub class")

print(I1.x, I1.y) 
print(I1.__class__.__dict__["x"], I1.__class__.__dict__["y"])

print(I2.y, I2.z) 
print(I2.__class__.__dict__["y"], I2.__class__.__dict__["z"])

print(I3.x, I3.y, I3.z) 
print(I3.__class__.__bases__[0].__dict__["x"], I3.__class__.__dict__["y"], I3.__class__.__bases__[1].__dict__["z"])

"""
output:
('sup1', 10) ('sup1', 10)
('sup1', 10) ('sup1', 10)
('sup2', 10) ('sup2', 10)
('sup2', 10) ('sup2', 10)
('sup1', 10) ('sub', 10) ('sup2', 10)
('sup1', 10) ('sub', 10) ('sup2', 10)
"""
