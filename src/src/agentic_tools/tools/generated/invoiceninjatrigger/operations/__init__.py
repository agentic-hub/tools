# invoiceNinjaTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all invoiceNinjaTrigger operation tools."""
    tools = []
    from .default import InvoiceninjatriggerDefaultTool
    tools.append(InvoiceninjatriggerDefaultTool())
    return tools
