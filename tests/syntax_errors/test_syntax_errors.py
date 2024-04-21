import pytest
import os

from compiler.frontend import tree_from_file
from compiler.core.errors.compiler_syntaxerror import CompilerSyntaxError


@pytest.mark.parametrize("input_file", os.listdir("./tests/syntax_errors/files"))
def test_syntax_err(input_file) -> None:
    with pytest.raises(CompilerSyntaxError):
        tree_from_file(f"./files/{input_file}")
