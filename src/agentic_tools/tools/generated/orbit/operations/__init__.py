# orbit operations
from typing import List
from langchain.tools import BaseTool
from .. import OrbitCredentials

def get_tools() -> List[BaseTool]:
    """Get all orbit operation tools."""
    tools = []
    from .create import OrbitCreateTool
    tools.append(OrbitCreateTool())
    from .getall import OrbitGetallTool
    tools.append(OrbitGetallTool())
    from .upsert import OrbitUpsertTool
    tools.append(OrbitUpsertTool())
    from .delete import OrbitDeleteTool
    tools.append(OrbitDeleteTool())
    from .get import OrbitGetTool
    tools.append(OrbitGetTool())
    from .getall import OrbitGetallTool
    tools.append(OrbitGetallTool())
    from .lookup import OrbitLookupTool
    tools.append(OrbitLookupTool())
    from .update import OrbitUpdateTool
    tools.append(OrbitUpdateTool())
    from .create import OrbitCreateTool
    tools.append(OrbitCreateTool())
    from .getall import OrbitGetallTool
    tools.append(OrbitGetallTool())
    from .update import OrbitUpdateTool
    tools.append(OrbitUpdateTool())
    from .create import OrbitCreateTool
    tools.append(OrbitCreateTool())
    from .getall import OrbitGetallTool
    tools.append(OrbitGetallTool())
    from .delete import OrbitDeleteTool
    tools.append(OrbitDeleteTool())
    return tools
