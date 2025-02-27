# awsrekognition toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_awsrekognition_tools() -> List[BaseTool]:
    """Get all awsrekognition tools."""
    from . import operations
    return operations.get_tools()

class AwsrekognitionCredentials(BaseModel):
    """Credentials for awsrekognition authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwsRekognitionToolkit(AgenticHubToolkit):
    """Toolkit for interacting with awsrekognition."""

    def __init__(self, credentials: Optional[AwsrekognitionCredentials] = None):
        """Initialize the awsrekognition toolkit with optional credentials.

        Args:
            credentials: AwsrekognitionCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all awsrekognition tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        # Apply credentials to each tool if provided
        if self.credentials:
            for tool in tools:
                # Set credentials on each tool instance
                tool.credentials = self.credentials
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awsrekognition tools with default credentials."""
        return get_awsrekognition_tools()
