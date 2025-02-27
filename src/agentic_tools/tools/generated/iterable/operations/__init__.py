# iterable operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import IterableCredentials

def get_tools() -> List[BaseTool]:
    """Get all iterable operation tools."""
    tools = []
    from .track import IterableTrackTool
    tools.append(IterableTrackTool())
    from .upsert import IterableUpsertTool
    tools.append(IterableUpsertTool())
    from .delete import IterableDeleteTool
    tools.append(IterableDeleteTool())
    from .get import IterableGetTool
    tools.append(IterableGetTool())
    from .add import IterableAddTool
    tools.append(IterableAddTool())
    from .remove import IterableRemoveTool
    tools.append(IterableRemoveTool())
    return tools
