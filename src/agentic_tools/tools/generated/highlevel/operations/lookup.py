from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HighlevelCredentials(BaseModel):
    """Credentials for highLevel authentication."""
    high_level_api: Optional[Dict[str, Any]] = Field(None, description="highLevelApi")

class HighlevelLookupToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HighlevelCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Lookup Contact by Email. If Email is not found it will try to find a contact by phone.")
    phone: Optional[str] = Field(None, description="Lookup Contact by Phone. It will first try to find a contact by Email and than by Phone.")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="Task ID")
    opportunity_id: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    title: Optional[str] = Field(None, description="Title")


class HighlevelLookupTool(BaseTool):
    name = "highlevel_lookup"
    description = "Tool for highLevel lookup operation - lookup operation"
    
    def __init__(self, credentials: Optional[HighlevelCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the highLevel lookup operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running highLevel lookup operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running highLevel lookup operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the highLevel lookup operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
