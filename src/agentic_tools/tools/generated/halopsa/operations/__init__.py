# haloPSA operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import HalopsaCredentials

def get_tools() -> List[BaseTool]:
    """Get all haloPSA operation tools."""
    tools = []
    from .create import HalopsaCreateTool
    tools.append(HalopsaCreateTool())
    from .delete import HalopsaDeleteTool
    tools.append(HalopsaDeleteTool())
    from .get import HalopsaGetTool
    tools.append(HalopsaGetTool())
    from .getall import HalopsaGetallTool
    tools.append(HalopsaGetallTool())
    from .update import HalopsaUpdateTool
    tools.append(HalopsaUpdateTool())
    from .create import HalopsaCreateTool
    tools.append(HalopsaCreateTool())
    from .delete import HalopsaDeleteTool
    tools.append(HalopsaDeleteTool())
    from .get import HalopsaGetTool
    tools.append(HalopsaGetTool())
    from .getall import HalopsaGetallTool
    tools.append(HalopsaGetallTool())
    from .update import HalopsaUpdateTool
    tools.append(HalopsaUpdateTool())
    from .create import HalopsaCreateTool
    tools.append(HalopsaCreateTool())
    from .delete import HalopsaDeleteTool
    tools.append(HalopsaDeleteTool())
    from .get import HalopsaGetTool
    tools.append(HalopsaGetTool())
    from .getall import HalopsaGetallTool
    tools.append(HalopsaGetallTool())
    from .update import HalopsaUpdateTool
    tools.append(HalopsaUpdateTool())
    from .create import HalopsaCreateTool
    tools.append(HalopsaCreateTool())
    from .delete import HalopsaDeleteTool
    tools.append(HalopsaDeleteTool())
    from .get import HalopsaGetTool
    tools.append(HalopsaGetTool())
    from .getall import HalopsaGetallTool
    tools.append(HalopsaGetallTool())
    from .update import HalopsaUpdateTool
    tools.append(HalopsaUpdateTool())
    return tools
