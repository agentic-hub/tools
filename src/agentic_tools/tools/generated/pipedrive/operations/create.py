from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PipedriveCredentials(BaseModel):
    """Credentials for pipedrive authentication."""
    pipedrive_api: Optional[Dict[str, Any]] = Field(None, description="pipedriveApi")
    pipedrive_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pipedriveOAuth2Api")

class PipedriveCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PipedriveCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="The content of the note to create")
    file_id: Optional[float] = Field(None, description="ID of the file to delete")
    type: Optional[str] = Field(None, description="Type of the activity like \"call\", \"meeting\", etc")
    org_id: Optional[float] = Field(None, description="ID of the organization this deal will be associated with")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    person_id: Optional[float] = Field(None, description="ID of the person this deal will be associated with")
    activity_id: Optional[float] = Field(None, description="ID of the activity to delete")
    subject: Optional[str] = Field(None, description="The subject of the activity to create")
    operation: Optional[str] = Field(None, description="Operation")
    product_attachment_id: Optional[str] = Field(None, description="ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    done: Optional[str] = Field(None, description="Whether the activity is done or not")
    name: Optional[str] = Field(None, description="The name of the organization to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    associate_with: Optional[str] = Field(None, description="Type of entity to link to this deal")
    person_id: Optional[float] = Field(None, description="ID of the person to delete")
    organization_id: Optional[float] = Field(None, description="ID of the organization to link to this lead")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    deal_id: Optional[float] = Field(None, description="ID of the deal to delete")
    term: Optional[str] = Field(None, description="The search term to look for. Minimum 2 characters (or 1 if using exact_match).")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    organization_id: Optional[float] = Field(None, description="ID of the organization to delete")
    authentication: Optional[str] = Field(None, description="Authentication")
    note_id: Optional[float] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="The title of the deal to create")
    lead_id: Optional[str] = Field(None, description="ID of the lead to delete")


class PipedriveCreateTool(BaseTool):
    name = "pipedrive_create"
    description = "Tool for pipedrive create operation - create operation"
    
    def __init__(self, credentials: Optional[PipedriveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the pipedrive create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running pipedrive create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running pipedrive create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pipedrive create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
