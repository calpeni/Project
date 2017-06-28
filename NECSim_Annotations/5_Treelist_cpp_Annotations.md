# 5_Treelist.cpp Annotations

### source file
contains Treelist class implementation


**don't understand**
syntax is familiar, but don't know what code does


## 'void Treelist::setList(Row<Treenode>& l)' - Member functions p157
definition of member function
```C++
istream& Student_info::read(istream& in)
{
	in >> name >> midterm >> final;
	read_hw(in, homework);
	return in;
}
```
put these functions in a source file named 'Student_info.cpp'  
name of function is `Student_info::read` instead of `read`.  
do not need to pass Student_info object as argument  
access data elements of object directly. Eg refer to `midterm`, not `s.midterm`

`nodes` is a `Row<Treenode>` object (see Treelist.h)

## 'Treelist::setDatabase(...'
`bFileSet` - boolean for whether database is already set (Treelist.h)  
`database` - pointer to an sqlite3 object - the database connection (Treelist.h)

## 'Treelist::hasImportedData()'
`bDataImport` - bool - whether simulation data is imported (Treelist.h)  
-initialised to F in Treelist constructor  
(default constructor p165 - ensures object's data members properly initialised)  

## 'Treelist::getMinimumSpeciation()'
`min_spec_rate` - min speciation rate of original simulation (read from database's SIMULATION_PARAMETERS table) (Treelist.h)

## 'Treelist::importSamplemask(string sSamplemask)'
`bSample` - bool - whether samplemask already imported

`samplemask` - a Samplematrix object (Treelist.h) - defines areas to sample from  
-coalescence is sampling based - can simulate a small part of community without simulating whole community

std::stringstream *?*  
(en.cppreference.com/w/cpp/io/basic_stringstream)

`samplemask.SetSize(...`  
call 'SetSize' member function of Matrix class  
-makes an array of 'Row<T>' objects (Matrix\_h\_Annotations.md)

`samplemask.setIsNull(false)`  
call 'setIsNull' member function of Samplematrix class (derived from Matrix)
-checks whether object is null (Treelist.h)  
Sets the bool 'bIsNull' to F  
**What is 'bIsNull'?**

`samplemask.import(...`  
`import` is a matrix class function (samplemask derived from matrix)

## 'Treelist::countSpecies()'
`size()` returns size of array (or container with size method)

### `if(nodes[i].hasSpeciated())`  
`nodes` is a `Row<Treenode>` object and member of class Treelist (see Treelist.h)  
-`nodes[i]` is a Treenode object

call `hasSpeciated()` member function of Treenode class (Treenode.h)  
`speciated` (in `hasSpeciated()`) - bool - true if lineage speciated

If if statement evaluates to not zero...

## 'Treelist::doubleCompare(...'
**What is this for?**

## 'Treelist::calcSpecies(double s)'
`bSample` - bool - whether samplemask is imported (Treelist.h)

**?** 'check that tips exist within the spatial and temporal frame of interest'

`nodes[i].isTip()` - returns 'tip'  
-bool - 0 means node is a coalescence; 1 means node is a leaf and counts towards diversity (Treenode.h)  
**? leaf**  

(Treenode.h)  
`nodes[i].speciate()` - sets `speciation` bool to T  
`nodes[i].getSpeciesID()` - returns `species_id`  
`nodes[i].getExistance()` - returns `does_exist`  
-bool - whether lineage exists at end - if all lineage's children speciated, lineage does not exist

## 'Treelist::calcSpeciesAbundance()'
(Treelist.h)  
`rOut` - `Row<unsigned int>` object  
`unsigned long iSpecies`  
`long double generation` - time of interest for simulation

## 'Treelist::resetTree()'
`nodes[i].qReset()` - see Treenode.h

## 'Treelist::detectDimensions(...', 'Treelist::openSqlConnection(...'
**unfamiliar syntax - sqlite**

## 'Treelist::importData(...'
see 'Treelist::importSimParameters(string file)' below  

**X raises questions**  
What information is in a GIS map?  
- Could I see an eg map?  
- Is it cells with density per cell of various species?  

How does the code read a GIS map - what does it convert the map to?  
What does it do with map?  
-surely purpose of inputting map into package is to compare simulation results and empirical data  
(or maybe parameterise simulation so it is similar to empirical data - area size)  

What does a spatially-explicit coalescence simulation look like in 2D? What's the starting point?  
paper described it in 1D  
-start with row of individuals of unknown species  

**no - sqlite is simulation output - used by Treelist to produce result for any speciation rate**  
**but need to understand what output looks like**  

(Treenode.h)
`nodes[index].burnSpecies(...` - sets species ID, `species_id`  

`nodes[index].setSpec(...` - sets `dSpec`  
-randomly-generated number (from NRrand.d0()) for lineage's speciation probability  
-speciation probability - needs to be multiplied by number of generations to get actual probability  
**?**  

`nodes[index].setExistance(...`  - sets lineage's existance, `does_exist`  
-bool - whether lineage exists at end - if all lineage's children speciated, lineage does not exist  

`nodes[index].setIGen(...` - sets `iGen` - number of generations lineage existed for  
`nodes[index].setParent(...` - sets parent reference  

`nodes[index].setSpeciation(...` - sets `speciated` bool  
-T if lineage speciated (in which case, it should not have parent because lineages not traced beyond speciation)

## 'Treelist::setGeneration(...'
`long double generation` - time of interest for simulation (Treelist.h)  

**?** 'Set the time of interest where all analysis will be performed' (Treelist.h > @brief)

## Treelist::createDatabase(double s)
(Treelist.h > @brief)  
Makes new table in database and outputs database object to same file as input  
new SPECIES_ABUNDANCES table contains species abundance distribution for samplemask  
s - speciation rate to apply  

**note - code prints text for user**  

**unfamiliar syntax - sqlite**

##


internalOption
importData
importSimParameters
setGeneration
createDatabase
createFragmentDatabase
exportDatabase
recordSpatial
calcFragments
applyFragments
