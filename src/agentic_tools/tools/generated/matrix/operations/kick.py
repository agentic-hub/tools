from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MatrixCredentials(BaseModel):
    """Credentials for matrix authentication."""
    matrix_api: Optional[Dict[str, Any]] = Field(None, description="matrixApi")

class MatrixKickToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MatrixCredentials] = Field(None, description="Custom credentials for authentication")
    room_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reason: Optional[str] = Field(None, description="Reason for kick")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixKickTool(BaseTool):
    name = "matrix_kick"
    description = "Tool for matrix kick operation - kick operation"
    
    def __init__(self, credentials: Optional[MatrixCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the matrix kick operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running matrix kick operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running matrix kick operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the matrix kick operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
