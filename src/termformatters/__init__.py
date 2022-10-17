"""Terminal font style and base 16 colors formatters

Simple Python package for producing colored and formated terminal
text.

Terminals traditionally  take an input  of bytes and display them
as white text on a black  background.  But if the  input contains
specific  CSI (Control  Sequence Introducer)  sequences  then the
terminal may alter certain  display properties of the  text, such
as  the  style or  color.  Using   styles  and colors  in console
applications  helps us analyze  information faster and   focus on
important parts of the displayed information.

The package creates ANSI escape  character sequences for changing
the   color  and  style   of the  font, based   on human-readable
parameters like black, green, italic etc.

ANSI Escape Codes for Terminal Graphics

The ANSI  escape code standard, formally adopted as ISO/IEC 6429,
defines a  series of  control   sequences.  Each  control sequenc
e begins  with a Control   Sequence Introducer (CSI), defined  as
an escape character followed immediately   by a bracket:  `ESC[`.
The ANSI  ASCII  standard  represents the escape ESC character by
the decimal number 27 (33 in octal, 1B in hexadecimal).  The `ESC
[` is followed by any number (including   none) of "parameter byt
es" in the range `0x30–0x3F`,  then  by any  number of "intermedi
ate bytes" in the  range `0x20–0x2F`,  then finally  by  a single
"final byte"  in the range `0x40–0x7E`.

All  common sequences just   use  the parameters as  a  series of
semicolon-separated numbers. Missing numbers are treated as 0 and
no parameters at all in `ESC[m` acts like a 0 reset code.

Select Graphic Rendition (SGR) parameters

The control  sequence `CSI n   m`, named Select Graphic Rendition
(SGR), sets display attributes. Several attributes can be  set in
the   same sequence,    separated  by  semicolons.   Each display
attribute remains  in effect until  a following occurrence of SGR
resets it. If no codes are given, `CSI m` is treated as `CSI 0 m`
(reset/normal).

The package uses only  basic parameters to control the font style
and  its  color. The most commonly used SGR parameters to control
the font style in the range  (0-8) and the 8 actual colors within
the ranges (30-37, 40-47, 90-97, 100-107) are defined by the ANSI
standard. The package put these  parameters together to  create a
full SGR command.

The original  specification only had 8 colors, and just gave them
names. The SGR parameters  30–37  selected the  foreground color,
while  40–47 selected the   background.  Quite  a   few terminals
implemented "bold" (SGR code 1) as a brighter color rather than a
different  font,  thus  providing 8 additional foreground colors.
Usually you could not get    these  as background  colors, though
sometimes  inverse video (SGR code 7) would allow that. Examples:
to get black letters on white background use `ESC[30;47m`, to get
red use `ESC[31m`, to   get  bright red use  ESC[1;31m.  To reset
colors to their defaults, use `ESC[39;49m` (not supported on some
terminals),  or reset all attributes with ESC[0m. Later terminals
added the  ability to directly   specify the "bright" colors with
90–97 and 100–107.

The package supports the parameters shown in the tables below:

Font Styles SGR parameters

     Name           : Style :
    .........................
    "Bold"          :   1   :
    "Faint"         :   2   :
    "Italic"        :   3   :
    "Underline"     :   4   :
    "Blink"         :   5   :
    "Negative"      :   7   :
    "Concealed"     :   8   :

Foreground/Background Colors SGR parameters

     Name           :  FG  :  BG  :
    ...............................
    "Black"         :  30  :  40  :
    "Red"           :  31  :  41  :
    "Green"         :  32  :  42  :
    "Yellow"        :  33  :  43  :
    "Blue"          :  34  :  44  :
    "Magenta"       :  35  :  45  :
    "Cyan"          :  36  :  46  :
    "White"         :  37  :  47  :
    "Black Bright"  :  90  :  100 :
    "Red Bright"    :  91  :  101 :
    "Green Bright"  :  92  :  102 :
    "Yellow Bright" :  93  :  103 :
    "Blue Bright"   :  94  :  104 :
    "Magenta Bright":  95  :  105 :
    "Cyan Bright"   :  96  :  106 :
    "White Bright"  :  97  :  107 :

Test   scripts   in    the     source  code    repository print
formatted/colored tables using supported   ANSI sequences.  The
package has no requirements other than the standard library.

References
    https://en.wikipedia.org/wiki/ANSI_escape_code
"""
__version__ = "0.2.1"
# Main Formatters import
from .base import StyleFormatters
from .base import ForegroundFormatters
from .base import BackgroundFormatters


__all__ = ["StyleFormatters", "ForegroundFormatters", "BackgroundFormatters"]


def update_formatters_classes(cls):
    """Adding dynamic methods to formatters classes"""

    # Main formatters
    formatsList = [
        "fg_black",
        "fg_red",
        "fg_green",
        "fg_yellow",
        "fg_blue",
        "fg_magenta",
        "fg_cyan",
        "fg_white",
        "fg_black_bright",
        "fg_red_bright",
        "fg_green_bright",
        "fg_yellow_bright",
        "fg_blue_bright",
        "fg_magenta_bright",
        "fg_cyan_bright",
        "fg_white_bright",
        "bg_black",
        "bg_red",
        "bg_green",
        "bg_yellow",
        "bg_blue",
        "bg_magenta",
        "bg_cyan",
        "bg_white",
        "bg_black_bright",
        "bg_red_bright",
        "bg_green_bright",
        "bg_yellow_bright",
        "bg_blue_bright",
        "bg_magenta_bright",
        "bg_cyan_bright",
        "bg_white_bright",
    ]

    # Main styles
    # (disabled, additional aliases for styles will not be created)
    #
    # stylesList = [
    #     "green",
    #     "bold",
    #     "faint",
    #     "italic",
    #     "underline",
    #     "blink",
    #     "negative",
    #     "concealed",
    # ]

    methodsList = [
        method
        for method in dir(cls)
        if method.startswith("fg_") is True or method.startswith("bg_") is True
    ]

    notInList = []
    # Building method aliases
    for formatName in formatsList:
        for methodName in methodsList:
            aliasesList = []
            if formatName == methodName:
                methodNameParts = methodName.strip().split("_")
                # Standart colors
                if len(methodNameParts) == 2:
                    aliasesList.append(methodNameParts[1])
                # Bright colors
                elif len(methodNameParts) == 3:
                    aliasesList.append(
                        methodNameParts[0]
                        + "_"
                        + methodNameParts[2]
                        + "_"
                        + methodNameParts[1]
                    )
                    aliasesList.append(methodNameParts[1] + "_" + methodNameParts[2])
                    aliasesList.append(methodNameParts[2] + "_" + methodNameParts[1])
                else:
                    print("Unknown method name format: {}".format(methodName))
            else:
                notInList.append(formatName)

            if len(aliasesList) > 0:
                for aliasName in aliasesList:
                    destName = str(cls.__name__) + "." + methodName
                    setattr(cls, aliasName, staticmethod(eval(destName)))

    return (cls, notInList)


# Adding method aliases to Foreground and Background classes
#
update_formatters_classes(ForegroundFormatters)
update_formatters_classes(BackgroundFormatters)
