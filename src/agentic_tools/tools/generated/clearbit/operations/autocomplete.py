from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ClearbitCredentials(BaseModel):
    """Credentials for clearbit authentication."""
    clearbit_api: Optional[Dict[str, Any]] = Field(None, description="clearbitApi")

class ClearbitAutocompleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ClearbitCredentials] = Field(None, description="Custom credentials for authentication")
    name: Optional[str] = Field(None, description="Name is the partial name of the company")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class ClearbitAutocompleteTool(BaseTool):
    name = "clearbit_autocomplete"
    description = "Tool for clearbit autocomplete operation - autocomplete operation"
    
    def __init__(self, credentials: Optional[ClearbitCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the clearbit autocomplete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running clearbit autocomplete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running clearbit autocomplete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the clearbit autocomplete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
