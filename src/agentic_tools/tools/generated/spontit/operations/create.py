from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SpontitCredentials(BaseModel):
    """Credentials for spontit authentication."""
    spontit_api: Optional[Dict[str, Any]] = Field(None, description="spontitApi")

class SpontitCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SpontitCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="To provide text in a push, supply one of either \"content\" or \"pushContent\" (or both). Limited to 2500 characters. (Required if a value for \"pushContent\" is not provided).")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class SpontitCreateTool(BaseTool):
    name = "spontit_create"
    description = "Tool for spontit create operation - create operation"
    
    def __init__(self, credentials: Optional[SpontitCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the spontit create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running spontit create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running spontit create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the spontit create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
