# grist operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GristCredentials

def get_tools() -> List[BaseTool]:
    """Get all grist operation tools."""
    tools = []
    from .create import GristCreateTool
    tools.append(GristCreateTool())
    from .delete import GristDeleteTool
    tools.append(GristDeleteTool())
    from .getall import GristGetallTool
    tools.append(GristGetallTool())
    from .update import GristUpdateTool
    tools.append(GristUpdateTool())
    return tools
