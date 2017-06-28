# 4_Treelist.h Annotations

### 'Brief Class Descriptions'
routines for applying different speciation rates to tree

### 'Class Treelist'
contains  
- tree object lineages  
- functions that calculate number of species for given a speciation rate, outputting spatial data and species abundance distributions  
needs link to SQLite database (simulation output) - puts results in same file

### header file
contains Treelist object, used for reconstructing the coalescence tree after simulations  
used by Treelist.cpp and SpeciationCounter.cpp


## Header files (p5 Pocket Reference)
(also Treenode\_h\_Annotations.md > 'Program structure')  
contain source code to be included in multiple files  
should never contain following - definitions for:  
- variables and static data members  
- functions, except template/inline functions

(Header files in the Standard Library do not use .h extension - have no extension.)

Often you create header file for each major class you define.  
eg `Account` defined in Account.h
```C++
#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account
{
public:
  Account(double b);

  void		deposit(double amt);
  void		withdraw(double amt);
  double	getBalance() const;

private:
  double	balance;
};

#endif
```

implementation of this class is in Account.cpp  
use preprocessor directive #include to include header file within another file.

Because header files often included by other headers, must take care not to include same file more than once -> compilation errors.  
To avoid this, wrap header file contents with preprocessor directives #ifndef, #define, #endif.

##
`bool checkSpeciation(...`  
-function declaration?

## 'struct Fragment'
see 'CustomExceptions\_h\_Annotations.md'
**fragments?**

### [pycoalescence.readthedocs.io/en/release] > 'Struct Fragment'
contains information for defining a fragment  
...

## 'class Samplematrix :  public Matrix<bool>...'
see 'CustomExceptions\_h\_Annotations.md' > 'Inheritance'
defining new type, Samplematrix, derived from/inherits from Matrix  

### [pycoalescence.readthedocs.io/en/release] > 'Class Samplematrix'
used for determining where to sample species from  
inherits from Matrix<bool>

### p88 (Pocket Reference)
When you derive one class from another, derived class inherits data members and member functions that other class defines (subject to access) while adding its own.

derive new class, BankAccount, from Account  
Account - *base class/superclass*  
BankAccount - *derived class/subclass*

## 'Row<Treenode> &nodes'
`const vector<double>& hw`  
reference to const vector of double  
Saying a name is a reference to an object says the name is another name for the object.

```C++
vector<double> homework;
vector<double>& hw = homework; // hw is synonym for homework
```

**'samplemask'?**

## 'Treelist(Row<Treenode>&r):nodes(r)'
constructor that takes an argument

## 'void setList(Row<Treenode> &l);'
function declaration, not definition (see Treelist.cpp)
