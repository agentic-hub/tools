# ftp operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all ftp operation tools."""
    tools = []
    from .delete import FtpDeleteTool
    tools.append(FtpDeleteTool())
    from .download import FtpDownloadTool
    tools.append(FtpDownloadTool())
    from .list import FtpListTool
    tools.append(FtpListTool())
    from .rename import FtpRenameTool
    tools.append(FtpRenameTool())
    from .upload import FtpUploadTool
    tools.append(FtpUploadTool())
    return tools
