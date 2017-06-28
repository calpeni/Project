# Macros
p1055, Programming: Principles and Practice Using C++  

Beware - their use has serious side effects because they don't obey usual scope and type rules  
Macros - a form of text substitution  

Give macros ALL_CAPS names  
Don't give anything that isn't a macro an ALL_CAPS name  

Main uses  
- definition of  
  - "constants"  
  - function-like constructs  
- conditional compilation  

## Function-like macros
`#define MAX(x,y) ((x)>=(y)?(x):(y))`  
different from a function: no argument types, no block, no return statements  
put every use of an argument as an expression in parentheses.  
Don't pass an argument with a side effect to a macro.  

## Conditional compilation
Imagine two versions of header file, one for Linux, one for Windows

```C++
#ifdef WINDOWS
	#include "my_windows_header.h"
#else
	#inlclude "my_linux_header.h"
#endif
```

if someone defined WINDOWS, the effect is `#include "my_windows_header.h"`  
The `#ifdef WINDOWS` test doesn't care what WINDOWS is defined to be; it just tests it is defined.  
(all operating systems have macros defined so you can check)  
