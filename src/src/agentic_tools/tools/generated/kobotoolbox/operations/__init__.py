# koBoToolbox operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all koBoToolbox operation tools."""
    tools = []
    from .get import KobotoolboxGetTool
    tools.append(KobotoolboxGetTool())
    from .getall import KobotoolboxGetallTool
    tools.append(KobotoolboxGetallTool())
    from .redeploy import KobotoolboxRedeployTool
    tools.append(KobotoolboxRedeployTool())
    from .__custom_api_call__ import Kobotoolbox__custom_api_call__Tool
    tools.append(Kobotoolbox__custom_api_call__Tool())
    from .get import KobotoolboxGetTool
    tools.append(KobotoolboxGetTool())
    from .getall import KobotoolboxGetallTool
    tools.append(KobotoolboxGetallTool())
    from .getlogs import KobotoolboxGetlogsTool
    tools.append(KobotoolboxGetlogsTool())
    from .retryall import KobotoolboxRetryallTool
    tools.append(KobotoolboxRetryallTool())
    from .retryone import KobotoolboxRetryoneTool
    tools.append(KobotoolboxRetryoneTool())
    from .__custom_api_call__ import Kobotoolbox__custom_api_call__Tool
    tools.append(Kobotoolbox__custom_api_call__Tool())
    from .delete import KobotoolboxDeleteTool
    tools.append(KobotoolboxDeleteTool())
    from .get import KobotoolboxGetTool
    tools.append(KobotoolboxGetTool())
    from .getall import KobotoolboxGetallTool
    tools.append(KobotoolboxGetallTool())
    from .getvalidation import KobotoolboxGetvalidationTool
    tools.append(KobotoolboxGetvalidationTool())
    from .setvalidation import KobotoolboxSetvalidationTool
    tools.append(KobotoolboxSetvalidationTool())
    from .__custom_api_call__ import Kobotoolbox__custom_api_call__Tool
    tools.append(Kobotoolbox__custom_api_call__Tool())
    from .create import KobotoolboxCreateTool
    tools.append(KobotoolboxCreateTool())
    from .delete import KobotoolboxDeleteTool
    tools.append(KobotoolboxDeleteTool())
    from .get import KobotoolboxGetTool
    tools.append(KobotoolboxGetTool())
    from .getall import KobotoolboxGetallTool
    tools.append(KobotoolboxGetallTool())
    from .__custom_api_call__ import Kobotoolbox__custom_api_call__Tool
    tools.append(Kobotoolbox__custom_api_call__Tool())
    return tools
