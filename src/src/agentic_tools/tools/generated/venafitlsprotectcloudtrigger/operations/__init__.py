# venafiTlsProtectCloudTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all venafiTlsProtectCloudTrigger operation tools."""
    tools = []
    from .default import VenafitlsprotectcloudtriggerDefaultTool
    tools.append(VenafitlsprotectcloudtriggerDefaultTool())
    return tools
