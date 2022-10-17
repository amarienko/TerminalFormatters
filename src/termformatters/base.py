"""Base 16 collors formatter
"""
import sys

# https://docs.python.org/3/library/functools.html
import functools
from functools import wraps
from functools import update_wrapper

# https://docs.python.org/3/library/inspect.html
import inspect


class SelectFormatter:
    """Format decorator

    Attributes
    ----------

    func : object
        decorated function name
    suffix : str
        format reset string
    stylesSwitch : dict
        foreground style to style code definition
    colorsSwitchFG : dict
        foreground color to color code definition
    colorsSwitchBG : dict
        background color to color code definition

    Methods
    -------

    __init__
        decorator init
    __call__
        style/colors function wrapper
    """

    def __init__(self, func):
        """Decorator definition

        Parameters
        ----------

        func : object
            decorated function name

        """
        update_wrapper(self, func)
        self.func = func
        self.suffix = "\x1b[0m"
        # Styles
        self.stylesSwitch = {
            "bold": 1,
            "faint": 2,
            "italic": 3,
            "underline": 4,
            "blink": 5,
            "negative": 7,
            "concealed": 8,
        }
        # Foreground colors
        self.colorsSwitchFG = {
            "fg_black": 30,
            "fg_red": 31,
            "fg_green": 32,
            "fg_yellow": 33,
            "fg_blue": 34,
            "fg_magenta": 35,
            "fg_cyan": 36,
            "fg_white": 37,
            "fg_black_bright": 90,
            "fg_red_bright": 91,
            "fg_green_bright": 92,
            "fg_yellow_bright": 93,
            "fg_blue_bright": 94,
            "fg_magenta_bright": 95,
            "fg_cyan_bright": 96,
            "fg_white_bright": 97,
        }
        # Background colors
        self.colorsSwitchBG = {
            "bg_black": 40,
            "bg_red": 41,
            "bg_green": 42,
            "bg_yellow": 43,
            "bg_blue": 44,
            "bg_magenta": 45,
            "bg_cyan": 46,
            "bg_white": 47,
            "bg_black_bright": 100,
            "bg_red_bright": 101,
            "bg_green_bright": 102,
            "bg_yellow_bright": 103,
            "bg_blue_bright": 104,
            "bg_magenta_bright": 105,
            "bg_cyan_bright": 106,
            "bg_white_bright": 107,
        }

    def __call__(self, initString, *args, **kwargs):
        """Style/Colors function wrapper"""
        self.formats = {
            **self.stylesSwitch,
            **self.colorsSwitchFG,
            **self.colorsSwitchBG,
        }
        if self.func.__name__ in self.formats.keys():
            formatNumber = self.formats.get(self.func.__name__, None)
            if formatNumber:
                prefix = "\x1b[" + str(formatNumber) + "m"
            else:
                prefix = self.suffix

            # Update result string
            updatedString = prefix + initString + self.suffix
            return self.func(updatedString, *args, **kwargs)
        else:
            # When style/color not in lists return original string
            return self.func(initString, *args, **kwargs)


class BaseFormat(object):
    """Main class decorator"""

    def __init__(self, decorator):
        self.decorator = decorator

    def __call__(self, cls, *args, **kwargs):
        """Assigning a decorator to a method"""
        # for funcName, funcRef in inspect.getmembers(cls, inspect.isfunction):
        for methodName, methodRef in inspect.getmembers(cls, inspect.ismethod):
            setattr(cls, methodName, self.decorator(methodRef))

        return cls


"""Formatters Classes Methods definition options:

: basic

    def bold(string: str) -> str: return string

: classmethod

    @classmethod
    def italic(cls, string: str) -> str: return string

: staticmethod

    @staticmethod
    def green(string: str) -> str: return string

"""


@BaseFormat(SelectFormatter)
class StyleFormatters:
    """Set of text style formatters"""

    @classmethod
    def bold(cls, string: str) -> str:
        return string

    @classmethod
    def faint(cls, string: str) -> str:
        return string

    @classmethod
    def italic(cls, string: str) -> str:
        return string

    @classmethod
    def underline(cls, string: str) -> str:
        return string

    @classmethod
    def blink(cls, string: str) -> str:
        return string

    @classmethod
    def negative(cls, string: str) -> str:
        return string

    @classmethod
    def concealed(cls, string: str) -> str:
        return string


@BaseFormat(SelectFormatter)
class ForegroundFormatters:
    """Set of foregroud color formatters"""

    @classmethod
    def fg_black(cls, string: str) -> str:
        return string

    @classmethod
    def fg_red(cls, string: str) -> str:
        return string

    @classmethod
    def fg_green(cls, string: str) -> str:
        return string

    @classmethod
    def fg_yellow(cls, string: str) -> str:
        return string

    @classmethod
    def fg_blue(cls, string: str) -> str:
        return string

    @classmethod
    def fg_magenta(cls, string: str) -> str:
        return string

    @classmethod
    def fg_cyan(cls, string: str) -> str:
        return string

    @classmethod
    def fg_white(cls, string: str) -> str:
        return string

    @classmethod
    def fg_black_bright(cls, string: str) -> str:
        return string

    @classmethod
    def fg_red_bright(cls, string: str) -> str:
        return string

    @classmethod
    def fg_green_bright(cls, string: str) -> str:
        return string

    @classmethod
    def fg_yellow_bright(cls, string: str) -> str:
        return string

    @classmethod
    def fg_blue_bright(cls, string: str) -> str:
        return string

    @classmethod
    def fg_magenta_bright(cls, string: str) -> str:
        return string

    @classmethod
    def fg_cyan_bright(cls, string: str) -> str:
        return string

    @classmethod
    def fg_white_bright(cls, string: str) -> str:
        return string


@BaseFormat(SelectFormatter)
class BackgroundFormatters:
    """Set of backgroud color formatters"""

    @classmethod
    def bg_black(cls, string: str) -> str:
        return string

    @classmethod
    def bg_red(cls, string: str) -> str:
        return string

    @classmethod
    def bg_green(cls, string: str) -> str:
        return string

    @classmethod
    def bg_yellow(cls, string: str) -> str:
        return string

    @classmethod
    def bg_blue(cls, string: str) -> str:
        return string

    @classmethod
    def bg_magenta(cls, string: str) -> str:
        return string

    @classmethod
    def bg_cyan(cls, string: str) -> str:
        return string

    @classmethod
    def bg_white(cls, string: str) -> str:
        return string

    @classmethod
    def bg_black_bright(cls, string: str) -> str:
        return string

    @classmethod
    def bg_red_bright(cls, string: str) -> str:
        return string

    @classmethod
    def bg_green_bright(cls, string: str) -> str:
        return string

    @classmethod
    def bg_yellow_bright(cls, string: str) -> str:
        return string

    @classmethod
    def bg_blue_bright(cls, string: str) -> str:
        return string

    @classmethod
    def bg_magenta_bright(cls, string: str) -> str:
        return string

    @classmethod
    def bg_cyan_bright(cls, string: str) -> str:
        return string

    @classmethod
    def bg_white_bright(cls, string: str) -> str:
        return string
