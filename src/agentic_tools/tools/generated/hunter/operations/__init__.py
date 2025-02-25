# hunter operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all hunter operation tools."""
    tools = []
    from .domainsearch import HunterDomainsearchTool
    tools.append(HunterDomainsearchTool())
    from .emailfinder import HunterEmailfinderTool
    tools.append(HunterEmailfinderTool())
    from .emailverifier import HunterEmailverifierTool
    tools.append(HunterEmailverifierTool())
    return tools
