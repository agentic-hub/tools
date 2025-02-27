# actionNetwork operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ActionnetworkCredentials

def get_tools() -> List[BaseTool]:
    """Get all actionNetwork operation tools."""
    tools = []
    from .create import ActionnetworkCreateTool
    tools.append(ActionnetworkCreateTool())
    from .get import ActionnetworkGetTool
    tools.append(ActionnetworkGetTool())
    from .getall import ActionnetworkGetallTool
    tools.append(ActionnetworkGetallTool())
    from .__custom_api_call__ import Actionnetwork__custom_api_call__Tool
    tools.append(Actionnetwork__custom_api_call__Tool())
    from .create import ActionnetworkCreateTool
    tools.append(ActionnetworkCreateTool())
    from .get import ActionnetworkGetTool
    tools.append(ActionnetworkGetTool())
    from .getall import ActionnetworkGetallTool
    tools.append(ActionnetworkGetallTool())
    from .__custom_api_call__ import Actionnetwork__custom_api_call__Tool
    tools.append(Actionnetwork__custom_api_call__Tool())
    from .create import ActionnetworkCreateTool
    tools.append(ActionnetworkCreateTool())
    from .get import ActionnetworkGetTool
    tools.append(ActionnetworkGetTool())
    from .getall import ActionnetworkGetallTool
    tools.append(ActionnetworkGetallTool())
    from .update import ActionnetworkUpdateTool
    tools.append(ActionnetworkUpdateTool())
    from .__custom_api_call__ import Actionnetwork__custom_api_call__Tool
    tools.append(Actionnetwork__custom_api_call__Tool())
    from .create import ActionnetworkCreateTool
    tools.append(ActionnetworkCreateTool())
    from .get import ActionnetworkGetTool
    tools.append(ActionnetworkGetTool())
    from .getall import ActionnetworkGetallTool
    tools.append(ActionnetworkGetallTool())
    from .update import ActionnetworkUpdateTool
    tools.append(ActionnetworkUpdateTool())
    from .__custom_api_call__ import Actionnetwork__custom_api_call__Tool
    tools.append(Actionnetwork__custom_api_call__Tool())
    from .create import ActionnetworkCreateTool
    tools.append(ActionnetworkCreateTool())
    from .get import ActionnetworkGetTool
    tools.append(ActionnetworkGetTool())
    from .getall import ActionnetworkGetallTool
    tools.append(ActionnetworkGetallTool())
    from .update import ActionnetworkUpdateTool
    tools.append(ActionnetworkUpdateTool())
    from .__custom_api_call__ import Actionnetwork__custom_api_call__Tool
    tools.append(Actionnetwork__custom_api_call__Tool())
    from .create import ActionnetworkCreateTool
    tools.append(ActionnetworkCreateTool())
    from .get import ActionnetworkGetTool
    tools.append(ActionnetworkGetTool())
    from .getall import ActionnetworkGetallTool
    tools.append(ActionnetworkGetallTool())
    from .__custom_api_call__ import Actionnetwork__custom_api_call__Tool
    tools.append(Actionnetwork__custom_api_call__Tool())
    from .add import ActionnetworkAddTool
    tools.append(ActionnetworkAddTool())
    from .remove import ActionnetworkRemoveTool
    tools.append(ActionnetworkRemoveTool())
    from .__custom_api_call__ import Actionnetwork__custom_api_call__Tool
    tools.append(Actionnetwork__custom_api_call__Tool())
    return tools
