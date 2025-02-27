# scade-toolsTrainingCustomerMessenger operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all scade-toolsTrainingCustomerMessenger operation tools."""
    tools = []
    from .default import Scade-toolstrainingcustomermessengerDefaultTool
    tools.append(Scade-toolstrainingcustomermessengerDefaultTool())
    return tools
