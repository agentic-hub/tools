from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BannerbearCredentials(BaseModel):
    """Credentials for bannerbear authentication."""
    bannerbear_api: Optional[Dict[str, Any]] = Field(None, description="bannerbearApi")

class BannerbearGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BannerbearCredentials] = Field(None, description="Custom credentials for authentication")
    template_id: Optional[str] = Field(None, description="The template ID you want to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class BannerbearGetallTool(BaseTool):
    name = "bannerbear_getall"
    description = "Tool for bannerbear getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[BannerbearCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the bannerbear getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running bannerbear getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running bannerbear getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bannerbear getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
