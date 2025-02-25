from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ClickupCredentials(BaseModel):
    """Credentials for clickUp authentication."""
    click_up_api: Optional[Dict[str, Any]] = Field(None, description="clickUpApi")
    click_up_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="clickUpOAuth2Api")

class ClickupSetcustomfieldToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ClickupCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    space: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    checklist: Optional[str] = Field(None, description="Checklist ID")
    time_entry_ids: Optional[str] = Field(None, description="Time Entry IDs")
    json_parse: Optional[bool] = Field(None, description="The value is JSON and will be parsed as such. Is needed if for example needed for labels which expects the value to be an array.")
    list: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The value to set on custom field")
    task: Optional[str] = Field(None, description="The ID of the task to add custom field to")
    key_result: Optional[str] = Field(None, description="Key Result ID")
    checklist_item: Optional[str] = Field(None, description="Checklist Item ID")
    time_entry: Optional[str] = Field(None, description="Time Entry ID")
    id: Optional[str] = Field(None, description="ID")
    operation: Optional[str] = Field(None, description="Operation")
    goal: Optional[str] = Field(None, description="Goal ID")
    task_id: Optional[str] = Field(None, description="Task ID")
    name: Optional[str] = Field(None, description="Name")
    depends_on_task: Optional[str] = Field(None, description="Depends On Task ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_names: Optional[str] = Field(None, description="tagNames")
    folderless: Optional[bool] = Field(None, description="Folderless List")
    comment: Optional[str] = Field(None, description="Comment ID")
    folder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    team: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    field: Optional[str] = Field(None, description="The ID of the field to add custom field to")


class ClickupSetcustomfieldTool(BaseTool):
    name = "clickup_setcustomfield"
    description = "Tool for clickUp setCustomField operation - setCustomField operation"
    
    def __init__(self, credentials: Optional[ClickupCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the clickUp setCustomField operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running clickUp setCustomField operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running clickUp setCustomField operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the clickUp setCustomField operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
