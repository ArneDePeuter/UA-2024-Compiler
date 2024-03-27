from abc import ABC
from typing import Optional, List
from dataclasses import dataclass, field


@dataclass
class AST(ABC):
    line: Optional[int] = field(default=None, kw_only=True)
    position: Optional[int] = field(default=None, kw_only=True)
    c_syntax: Optional[str] = field(default=None, kw_only=True)
