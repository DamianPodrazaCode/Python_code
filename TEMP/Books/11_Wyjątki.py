# print(1/0) #ZeroDivisionError: division by zero
x = 1
y = 0
try :
    # tutaj kod w który szuka sięwyjątku
    print(x/y)
except ZeroDivisionError: 
    print('tu obsługiwany jest tylko wyjątek dzielenia')
except (ZeroDivisionError, IOError): 
    print('można obsłużyć kilka wyjątków')
except:  # wszystkie wyjątki można obsługiwać tylko na końcu 
    print('tu obsługujemy wszystkie wyjątki')    

'''
IndentationError 	    Raised when indentation is not correct
LookupError 	        Raised when errors raised cant be found
ReferenceError 	        Raised when a weak reference object does not exist
RuntimeError 	        Raised when an error occurs that do not belong to any specific exceptions
SyntaxError 	        Raised when a syntax error occurs
TabError 	            Raised when indentation consists of tabs or spaces
SystemError 	        Raised when a system error occurs
TypeError 	            Raised when two different types are combined
UnboundLocalError 	    Raised when a local variable is referenced before assignment
UnicodeError 	        Raised when a unicode problem occurs
UnicodeEncodeError 	    Raised when a unicode encoding problem occurs
UnicodeDecodeError 	    Raised when a unicode decoding problem occurs
UnicodeTranslateError 	Raised when a unicode translation problem occurs
ValueError 	            Raised when there is a wrong value in a specified data type
'''
try:
    print(1/0)
except:
    print("wyjątek dzielenia")
finally:
    print("co by się nie działo to ja się uruchamiam")

try:
    print("info")
except ValueError:
    print("wyjątek")
else:
    print("nie bylo wyjatku")

try:
    raise TypeError() # wywołanie wyjątku
except TypeError:
    print("to było do przewidzenia...")    