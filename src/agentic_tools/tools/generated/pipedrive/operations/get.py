from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PipedriveCredentials(BaseModel):
    """Credentials for pipedrive authentication."""
    pipedrive_api: Optional[Dict[str, Any]] = Field(None, description="pipedriveApi")
    pipedrive_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pipedriveOAuth2Api")

class PipedriveGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PipedriveCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resolve_properties: Optional[bool] = Field(None, description="By default do custom properties get returned only as ID instead of their actual name. Also option fields contain only the ID instead of their actual value. If this option gets set they get automatically resolved.")
    file_id: Optional[float] = Field(None, description="ID of the file to get")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    person_id: Optional[float] = Field(None, description="ID of the person this deal will be associated with")
    activity_id: Optional[float] = Field(None, description="ID of the activity to get")
    operation: Optional[str] = Field(None, description="Operation")
    product_attachment_id: Optional[str] = Field(None, description="ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    name: Optional[str] = Field(None, description="The name of the organization to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    associate_with: Optional[str] = Field(None, description="Type of entity to link to this deal")
    person_id: Optional[float] = Field(None, description="ID of the person to get")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    deal_id: Optional[float] = Field(None, description="ID of the deal to get")
    term: Optional[str] = Field(None, description="The search term to look for. Minimum 2 characters (or 1 if using exact_match).")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organization_id: Optional[float] = Field(None, description="ID of the organization to get")
    authentication: Optional[str] = Field(None, description="Authentication")
    note_id: Optional[float] = Field(None, description="ID of the note to get")
    title: Optional[str] = Field(None, description="The title of the deal to create")
    lead_id: Optional[str] = Field(None, description="ID of the lead to retrieve")


class PipedriveGetTool(BaseTool):
    name = "pipedrive_get"
    description = "Tool for pipedrive get operation - get operation"
    
    def __init__(self, credentials: Optional[PipedriveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the pipedrive get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running pipedrive get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running pipedrive get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pipedrive get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
