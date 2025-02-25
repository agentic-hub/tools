# openThesaurus toolkit
from langchain.tools import BaseTool
from typing import List

def get_openthesaurus_tools() -> List[BaseTool]:
    """Get all openThesaurus tools."""
    from . import operations
    return operations.get_tools()
