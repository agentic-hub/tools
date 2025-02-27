# helpScout operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import HelpscoutCredentials

def get_tools() -> List[BaseTool]:
    """Get all helpScout operation tools."""
    tools = []
    from .create import HelpscoutCreateTool
    tools.append(HelpscoutCreateTool())
    from .delete import HelpscoutDeleteTool
    tools.append(HelpscoutDeleteTool())
    from .get import HelpscoutGetTool
    tools.append(HelpscoutGetTool())
    from .getall import HelpscoutGetallTool
    tools.append(HelpscoutGetallTool())
    from .__custom_api_call__ import Helpscout__custom_api_call__Tool
    tools.append(Helpscout__custom_api_call__Tool())
    from .create import HelpscoutCreateTool
    tools.append(HelpscoutCreateTool())
    from .get import HelpscoutGetTool
    tools.append(HelpscoutGetTool())
    from .getall import HelpscoutGetallTool
    tools.append(HelpscoutGetallTool())
    from .properties import HelpscoutPropertiesTool
    tools.append(HelpscoutPropertiesTool())
    from .update import HelpscoutUpdateTool
    tools.append(HelpscoutUpdateTool())
    from .__custom_api_call__ import Helpscout__custom_api_call__Tool
    tools.append(Helpscout__custom_api_call__Tool())
    from .get import HelpscoutGetTool
    tools.append(HelpscoutGetTool())
    from .getall import HelpscoutGetallTool
    tools.append(HelpscoutGetallTool())
    from .__custom_api_call__ import Helpscout__custom_api_call__Tool
    tools.append(Helpscout__custom_api_call__Tool())
    from .create import HelpscoutCreateTool
    tools.append(HelpscoutCreateTool())
    from .getall import HelpscoutGetallTool
    tools.append(HelpscoutGetallTool())
    from .__custom_api_call__ import Helpscout__custom_api_call__Tool
    tools.append(Helpscout__custom_api_call__Tool())
    return tools
