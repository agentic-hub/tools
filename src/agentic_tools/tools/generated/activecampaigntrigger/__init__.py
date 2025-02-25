# activeCampaignTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_activecampaigntrigger_tools() -> List[BaseTool]:
    """Get all activeCampaignTrigger tools."""
    from . import operations
    return operations.get_tools()
