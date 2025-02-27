# egoi operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import EgoiCredentials

def get_tools() -> List[BaseTool]:
    """Get all egoi operation tools."""
    tools = []
    from .create import EgoiCreateTool
    tools.append(EgoiCreateTool())
    from .get import EgoiGetTool
    tools.append(EgoiGetTool())
    from .getall import EgoiGetallTool
    tools.append(EgoiGetallTool())
    from .update import EgoiUpdateTool
    tools.append(EgoiUpdateTool())
    return tools
