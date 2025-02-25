# venafiTlsProtectCloud operations
from typing import List
from langchain.tools import BaseTool
from .. import VenafitlsprotectcloudCredentials

def get_tools() -> List[BaseTool]:
    """Get all venafiTlsProtectCloud operation tools."""
    tools = []
    from .delete import VenafitlsprotectcloudDeleteTool
    tools.append(VenafitlsprotectcloudDeleteTool())
    from .download import VenafitlsprotectcloudDownloadTool
    tools.append(VenafitlsprotectcloudDownloadTool())
    from .get import VenafitlsprotectcloudGetTool
    tools.append(VenafitlsprotectcloudGetTool())
    from .getmany import VenafitlsprotectcloudGetmanyTool
    tools.append(VenafitlsprotectcloudGetmanyTool())
    from .renew import VenafitlsprotectcloudRenewTool
    tools.append(VenafitlsprotectcloudRenewTool())
    from .__custom_api_call__ import Venafitlsprotectcloud__custom_api_call__Tool
    tools.append(Venafitlsprotectcloud__custom_api_call__Tool())
    from .create import VenafitlsprotectcloudCreateTool
    tools.append(VenafitlsprotectcloudCreateTool())
    from .get import VenafitlsprotectcloudGetTool
    tools.append(VenafitlsprotectcloudGetTool())
    from .getmany import VenafitlsprotectcloudGetmanyTool
    tools.append(VenafitlsprotectcloudGetmanyTool())
    from .__custom_api_call__ import Venafitlsprotectcloud__custom_api_call__Tool
    tools.append(Venafitlsprotectcloud__custom_api_call__Tool())
    return tools
