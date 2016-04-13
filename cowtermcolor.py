#!/usr/bin/python
#coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        cowtermcolor.py                           ##
##            █ █        █ █        cowtermcolor                              ##
##             ████████████                                                   ##
##           █              █       Copyright (c) 2016                        ##
##          █     █    █     █      AmazingCow - www.AmazingCow.com           ##
##          █     █    █     █                                                ##
##           █              █       N2OMatt - n2omatt@amazingcow.com          ##
##             ████████████         www.amazingcow.com/n2omatt                ##
##                                                                            ##
##                  This software is licensed as GPLv3                        ##
##                 CHECK THE COPYING FILE TO MORE DETAILS                     ##
##                                                                            ##
##    Permission is granted to anyone to use this software for any purpose,   ##
##   including commercial applications, and to alter it and redistribute it   ##
##               freely, subject to the following restrictions:               ##
##                                                                            ##
##     0. You **CANNOT** change the type of the license.                      ##
##     1. The origin of this software must not be misrepresented;             ##
##        you must not claim that you wrote the original software.            ##
##     2. If you use this software in a product, an acknowledgment in the     ##
##        product IS HIGHLY APPRECIATED, both in source and binary forms.     ##
##        (See opensource.AmazingCow.com/acknowledgment.html for details).    ##
##        If you will not acknowledge, just send us a email. We'll be         ##
##        *VERY* happy to see our work being used by other people. :)         ##
##        The email is: acknowledgment_opensource@AmazingCow.com              ##
##     3. Altered source versions must be plainly marked as such,             ##
##        and must not be misrepresented as being the original software.      ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##

## Imports ##
import os
import sys;
import re;

VERSION = (0, 1, 0);


################################################################################
## Color Mode                                                                 ##
################################################################################
COLOR_MODE_ONLY_IF_TERMINAL = 0;
COLOR_MODE_ALWAYS           = 1;
COLOR_MODE_NEVER            = 2;
COLOR_MODE_DEFAULT          = COLOR_MODE_ONLY_IF_TERMINAL;

COLOR_MODE = COLOR_MODE_DEFAULT;


################################################################################
## Color Codes                                                                ##
################################################################################
## Reset ##
RESET = 0;
## Foreground Colors ##
GREY    = 30;
RED     = 31;
GREEN   = 32;
YELLOW  = 33;
BLUE    = 34;
MAGENTA = 35;
CYAN    = 36;
WHITE   = 37;
## Background Colors ##
ON_GREY    = 40;
ON_RED     = 41;
ON_GREEN   = 42;
ON_YELLOW  = 43;
ON_BLUE    = 44;
ON_MAGENTA = 45;
ON_CYAN    = 46;
ON_WHITE   = 47;
## Attributes ##
BLINK     = 5;
BOLD      = 1;
CONCEALED = 8;
DARK      = 2;
REVERSE   = 7;
UNDERLINE = 4;


################################################################################
## Color Class                                                                ##
################################################################################
class Color(object):
    def __init__(self, fg = None, bg = None, list_of_attr = None):
        self._foreground = fg;
        self._background = bg;
        self._attrs      = list_of_attr;

    def __call__(self, s = ""):
        r = _put_color(self._foreground);

        if(self._background is not None):
            r += _put_color(self._background);

        if(self._attrs is not None):
            for attr in self._attrs:
                r += _put_color(attr);

        r += s + _put_color(RESET);

        return r;


################################################################################
## Color Functions                                                            ##
################################################################################
## Reset  ##
def reset(s = ""): return _put_color(RESET) + s;
## Foregrounds ##
def grey   (s = ""): return _put_color(GREY   ) + s;
def red    (s = ""): return _put_color(RED    ) + s;
def green  (s = ""): return _put_color(GREEN  ) + s;
def yellow (s = ""): return _put_color(YELLOW ) + s;
def blue   (s = ""): return _put_color(BLUE   ) + s;
def magenta(s = ""): return _put_color(MAGENTA) + s;
def cyan   (s = ""): return _put_color(CYAN   ) + s;
def white  (s = ""): return _put_color(WHITE  ) + s;
## Backgrounds ##
def on_grey   (s = ""): return _put_color(ON_GREY   ) + s;
def on_red    (s = ""): return _put_color(ON_RED    ) + s;
def on_green  (s = ""): return _put_color(ON_GREEN  ) + s;
def on_yellow (s = ""): return _put_color(ON_YELLOW ) + s;
def on_blue   (s = ""): return _put_color(ON_BLUE   ) + s;
def on_magenta(s = ""): return _put_color(ON_MAGENTA) + s;
def on_cyan   (s = ""): return _put_color(ON_CYAN   ) + s;
def on_white  (s = ""): return _put_color(ON_WHITE  ) + s;
## Attributes ##
def bold     (s = ""): return _put_color(BOLD     ) + s;
def dark     (s = ""): return _put_color(DARK     ) + s;
def underline(s = ""): return _put_color(UNDERLINE) + s;
def blink    (s = ""): return _put_color(BLINK    ) + s;
def reverse  (s = ""): return _put_color(REVERSE  ) + s;
def conceale (s = ""): return _put_color(CONCEALE ) + s;


################################################################################
## Helper Functions                                                           ##
################################################################################
def code_to_escape_str(code):
    return "%s%d%s" %(__START_ESCAPE_STR, code, __END_ESCAPE_STR);

def remove_all_escape_codes(s):
    return re.sub("\033\[\d+m", "", s);

def str_len(s):
    return len(remove_all_escape_codes(s));


################################################################################
## Private Stuff                                                              ##
################################################################################
__START_ESCAPE_STR = "\033[";
__END_ESCAPE_STR   = "m";

def _put_color(color):
    global COLOR_MODE;
    if(COLOR_MODE == COLOR_MODE_ALWAYS):
        return code_to_escape_str(color);
    elif(COLOR_MODE == COLOR_MODE_NEVER):
        return "";
    #COLOR_MODE_ONLY_IF_TERMINAL | COLOR_COLOR_DEFAUT
    elif(os.isatty(sys.stdout.fileno())):
        return code_to_escape_str(color);

    return ""


################################################################################
## Script Initialization                                                      ##
################################################################################
if __name__ == '__main__':
    red("ola");
    pass;


