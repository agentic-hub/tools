# philipsHue operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import PhilipshueCredentials

def get_tools() -> List[BaseTool]:
    """Get all philipsHue operation tools."""
    tools = []
    from .delete import PhilipshueDeleteTool
    tools.append(PhilipshueDeleteTool())
    from .get import PhilipshueGetTool
    tools.append(PhilipshueGetTool())
    from .getall import PhilipshueGetallTool
    tools.append(PhilipshueGetallTool())
    from .update import PhilipshueUpdateTool
    tools.append(PhilipshueUpdateTool())
    from .__custom_api_call__ import Philipshue__custom_api_call__Tool
    tools.append(Philipshue__custom_api_call__Tool())
    return tools
