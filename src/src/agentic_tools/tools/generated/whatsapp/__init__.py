# whatsApp toolkit
from langchain.tools import BaseTool
from typing import List

def get_whatsapp_tools() -> List[BaseTool]:
    """Get all whatsApp tools."""
    from . import operations
    return operations.get_tools()
