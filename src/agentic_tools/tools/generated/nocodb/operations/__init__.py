# nocoDb operations
from typing import List
from langchain.tools import BaseTool
from .. import NocodbCredentials

def get_tools() -> List[BaseTool]:
    """Get all nocoDb operation tools."""
    tools = []
    from .create import NocodbCreateTool
    tools.append(NocodbCreateTool())
    from .delete import NocodbDeleteTool
    tools.append(NocodbDeleteTool())
    from .get import NocodbGetTool
    tools.append(NocodbGetTool())
    from .getall import NocodbGetallTool
    tools.append(NocodbGetallTool())
    from .update import NocodbUpdateTool
    tools.append(NocodbUpdateTool())
    from .__custom_api_call__ import Nocodb__custom_api_call__Tool
    tools.append(Nocodb__custom_api_call__Tool())
    return tools
