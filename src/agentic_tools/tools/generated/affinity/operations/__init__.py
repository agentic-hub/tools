# affinity operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import AffinityCredentials

def get_tools() -> List[BaseTool]:
    """Get all affinity operation tools."""
    tools = []
    from .get import AffinityGetTool
    tools.append(AffinityGetTool())
    from .getall import AffinityGetallTool
    tools.append(AffinityGetallTool())
    from .create import AffinityCreateTool
    tools.append(AffinityCreateTool())
    from .delete import AffinityDeleteTool
    tools.append(AffinityDeleteTool())
    from .get import AffinityGetTool
    tools.append(AffinityGetTool())
    from .getall import AffinityGetallTool
    tools.append(AffinityGetallTool())
    from .create import AffinityCreateTool
    tools.append(AffinityCreateTool())
    from .delete import AffinityDeleteTool
    tools.append(AffinityDeleteTool())
    from .get import AffinityGetTool
    tools.append(AffinityGetTool())
    from .getall import AffinityGetallTool
    tools.append(AffinityGetallTool())
    from .update import AffinityUpdateTool
    tools.append(AffinityUpdateTool())
    from .create import AffinityCreateTool
    tools.append(AffinityCreateTool())
    from .delete import AffinityDeleteTool
    tools.append(AffinityDeleteTool())
    from .get import AffinityGetTool
    tools.append(AffinityGetTool())
    from .getall import AffinityGetallTool
    tools.append(AffinityGetallTool())
    from .update import AffinityUpdateTool
    tools.append(AffinityUpdateTool())
    return tools
