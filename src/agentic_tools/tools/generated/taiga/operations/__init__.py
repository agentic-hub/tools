# taiga operations
from typing import List
from langchain.tools import BaseTool
from .. import TaigaCredentials

def get_tools() -> List[BaseTool]:
    """Get all taiga operation tools."""
    tools = []
    from .create import TaigaCreateTool
    tools.append(TaigaCreateTool())
    from .delete import TaigaDeleteTool
    tools.append(TaigaDeleteTool())
    from .get import TaigaGetTool
    tools.append(TaigaGetTool())
    from .getall import TaigaGetallTool
    tools.append(TaigaGetallTool())
    from .update import TaigaUpdateTool
    tools.append(TaigaUpdateTool())
    from .create import TaigaCreateTool
    tools.append(TaigaCreateTool())
    from .delete import TaigaDeleteTool
    tools.append(TaigaDeleteTool())
    from .get import TaigaGetTool
    tools.append(TaigaGetTool())
    from .getall import TaigaGetallTool
    tools.append(TaigaGetallTool())
    from .update import TaigaUpdateTool
    tools.append(TaigaUpdateTool())
    from .create import TaigaCreateTool
    tools.append(TaigaCreateTool())
    from .delete import TaigaDeleteTool
    tools.append(TaigaDeleteTool())
    from .get import TaigaGetTool
    tools.append(TaigaGetTool())
    from .getall import TaigaGetallTool
    tools.append(TaigaGetallTool())
    from .update import TaigaUpdateTool
    tools.append(TaigaUpdateTool())
    from .create import TaigaCreateTool
    tools.append(TaigaCreateTool())
    from .delete import TaigaDeleteTool
    tools.append(TaigaDeleteTool())
    from .get import TaigaGetTool
    tools.append(TaigaGetTool())
    from .getall import TaigaGetallTool
    tools.append(TaigaGetallTool())
    from .update import TaigaUpdateTool
    tools.append(TaigaUpdateTool())
    return tools
