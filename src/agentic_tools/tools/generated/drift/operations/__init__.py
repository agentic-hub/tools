# drift operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import DriftCredentials

def get_tools() -> List[BaseTool]:
    """Get all drift operation tools."""
    tools = []
    from .create import DriftCreateTool
    tools.append(DriftCreateTool())
    from .getcustomattributes import DriftGetcustomattributesTool
    tools.append(DriftGetcustomattributesTool())
    from .delete import DriftDeleteTool
    tools.append(DriftDeleteTool())
    from .get import DriftGetTool
    tools.append(DriftGetTool())
    from .update import DriftUpdateTool
    tools.append(DriftUpdateTool())
    from .__custom_api_call__ import Drift__custom_api_call__Tool
    tools.append(Drift__custom_api_call__Tool())
    return tools
