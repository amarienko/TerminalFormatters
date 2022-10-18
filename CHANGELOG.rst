v0.2.1
~~~~~~~~~

- Initial stable release

v0.2.1rc2
~~~~~~~~~

- Fix of syntax errors or undefined names according to the flake8 report:

.. code-block::

  0
  ./src/test_termformatters.py:113:9: F841 local variable 'S' is assigned to but never used
  ./src/test_termformatters.py:114:9: F841 local variable 'FG' is assigned to but never used
  ./src/test_termformatters.py:115:9: F841 local variable 'BG' is assigned to but never used
  ./src/termformatters/__init__.py:30:31: W605 invalid escape sequence '\]'
  ./src/termformatters/__init__.py:109:1: F401 'sys' imported but unused
  ./src/termformatters/__init__.py:112:1: F401 '.base.SelectFormatter' imported but unused
  ./src/termformatters/__init__.py:112:1: E402 module level import not at top of file
  ./src/termformatters/__init__.py:113:1: F401 '.base.BaseFormat' imported but unused
  ./src/termformatters/__init__.py:113:1: E402 module level import not at top of file
  ./src/termformatters/__init__.py:116:1: E402 module level import not at top of file
  ./src/termformatters/__init__.py:117:1: E402 module level import not at top of file
  ./src/termformatters/__init__.py:118:1: E402 module level import not at top of file
  ./src/termformatters/__init__.py:163:5: F841 local variable 'stylesList' is assigned to but never used
  ./src/termformatters/__init__.py:214:1: E266 too many leading '#' for block comment
  ./src/termformatters/base.py:3:1: F401 'sys' imported but unused
  ./src/termformatters/base.py:6:1: F401 'functools' imported but unused
  ./src/termformatters/base.py:7:1: F401 'functools.wraps' imported but unused
  1     E266 too many leading '#' for block comment
  5     E402 module level import not at top of file
  6     F401 'sys' imported but unused
  4     F841 local variable 'stylesList' is assigned to but never used
  1     W605 invalid escape sequence '\]'
  17

- Changes in '__init__.py' doc string and comments according to final flake8 report:

.. code-block::

  0
  ./src/termformatters/__init__.py:30:31: W605 invalid escape sequence '\]'
  ./src/termformatters/__init__.py:211:1: E266 too many leading '#' for block comment
  1     E266 too many leading '#' for block comment
  1     W605 invalid escape sequence '\]'
  2

v0.2.1rc1
~~~~~~~~~

- Initial stable pre-release
