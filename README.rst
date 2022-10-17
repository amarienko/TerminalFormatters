|Test Package| |Black badge|

Terminal Formatters
===================

Simple Python package for producing colored and formated terminal text.

|colored-text-python|

Terminals traditionally take an input of bytes and display them as white
text on a black background. But if the input contains specific CSI
(Control Sequence Introducer) sequences then the terminal may alter
certain display properties of the text, such as the style or color.
Using styles and colors in console applications helps us analyze
information faster and focus on important parts of the displayed
information.

The package creates ANSI escape character sequences for changing the
color and style of the font, based on human-readable parameters like
``black``, ``green``, ``italic`` etc.

ANSI Escape Codes for Terminal Graphics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `ANSI escape code
standard <https://en.wikipedia.org/wiki/ANSI_escape_code>`__, formally
adopted as `ISO/IEC
6429 <https://www.ecma-international.org/publications/standards/Ecma-048.htm>`__,
defines a series of control sequences. Each control sequence begins with
a *Control Sequence Introducer* (CSI), defined as an escape character
followed immediately by a bracket: ``ESC[``. The ANSI ASCII standard
represents the escape ESC character by the decimal number 27 (33 in
octal, 1B in hexadecimal). The ``ESC[`` is followed by any number
(including none) of "parameter bytes" in the range ``0x30–0x3F`` (ASCII
``0–9:;<=>?``), then by any number of "intermediate bytes" in the range
``0x20–0x2F`` (ASCII ``space`` and ``!"#$%&'()*+,-./)``, then finally by
a single "final byte" in the range ``0x40–0x7E`` (ASCII
``@A–Z[\]^_``\ a–z{|}~`).

All common sequences just use the parameters as a series of
semicolon-separated numbers. Missing numbers are treated as 0 and no
parameters at all in ``ESC[m`` acts like a 0 reset code.

Select Graphic Rendition (SGR) parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The control sequence ``CSI n m``, named *Select Graphic Rendition*
(SGR), sets display attributes. Several attributes can be set in the
same sequence, separated by semicolons. Each display attribute remains
in effect until a following occurrence of SGR resets it. If no codes are
given, ``CSI m`` is treated as ``CSI 0 m`` (reset / normal).

The package uses only basic parameters to control the font style and its
color. The most commonly used SGR parameters to control the font style
in the range (0-8) and the 8 actual colors within the ranges (30-37,
40-47, 90-97, 100-107) are defined by the ANSI standard. The package put
these parameters together to create a full SGR command.

The original specification only had 8 colors, and just gave them names.
The SGR parameters ``30–37`` selected the foreground color, while
``40–47`` selected the background. Quite a few terminals implemented
"bold" (SGR code ``1``) as a brighter color rather than a different
font, thus providing 8 additional foreground colors. Usually you could
not get these as background colors, though sometimes inverse video (SGR
code 7) would allow that. Examples: to get black letters on white
background use ``ESC[30;47m``, to get red use ``ESC[31m``, to get bright
red use ``ESC[1;31m``. To reset colors to their defaults, use
``ESC[39;49m`` (not supported on some terminals), or reset all
attributes with ``ESC[0m``. Later terminals added the ability to
directly specify the "bright" colors with ``90–97`` and ``100–107``.

The following diagram shows the complete text style and color rendering
scheme.

|how-to-print-colored-text-in-python|

The package supports the parameters shown in the tables below:

Font Styles
^^^^^^^^^^^

+-----------+---------------------------+---------------------------+
| Parameter | Name                      | Note                      |
+===========+===========================+===========================+
| 0         | Reset or normal           | All attributes off        |
+-----------+---------------------------+---------------------------+
| 1         | Bold or increased         | As with faint, the color  |
|           | intensity                 | change is a PC (SCO/CGA)  |
|           |                           | invention                 |
+-----------+---------------------------+---------------------------+
| 2         | Faint, decreased          | May be implemented as a   |
|           | intensity, or dim         | light font weight like    |
|           |                           | bold                      |
+-----------+---------------------------+---------------------------+
| 3         | Italic                    | Not widely supported.     |
|           |                           | Sometimes treated as      |
|           |                           | inverse or blink          |
+-----------+---------------------------+---------------------------+
| 4         | Underline                 | Style extensions exist    |
|           |                           | for Kitty, VTE, mintty    |
|           |                           | and iTerm2                |
+-----------+---------------------------+---------------------------+
| 5         | Blink or Slow blink       | Sets blinking to less     |
|           |                           | than 150 times per minute |
+-----------+---------------------------+---------------------------+
| 7         | Negative, Reverse or      | Swap foreground and       |
|           | invert                    | background colors;        |
|           |                           | inconsistent emulation    |
+-----------+---------------------------+---------------------------+
| 8         | Conceal or hide           | Not widely supported      |
+-----------+---------------------------+---------------------------+

Foreground/Background Colors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========== ========== ====================
Foreground Background Name
========== ========== ====================
30         40         Black
31         41         Red
32         42         Green
33         43         Yellow
34         44         Blue
35         45         Magenta
36         46         Cyan
37         47         White
90         100        Black Bright or Grey
91         101        Red Bright
92         102        Green Bright
93         103        Yellow Bright
94         104        Blue Bright
95         105        Magenta Bright
96         106        Cyan Bright
97         107        Bright
========== ========== ====================

Test scripts in the source code repository print formatted/colored
tables using supported ANSI sequences. The following styles and colors
works with most terminal applications.

|colored-style--python|

|colored-text--python|

The package has no requirements other than the standard library.

Usage
~~~~~

How to use the module in your own python code:

.. code-block:: python

   from termformatters import StyleFormatters
   from termformatters import ForegroundFormatters
   from termformatters import BackgroundFormatters

   """Creating Formatters Instances"""
   S = StyleFormatters()
   FG = ForegroundFormatters()
   BG = BackgroundFormatters()

   print(FG.green("Printing `Green` colored text"))
   print(FG.cyan("Printing `Cyan` colored text"))
   print(
       S.bold(
           FG.white_bright(
               "Printing `Bold` and `White Bright` text"
           )
       )
   )
   print(
       FG.yellow(
           BG.blue_bright(
               "Printing `Yellow` text on `Blue` background"
           )
       )
   )

References
~~~~~~~~~~

-  `ANSI escape code
   standard <https://en.wikipedia.org/wiki/ANSI_escape_code>`__
-  `ISO/IEC
   6429 <https://www.ecma-international.org/publications/standards/Ecma-048.htm>`__

.. |colored-text-python| image:: https://user-images.githubusercontent.com/101603641/195454314-e0b5352f-3312-496a-a9aa-1f67ac370efc.jpg
.. |how-to-print-colored-text-in-python| image:: https://user-images.githubusercontent.com/101603641/195437212-1de20dbd-47ce-43fa-826f-e8f069813e3b.jpg
.. |colored-style--python| image:: https://user-images.githubusercontent.com/101603641/195454430-4856cf8d-3a71-4584-b462-cf56430c5d64.gif
.. |colored-text--python| image:: https://user-images.githubusercontent.com/101603641/195454450-625c2d22-0b2e-4db0-8016-7c4cafad6116.jpg
.. |Test Package| image:: https://github.com/amarienko/TerminalFormatters/actions/workflows/termformatters-main-lint-and-test.yaml/badge.svg?branch=main
   :target: https://github.com/amarienko/TerminalFormatters/actions/workflows/termformatters-main-lint-and-test.yaml
.. |Black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
