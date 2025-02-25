# activeCampaignTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all activeCampaignTrigger operation tools."""
    tools = []
    from .default import ActivecampaigntriggerDefaultTool
    tools.append(ActivecampaigntriggerDefaultTool())
    return tools
