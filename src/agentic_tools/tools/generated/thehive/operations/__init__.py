# theHive operations
from typing import List
from langchain.tools import BaseTool
from .. import ThehiveCredentials

def get_tools() -> List[BaseTool]:
    """Get all theHive operation tools."""
    tools = []
    from .create import ThehiveCreateTool
    tools.append(ThehiveCreateTool())
    from .executeresponder import ThehiveExecuteresponderTool
    tools.append(ThehiveExecuteresponderTool())
    from .getall import ThehiveGetallTool
    tools.append(ThehiveGetallTool())
    from .get import ThehiveGetTool
    tools.append(ThehiveGetTool())
    from .__custom_api_call__ import Thehive__custom_api_call__Tool
    tools.append(Thehive__custom_api_call__Tool())
    return tools
