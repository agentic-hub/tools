# paddle operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all paddle operation tools."""
    tools = []
    from .create import PaddleCreateTool
    tools.append(PaddleCreateTool())
    from .getall import PaddleGetallTool
    tools.append(PaddleGetallTool())
    from .update import PaddleUpdateTool
    tools.append(PaddleUpdateTool())
    from .getall import PaddleGetallTool
    tools.append(PaddleGetallTool())
    from .reschedule import PaddleRescheduleTool
    tools.append(PaddleRescheduleTool())
    from .get import PaddleGetTool
    tools.append(PaddleGetTool())
    from .getall import PaddleGetallTool
    tools.append(PaddleGetallTool())
    from .getall import PaddleGetallTool
    tools.append(PaddleGetallTool())
    from .getall import PaddleGetallTool
    tools.append(PaddleGetallTool())
    return tools
