# Generated tools package
from typing import List
from langchain.tools import BaseTool


def get_all_tools() -> List[BaseTool]:
    """Get all available tools from generated modules."""
    tools = []

    # Import and add tools from each generated toolkit
    from .bamboohr import get_bamboohr_tools

    tools.extend(get_bamboohr_tools())

    # Add imports for other toolkits as needed
    # For example:
    # from .gmail import get_gmail_tools
    # tools.extend(get_gmail_tools())

    return tools
