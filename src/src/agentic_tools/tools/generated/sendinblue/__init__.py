# sendInBlue toolkit
from langchain.tools import BaseTool
from typing import List

def get_sendinblue_tools() -> List[BaseTool]:
    """Get all sendInBlue tools."""
    from . import operations
    return operations.get_tools()
