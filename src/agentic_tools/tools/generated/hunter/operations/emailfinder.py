from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HunterCredentials(BaseModel):
    """Credentials for hunter authentication."""
    hunter_api: Optional[Dict[str, Any]] = Field(None, description="hunterApi")

class HunterEmailfinderToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HunterCredentials] = Field(None, description="Custom credentials for authentication")
    lastname: Optional[str] = Field(None, description="The person's last name. It doesn't need to be in lowercase.")
    firstname: Optional[str] = Field(None, description="The person's first name. It doesn't need to be in lowercase.")
    operation: Optional[str] = Field(None, description="Operation to consume")
    domain: Optional[str] = Field(None, description="Domain name from which you want to find the email addresses. For example, \"stripe.com\".")


class HunterEmailfinderTool(BaseTool):
    name = "hunter_emailfinder"
    description = "Tool for hunter emailFinder operation - emailFinder operation"
    
    def __init__(self, credentials: Optional[HunterCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the hunter emailFinder operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running hunter emailFinder operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running hunter emailFinder operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the hunter emailFinder operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
