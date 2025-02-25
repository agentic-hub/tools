from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OrbitCredentials(BaseModel):
    """Credentials for orbit authentication."""
    orbit_api: Optional[Dict[str, Any]] = Field(None, description="orbitApi")

class OrbitCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[OrbitCredentials] = Field(None, description="Custom credentials for authentication")
    member_id: Optional[str] = Field(None, description="Member ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    workspace_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    note: Optional[str] = Field(None, description="Note")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    url: Optional[str] = Field(None, description="Supply any URL and Orbit will do its best job to parse out a title, description, and image")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resolve_identities: Optional[bool] = Field(None, description="By default, the response just includes the reference of the identity. When set to true the identities will be resolved automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title")


class OrbitCreateTool(BaseTool):
    name = "orbit_create"
    description = "Tool for orbit create operation - create operation"
    
    def __init__(self, credentials: Optional[OrbitCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the orbit create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running orbit create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running orbit create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the orbit create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
