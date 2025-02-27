# googleTasks operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GoogletasksCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleTasks operation tools."""
    tools = []
    from .create import GoogletasksCreateTool
    tools.append(GoogletasksCreateTool())
    from .delete import GoogletasksDeleteTool
    tools.append(GoogletasksDeleteTool())
    from .get import GoogletasksGetTool
    tools.append(GoogletasksGetTool())
    from .getall import GoogletasksGetallTool
    tools.append(GoogletasksGetallTool())
    from .update import GoogletasksUpdateTool
    tools.append(GoogletasksUpdateTool())
    from .__custom_api_call__ import Googletasks__custom_api_call__Tool
    tools.append(Googletasks__custom_api_call__Tool())
    return tools
