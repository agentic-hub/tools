# ssh operations
from typing import List
from langchain.tools import BaseTool
from .. import SshCredentials

def get_tools() -> List[BaseTool]:
    """Get all ssh operation tools."""
    tools = []
    from .execute import SshExecuteTool
    tools.append(SshExecuteTool())
    from .download import SshDownloadTool
    tools.append(SshDownloadTool())
    from .upload import SshUploadTool
    tools.append(SshUploadTool())
    return tools
