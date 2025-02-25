# microsoftOneDrive operations
from typing import List
from langchain.tools import BaseTool
from .. import MicrosoftonedriveCredentials

def get_tools() -> List[BaseTool]:
    """Get all microsoftOneDrive operation tools."""
    tools = []
    from .copy import MicrosoftonedriveCopyTool
    tools.append(MicrosoftonedriveCopyTool())
    from .delete import MicrosoftonedriveDeleteTool
    tools.append(MicrosoftonedriveDeleteTool())
    from .download import MicrosoftonedriveDownloadTool
    tools.append(MicrosoftonedriveDownloadTool())
    from .get import MicrosoftonedriveGetTool
    tools.append(MicrosoftonedriveGetTool())
    from .rename import MicrosoftonedriveRenameTool
    tools.append(MicrosoftonedriveRenameTool())
    from .search import MicrosoftonedriveSearchTool
    tools.append(MicrosoftonedriveSearchTool())
    from .share import MicrosoftonedriveShareTool
    tools.append(MicrosoftonedriveShareTool())
    from .upload import MicrosoftonedriveUploadTool
    tools.append(MicrosoftonedriveUploadTool())
    from .create import MicrosoftonedriveCreateTool
    tools.append(MicrosoftonedriveCreateTool())
    from .delete import MicrosoftonedriveDeleteTool
    tools.append(MicrosoftonedriveDeleteTool())
    from .getchildren import MicrosoftonedriveGetchildrenTool
    tools.append(MicrosoftonedriveGetchildrenTool())
    from .rename import MicrosoftonedriveRenameTool
    tools.append(MicrosoftonedriveRenameTool())
    from .search import MicrosoftonedriveSearchTool
    tools.append(MicrosoftonedriveSearchTool())
    from .share import MicrosoftonedriveShareTool
    tools.append(MicrosoftonedriveShareTool())
    return tools
