# dropcontact operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import DropcontactCredentials

def get_tools() -> List[BaseTool]:
    """Get all dropcontact operation tools."""
    tools = []
    from .enrich import DropcontactEnrichTool
    tools.append(DropcontactEnrichTool())
    from .fetchrequest import DropcontactFetchrequestTool
    tools.append(DropcontactFetchrequestTool())
    from .__custom_api_call__ import Dropcontact__custom_api_call__Tool
    tools.append(Dropcontact__custom_api_call__Tool())
    return tools
