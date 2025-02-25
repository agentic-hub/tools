# raindrop operations
from typing import List
from langchain.tools import BaseTool
from .. import RaindropCredentials

def get_tools() -> List[BaseTool]:
    """Get all raindrop operation tools."""
    tools = []
    from .create import RaindropCreateTool
    tools.append(RaindropCreateTool())
    from .delete import RaindropDeleteTool
    tools.append(RaindropDeleteTool())
    from .get import RaindropGetTool
    tools.append(RaindropGetTool())
    from .getall import RaindropGetallTool
    tools.append(RaindropGetallTool())
    from .update import RaindropUpdateTool
    tools.append(RaindropUpdateTool())
    from .__custom_api_call__ import Raindrop__custom_api_call__Tool
    tools.append(Raindrop__custom_api_call__Tool())
    from .create import RaindropCreateTool
    tools.append(RaindropCreateTool())
    from .delete import RaindropDeleteTool
    tools.append(RaindropDeleteTool())
    from .get import RaindropGetTool
    tools.append(RaindropGetTool())
    from .getall import RaindropGetallTool
    tools.append(RaindropGetallTool())
    from .update import RaindropUpdateTool
    tools.append(RaindropUpdateTool())
    from .__custom_api_call__ import Raindrop__custom_api_call__Tool
    tools.append(Raindrop__custom_api_call__Tool())
    from .delete import RaindropDeleteTool
    tools.append(RaindropDeleteTool())
    from .getall import RaindropGetallTool
    tools.append(RaindropGetallTool())
    from .__custom_api_call__ import Raindrop__custom_api_call__Tool
    tools.append(Raindrop__custom_api_call__Tool())
    from .get import RaindropGetTool
    tools.append(RaindropGetTool())
    from .__custom_api_call__ import Raindrop__custom_api_call__Tool
    tools.append(Raindrop__custom_api_call__Tool())
    return tools
