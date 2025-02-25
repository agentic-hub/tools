# scade-tools operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all scade-tools operation tools."""
    tools = []
    from .generate import Scade-toolsGenerateTool
    tools.append(Scade-toolsGenerateTool())
    from .__custom_api_call__ import Scade-tools__custom_api_call__Tool
    tools.append(Scade-tools__custom_api_call__Tool())
    from .create import Scade-toolsCreateTool
    tools.append(Scade-toolsCreateTool())
    from .delete import Scade-toolsDeleteTool
    tools.append(Scade-toolsDeleteTool())
    from .getschema import Scade-toolsGetschemaTool
    tools.append(Scade-toolsGetschemaTool())
    from .__custom_api_call__ import Scade-tools__custom_api_call__Tool
    tools.append(Scade-tools__custom_api_call__Tool())
    from .get import Scade-toolsGetTool
    tools.append(Scade-toolsGetTool())
    from .getall import Scade-toolsGetallTool
    tools.append(Scade-toolsGetallTool())
    from .delete import Scade-toolsDeleteTool
    tools.append(Scade-toolsDeleteTool())
    from .__custom_api_call__ import Scade-tools__custom_api_call__Tool
    tools.append(Scade-tools__custom_api_call__Tool())
    from .activate import Scade-toolsActivateTool
    tools.append(Scade-toolsActivateTool())
    from .create import Scade-toolsCreateTool
    tools.append(Scade-toolsCreateTool())
    from .deactivate import Scade-toolsDeactivateTool
    tools.append(Scade-toolsDeactivateTool())
    from .delete import Scade-toolsDeleteTool
    tools.append(Scade-toolsDeleteTool())
    from .get import Scade-toolsGetTool
    tools.append(Scade-toolsGetTool())
    from .getall import Scade-toolsGetallTool
    tools.append(Scade-toolsGetallTool())
    from .update import Scade-toolsUpdateTool
    tools.append(Scade-toolsUpdateTool())
    from .__custom_api_call__ import Scade-tools__custom_api_call__Tool
    tools.append(Scade-tools__custom_api_call__Tool())
    return tools
