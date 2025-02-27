# freshservice operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import FreshserviceCredentials

def get_tools() -> List[BaseTool]:
    """Get all freshservice operation tools."""
    tools = []
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    from .create import FreshserviceCreateTool
    tools.append(FreshserviceCreateTool())
    from .delete import FreshserviceDeleteTool
    tools.append(FreshserviceDeleteTool())
    from .get import FreshserviceGetTool
    tools.append(FreshserviceGetTool())
    from .getall import FreshserviceGetallTool
    tools.append(FreshserviceGetallTool())
    from .update import FreshserviceUpdateTool
    tools.append(FreshserviceUpdateTool())
    return tools
