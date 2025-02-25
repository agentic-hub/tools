# airtable toolkit
from langchain.tools import BaseTool
from typing import List

def get_airtable_tools() -> List[BaseTool]:
    """Get all airtable tools."""
    from . import operations
    return operations.get_tools()
