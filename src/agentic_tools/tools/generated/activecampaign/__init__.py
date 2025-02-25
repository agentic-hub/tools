# activecampaign toolkit
from langchain.tools import BaseTool
from typing import List

def get_activecampaign_tools() -> List[BaseTool]:
    """Get all activecampaign tools."""
    from . import operations
    return operations.get_tools()

class ActivecampaignToolkit:
    """Toolkit for interacting with activecampaign."""

    def __init__(self):
        """Initialize the activecampaign toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all activecampaign tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all activecampaign tools with default credentials."""
        return get_activecampaign_tools()
