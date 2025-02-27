# ghost operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GhostCredentials

def get_tools() -> List[BaseTool]:
    """Get all ghost operation tools."""
    tools = []
    from .get import GhostGetTool
    tools.append(GhostGetTool())
    from .getall import GhostGetallTool
    tools.append(GhostGetallTool())
    from .__custom_api_call__ import Ghost__custom_api_call__Tool
    tools.append(Ghost__custom_api_call__Tool())
    from .create import GhostCreateTool
    tools.append(GhostCreateTool())
    from .delete import GhostDeleteTool
    tools.append(GhostDeleteTool())
    from .get import GhostGetTool
    tools.append(GhostGetTool())
    from .getall import GhostGetallTool
    tools.append(GhostGetallTool())
    from .update import GhostUpdateTool
    tools.append(GhostUpdateTool())
    from .__custom_api_call__ import Ghost__custom_api_call__Tool
    tools.append(Ghost__custom_api_call__Tool())
    return tools
