# microsoftGraphSecurity operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all microsoftGraphSecurity operation tools."""
    tools = []
    from .get import MicrosoftgraphsecurityGetTool
    tools.append(MicrosoftgraphsecurityGetTool())
    from .getall import MicrosoftgraphsecurityGetallTool
    tools.append(MicrosoftgraphsecurityGetallTool())
    from .get import MicrosoftgraphsecurityGetTool
    tools.append(MicrosoftgraphsecurityGetTool())
    from .getall import MicrosoftgraphsecurityGetallTool
    tools.append(MicrosoftgraphsecurityGetallTool())
    from .update import MicrosoftgraphsecurityUpdateTool
    tools.append(MicrosoftgraphsecurityUpdateTool())
    return tools
