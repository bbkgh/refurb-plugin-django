from dataclasses import dataclass

from mypy.nodes import CallExpr, NameExpr, StrExpr

from refurb.error import Error


@dataclass
class ErrorCallProperty(Error):
    """
    Don't call property instead of accessing it directly.

    Bad:
        class MyClass:
            @property
            def my_property(self):
                return 1
        MyClass().my_property()


    Good:
        class MyClass:
            @property
            def my_property(self):
                return 1
        MyClass().my_property

    """

    prefix = "PROPERTY"
    code = 700
    msg: str = "Calling property instead of accessing it as variable"


def check(node: CallExpr, errors: list[Error]) -> None:
    match node:
        case CallExpr(
            callee=NameExpr(fullname="builtins.print"),
            args=[StrExpr(value="Hello world!")],
        ):
            errors.append(ErrorCallProperty(node.line, node.column))
