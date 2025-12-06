class Factory:
    a = 1 
    def new(other):
        print(f"The class attribute is {other.a}.")
    
    @classmethod
    def work(cls):
        print(f"The class attribute is {cls.a}.")



e = Factory()
e.a = 45
e.new()
e.work()    # Generally, 
            # it shows the object attribute that we have set to 45, but instead,
            #  it shows the class attribute which is 1.




