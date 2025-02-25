# scade-toolsTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all scade-toolsTrigger operation tools."""
    tools = []
    from .default import Scade-toolstriggerDefaultTool
    tools.append(Scade-toolstriggerDefaultTool())
    return tools
