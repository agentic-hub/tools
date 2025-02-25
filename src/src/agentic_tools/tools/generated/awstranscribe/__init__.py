# awsTranscribe toolkit
from langchain.tools import BaseTool
from typing import List

def get_awstranscribe_tools() -> List[BaseTool]:
    """Get all awsTranscribe tools."""
    from . import operations
    return operations.get_tools()
