"""UnitTest for base formatters"""
import sys

# Ref: https://docs.python.org/3/library/unittest.html
import unittest

try:
    from termformatters import StyleFormatters
    from termformatters import ForegroundFormatters
    from termformatters import BackgroundFormatters
except ImportError as importError:
    print("Formatter import error!")
    print(importError)
    sys.exit(1)


class TestFormatters(unittest.TestCase):
    def setUp(self):
        """Definition of test variables"""

        self.prefixStart = "\x1b["
        self.prefixEnd = "m"
        self.suffix = "\x1b[0m"
        self.string = "Test"

        self.styleFormats = {
            1: "bold",
            2: "faint",
            3: "italic",
            4: "underline",
            5: "blink",
            7: "negative",
            8: "concealed",
        }

        self.colorFormatsFG = {
            30: "fg_black",
            31: "fg_red",
            32: "fg_green",
            33: "fg_yellow",
            34: "fg_blue",
            35: "fg_magenta",
            36: "fg_cyan",
            37: "fg_white",
            90: "fg_black_bright",
            91: "fg_red_bright",
            92: "fg_green_bright",
            93: "fg_yellow_bright",
            94: "fg_blue_bright",
            95: "fg_magenta_bright",
            96: "fg_cyan_bright",
            97: "fg_white_bright",
        }

        self.colorFormatsBG = {
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

    def test_instances(self):
        """Creating formatters instances"""

        # Formatters instances
        self.S = StyleFormatters()
        self.FG = ForegroundFormatters()
        self.BG = BackgroundFormatters()

        self.assertIsInstance(
            self.S, StyleFormatters, msg=f"Error creating instance: {self.S}"
        )
        self.assertIsInstance(
            self.FG, ForegroundFormatters, msg=f"Error creating instance: {self.FG}"
        )
        self.assertIsInstance(
            self.BG, BackgroundFormatters, msg=f"Error creating instance: {self.BG}"
        )

        # Deleting the test objects
        del self.S
        del self.FG
        del self.BG

    def test_style_formatter(self):
        """Formatters methods testing

        Composition of a fully formatted string by adding a prefix
        and a suffix: prefix + string + suffix, where

        prefix = "\x1b["
            + style | foreground | background
            +"m"

        string = "Test string"

        suffix = "\x1b[0m"
        """

        # Formatters instances
        S = StyleFormatters()
        FG = ForegroundFormatters()
        BG = BackgroundFormatters()

        print()
        self.allBaseFormats = {
            **self.styleFormats,
            **self.colorFormatsFG,
            **self.colorFormatsBG,
        }
        self.assertIs(type(self.allBaseFormats), dict, msg=None)

        for currentFormat in self.allBaseFormats:
            format = str(currentFormat)
            # Building formatter method name
            func = self.allBaseFormats[currentFormat]
            if func.startswith("fg_") or func.startswith("bg_"):
                printName = func[3:].replace("_", " ")
            else:
                printName = func

            # Instance selection
            if 1 <= currentFormat <= 8:
                funcName = "S." + func + "('" + self.string + "')"
            elif currentFormat in list(self.colorFormatsFG.keys()):
                funcName = "FG." + func + "('" + self.string + "')"
            elif currentFormat in list(self.colorFormatsBG.keys()):
                funcName = "BG." + func + "('" + self.string + "')"
            else:
                funcName = None
                self.assertIsNotNone(
                    funcName, msg=f"Invalid formatter name received: {funcName}"
                )

            expectedResult = (
                self.prefixStart + format + self.prefixEnd + self.string + self.suffix
            )
            obtainedResult = eval(funcName)
            print(
                "Current formater is {:<17s} formatted string   `{}`".format(
                    repr(printName), obtainedResult
                )
            )

            self.assertIsNotNone(obtainedResult)
            self.assertIs(type(obtainedResult), str)

            self.assertEqual(obtainedResult, expectedResult)


if __name__ == "__main__":
    # Print current Python version
    print(sys.version)
    print()
    unittest.main(verbosity=2)
