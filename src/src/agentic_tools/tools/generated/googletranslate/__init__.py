# googleTranslate toolkit
from langchain.tools import BaseTool
from typing import List

def get_googletranslate_tools() -> List[BaseTool]:
    """Get all googleTranslate tools."""
    from . import operations
    return operations.get_tools()
