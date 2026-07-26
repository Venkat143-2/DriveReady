'''
Given Code:
def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart
print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))
Buggy output:
['pen']
['pen', 'book']
['pen', 'book', 'bag']
Expected output after your fix:
['pen']
['book']
['bag']'''
"my Code"
def add_to_cart(item, cart=None):
    if cart is None:
        cart=[]
    cart.append(item)
    return cart
print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))
'''
what is the difference btw given code and my code
first thing both codes are working well but the difference is in arguments in given code the cart=[] is list which is mutable type but in my code the
cart is not a mutable type first we need to understand what is mutable and immutable types
we need to understand some things:
1)what is meaining for Mutable and immutable
2) when the memory is created for default arugument
3) scope for default arguments
4) when we call the function the reassignment is happen to the default arguments or not
5) why the muttable types are modified every call but the immuttable types are not modified
6) None and the None is muttable or immutable
7) why we use of None keyword
8) why None keyword is used for muttable types
9) when user passes the value to the function which has default args what happen and the default argument points to user provided value only not to default or 
   points to both default and user provided values
'''
