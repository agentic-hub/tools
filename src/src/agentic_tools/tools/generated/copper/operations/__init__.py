# copper operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all copper operation tools."""
    tools = []
    from .create import CopperCreateTool
    tools.append(CopperCreateTool())
    from .delete import CopperDeleteTool
    tools.append(CopperDeleteTool())
    from .get import CopperGetTool
    tools.append(CopperGetTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    from .update import CopperUpdateTool
    tools.append(CopperUpdateTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    from .create import CopperCreateTool
    tools.append(CopperCreateTool())
    from .delete import CopperDeleteTool
    tools.append(CopperDeleteTool())
    from .get import CopperGetTool
    tools.append(CopperGetTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    from .update import CopperUpdateTool
    tools.append(CopperUpdateTool())
    from .create import CopperCreateTool
    tools.append(CopperCreateTool())
    from .delete import CopperDeleteTool
    tools.append(CopperDeleteTool())
    from .get import CopperGetTool
    tools.append(CopperGetTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    from .update import CopperUpdateTool
    tools.append(CopperUpdateTool())
    from .create import CopperCreateTool
    tools.append(CopperCreateTool())
    from .delete import CopperDeleteTool
    tools.append(CopperDeleteTool())
    from .get import CopperGetTool
    tools.append(CopperGetTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    from .update import CopperUpdateTool
    tools.append(CopperUpdateTool())
    from .create import CopperCreateTool
    tools.append(CopperCreateTool())
    from .delete import CopperDeleteTool
    tools.append(CopperDeleteTool())
    from .get import CopperGetTool
    tools.append(CopperGetTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    from .update import CopperUpdateTool
    tools.append(CopperUpdateTool())
    from .create import CopperCreateTool
    tools.append(CopperCreateTool())
    from .delete import CopperDeleteTool
    tools.append(CopperDeleteTool())
    from .get import CopperGetTool
    tools.append(CopperGetTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    from .update import CopperUpdateTool
    tools.append(CopperUpdateTool())
    from .getall import CopperGetallTool
    tools.append(CopperGetallTool())
    return tools
