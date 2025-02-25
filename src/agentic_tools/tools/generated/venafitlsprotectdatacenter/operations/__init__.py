# venafiTlsProtectDatacenter operations
from typing import List
from langchain.tools import BaseTool
from .. import VenafitlsprotectdatacenterCredentials

def get_tools() -> List[BaseTool]:
    """Get all venafiTlsProtectDatacenter operation tools."""
    tools = []
    from .create import VenafitlsprotectdatacenterCreateTool
    tools.append(VenafitlsprotectdatacenterCreateTool())
    from .delete import VenafitlsprotectdatacenterDeleteTool
    tools.append(VenafitlsprotectdatacenterDeleteTool())
    from .download import VenafitlsprotectdatacenterDownloadTool
    tools.append(VenafitlsprotectdatacenterDownloadTool())
    from .get import VenafitlsprotectdatacenterGetTool
    tools.append(VenafitlsprotectdatacenterGetTool())
    from .getmany import VenafitlsprotectdatacenterGetmanyTool
    tools.append(VenafitlsprotectdatacenterGetmanyTool())
    from .renew import VenafitlsprotectdatacenterRenewTool
    tools.append(VenafitlsprotectdatacenterRenewTool())
    from .__custom_api_call__ import Venafitlsprotectdatacenter__custom_api_call__Tool
    tools.append(Venafitlsprotectdatacenter__custom_api_call__Tool())
    from .get import VenafitlsprotectdatacenterGetTool
    tools.append(VenafitlsprotectdatacenterGetTool())
    from .__custom_api_call__ import Venafitlsprotectdatacenter__custom_api_call__Tool
    tools.append(Venafitlsprotectdatacenter__custom_api_call__Tool())
    return tools
