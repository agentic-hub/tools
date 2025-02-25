# odoo toolkit
from langchain.tools import BaseTool
from typing import List

def get_odoo_tools() -> List[BaseTool]:
    """Get all odoo tools."""
    from . import operations
    return operations.get_tools()

class OdooToolkit:
    """Toolkit for interacting with odoo."""

    def __init__(self):
        """Initialize the odoo toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all odoo tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all odoo tools with default credentials."""
        return get_odoo_tools()
