# salesmate operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all salesmate operation tools."""
    tools = []
    from .create import SalesmateCreateTool
    tools.append(SalesmateCreateTool())
    from .delete import SalesmateDeleteTool
    tools.append(SalesmateDeleteTool())
    from .get import SalesmateGetTool
    tools.append(SalesmateGetTool())
    from .getall import SalesmateGetallTool
    tools.append(SalesmateGetallTool())
    from .update import SalesmateUpdateTool
    tools.append(SalesmateUpdateTool())
    from .create import SalesmateCreateTool
    tools.append(SalesmateCreateTool())
    from .delete import SalesmateDeleteTool
    tools.append(SalesmateDeleteTool())
    from .get import SalesmateGetTool
    tools.append(SalesmateGetTool())
    from .getall import SalesmateGetallTool
    tools.append(SalesmateGetallTool())
    from .update import SalesmateUpdateTool
    tools.append(SalesmateUpdateTool())
    from .create import SalesmateCreateTool
    tools.append(SalesmateCreateTool())
    from .delete import SalesmateDeleteTool
    tools.append(SalesmateDeleteTool())
    from .get import SalesmateGetTool
    tools.append(SalesmateGetTool())
    from .getall import SalesmateGetallTool
    tools.append(SalesmateGetallTool())
    from .update import SalesmateUpdateTool
    tools.append(SalesmateUpdateTool())
    return tools
