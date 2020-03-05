# Features about managing flight records data

At first the pandora software should be able to take one airbus flight records data as an input and produce an analysis for it. Advanced input functionalities include taking multiple files in a process call batching to automate the processing of multiple files, taking multiple files to compute summary analysis, managing different plane constructors (and thus different ways of storing the information ), managing corrupted records.

# Managing multiple input files

while running `pandora ...source` the program should behave differently depending on what `source` is :
* _one file_ : **mono**
* _multiple files_ or _folder_: **multi**
* _multiple folders_ or _a mix of folder and files_ : **batch**
