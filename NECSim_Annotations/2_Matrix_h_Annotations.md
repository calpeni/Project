# 2_Matrix.h Annotations

### 'Brief Class Descriptions'
Handles:  
 indexing the 2-D object  
 importing values from csv  

### 'Class Matrix'
contains:  
 Matrix object - array of Row objects  
 importCsv() function for file reading, as well as basic operations  

### header file
template for a matrix with overloaded operations  
used [this](http://www.devarticles.com/c/a/Cplusplus/Operator-Overloading-in-C-plus/1)  
two classes: Row, Matrix  


## #include Directives
`fstream`  
objects the standard library uses for *file* input/output have different types than for standard input/output  
to work with input/output file, must create an object of type ifstream/ofstream - definition of these classes in header `<fstream>`

`cstdlib`  
standard library includes function named rand (defined in `<cstdlib>`) - no arguments, returns random integer in range `[0, RAND_MAX]` - RAND_MAX is a large integer, defined in `<cstdlib>`  
  
`cstring`  
a function called strlen tells us how many characters are in a string literal or other null-terminated array of characters (not counting the null at the end)  

`stdexcept`  
p53 - what we do if vector is empty - complain to whoever running program - throw an exception  
execution stops, and passes to another program part, along with exception object, which contains information caller can use to act on exception  
In this eg, exception we throw is domain_error - type the standard library defines in `<stdexcept>` for reporting a function's argument is outside the values function can accept.  
When we create domain_error object, can give it a string describing what went wrong.  
  
**others?**  


## Class Definition `template<class T> class Row {...`
p187 chp11  
Row is a *template class*, with one parameter T.  
template class - allow users to use eg `Vecs` to hold a variety of types  
compiler will replace T with whatever type the user names when creating a Vec  
eg `vec<int> v;` - a version of Vec class in which int replaces each T  
-gives `row` the type int*

## 'T* row'
**Implementing the class p188**  
define a pointer to a T - pointer is called row  
-will point to first element in Row  
(but have not allocated memory for array yet)  
(name of array represents a pointer to array's initial element)

## Constructors p164, 190
see Treenode\_h\_Annotations  
role is to ensure object is correctly initialised - to an appropriate value  

`Row(int cols = 0):row(0)`  
takes a parameter with a default argument  
What is `:row(0)`? See 'Tree\_h\_Annotations' > Constructors  
**?** a constructor initialiser - pointer with value 0

## Destructors p200
(see Treenode\_h\_Annotations)  
**delete[]** deallocates an entire array (rather than a single element - destroys each element)  
`row` is a pointer - an argument to delete[]

(`delete p` - destroys object to which p points - frees the memory used to hold *p  
-pointer must point to an object that was dynamically allocated (allocated by `new`), or be equal to zero)  
p183, 186

## Copy constructor p195
a member function with same name as class  
initialises a new object as a copy of an existing object of the same type - takes one argument, the same type as the class - essential the parameter be a reference  
defines what it means to make a copy (passing an object by value to a function, or returning from a function, implicitly copies the object)  
copying an object should not change the object, so copy constructor takes a const reference to the object from which to copy  
what should it do? (in the book, copy constructor forwards its work to a function not yet defined)  
-calls `SetRowSize(...)`

-`row` now points to first element in array

`handles[i]` equivalent to `*(handles + i)`  
`matrix[i][j]` equivalent to `*(*(matrix + i) + j)`  
`handles` is a pointer - points to mth element of an array

### 'SetRowSize()'
like `create()` (2nd one, p207) - allocates memory, initialises elements in that memory, sets pointers  
uses n to allocate appropriate amount of memory  
  
p208  
if `row` is not 0, destroy objects in array to which `row` points  
(member function so do not need to qualify `row`, `Row::row`, or pass it as argument)  

`new T[n]` (p183, 186) allocates and default-initialises array of n objects of type T  
returns pointer to initial element  
  
`else{row = 0;}`  
pointer `row` starts with 0 value  
  
## 'changeSize()'
p59, 60, 72  
eg `try {...} catch(domain_error)`
tries to execute statement in {}  
if a domain_error exception occurs, it stops executing and continues with other {}-enclosed statements (the *catch clause*)  
catch indicates type of exception it is catching  
see above - `stdexcept`  

### standard error stream p180
useful for program to comment about what it is doing - notify user about errors, or log significant events  
To distinguish such comments from ordinary output, C++ defines a standard error stream, in addition to standard input/output  
to write to standard error stream, use cerr or clog  

## Overloaded operators p192, 210
see Treenode\_h\_Annotations  
**unsure what `#ifdef` does here - note not `ifndef`**

## 'Row&  operator=(const Row& r)' - Assignment p196-199
class definition controls the assignment operator  
may define several instances of the assigment operator - overloaded by differing types for its argument  
-version that takes a const reference to the class is special: defines what it means to assign one value of the class type to another.  
a member of the class  
return a reference to left-hand side  

differs from copy constructor - assignment obliterates existing value (left-hand side) and replaces it with new value (right-hand side).  
When we make a copy, we create a new object, so there is no preexisting object to deallocate.  

Assignment is not initialisation  
= symbol involved in both initialisation and assignment  
When we use =  
- to give a variable an initial value, we invoke the copy constructor.  
- in an assignment expression, we call operator=.  
Assignment (operator=) obliterates a previous value; initialisation never does.  
Rather, initialisation creates a new object and gives it a value.  
eg
```C++
string url_ch = "~;/?";			// initialisation
string spaces(url_ch.size(), '');	// initialisation
string y;				// initialisation
y = url_ch;				// assignment
```

**this**  
valid only inside a member function  
denotes a pointer to the object on which the member function is operating  
eg inside Vec::operator=, type of `this` is Vec*, because `this` is a pointer to the Vec object of which operator= is a member.  
For a binary operator, such as assignment, `this` is bound to left-hand operand.  

return statement dereferences `this` to obtain object to which it points.  
We then return a reference to that object.  
(in returning a reference, crucial that object to which reference refers persists after function has returned - exists outside the scope of assignment operator)  

## Friends p217 (refers to p161 'Accessor functions')
eg  
operator>> not a member of class Str, so it cannot access `data` member of s.  
p161 solved problem by adding an accessor function  
-Here, input operator needs to write `data`, not just read it - read access to `data` not enough.  
do not want all users to have write access to `data`, so cannot add a (public) access function that would let operator>> (and any user) write to `data`.  
Rather, we can make input operator a `friend` of class Str - has same access rights as a member  
-allows it, along with member functions, to access private members of class Str:  

```C++
class Str {
	friend std::istream& operator>>(std::istream&, Str&);
};
```
a `friend` declaration - says the version of operator>> that takes an istream& and Str& may access  private members of Str  


**'delim'?**  


## 'SetSize(...'
`int rows`...  
`new Row<T>[rows]`  
(p109, Pocket Reference) To dynamically allocate storage for an array, use the new[] operator. Eg:  
`double		*da = new double[5];`  
(The class for objects being allocated must have a default constructor. This is called for each object.)  

make an array of 'Row<T>' objects  
\> set size of `Row<T>` objects  

### Allocating an object p183
`new T` allocates an object of type T, which is default-initialised, and yields a pointer to this (unnamed) object.  
give a value when initialising object: new T(*args*)  
eg  
`int* p = new int(42)`  
-allocate an unnamed new object of type int, initialise object to 42 - p points to that object.  

### Allocating an array p184
`new T[n]` allocates an array of n objects of type T and returns pointer (type T*) to initial element of array.  
Each object is default-initialised. If T is class type, each element is initialised by default constructor.  
(Chp 11 - more preferable mechanism for dynamically allocating arrays)  

## `Row<T>& operator[](...`
**unsure what `#ifdef` does here - note not `ifndef`**  

p185 - Indexing an array is defined in terms of pointer operations: For array a and index n, a[n] is same as *(a+n).  
-element itself, not address of element  

Note `Row<T>& operator[](...` returns reference to element.  

## `Row& operator=(...`
see above  
- `this`
- 'Assignment p196-199'

Argument is operand on rhs  
I think lhs is an implicit argument  
-Note in earlier code (up page), `matrix` has type `Row<T>*` (pointer to a matrix element)  
-access data elements of our object directly. Eg `midterm` instead of `s.midterm`  

how operands are bound to parameters of the overloaded operator function  
For binary operation, left operand is bound to first parameter, right operand is bound to second.  
In member operator functions, first parameter (left operand) is passed implicitly to the member function.  

**?** `Row<T>(m.matrix[r])`  
see 'Treenode\_h\_Annotations' > 'Constructors p190' > `Vec<double> vs(100)` - uses the constructor that takes a size  
\> see constructors of Row class  
\> does this code call standard or copy constructor?  

standard takes an int argument; copy, a reference to a Row  

`matrix` member of m is a pointer to a Row<T>  
matrix[r] = *(matrix + r)  
so it is an object of type Row  
so code calls copy constructor  

## 'const Matrix operator+(...'
**? unsure**  
`result[r][c]` - where does the code set up row AND column indexing?  

`result` is a matrix  
-`matrix` member of m is a pointer to a Row<T>  
matrix[r] = *(matrix + r)  
-result[r] is an object of type Row  

(result[r])[c] - then we index the Row object  

## 'setValue'?
p5, Pocket Reference  
`atof` used to convert command-line argument from string to double  

**?**
Do overloaded setValue functions facilitate importing data/matrices?  
-when reading a file, values are read as strings but we want them to be doubles  
When are they used?

Why pass in t?  

**?**
`int8_t` - signed integer type with width of 8 bits  
`unint8_t` - unsigned  

`atoi` - convert string to integer

## 'void import(string filename)'
p9, Pocket Reference  
`#ifdef` directive causes preprocessor to include different code based on whether an identifier is defined  
eg
```C++
#ifdef LOGGING_ENABLED
cout << "Logging is enabled" << endl;
#else
cout << "Logging is disabled" << endl;
#endif
```
(`#ifndef' similar but includes code if identifier not defined)  

[en.cppreference.com/w/cpp/preprocessor/conditional]  
if directive evaluates to true, compiles the code block

**?**  
What's an identifier?  
Why need #ifdef - got `else if`?  

std::string::find - finds first substring equal to given character sequence  
[en.cppreference.com/w/cpp/string/basic_string/find]  

std::string::npos - max value representable by type size_type  
eg
```C++
int main()
{
std::string s = "test";
if(s.find('a') == std::string::npos)
	std::cout << "no 'a' in 'test'\n";
}
```

## 'importTif(...'
**get help**
