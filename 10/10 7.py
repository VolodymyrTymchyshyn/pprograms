class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'
        self.fullname="Cracow University Economical"

    # object bahaviors (methods)
    def print_fullname(self):  
        print(self.fullname)
    
    def print_name(self):  
        print(self.name)
        
    def set_fullname(self, fullname):
        self.fullname = fullname
        
    def set_name(self, name):
        self.name = name

c=University()
c.set_fullname("Mes I t ")
c.print_fullname()