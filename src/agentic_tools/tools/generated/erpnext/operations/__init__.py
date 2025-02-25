# erpNext operations
from typing import List
from langchain.tools import BaseTool
from .. import ErpnextCredentials

def get_tools() -> List[BaseTool]:
    """Get all erpNext operation tools."""
    tools = []
    from .create import ErpnextCreateTool
    tools.append(ErpnextCreateTool())
    from .delete import ErpnextDeleteTool
    tools.append(ErpnextDeleteTool())
    from .get import ErpnextGetTool
    tools.append(ErpnextGetTool())
    from .getall import ErpnextGetallTool
    tools.append(ErpnextGetallTool())
    from .update import ErpnextUpdateTool
    tools.append(ErpnextUpdateTool())
    from .__custom_api_call__ import Erpnext__custom_api_call__Tool
    tools.append(Erpnext__custom_api_call__Tool())
    return tools
