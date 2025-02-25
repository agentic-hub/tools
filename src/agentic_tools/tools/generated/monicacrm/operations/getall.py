from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MonicacrmCredentials(BaseModel):
    """Credentials for monicaCrm authentication."""
    monica_crm_api: Optional[Dict[str, Any]] = Field(None, description="monicaCrmApi")

class MonicacrmGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MonicacrmCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Description of the call - max 100,000 characters")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    tags_to_remove: Optional[str] = Field(None, description="tagsToRemove")
    contact_field_type_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reminder_id: Optional[str] = Field(None, description="ID of the reminder to delete")
    journal_id: Optional[str] = Field(None, description="ID of the journal entry to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contact_field_id: Optional[str] = Field(None, description="ID of the contactField to delete")
    tags_to_add: Optional[str] = Field(None, description="tagsToAdd")
    activity_id: Optional[str] = Field(None, description="ID of the activity to delete")
    happened_at: Optional[str] = Field(None, description="Date when the activity happened")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    call_id: Optional[str] = Field(None, description="ID of the call to delete")
    conversation_id: Optional[str] = Field(None, description="ID of the conversation to delete")
    tag_id: Optional[str] = Field(None, description="ID of the tag to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="ID of the contact whose fields to retrieve")
    note_id: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmGetallTool(BaseTool):
    name = "monicacrm_getall"
    description = "Tool for monicaCrm getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[MonicacrmCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the monicaCrm getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running monicaCrm getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running monicaCrm getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the monicaCrm getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
