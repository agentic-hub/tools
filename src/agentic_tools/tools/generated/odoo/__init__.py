# odoo toolkit
from langchain.tools import BaseTool
from typing import List

def get_odoo_tools() -> List[BaseTool]:
    """Get all odoo tools."""
    from . import operations
    return operations.get_tools()
