# venafiTlsProtectCloudTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_venafitlsprotectcloudtrigger_tools() -> List[BaseTool]:
    """Get all venafiTlsProtectCloudTrigger tools."""
    from . import operations
    return operations.get_tools()
