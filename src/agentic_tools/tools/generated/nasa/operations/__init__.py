# nasa operations
from typing import List
from langchain.tools import BaseTool
from .. import NasaCredentials

def get_tools() -> List[BaseTool]:
    """Get all nasa operation tools."""
    tools = []
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .getall import NasaGetallTool
    tools.append(NasaGetallTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    from .get import NasaGetTool
    tools.append(NasaGetTool())
    return tools
