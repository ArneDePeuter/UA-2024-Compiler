from src.parser.visitor.dotvisitor import DotVisitor
from src.parser.ast.expression import *

visitor = DotVisitor()
expr = BinaryArithmetic(
    BinaryArithmetic(
        INT(3),
        INT(4),
        BinaryArithmetic.Operator.plus
    ),
    BinaryArithmetic(
        INT(5),
        INT(6),
        BinaryArithmetic.Operator.minus
    ),
    BinaryArithmetic.Operator.mul
)
visitor.visit_ast(expr)
visitor.output("dot_test.dot")

