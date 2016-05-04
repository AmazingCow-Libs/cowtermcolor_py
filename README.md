# cowtermcolor_py

**Made with <3 by [Amazing Cow](http://www.amazingcow.com).**



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Websites:

* [cowtermcolor_py Website](http://opensource.amazingcow.com/libs/cowtermcolor_py/)
* [Libs Website](http://opensource.amazingcow.com/libs/) - 
The Amazing Cow's Libs site.

* [PyPi Website](https://pypi.python.org/pypi/cowtermcolor)


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Description:

```cowtermcolor_py``` is a library to ease the terminal coloring.    
It was inspired by the Amazing Cow's C++ [Termcolor_cpp](http://www.github.com/AmazingCow-Libs/Termcolor_cpp),
which was inspired by the python's termcolor.


#### With ```cowtermcolor_py``` we can:

* Use the colored function - 
_"Same"_ as the [Termcolor_cpp](http://www.github.com/AmazingCow-Libs/Termcolor_cpp) colored function.
* Use standalone functions - Like ```print on_yellow(red("MyString")) + reset());```
* Use functor objects - This is nice because we can setup the coloring options
and use it later, possible multiple times.


#### Smart coloring:

What is really nice in ```cowtermcolor_py``` and in [Termcolor_cpp](http://www.github.com/AmazingCow-Libs/Termcolor_cpp)
is both libs _knows_ if the output is the terminal or not,  i.e. them knows
if the ```stdout``` is attached to a ```tty```.

And what we gain with this?

1. By default it will output the coloring escape sequences only if the ```stdout```
is a ```tty```.
2. Cleaner code - We don't need check the output anymore (If we want the default).
3. More cleaner code - To enable, or disable the coloring we can set it only once.

For example, let's imagine that you have an program that output the colors in 
terminal. So far, so good, but what is gonna happen if the user redirects it
to a file?

``` 
$ your-awesome-app > file.txt
$ less file.txt

#Output by less... (Imagine, that this was the output of your app ;p)
ESC[31mColors play nice with terminalESC[0m
ESC[31mColors doesn't like files :DESC[0m
```

As you see, the terminal colors are just a string that has some meaning to the 
terminal - i.e. they are escape sequences, nothing more. In a file them are
meaningless.    

**We don't want code "a lot" just to handle this case.**

So let the lib handle this for us... (Of course we have a way to override this
if we want to).

In ```cowtermcolor_py``` we have the ```ColorMode.mode``` module object that 
defines the desired behavior.   
For default it is ColorMode.ONLY_IF_TERMINAL, but can be others values too 
(check the [examples](#Examples:) section).

So the lib will check the type of the output and put colors correctly :D


### Motivation:

COWTODO: Add the motivation.


<br>

As usual, you are **very welcomed** to **share** and **hack** it.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Examples:

There are some examples in ```cowtermcolor.py``` file, but here is a brief
usage of ```cowtermcolor_py```:

### Colored function:

``` python
from cowtermcolor import *;

def f(path):
    print "{} - Path is invalid ({})".format(colored("[FATAL]", RED),
                                             colored(path, MAGENTA));
    exit(1);
```

### Standalone functions:

``` python
from cowtermcolor import *;

def f(path):
    #Mot a easier way to do this in python, but included to match 
    #the C++ TermColor_cpp lib. Besides in some ways, it might be useful.
    print red("[FATAL]"), 
          reset("- Path is invalid ("), 
          magenta(path), 
          reset(")");
    exit(1); 
```

### Functors:

``` python
from cowtermcolor import *;

def f(path):
{
    #Functors are great because it "holds" the information about 
    #the coloring options, so it can be passed as arguments to functions,
    #be used multiple times, etc.
    red_color     = Color(RED);
    magenta_color = Color(MAGENTA);

    print red_color("[FATAL]"), 
          "- Path is invalid (",
          magenta_color(path),
          ").";
    exit(1);
}
```

### Controlling the Coloring options:

The ```ColorMode.mode``` module object defines the behavior of coloring in
```cowtermcolor_py``` .

It has the following _constants_ that can be used:

* ```ColorMode.ONLY_IF_TERMINAL``` - Color escapes codes are only put into the 
strings if the ```os.stdout``` is assigned to a ```tty```.
* ```ColorMode.ALWAYS``` - Don't care for where the ```os.stdout``` is assigned. 
Put the coloring escape sequences anyway.
* ```ColorMode.NEVER``` - Don't care for where the ```os.stdout``` is assigned. 
**DO NOT** put the coloring escape sequences anyway.


So let's write a simple program to check this:

#### Only put colors if the stdout is the tty.

```python
from cowtermcolor import *;

#Note that we don't need to do anything, because ColorMode.ONLY_IF_TERMINAL
#is the default, but we of course can be explicit if we want...

ColorMode.mode = ColorMode.ONLY_IF_TERMINAL;
print green("Only in Terminal") + reset();
```

#### Put colors ALWAYS.

```python
from cowtermcolor import *;

#This will output colors always - This is not default behavior so 
#we NEED to be explicit here.
ColorMode.mode = ColorMode.ALWAYS;
print green("I will mess the output if I'm went to a file") + reset();
```

#### Put colors NEVER.

```python
from cowtermcolor import *;

#This will output colors never - This is not default behavior so 
#we NEED to be explicit here.
ColorMode.mode = ColorMode.NEVER;
print green("I'm never colored :/") + reset();
```

#### Wrap-up:

We think that the most valuable options are the ```ColorMode.ONLY_IF_TERMINAL```, 
and the ```ColorMode.NEVER```

We do a lot of this in our [tools](http://www.github.com/AmazingCow-Tools) - 
We add a ```--no-colors``` flag to let the user decide if don't want colors 
at all and let the lib decides the output for us.

For example:

```python
...
#Parsing the flags.
if(flag == "--no-colors"):
    ColorMode.mode = ColorMode.NEVER;
...
```

```bash 
$ some-app             #Print colors...
$ some-app --no-colors #DO NOT PUT COLORS - Explicit.
$ some-app > file      #DO NOT PUT COLORS - Handled by lib.
```

We hope that you enjoy the ```cowtermcolor_py```.

<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Documentation:

We strive to make our source code fully documented.   
While there are a myriad of comments, one might find useful take a look at:

* [Project Website](http://opensource.amazingcow.com/libs/cowtermcolor_py/).
* [Pydoc Docs](http://opensource.amazingcow.com/libs/cowtermcolor_py/pydoc/).
* [A list of blog posts about the project](http://opensource.amazingcow.com/libs/cowtermcolor_py/posts/).

Anyway if you didn't understand something let us know sending a mail to  
[help_opensource@amazingcow.com]() with the subject filled with the
name of this repo.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Dependencies:

* There is no dependency for **cowtermcolor_py**



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## License:

This software is released under GPLv3.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## TODO:

Check the TODO file for general things.

This projects uses the COWTODO tags.   
So install [cowtodo](http://www.github.com/AmazingCow-Tools/COWTODO) and run:

``` bash
$ cd path/to/the/project
$ cowtodo 
```

That's gonna give you all things to do :D.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Others:

Check our repos and take a look at our 
[open source site](http://opensource.amazingcow.com).
