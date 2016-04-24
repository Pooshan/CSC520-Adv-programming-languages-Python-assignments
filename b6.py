    
def increment_counter(method):
    def wrapper(self, *args, **kw):
        self._COUNTER += 1
        print ("call %s to %s" % (self._COUNTER,method.__name__))
        return method(self, *args, **kw)
    return wrapper
    
class A():
    _COUNTER = 0

    @increment_counter
    def foo(self,a,b,c):
        return a+b+c
a=A()
#print a.foo(1,3,4)
#print a.foo('a','b','c')
    
_COUNTER=0
def increment_counter1(method):
    def wrapper(*args, **kw):
        global _COUNTER
        _COUNTER += 1
        print ("call %s to %s" % (_COUNTER,method.__name__))
        return method( *args, **kw)
    return wrapper

@increment_counter1
def foo(a,b,c):
    return a+b+c
print(foo(1, 2, 3)) 
print(foo('a', 'b', 'c'))