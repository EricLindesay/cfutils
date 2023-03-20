# cfutils

Some helpful tools for codeforces challenges.  
- [fix_readme](#fix-readme)  
- [mkreadme](#mkreadme)
- [cflist](#cflist)
- [cfsetup](#cfsetup)
- [runtestio](#runtestio)  


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
[mkreadme](mkreadme)

This automatically creates a README file when given a link to a codeforces page.  
It generates everything up to the solutions header. There may be issues with latex not being formatted correctly.  
This means that fix_readme is no longer necessary for most cases.  
It warns you if the readme file already exists.  

```
mkreadme <url>
```

### Optional Parameters
- -h, --help = help
- -d, --dir \<PATH\> = The directory you want to store the file. Defaults to current directory.  
- -f, --file \<FILE\> = The name of the file. Defaults to README.md.
- --force = Ignore warnings


## cflist
[cflist](cflist)  

This should only be used in the `/codeforces` directory.  
This has two optional parameters, no parameters means it shows solved and unsolved problems.
The parameters can be used to show only one of those categories.  
A challenge is solved if it contains the string "Solved!".  
This string should by convention be at the end of the file, but may not be.  
Prints the challenges to stdout.  
You can also sort by tags/difficulty and only show problems containing all of those tags/difficulty.  

```
cflist
```

### Optional Parameters
- -h, --help = help
- -t, --todo = List incomplete challenges  
- -c, --completed = List completed challenges
- --show-tags = Whether to show the tags for each problem or not
- --show-all = Overwrites anything in the ignore lists
- --show = A list of difficulties/tags to show
- --hide = A list of difficulties/tags to hide. Defaults to hide easy difficulty


## cfsetup
[cfsetup](cfsetup)  

This is essentially an extension of mkreadme.  
It puts the readme in the correct file based off name and difficulty.  
Should be done in the codeforces directory.  

```
cfsetup <url>
```

## runtestio
[runtestio](runtestio)

Run Test IO name due to it testing the IO using stdin, rather than a function like runtest tests.  
Runs a test file using stdin as the input to the file. This can run any type of file but was meant to be used on c++ codeforces files.  

```
runtest <testfile> <files to test>
```

### Optional Params
- -h, --help   = help  
- -a, --all    = show the result of each test  
- -t, --total  = show the total time taken for the tests  
- -c, --cpp    = whether the file is a c++ file  
- -o, --output = print program output to stdout
- --timeout \<int\> = how long to run the program before it times out (seconds)

### Testfile Format
```
testcase 1  
-----  
testcase 2  
-----   
testcase 3    
```
Testcases can be multiple lines.
Note the 5 dashes.
