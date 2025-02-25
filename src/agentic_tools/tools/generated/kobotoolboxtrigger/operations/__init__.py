# koBoToolboxTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all koBoToolboxTrigger operation tools."""
    tools = []
    from .default import KobotoolboxtriggerDefaultTool
    tools.append(KobotoolboxtriggerDefaultTool())
    return tools
