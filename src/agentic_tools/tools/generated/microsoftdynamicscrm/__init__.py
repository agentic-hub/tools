# microsoftDynamicsCrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftdynamicscrm_tools() -> List[BaseTool]:
    """Get all microsoftDynamicsCrm tools."""
    from . import operations
    return operations.get_tools()
