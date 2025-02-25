# adalo operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all adalo operation tools."""
    tools = []
    from .create import AdaloCreateTool
    tools.append(AdaloCreateTool())
    from .delete import AdaloDeleteTool
    tools.append(AdaloDeleteTool())
    from .get import AdaloGetTool
    tools.append(AdaloGetTool())
    from .getall import AdaloGetallTool
    tools.append(AdaloGetallTool())
    from .update import AdaloUpdateTool
    tools.append(AdaloUpdateTool())
    from .__custom_api_call__ import Adalo__custom_api_call__Tool
    tools.append(Adalo__custom_api_call__Tool())
    return tools
