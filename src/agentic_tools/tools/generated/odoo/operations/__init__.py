# odoo operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all odoo operation tools."""
    tools = []
    from .create import OdooCreateTool
    tools.append(OdooCreateTool())
    from .delete import OdooDeleteTool
    tools.append(OdooDeleteTool())
    from .get import OdooGetTool
    tools.append(OdooGetTool())
    from .getall import OdooGetallTool
    tools.append(OdooGetallTool())
    from .update import OdooUpdateTool
    tools.append(OdooUpdateTool())
    from .create import OdooCreateTool
    tools.append(OdooCreateTool())
    from .delete import OdooDeleteTool
    tools.append(OdooDeleteTool())
    from .get import OdooGetTool
    tools.append(OdooGetTool())
    from .getall import OdooGetallTool
    tools.append(OdooGetallTool())
    from .update import OdooUpdateTool
    tools.append(OdooUpdateTool())
    from .create import OdooCreateTool
    tools.append(OdooCreateTool())
    from .delete import OdooDeleteTool
    tools.append(OdooDeleteTool())
    from .get import OdooGetTool
    tools.append(OdooGetTool())
    from .getall import OdooGetallTool
    tools.append(OdooGetallTool())
    from .update import OdooUpdateTool
    tools.append(OdooUpdateTool())
    from .create import OdooCreateTool
    tools.append(OdooCreateTool())
    from .delete import OdooDeleteTool
    tools.append(OdooDeleteTool())
    from .get import OdooGetTool
    tools.append(OdooGetTool())
    from .getall import OdooGetallTool
    tools.append(OdooGetallTool())
    from .update import OdooUpdateTool
    tools.append(OdooUpdateTool())
    return tools
