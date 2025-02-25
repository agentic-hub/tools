from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HighlevelCredentials(BaseModel):
    """Credentials for highLevel authentication."""
    high_level_api: Optional[Dict[str, Any]] = Field(None, description="highLevelApi")

class HighlevelCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HighlevelCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email or Phone are required to create contact")
    phone: Optional[str] = Field(None, description="Phone or Email are required to create contact. Phone number has to start with a valid <a href=\"https://en.wikipedia.org/wiki/List_of_country_calling_codes\">country code</a> leading with + sign.")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="Task ID")
    opportunity_id: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    contact_identifier: Optional[str] = Field(None, description="Either Email, Phone or Contact ID")
    stage_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    due_date: Optional[str] = Field(None, description="Due Date")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    contact_id: Optional[str] = Field(None, description="Contact the task belongs to")
    pipeline_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    title: Optional[str] = Field(None, description="Title")
    contact_create_notice: Optional[str] = Field(None, description="Create a new contact or update an existing one if email or phone matches (upsert)")


class HighlevelCreateTool(BaseTool):
    name = "highlevel_create"
    description = "Tool for highLevel create operation - create operation"
    
    def __init__(self, credentials: Optional[HighlevelCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the highLevel create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running highLevel create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running highLevel create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the highLevel create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
