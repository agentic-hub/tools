# facebookGraphApi toolkit
from langchain.tools import BaseTool
from typing import List

def get_facebookgraphapi_tools() -> List[BaseTool]:
    """Get all facebookGraphApi tools."""
    from . import operations
    return operations.get_tools()
