#!/usr/bin/python3

'''
Created on 6 May 2015

@author: matthew

Goal: Get familiar with all the built in functions of Python
'''
import sys
if sys.version_info[0] < 3:  # REQUIRE VERSION 3.0 or higher of Python
    raise Exception("Python 3 or a more recent version is required.")
    quit(1)
def nl(): print('-'*50) # create a separation between blocks of code in the print order. Basically like a <hr> in HTML

"""Start"""
#abs(x)
print("abs(x) of -3: {}; 2.0001: {}; -4531: {};".format(abs(-3), abs(2.0001), abs(-4531)))
nl()
#all(iterable)
print("all(tuple with 0):{}; all(list without 0):{}".format(all((33,0,1)),all([5,1,1])))
nl()
#ascii(object)
print("ascii(object) of unicode é:{}, д:{}".format(ascii("é"),ascii("д")))
nl()
#bin(x) #Works only with integers
print("bin(x) of 2:{}, -2:{}".format(bin(12),bin(-8)))
nl()
#class bool([x])
for item in (-3,0,1):
    print("class bool([x]) of {}:{}".format(item,bool(item)))
nl()
#
#
#Callable(method/other) (checks if it has __call__() method
for item in (True,False,abs,int,str,exit):
    print("callable() of {}:{}".format(item,callable(item)))
nl()
#chr(i) for i in range 0 through 1,114,111 (UNICODE) #ord() does inverse
for i in (0,5,55,115):
    print("chr() of {}:{}".format(i,chr(i)))
nl()
#classmethod
nl()
#compile
nl()
#class complex([real[, imag]])
for item in (1, -1, '3+2j'):
    print("complex() of {}:{}".format(item,complex(item)))
print("complex() of {}:{}".format((2,-3),complex(2,-3)))
a,b=complex("2-33j"), complex("-3+12j")
print("Can add, multiply complex: {}+{}={}; {}*{}={}".format(a,b,a+b,a,b,a*b))
nl()
#delattr(object, name) <-deletes it from Class not instance!
class Foo():    x,y,z=22,-33,complex("2+1j")
bar=Foo()
print(bar.z)
delattr(Foo,'z')
del Foo.x
#print(bar.z) throws error FIXME
nl()
#dict->4
nl()
#dir([object])
print("dir() shows *list* of accessible modules and defined variables: "+str(dir()))
print("dir(dict) shows *list* of attributes for the dictionary object: "+str(dir(dict)))
nl()
#divmod(a, b) ->(a // b, a % b) OR for float: (q,a%b) where q = math.floor(a / b) (maybe 1 less)<- q=float!
for a,b in ((2,1),(-4,2), (444,10),(8.4,4)):
    print("divmod({},{}):{}".format(a,b,divmod(a,b)))
nl()
# enumerate(iterable, start=0)
seqDays=["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
print("enumerate({}):{}".format(seqDays, list(enumerate(seqDays))))
print("enumerate({},{}):{}".format(seqDays,1, list(enumerate(seqDays,1))))
nl()
#eval(expression, globals=None, locals=None) TODO: what about globals/locals (and next)
for item in ("2+5","44*2","a+b"):
    print("eval({}):{}".format(item,eval(item)))
nl()
#exec(object[, globals[, locals]]) TODO: try with code object
s="print('Hello World!')\nprint('end')\n"
print("exec({}) executes the code, returns none. quit() will exit entirely!".format(s))
print(exec(s))
nl()
#filter(function, iterable) ======(item for item in iterable if function(item))
def contE(item): 
    if 'e' in item: return True; return False 
print(list(filter(contE,seqDays)))
print(list(filter(None,[0,33,22-22,-3,0])))
#float([x]) #empty is ok, but not ""
print("empty: "+str(float()))
for lit in ("   -3.14","nan","-InfinItY","+1e-2", "5.1e12"):
    print("float({}): {}".format(lit, float(lit)))
nl()
#format(value[, format_spec]) #without spec, it is like str(value)
print("Format(22): "+format(22))
print("Format(22,'+'): "+format(22,'+')) #Link to 6 for string operations
nl()
# class frozenset([iterable]) # make into a frozen set
print(type(frozenset(["this", 'is','frozen'])))
print(frozenset(["this", 'is','frozen']))
nl()
#getattr(object, name[, default])
print("getattr(Foo, 'y'): {}".format(getattr(Foo, 'y'))) #x will rais attribute error because it was deleted
print(getattr(Foo, 'x', "the attribute \'x\' doesn\'t exist")) #DEFAULT is very handy!
nl()
#globals() #dictionary of current module 
print(globals())
nl()
#hasattr(object, name)
for item in ('x','y','z'):
    print("hasattr(bar, {}): {}".format(item, hasattr(bar, item)))
nl()
#hash(object)
for i in (1,1.0,-33,33.3, "Hello"):
    print("hash({}): {}".format(i, hash(i)))
nl()
#help()
#help(list) e.g. - best used in interactive mode
#hex() returns 0x__ as lowercase hexdecimal value for integer. Use float.hex() for floats; int() for string
for i in (1,321,-33,-44):
    print("hex({}): {}".format(i, hex(i)))
nl()
#id() - memory address
b=a
for item in (a,b, 22, seqDays):
    print("id({}): {}".format(item, id(item)))
print("id({})==id({}):{}; a is b:{}; id({}) *is* id({}):{}".format(a,b,id(a)==id(b),a is b,a,b,id(a)is id(b)))
nl()
#input([prompt])
print('input("Enter random number: ")'+"---suspended")
nl()
# class int(x, base=10) #x is considered as base, and return value is of base 10. Therefore digits in x must be smaller than base. e.g "211",2 throws error!
for i,j in (['010',8],['-33',21],['255',16],["1001",2]):
    print("int({},{}): {}".format(i,j, int(i,j)))
nl()
#isinstance(object, classinfo)
print("isinstance(bar, Foo): {}, isinstance(2,str):{}".format(isinstance(bar, Foo), isinstance(2, str)))
nl()
#issubclass(class, classinfo) #Note: class is considered subclass of self
for c,s in ([Foo,Foo],[Foo,Foo]): #TODO: make more examples...
    print("issubclass({},{}):{}".format(c,s,issubclass(c, s)))
nl()
#iter(object[, sentinel])
with open('mydata.txt') as fp: #TODO: is this equal to fp=open(...)???
    for line in iter(fp.readline, ""): #TODO: get better handle on usage
        print(line)
nl()
#len(x)
for item in ("a,b, 22",range(0,22), seqDays):
    print("len({}):{}".format(item,len(item)))
nl()
# class list([iterable])
print(range(2,17,2), list(range(2,17,2)))
nl()
#locals() #can be used in functions to return 'free' variables
print(locals()) #can (but shouldn't!) assign it to dict (is!) and then change things.
nl()
#map()
def addSpace(item,item2): return item+' '+item2
print(list(map(addSpace,seqDays, seqDays))) #for each element in shortest list, calls function to pair (depending on how many arguements it takes.
nl()
#max(iterable, *[, key, default])
for lst in ([],[1,2,5],['005','9']):
    print("max({}, default=0,key=int):{}".format(lst,max(lst,default=0,key=int))) #another key is str.lower to normalise
print(max(66,-22)) # max(arg1, arg2, *args[, key])
nl()
# memoryview(obj)
v= memoryview(b'abcdefg')
print(str(v), v[1],v[5])
nl()
#min(iterable, *[, key, default])
for lst in ([],[1,2,5],['005','9']):
    print("min({}, default=0,key=int):{}".format(lst,min(lst,default=0,key=int))) #another key is str.lower to normalise
print(min(66,-22)) # min(arg1, arg2, *args[, key])
nl()
#next(iterator[, default])
with open('mydata.txt') as fp:
    a=iter(fp.readline, "")
    print(a,next(a,0),next(a,'0'))
nl()
#class object
o=object()
print(o,"dict is a subclass of object: ",issubclass(dict, object))
nl()
#oct(x)
for i in [2,33,-2]:
    print("oct({}): {}".format(i,oct(i)))
nl()
#open()
""""x=open("newCreatedFile", mode='x', buffering=1, encoding='UTF-8', errors=None, newline=None, closefd=True, opener=None)
print("random line", file=x) #can be used to out to a file
print('line 2', file=x,end=''), print(" line 2, part 2", file=x)
x.close
del x"""
x2=open("newCreatedFile", mode='a',) #TODO: study more and esp. how to seek and write in specific places
print(x2)
x2.close()
del x2
nl()
#ord(c) #opposite to char(c) - gives code for unicode character
print("ord('d'):{}".format(ord('d')))
print("ord('\u2020'):{}".format(ord('\u2020')))
nl()
#pow(x, y[, z])
for x,y,z in ([2,4,3],[-22,3,1]):
    print("pow({},{},{}):{}".format(x,y,z,pow(x,y,z)))
nl()
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(2,3,5,3, sep='+', end='=?\n', file=sys.stdout, flush=True)
nl()
#property #TODO
nl()
#range([start,] stop[, step])
print(list(range(1,33,3)))
nl()
#repr(object)
for obj in (object,True,i):
    print(repr(obj))
nl()
#reversed(seq)
l=[1,2,4,56,6]
lr=list(reversed(l)) #==list(l.__reversed__())
print("list(reversed({})): {}".format(l,lr))
nl()
#round(number[, ndigits])
print("round()\n)", round(2.431),type(round(2.431)))
print(round(2.431,2),type(round(2.431,2)))
nl()
# class set([iterable])
print("set({}):{}; type(set({})):{}".format(l,set(l),l,type(set(l))))
nl()
#
def prtr(func,varz, kws=None,result=1):
    if not kws:
        for prs in varz:
            exec("globals()['result']={}(*{})".format(func,prs))
            print("{}({})={}".format(func,prs,globals()['result']))
    else:
        for pr,kw in zip(varz,kws):
            exec("globals()['result']={}({},{})".format(func,pr,kw))
            print("{}({},{})={}".format(func,pr,kw,globals()['result']))
    nl()
prtr('round',[2.111, 3.2],[2,0])
#setattr(object, name, value) 
setattr(bar, 'd', 55)#==bar.d=55 (if d does not yet exist, it must be quoted)
print(bar.d)
nl()
# class slice(start, stop[, step]) #TODO:
#sorted(iterable[, key][, reverse])
class eg:
    def __init__(self, n):
        self.n=n
lstClasses=[eg(22),eg(33),eg(2),eg(3421),eg(20)]
print([item.n for item in lstClasses])
lstClasses=sorted(lstClasses, key=lambda e: e.n, reverse=True) #Sorted doesn't change the original! It just returns a sorted copy
print([item.n for item in lstClasses])
nl()
#str(object=b'', encoding='utf-8', errors='strict'
print(str(b'fsef', encoding='ascii', errors=''))
nl()
#sum(iterable[, start])
print('sum:'+str(sum([item.n for item in lstClasses], -3000))) #Adds iterable to [start]
nl()
#super([type[, object-or-type]])
print(super(str))#TODO: figure out the use of this when learning classes
nl()
# tuple([iterable])
print(lstClasses, tuple(lstClasses))
nl()
# class type(name, bases, dict)
print(type(bar), bar.__class__) #Can be used with more arguments to create a class
nl()
#vars([object])
print(vars(bar), vars(Foo))
nl()
#zip(*iterables)
z=zip([1,2,3], [4,5,6])
print(list(z),z)
z=zip([1,2,3], [4,5,6]) # the zip dies after use!!!
print(list(zip(*[(1, 4), (2, 5), (3, 6)])), list(zip(*z)))#to unzip, use *
nl()
#Don't need to use __import__ for now.
'''END'''

