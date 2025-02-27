# todoist operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import TodoistCredentials

def get_tools() -> List[BaseTool]:
    """Get all todoist operation tools."""
    tools = []
    from .close import TodoistCloseTool
    tools.append(TodoistCloseTool())
    from .create import TodoistCreateTool
    tools.append(TodoistCreateTool())
    from .delete import TodoistDeleteTool
    tools.append(TodoistDeleteTool())
    from .get import TodoistGetTool
    tools.append(TodoistGetTool())
    from .getall import TodoistGetallTool
    tools.append(TodoistGetallTool())
    from .move import TodoistMoveTool
    tools.append(TodoistMoveTool())
    from .reopen import TodoistReopenTool
    tools.append(TodoistReopenTool())
    from .update import TodoistUpdateTool
    tools.append(TodoistUpdateTool())
    from .__custom_api_call__ import Todoist__custom_api_call__Tool
    tools.append(Todoist__custom_api_call__Tool())
    return tools
