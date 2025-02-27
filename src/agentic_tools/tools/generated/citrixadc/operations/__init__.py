# citrixAdc operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import CitrixadcCredentials

def get_tools() -> List[BaseTool]:
    """Get all citrixAdc operation tools."""
    tools = []
    from .create import CitrixadcCreateTool
    tools.append(CitrixadcCreateTool())
    from .install import CitrixadcInstallTool
    tools.append(CitrixadcInstallTool())
    from .__custom_api_call__ import Citrixadc__custom_api_call__Tool
    tools.append(Citrixadc__custom_api_call__Tool())
    from .delete import CitrixadcDeleteTool
    tools.append(CitrixadcDeleteTool())
    from .download import CitrixadcDownloadTool
    tools.append(CitrixadcDownloadTool())
    from .upload import CitrixadcUploadTool
    tools.append(CitrixadcUploadTool())
    from .__custom_api_call__ import Citrixadc__custom_api_call__Tool
    tools.append(Citrixadc__custom_api_call__Tool())
    return tools
