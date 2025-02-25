# awsrekognition toolkit
from langchain.tools import BaseTool
from typing import List

def get_awsrekognition_tools() -> List[BaseTool]:
    """Get all awsrekognition tools."""
    from . import operations
    return operations.get_tools()

class AwsRekognitionToolkit:
    """Toolkit for interacting with awsrekognition."""

    def __init__(self):
        """Initialize the awsrekognition toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awsrekognition tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awsrekognition tools with default credentials."""
        return get_awsrekognition_tools()
