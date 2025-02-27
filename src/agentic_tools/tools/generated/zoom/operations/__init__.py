# zoom operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ZoomCredentials

def get_tools() -> List[BaseTool]:
    """Get all zoom operation tools."""
    tools = []
    from .create import ZoomCreateTool
    tools.append(ZoomCreateTool())
    from .delete import ZoomDeleteTool
    tools.append(ZoomDeleteTool())
    from .get import ZoomGetTool
    tools.append(ZoomGetTool())
    from .getall import ZoomGetallTool
    tools.append(ZoomGetallTool())
    from .update import ZoomUpdateTool
    tools.append(ZoomUpdateTool())
    from .__custom_api_call__ import Zoom__custom_api_call__Tool
    tools.append(Zoom__custom_api_call__Tool())
    return tools
