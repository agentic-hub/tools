# bitwarden operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import BitwardenCredentials

def get_tools() -> List[BaseTool]:
    """Get all bitwarden operation tools."""
    tools = []
    from .delete import BitwardenDeleteTool
    tools.append(BitwardenDeleteTool())
    from .get import BitwardenGetTool
    tools.append(BitwardenGetTool())
    from .getall import BitwardenGetallTool
    tools.append(BitwardenGetallTool())
    from .update import BitwardenUpdateTool
    tools.append(BitwardenUpdateTool())
    from .getall import BitwardenGetallTool
    tools.append(BitwardenGetallTool())
    from .create import BitwardenCreateTool
    tools.append(BitwardenCreateTool())
    from .delete import BitwardenDeleteTool
    tools.append(BitwardenDeleteTool())
    from .get import BitwardenGetTool
    tools.append(BitwardenGetTool())
    from .getall import BitwardenGetallTool
    tools.append(BitwardenGetallTool())
    from .getmembers import BitwardenGetmembersTool
    tools.append(BitwardenGetmembersTool())
    from .update import BitwardenUpdateTool
    tools.append(BitwardenUpdateTool())
    from .updatemembers import BitwardenUpdatemembersTool
    tools.append(BitwardenUpdatemembersTool())
    from .create import BitwardenCreateTool
    tools.append(BitwardenCreateTool())
    from .delete import BitwardenDeleteTool
    tools.append(BitwardenDeleteTool())
    from .get import BitwardenGetTool
    tools.append(BitwardenGetTool())
    from .getgroups import BitwardenGetgroupsTool
    tools.append(BitwardenGetgroupsTool())
    from .getall import BitwardenGetallTool
    tools.append(BitwardenGetallTool())
    from .update import BitwardenUpdateTool
    tools.append(BitwardenUpdateTool())
    from .updategroups import BitwardenUpdategroupsTool
    tools.append(BitwardenUpdategroupsTool())
    return tools
