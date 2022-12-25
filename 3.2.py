#Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.


def do_four(func , arg):
    func(arg)
    func(arg)
    
def print_twice(arg):
    print(arg)
    print(arg)
    
do_four(print_twice , "xmas")
