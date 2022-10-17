#!/usr/bin/env python3
import sys

from termformatters import StyleFormatters
from termformatters import ForegroundFormatters
from termformatters import BackgroundFormatters


# Print current Python version
print(sys.version)
print()

"""Formatters"""
S = StyleFormatters()
FG = ForegroundFormatters()
BG = BackgroundFormatters()


# CP437 (249 F9)
testChars249 = "∙∙∙"

stylesPrint = {
    1: "bold",
    2: "faint",
    3: "italic",
    4: "underline",
    5: "blink",
    7: "negative",
    8: "concealed",
}

colorNumbersFG = {
    30: "fg_black",  # Black
    31: "fg_red",  # Red
    32: "fg_green",  # Green
    33: "fg_yellow",  # Yellow
    34: "fg_blue",  # Blue
    35: "fg_magenta",  # Magenta
    36: "fg_cyan",  # Cyan
    37: "fg_white",  # White
    90: "fg_black_bright",  # Black Bright
    91: "fg_red_bright",  # Red Bright
    92: "fg_green_bright",  # Green Bright
    93: "fg_yellow_bright",  # Yellow Bright
    94: "fg_blue_bright",  # Blue Bright
    95: "fg_magenta_bright",  # Magenta Bright
    96: "fg_cyan_bright",  # Cyan Bright
    97: "fg_white_bright",  # White Bright
}

colorNumbersBG = {
    40: "bg_black",
    41: "bg_red",
    42: "bg_green",
    43: "bg_yellow",
    44: "bg_blue",
    45: "bg_magenta",
    46: "bg_cyan",
    47: "bg_white",
    100: "bg_black_bright",
    101: "bg_red_bright",
    102: "bg_green_bright",
    103: "bg_yellow_bright",
    104: "bg_blue_bright",
    105: "bg_magenta_bright",
    106: "bg_cyan_bright",
    107: "bg_white_bright",
}


"""Foreground/Background Table"""
print()
print(
    S.bold(
        FG.white_bright(
            "--- 8/16 base colors: SGR attributes 30..37 (90..97) and 40..47 (100..107) ---"
        )
    )
)
print()
# Colors table header
print("     color name", end="")
print("  dfl", end="")
print("   040   041   042   043   044   045   046   047", end="")
print("   100   101   102   103   104   105   106   107")
print()

for colorNumberFG in list(colorNumbersFG.keys()):
    currentColorNameFG = colorNumbersFG[colorNumberFG]  # "fg_name"
    currentFGName = currentColorNameFG[3:].replace("_", " ")

    print("{:>15s}".format(currentFGName), end="")
    print(" ", end="")

    # Building FG method name
    # currentColorFuncFG = "FG." + currentColorNameFG + "(' " + "gYw" + " ')"
    currentColorFuncFG = "FG." + currentColorNameFG + "(' " + testChars249 + " ')"

    # Eval Foreground function with default background
    currentForegroundFunc = eval(currentColorFuncFG)

    print("{:^5s}".format(currentForegroundFunc), end="")
    print(" ", end="")

    for colorNumberBG in list(colorNumbersBG.keys()):
        currentColorNumberBG = str(colorNumberBG)

        # Getting the `Backgorund` method name
        currentColorNameBG = colorNumbersBG[colorNumberBG]  # "bg_name"

        # Building and Eval full function
        currentFullFuncName = (
            "BG." + currentColorNameBG + "(" + currentColorFuncFG + ")"
        )
        currentFullFunc = eval(currentFullFuncName)

        print("{:^5s}".format(currentFullFunc), end="")
        print(" ", end="")

    print()

print()

"""Styles Table"""
print()
print(S.bold(FG.white_bright("--- base styles: SGR attributes 1..7 ---")))
print()
# Styles table header
print("     style name", end="")
print("  stl", end="")
print("   000   001   002   003   004   005   006   007", end="")
print("   008   009   010   011   012   013   014   015")
print()

for style in list(stylesPrint.keys()):
    currentStyleName = stylesPrint[style]  # "style"

    # Building and Evla `Style` formatter
    currentStyleMethod = "S." + currentStyleName
    currentStyleFunc = "S." + currentStyleName + "('" + currentStyleName + "')"
    currentStyleEval = eval(currentStyleFunc)

    if currentStyleName != "concealed":
        # {:>[num + 8]s} format() padding value with eval()
        # look like 2 x ESC ("\1xb")
        print("{:>23s}".format(currentStyleEval), end="")
    else:
        # {:>[num]s} format() padding value
        print("{:>15s}".format(stylesPrint[style]), end="")

    print(" ", end="")
    # Printing Style Number
    # print(" {:^3s} ".format(str(style)), end="")
    formatedStyle = str("{:03d}".format(style))
    print(" {:3s} ".format(formatedStyle), end="")
    print(" ", end="")

    for colorNumberFG in list(colorNumbersFG.keys()):
        currentColorNameFG = colorNumbersFG[colorNumberFG]  # "fg_name"
        formatedColorNumber = str("{:03d}".format(colorNumberFG))

        # Building `Foreground` formatter method name
        currentColorFuncFG = (
            "FG."
            + currentColorNameFG
            + "('"
            + "{:3s}".format(formatedColorNumber)
            + "')"
        )

        # Full Style+Foreground formatter
        currentFullFuncName = currentStyleMethod + "(" + currentColorFuncFG + ")"
        currentFullFunc = eval(currentFullFuncName)

        print(" {:3s} ".format(currentFullFunc), end="")
        print(" ", end="")

    print()

print()
