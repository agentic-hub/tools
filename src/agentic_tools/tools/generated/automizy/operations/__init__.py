# automizy operations
from typing import List
from langchain.tools import BaseTool
from .. import AutomizyCredentials

def get_tools() -> List[BaseTool]:
    """Get all automizy operation tools."""
    tools = []
    from .create import AutomizyCreateTool
    tools.append(AutomizyCreateTool())
    from .delete import AutomizyDeleteTool
    tools.append(AutomizyDeleteTool())
    from .get import AutomizyGetTool
    tools.append(AutomizyGetTool())
    from .getall import AutomizyGetallTool
    tools.append(AutomizyGetallTool())
    from .update import AutomizyUpdateTool
    tools.append(AutomizyUpdateTool())
    from .create import AutomizyCreateTool
    tools.append(AutomizyCreateTool())
    from .delete import AutomizyDeleteTool
    tools.append(AutomizyDeleteTool())
    from .get import AutomizyGetTool
    tools.append(AutomizyGetTool())
    from .getall import AutomizyGetallTool
    tools.append(AutomizyGetallTool())
    from .update import AutomizyUpdateTool
    tools.append(AutomizyUpdateTool())
    return tools
