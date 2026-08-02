# 🐍 Python Mutable Default Arguments Explained

> **Core Concept:**
> Understanding how Python creates functions, stores default arguments, binds parameters, manages mutable and immutable objects, and allocates memory.

---

# 📝 Problem Statement

### Given Code (Buggy)

```python
def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart

print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))
```

### Output

```python
['pen']
['pen', 'book']
['pen', 'book', 'bag']
```

---

### Expected Output

```python
['pen']
['book']
['bag']
```

---

### Correct Solution

```python
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart

print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))
```

### Output

```python
['pen']
['book']
['bag']
```

---

# ❓ Why Does the First Program Fail?

The issue is **not** simply because lists are mutable.

The real reason is:

> **Python evaluates default arguments only once—when the function is defined, not every time the function is called.**

When Python executes

```python
def add_to_cart(item, cart=[]):
```

it immediately creates a function object.

```
Heap Memory
────────────────────────────────────────────

Function Object

__defaults__
     │
     ▼
     []
```

The list is created **only once**.

Every function call that does not provide `cart` receives a reference to **the same list**.

---

## First Call

```
cart
 │
 ▼
[]

↓

append("pen")

↓

["pen"]
```

---

## Second Call

```
cart
 │
 ▼
["pen"]

↓

append("book")

↓

["pen", "book"]
```

---

## Third Call

```
cart
 │
 ▼
["pen", "book"]

↓

append("bag")

↓

["pen", "book", "bag"]
```

---

# ✅ Why Does `None` Fix the Problem?

When Python executes

```python
def add_to_cart(item, cart=None):
```

the function object stores

```
Heap Memory

Function Object

__defaults__

 │
 ▼

None
```

Every function call starts with

```
cart

↓

None
```

Then

```python
if cart is None:
    cart = []
```

creates a **brand new list**.

Every function call therefore gets its own independent list.

---

# 📚 Question 1 — What is Mutable and Immutable?

## Mutable Objects

A mutable object **can be modified after it is created**.

Examples

```
list
dict
set
bytearray
```

Example

```python
a = [1, 2]
a.append(3)
```

Result

```
[1, 2, 3]
```

The same list object is modified.

---

## Immutable Objects

An immutable object **cannot be modified after it is created**.

Examples

```
int
float
bool
str
tuple
frozenset
None
```

Example

```python
a = 10
a = a + 5
```

Python creates a **new integer object**.

```
10

↓

15
```

The integer **10 is never modified**.

---

# 📚 Question 2 — When Are Default Arguments Created?

Default arguments are created **only once**, when Python executes the `def` statement.

Example

```python
def fun(a=[]):
    pass
```

Python internally performs

```
Create list

↓

Create function object

↓

Store reference in __defaults__
```

The default object is **not recreated** on every function call.

---

# 📚 Question 3 — Scope of Default Arguments

The parameter

```python
a
```

is always a **local variable**.

The default value belongs to the **function object**.

```
Heap

Function Object

__defaults__

↓

[]
```

During a function call

```
Stack Frame

a

↓

same list
```

Every function call creates a **new local parameter**.

---

# 📚 Question 4 — Does Assignment Change the Default Argument?

No.

Example

```python
def fun(a=None):
    a = []
```

Initially

```
Local Variable

a

↓

None
```

After assignment

```
Local Variable

a

↓

[]
```

Only the **local variable** changes.

The function object's default value remains

```
None
```

---

# 📚 Question 5 — Why Do Mutable Defaults Persist But Immutable Ones Don't?

Mutable objects are modified **in place**.

Example

```python
def fun(a=[]):
    a.append(1)
```

The same list becomes

```
[]

↓

[1]

↓

[1,1]

↓

[1,1,1]
```

---

Immutable example

```python
def fun(a=10):
    a += 1
```

Python creates

```
10

↓

11
```

The original integer is unchanged.

---

# 📚 Question 6 — Is `None` Mutable?

No.

`None` is immutable.

Python contains **exactly one `None` object**.

Example

```python
a = None
b = None

print(a is b)
```

Output

```python
True
```

---

# 📚 Question 7 — Why Use `None`?

`None` means

> **"No value was supplied."**

It acts as a sentinel value.

Example

```python
def fun(a=None):
    if a is None:
        print("User didn't pass anything.")
```

---

# 📚 Question 8 — Why Is `None` Used for Mutable Defaults?

Instead of

```python
def fun(a=[]):
```

we write

```python
def fun(a=None):
    if a is None:
        a = []
```

Result

* New list every function call
* No shared mutable object
* Independent function calls

---

# 📚 Question 9 — What Happens If the User Passes a Value?

Example

```python
def fun(a=[]):
    pass

fun([100])
```

Python ignores the default argument.

The parameter becomes

```
a

↓

[100]
```

The parameter points **only** to the user-provided object.

It never points to both the default object and the user object.

The default value stored in the function object remains unchanged.

---

# 📚 Question 10 — How Is Python Memory Organized?

Simplified memory model

```
Python Process

────────────────────────

Call Stack

↓

Local Variables

Parameters

Function Calls

────────────────────────

Heap

↓

Objects

Lists

Functions

Classes

Strings

Integers

None

────────────────────────

Garbage Collector
```

Unlike Java, Python does **not** officially expose memory regions such as a Constant Pool or Method Area.

Function objects, lists, classes, instances, strings, and default argument objects all reside on the **heap**.

---

# 📚 Question 11 — Does `a = 10` Then `a = 25` Point to Both Objects?

No.

Initially

```
a

↓

10
```

After

```python
a = 25
```

```
a

↓

25
```

The variable always points to **one object at a time**.

The integer `10` continues to exist only if another reference still points to it.

Otherwise, Python eventually frees it.

---

# 📚 Question 12 — If the User Passes a Value, Does the Default Stop Pointing to Its Value?

No.

Example

```python
def fun(a=100):
    pass
```

Function object

```
Function Object

__defaults__

↓

100
```

Call

```python
fun(500)
```

Local variable

```
a

↓

500
```

The function object's default remains

```
100
```

It is simply **not used** during that function call.

---

# 🧠 Complete Memory Diagram

## Safe Version (`None`)

```
Heap
──────────────────────────────────────

Function Object

__defaults__

 │
 ▼

None
```

### First Call

```
Stack Frame

cart

↓

None

↓

cart = []

↓

["pen"]
```

Function returns

```
Stack Frame Destroyed

cart ❌

↓

List has no references

↓

Garbage Collector removes it
```

---

### Second Call

```
Stack Frame

cart

↓

None

↓

[]

↓

["book"]
```

Every function call creates a **new list**.

---

## Buggy Version (`[]`)

```
Heap

Function Object

__defaults__

 │
 ▼

[]
```

Call 1

```
cart

↓

same list

↓

["pen"]
```

Call 2

```
cart

↓

same list

↓

["pen", "book"]
```

Call 3

```
cart

↓

same list

↓

["pen", "book", "bag"]
```

The same list survives because the function object's `__defaults__` attribute still references it.

---

# 🎯 Three Rules to Remember

1. **Default arguments are evaluated only once**, when the function is defined.

2. **Parameters are local variables.** Every function call creates new parameter variables that reference either the default object or the user-provided object.

3. **Never use mutable objects as default arguments.** Use `None` instead and create the mutable object inside the function.

---

# ✅ Key Takeaways

* Lists are mutable; integers, strings, tuples, and `None` are immutable.
* Default argument objects are created once and stored in the function object's `__defaults__`.
* Parameters are local variables created for every function call.
* Assigning to a parameter changes only the local variable, never the stored default.
* Passing an argument completely overrides the default **for that call only**.
* Function objects and default argument objects live on the **heap**.
* Using `None` as a default argument prevents accidental sharing of mutable objects between function calls.
