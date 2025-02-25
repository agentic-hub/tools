# awsCertificateManager toolkit
from langchain.tools import BaseTool
from typing import List

def get_awscertificatemanager_tools() -> List[BaseTool]:
    """Get all awsCertificateManager tools."""
    from . import operations
    return operations.get_tools()
