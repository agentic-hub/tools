# cockpit operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import CockpitCredentials

def get_tools() -> List[BaseTool]:
    """Get all cockpit operation tools."""
    tools = []
    from .create import CockpitCreateTool
    tools.append(CockpitCreateTool())
    from .getall import CockpitGetallTool
    tools.append(CockpitGetallTool())
    from .update import CockpitUpdateTool
    tools.append(CockpitUpdateTool())
    from .submit import CockpitSubmitTool
    tools.append(CockpitSubmitTool())
    from .get import CockpitGetTool
    tools.append(CockpitGetTool())
    return tools
