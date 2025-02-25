# beeminder operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all beeminder operation tools."""
    tools = []
    from .create import BeeminderCreateTool
    tools.append(BeeminderCreateTool())
    from .delete import BeeminderDeleteTool
    tools.append(BeeminderDeleteTool())
    from .getall import BeeminderGetallTool
    tools.append(BeeminderGetallTool())
    from .update import BeeminderUpdateTool
    tools.append(BeeminderUpdateTool())
    from .__custom_api_call__ import Beeminder__custom_api_call__Tool
    tools.append(Beeminder__custom_api_call__Tool())
    return tools
