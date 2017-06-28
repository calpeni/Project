# 3_CustomExceptions.h Annotations

## struct p62, 72, 167, 161
eg
```C++
struct Student_info {
	string name;
	double midterm, final;
	vector<double> homework;
}; // note semicolon required
```
Student_info is a type, which has four data members.  
can define obects of that type, each of which will contain instance of these data members.  

Like all definitions, structure definition may appear only once per source file, so should appear in guarded header file.  

User-defined types can be either structs or classes.  
difference is default protection applied to members defined before first protection label:  
struct - public  
class - private  

```C++
class Student_info {
public:
	double grade() const;
};
```
equivalent to
```C++
struct Student_info {
	double grade() const; // public be default
};
```

## 'struct Main_Exception : public runtime_error` - Inheritance p227
(also p250, 269)
eg
Students can take course for undergraduate or graduate credit.  
in addition to homework and exams that all students complete, graduate students have to write thesis.  

a record for graduate credit is same as undergraduate credit, except it has additional properties (thesis)  
-one class just like another, except for extensions.  
define two classes: one to represent core requirements; the other, requirements for graduate credit.  

see p228:
```C++
class Grad: public Core {
public:
	Grad();
	Grad(std::istream&);
	double grade() const;
	std::istream& read(std::istream&);
private:
	double thesis;
};
```
defining new type, Grad, **derived from/inherits from** Core  
-Core **is a base class of** Grad  
every member of Core is also member of Grad - except for constructors, assignment operator, destructor.  
Grad class can add members of its own, as we do with data member `thesis` and constructors.  
can redefine members from base class, as we do with `grade` and `read` functions (see p228).  
derived class cannot delete base class' members.  

`public Core` - Grad inherits public interface to Core - public members of Core are public members of Grad.  
eg, for a Grad object, can call `name` member (see p228) to obtain student's name, even though Grad does not define its own `name` function.  

## class runtime_error
**?**
[en.cppreference.com/w/cpp/error/runtime_error]  
std::runtime_error  
defined in header <stdexcept>  

Member functions
```C++
explicit runtime_error( const std::string& what_arg );
explicit runtime_error( const char* what_arg );
```
Constructs exception object with what_arg as explanatory string that can be accessed through what().  

`explicit` p191  
makes sense only in definition of constructor that takes one argument.  
saying compiler will use constructor only in contexts in which user explicitly invokes constructor:
```C++
Vec<int> vi(100); // explicitly construct Vec from an int, 100
Vec<int> vi = 100; // error: implicitly construct Vec and copy it to vi (p199)
```

## 'Main_Exception():runtime_error(...){}'
**unsure**  
(defining and declaring function simultaneously)  
`Main_Exception():runtime_error(...){}` - default constructor  
`Main_Exception(string msg):runtime_error(msg.c_str()){}` - constructor with argument  

see
- specifically - Treenode\_h\_Annotations.md > 'constructor initialisers'
- generally - Treenode\_h\_Annotations.md and Matrix\_h\_Annotations.md > Constructors

`Student_info::Student_info(): midterm(0), final(0) { }`  
between : and { are **constructor initialisers** - tell compiler to initialise members with the values in parentheses - sets `midterm` and `final` to 0  

## 'c_str'
**?**
[http://en.cppreference.com/w/cpp/string/basic_string/c_str]  
std::basic\_string::c_str  
Returns pointer to null-terminated character array  
