# 1_Treenode.h Annotations

### 'Brief Class Descriptions'
a tree node (), to be used to reassemble the tree at simulation end  
-What is a tree node? A coalescence event (Rosindell et al 2008)?

### 'Class Treenode'
a class  
a data-storage object for the tree  
contains routines for changing a lineage's attributes - called by Treelist objects when generating new coalescence trees

### header file
used during simulation and after (when doing calculations with coalescence tree)  
coalescence events make a new Treenode object


## Program structure p66
how to package the `median` function so others can use it  
put definition of `median` into a source file eg median.cpp  
-must include declarations for all names `median` uses - the `vector` type, `sort` function... - include the headers for these  

next step - put names we define into a **header file** eg median.h  
users use it by writing `#include "median.h"` - a #include directive with double quotes not angle brackets  
what should be in it  
- a *declaration* for `median` - replace function body with semicolon; eliminate parameter names
- names the declaration uses
eg
```C++
#include <vector>
double median(vector<double>);
```

Header files should ensure it is safe to include the file more than once:
```C++
#ifndef GUARD_median_h
#define GUARD_median_h

#include <vector>
double median(vector<double>);

#endif
```
*#ifndef directive*  
asks the preprocessor to process everything between it and #endif if the given name is NOT defined
first time median.h is included, `GUARD_median_h` will be undefined, so preprocessor will look at rest of file  
it defines `GUARD_median_h`, so subsequent attempts to include median.h have no effect


##
short, long, unsigned - integral types  
double - float  

`bool tip` - what's a leaf node?  
?coalescence is sampling based - can simulate without simulating whole community  

`long xwrap` - why more than 1 wrap around torus?  
`double dSpec` - why multiply to get actual probability?  

?  
`long iGen` -> `void setIGen(...` - sets number of generations a lineage has existed  
`double generation_added` -> `void setGeneration(...` - lineage's birth generation (when it originated - via speciation?)


## 'Treenode() : ...' - Constructor
### Protection p160
allow the type's users to access the data only through member functions  
say which members are `public` (accessible to users), and which are `private` (inaccessible to users - references to these members from nonmember functions are illegal) - *protection labels*  

use of `class` instead of `struct` - both define a new type. Only difference is default protection (applies to members defined before first protection label)  
-`class` - every member between first { and first protection label is private - `struct`, public

### Constructors p164
member functions that define how objects are initialised  
creating an object of class type calls the constructor automatically as a side effect  
have same name as the class, and no return type  

want to define two constructors:
- first takes no arguments and creates an empty Student_info object
- second (*in this eg*) takes a reference to an input stream and initialises object by reading student record from stream  

allows users to write code such as  
```C++
Student_info s;		// an empty Student_info
Student_info s2(cin);	// initialise s2 by reading from cin
```

update class to add our constructors:
```C++
class Student_info {
public:
	Student_info();			// construct empty Student_info object
	Student_info(std::istream&);	// construct by reading a stream
};
```
(^function declarations not definitions)

#### default constructor p165
takes no arguments  
job is to ensure object's data members properly initialised  

`Student_info::Student_info(): midterm(0), final(0) { }`  
between : and { are **constructor initialisers** - tell compiler to initialise members with the values in parentheses - sets `midterm` and `final` to 0  
The need to give members a sensible initial value is especially critical for members of built-in type - otherwise, objects will be initialised with garbage  
we explicitly initialised only `midterm` and `final` (doubles), the other data members initialised implicitly - eg `homework` initialised by the `vector` default constructor

#### Constructors with arguments p166
`Student_info::Student_info(istream& is) { read(is) }`  
delegates work to `read` function

### Constructors p190
```C++
Vec<Student_info> vs;	// uses default constructor
Vec<double> vs(100);	// uses the constructor that takes a size
```

```C++
template <class T> class Vec {
public:
	Vec() { create(); }
	explicit Vec(std::size_t n, const T& val = T()) { create(n, val); }
};
```
default constructor (takes no arguments) indicates the Vec is empty - has no elements  
-does so by calling a member named `create`, which we have to write.


## '~Treenode() {}' - Destructor
**p200 chp11 (p188 chp11, p141 chp8)**
destructor - a special member function that controls what happens when objects of the type are destroyed  
have same name as the class prefixed by ~  
no arguments, no return value  
do cleanup that should be done whenever an object goes away - releasing memory


##
`void setup(...`  
returns void  
variables are defined outside the function - the function assigns values to them  
function a member of 'Treenode' class, so
- do not need to pass a Treenode object as an argument
- access data elements directly eg 'midterm' not 's.midterm'

`void setGeneration(...`  
'moves that don't involve coalescence'  
?:  
	speciate with probability nu, or coalesce probability 1-nu  
	only sampling 7 individuals - more complicated  
	J size of community, N number of lineages we're tracing  
	with probability 1-nu, probability of coalescence is N-1/J-1 (can't coalesce with self)  
	-divided by J-1 because there are still J individuals in system  
	could've come from individual we're not tracing  
	-possibility individual unborn and comes from another location but does not coalesce

`void increaseGen() {iGen++}`  
postfix increment - increment x, return original value of x


## Overloaded operators p192, 210
'our users should be able to...use the index operator to access elements in Vec  
we need to define what it means to use the subscript operator, [], on a Vec'  

define overloaded operator as we define any other function: has a name, takes arguments, specifies return type  
We form the name by appending operator symbol to the word operator - eg function we need to define will be called operator[]  
when user writes eg `vs[i]`, that expression calls the operator[] member of vs, passing i as its argument


`friend` - see Matrix\_h\_Annotations  
