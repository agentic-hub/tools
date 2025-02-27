# circleCi operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import CircleciCredentials

def get_tools() -> List[BaseTool]:
    """Get all circleCi operation tools."""
    tools = []
    from .get import CircleciGetTool
    tools.append(CircleciGetTool())
    from .getall import CircleciGetallTool
    tools.append(CircleciGetallTool())
    from .trigger import CircleciTriggerTool
    tools.append(CircleciTriggerTool())
    return tools
