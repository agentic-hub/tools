# activeCampaign toolkit
from langchain.tools import BaseTool
from typing import List

def get_activecampaign_tools() -> List[BaseTool]:
    """Get all activeCampaign tools."""
    from . import operations
    return operations.get_tools()
