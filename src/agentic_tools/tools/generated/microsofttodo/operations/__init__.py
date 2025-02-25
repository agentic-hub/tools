# microsoftToDo operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all microsoftToDo operation tools."""
    tools = []
    from .create import MicrosofttodoCreateTool
    tools.append(MicrosofttodoCreateTool())
    from .delete import MicrosofttodoDeleteTool
    tools.append(MicrosofttodoDeleteTool())
    from .get import MicrosofttodoGetTool
    tools.append(MicrosofttodoGetTool())
    from .getall import MicrosofttodoGetallTool
    tools.append(MicrosofttodoGetallTool())
    from .update import MicrosofttodoUpdateTool
    tools.append(MicrosofttodoUpdateTool())
    from .create import MicrosofttodoCreateTool
    tools.append(MicrosofttodoCreateTool())
    from .delete import MicrosofttodoDeleteTool
    tools.append(MicrosofttodoDeleteTool())
    from .get import MicrosofttodoGetTool
    tools.append(MicrosofttodoGetTool())
    from .getall import MicrosofttodoGetallTool
    tools.append(MicrosofttodoGetallTool())
    from .update import MicrosofttodoUpdateTool
    tools.append(MicrosofttodoUpdateTool())
    from .create import MicrosofttodoCreateTool
    tools.append(MicrosofttodoCreateTool())
    from .delete import MicrosofttodoDeleteTool
    tools.append(MicrosofttodoDeleteTool())
    from .get import MicrosofttodoGetTool
    tools.append(MicrosofttodoGetTool())
    from .getall import MicrosofttodoGetallTool
    tools.append(MicrosofttodoGetallTool())
    from .update import MicrosofttodoUpdateTool
    tools.append(MicrosofttodoUpdateTool())
    return tools
