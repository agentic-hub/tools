# demio operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import DemioCredentials

def get_tools() -> List[BaseTool]:
    """Get all demio operation tools."""
    tools = []
    from .get import DemioGetTool
    tools.append(DemioGetTool())
    from .getall import DemioGetallTool
    tools.append(DemioGetallTool())
    from .register import DemioRegisterTool
    tools.append(DemioRegisterTool())
    from .get import DemioGetTool
    tools.append(DemioGetTool())
    return tools
