from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ForwardRef,
    Literal,
    Optional,
    TypedDict,
    TypeVar,
    Union,
    _eval_type,  # type: ignore[misc]
    get_args,
    get_origin,
)

# New in version 3.10
try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

__all__ = [
    "TYPE_CHECKING",
    "Any",
    "Callable",
    "ForwardRef",
    "Literal",
    "Optional",
    "TypeVar",
    "TypedDict",
    "TypesDict",
    "Union",
    "eval_type",
    "get_args",
    "get_origin",
]

eval_type = _eval_type
TypesDict: TypeAlias = dict[str, Union[Optional[type], "TypesDict"]]  # type: ignore[assignment]
