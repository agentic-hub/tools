# seaTable operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import SeatableCredentials

def get_tools() -> List[BaseTool]:
    """Get all seaTable operation tools."""
    tools = []
    from .create import SeatableCreateTool
    tools.append(SeatableCreateTool())
    from .delete import SeatableDeleteTool
    tools.append(SeatableDeleteTool())
    from .get import SeatableGetTool
    tools.append(SeatableGetTool())
    from .getall import SeatableGetallTool
    tools.append(SeatableGetallTool())
    from .update import SeatableUpdateTool
    tools.append(SeatableUpdateTool())
    return tools
