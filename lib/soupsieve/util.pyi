# Stubs for soupsieve_py3.util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

MODULE: Any
DEBUG: int
RE_PATTERN_LINE_SPLIT: Any
LC_A: Any
LC_Z: Any
UC_A: Any
UC_Z: Any

def lower(string: Any): ...
def upper(string: Any): ...

class SelectorSyntaxError(Exception):
    line: Any = ...
    col: Any = ...
    context: Any = ...
    def __init__(self, msg: Any, pattern: Optional[Any] = ..., index: Optional[Any] = ...) -> None: ...

def deprecated(message: Any, stacklevel: int = ...): ...
def warn_deprecated(message: Any, stacklevel: int = ...) -> None: ...
def get_pattern_context(pattern: Any, index: Any): ...
