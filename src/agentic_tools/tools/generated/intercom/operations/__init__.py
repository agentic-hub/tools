# intercom operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all intercom operation tools."""
    tools = []
    from .create import IntercomCreateTool
    tools.append(IntercomCreateTool())
    from .delete import IntercomDeleteTool
    tools.append(IntercomDeleteTool())
    from .get import IntercomGetTool
    tools.append(IntercomGetTool())
    from .getall import IntercomGetallTool
    tools.append(IntercomGetallTool())
    from .update import IntercomUpdateTool
    tools.append(IntercomUpdateTool())
    from .create import IntercomCreateTool
    tools.append(IntercomCreateTool())
    from .delete import IntercomDeleteTool
    tools.append(IntercomDeleteTool())
    from .get import IntercomGetTool
    tools.append(IntercomGetTool())
    from .getall import IntercomGetallTool
    tools.append(IntercomGetallTool())
    from .update import IntercomUpdateTool
    tools.append(IntercomUpdateTool())
    from .create import IntercomCreateTool
    tools.append(IntercomCreateTool())
    from .get import IntercomGetTool
    tools.append(IntercomGetTool())
    from .getall import IntercomGetallTool
    tools.append(IntercomGetallTool())
    from .update import IntercomUpdateTool
    tools.append(IntercomUpdateTool())
    from .users import IntercomUsersTool
    tools.append(IntercomUsersTool())
    return tools
