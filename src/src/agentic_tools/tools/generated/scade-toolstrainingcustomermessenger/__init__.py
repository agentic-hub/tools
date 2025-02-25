# scade-toolsTrainingCustomerMessenger toolkit
from langchain.tools import BaseTool
from typing import List

def get_scade-toolstrainingcustomermessenger_tools() -> List[BaseTool]:
    """Get all scade-toolsTrainingCustomerMessenger tools."""
    from . import operations
    return operations.get_tools()
