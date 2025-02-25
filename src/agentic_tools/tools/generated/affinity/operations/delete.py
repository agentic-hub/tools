from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AffinityCredentials(BaseModel):
    """Credentials for affinity authentication."""
    affinity_api: Optional[Dict[str, Any]] = Field(None, description="affinityApi")

class AffinityDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AffinityCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    list_entry_id: Optional[str] = Field(None, description="The unique ID of the list entry object to be deleted")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="The unique ID of the list that contains the specified list_entry_id. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    person_id: Optional[str] = Field(None, description="Unique identifier for the person")
    emails: Optional[str] = Field(None, description="The email addresses of the person")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organization_id: Optional[str] = Field(None, description="Unique identifier for the organization")


class AffinityDeleteTool(BaseTool):
    name = "affinity_delete"
    description = "Tool for affinity delete operation - delete operation"
    
    def __init__(self, credentials: Optional[AffinityCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the affinity delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running affinity delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running affinity delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the affinity delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
