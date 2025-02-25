# bannerbear operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all bannerbear operation tools."""
    tools = []
    from .create import BannerbearCreateTool
    tools.append(BannerbearCreateTool())
    from .get import BannerbearGetTool
    tools.append(BannerbearGetTool())
    from .get import BannerbearGetTool
    tools.append(BannerbearGetTool())
    from .getall import BannerbearGetallTool
    tools.append(BannerbearGetallTool())
    return tools
