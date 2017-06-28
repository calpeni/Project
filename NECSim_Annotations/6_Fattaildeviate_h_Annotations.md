# 6 Fattaildeviate.h Annotations

### Header File
contains random number generator

## #define Directive
p8, 'C++ Pocket Reference'  
`#define` directive replaces an identifier with text that follows it wherever identifier occurs in source file  

(  
preferable to use  
-	enumerations, and to lesser degree, variables and data members declared using `const` or `static` for constant data  
-	templates and inline functions  
)

see Macros.md (macros made with #define)

`#define` is text substitution mechanism, handled by preprocessor (not compiler).  
eg `#define PI 3.14159` - preprocessor substitutes 'PI' for '3.14159'  
-does find and replace - everywhere you use 'PI', preprocessor replaces it with '3.14159'  
Compiler operates as if you wrote 3.14159  
[http://www.cplusplus.com/forum/beginner/175991/]

## #include Directives
`fstream`  
objects the standard library uses for *file* input/output have different types than for standard input/output  
to work with input/output file, must create an object of type ifstream/ofstream - definition of these classes in header `<fstream>`

## `class NRand`
['Brief Class Descriptions'](http://pycoalescence.readthedocs.io/en/release/Exhaled/exhaled_library.html#brief-class-descriptions)  
contains random number generator

['Class NRrand'](http://pycoalescence.readthedocs.io/en/release/Exhaled/exhaled_library.html#class-hierarchy)  
functions for random number generation


`long iv[NTAB]`
(p19, 'C++ Pocket Reference')  
must specify type and number of elements array will contain when it is defined (so compiler can reserve required space). Eg
```C++
enum
{
	HandleCount = 100
};

int	handles[HandleCount];
```

## typedef
p43
```C++
typedef vector<double>::size_type vec_sz;
vec_sz size = homework.size();
```
type is unwieldly to write  
To simplify program, used a typedef  
saying we want name we define to be synonym for given type (rather than variable of that type)  
defines `vec_sz` as synonym for `vector<double>::size_type`  
(have same scope as other names - can use name `vec_sz` as synonym for `size_type` until end of current scope)

## Pointers to functions p172
`typedef double (NRrand::*fptr)();`

Declarations for pointers to functions
(`int *p;` - *p has type int - p is pointer)
`int (*fp)(int);`
-if dereference fp, and call it with int argument, result has type int. fp is pointer to function that takes int argument and returns int result.

If wanted function that returned function pointer  
One way - use typedef to define, say, `analysis_fp` as name of type of appropriate pointer:  
`typedef double (*analysis_fp)(const vector<Student_info>&)`
(pointer to function that returns double and takes reference to a vector<Student_info>)  

Then use that type to declare function:
```C++
// get_analysis_ptr returns pointer to analysis function
analysis_fp get_analysis_ptr();
```

`typedef double (NRrand::*fptr)();`  
fptr - pointer to function that returns double and takes no argument *? check*

## Constructors
see 1\_Treenode\_h\_Annotations and 2\_Matrix\_h\_Annotations

## +=
Eg ` i += 5` adds 5 to i and assigns result to i

## `throw`
p117, 'C++ Pocket Reference'
Exception handling performed using try and catch  
You throw an exception inside a try block using `throw`.  
type of exception is used to determie which catch block to execute  
exception is passed as argument to catch block so it can be used in handling exception

## `this->*dispersalFunction`
dereferenced an iterator, then fetched element from value returned  
Instead of `(*iter).name` can write `iter->name`

**?** `this->*dispersalFunction`

## Friends
see Matrix\_h\_Annotations

the version of `operator<<` that takes an ostream& and NRand& may access  private members of NRand


Note: `double nu; // L value of dispersal kernel (the width - does not affect shape)`

