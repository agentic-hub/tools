# microsoftDynamicsCrm operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all microsoftDynamicsCrm operation tools."""
    tools = []
    from .create import MicrosoftdynamicscrmCreateTool
    tools.append(MicrosoftdynamicscrmCreateTool())
    from .delete import MicrosoftdynamicscrmDeleteTool
    tools.append(MicrosoftdynamicscrmDeleteTool())
    from .get import MicrosoftdynamicscrmGetTool
    tools.append(MicrosoftdynamicscrmGetTool())
    from .getall import MicrosoftdynamicscrmGetallTool
    tools.append(MicrosoftdynamicscrmGetallTool())
    from .update import MicrosoftdynamicscrmUpdateTool
    tools.append(MicrosoftdynamicscrmUpdateTool())
    return tools
