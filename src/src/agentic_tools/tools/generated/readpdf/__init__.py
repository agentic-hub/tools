# readPDF toolkit
from langchain.tools import BaseTool
from typing import List

def get_readpdf_tools() -> List[BaseTool]:
    """Get all readPDF tools."""
    from . import operations
    return operations.get_tools()
