# codeforcesTools
Some helpful tools for codeforces challenges  
- [runtest](#runtest)  
- [fix_readme](#fix-readme)  
- [mkreadme](#mkreadme)
- [cftodo](#cftodo)

## runtest
[runtest](runtest)

Runs a testfile on any number of python files to see which is faster. It tests speed, not results. More commonly used on codewars rather than codeforces.   

```
runtest \<testfile\> \<python files to test\>
```

### Optional Params
- -h, --help   = help  
- -a, --all    = show the result of each test  
- -t, --total  = show the total time taken for the tests  
- -r, --regex  = whether it uses regex or not. This is to clear the cache after each test.  

### Testfile Format
function_to_run  
arg1 arg2 arg3...  
arg1 arg2 arg3...  
arg1 arg2 arg3...  
arg1 arg2 arg3...  


## Fix Readme
[fix_readme](fix_readme)

Takes a README file and formats the Problem header section to be the correct format to maintain consistency across all challenges.  

Automatically puts in code blocks for the examples.  
Automatically changes sections to headers.  
Automatically changes inputCopy and outputCopy to Input and Output.  
Generates a backup file incase something goes wrong.  

```
fix_readme
```

### Optional Parameters
- -h, --help = help
- -d, --dir \<PATH\> = The directory of the file you want to change. Defaults to current directory.  
- -f, --file \<FILE\> = The file you want to change. Defaults to README.md.
- r, --revert = Copy the contents of the backup (the .back file) into the main file.  


## mkreadme
[mkreadme](mkreadme/mkreadme)

This automatically creates a README file when given a link to a codeforces page.  
It generates everything up to the solutions header. There may be issues with latex not being formatted correctly.  
This means that fix_readme is no longer necessary.  
It warns you if the readme file already exists.  

```
mkreadme <url>
```

### Optional Parameters
- -h, --help = help
- -d, --dir \<PATH\> = The directory you want to store the file. Defaults to current directory.  
- -f, --file \<FILE\> = The name of the file. Defaults to README.md.
- --force = Ignore warnings


## cftodo
[cftodo](cftodo)  

This should only be used in the `/codeforces` directory.  
This finds any unsolved challenges.  
A challenge is solved if it contains the string "Solved!".  
This string should by convention be at the end of the file, but may not be.  
Prints the unsolved challenges to stdout.  
```
cftodo
```

