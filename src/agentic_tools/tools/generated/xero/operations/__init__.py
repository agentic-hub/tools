# xero operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import XeroCredentials

def get_tools() -> List[BaseTool]:
    """Get all xero operation tools."""
    tools = []
    from .create import XeroCreateTool
    tools.append(XeroCreateTool())
    from .get import XeroGetTool
    tools.append(XeroGetTool())
    from .getall import XeroGetallTool
    tools.append(XeroGetallTool())
    from .update import XeroUpdateTool
    tools.append(XeroUpdateTool())
    from .__custom_api_call__ import Xero__custom_api_call__Tool
    tools.append(Xero__custom_api_call__Tool())
    from .create import XeroCreateTool
    tools.append(XeroCreateTool())
    from .get import XeroGetTool
    tools.append(XeroGetTool())
    from .getall import XeroGetallTool
    tools.append(XeroGetallTool())
    from .update import XeroUpdateTool
    tools.append(XeroUpdateTool())
    from .__custom_api_call__ import Xero__custom_api_call__Tool
    tools.append(Xero__custom_api_call__Tool())
    return tools
