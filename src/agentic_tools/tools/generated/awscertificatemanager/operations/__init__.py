# awsCertificateManager operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsCertificateManager operation tools."""
    tools = []
    from .delete import AwscertificatemanagerDeleteTool
    tools.append(AwscertificatemanagerDeleteTool())
    from .get import AwscertificatemanagerGetTool
    tools.append(AwscertificatemanagerGetTool())
    from .getmany import AwscertificatemanagerGetmanyTool
    tools.append(AwscertificatemanagerGetmanyTool())
    from .getmetadata import AwscertificatemanagerGetmetadataTool
    tools.append(AwscertificatemanagerGetmetadataTool())
    from .renew import AwscertificatemanagerRenewTool
    tools.append(AwscertificatemanagerRenewTool())
    from .__custom_api_call__ import Awscertificatemanager__custom_api_call__Tool
    tools.append(Awscertificatemanager__custom_api_call__Tool())
    return tools
