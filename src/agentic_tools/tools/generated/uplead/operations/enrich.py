from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class UpleadCredentials(BaseModel):
    """Credentials for uplead authentication."""
    uplead_api: Optional[Dict[str, Any]] = Field(None, description="upleadApi")

class UpleadEnrichToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[UpleadCredentials] = Field(None, description="Custom credentials for authentication")
    company: Optional[str] = Field(None, description="The name of the company (e.g – amazon)")
    lastname: Optional[str] = Field(None, description="Last name of the person (e.g – Benioff)")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email address (e.g – mbenioff@salesforce.com)")
    firstname: Optional[str] = Field(None, description="First name of the person (e.g – Marc)")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name (e.g – amazon.com)")


class UpleadEnrichTool(BaseTool):
    name = "uplead_enrich"
    description = "Tool for uplead enrich operation - enrich operation"
    
    def __init__(self, credentials: Optional[UpleadCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the uplead enrich operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running uplead enrich operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running uplead enrich operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the uplead enrich operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
