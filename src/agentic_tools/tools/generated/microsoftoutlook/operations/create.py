from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftoutlookCredentials(BaseModel):
    """Credentials for microsoftOutlook authentication."""
    microsoft_outlook_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftOutlookOAuth2Api")

class MicrosoftoutlookCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftoutlookCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    output: Optional[str] = Field(None, description="Output")
    display_name: Optional[str] = Field(None, description="Name of the folder")
    surname: Optional[str] = Field(None, description="Last Name")
    attachment_id: Optional[Dict[str, Any]] = Field(None, description="Attachment")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Data Field Name")
    subject: Optional[str] = Field(None, description="The subject of the message")
    end_date_time: Optional[str] = Field(None, description="End")
    folder_id: Optional[Dict[str, Any]] = Field(None, description="Folder")
    draft_id: Optional[Dict[str, Any]] = Field(None, description="Draft")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the calendar to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters_ui: Optional[Dict[str, Any]] = Field(None, description="Filters")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    calendar_id: Optional[Dict[str, Any]] = Field(None, description="Calendar")
    start_date_time: Optional[str] = Field(None, description="Start")
    given_name: Optional[str] = Field(None, description="First Name")
    body_content: Optional[str] = Field(None, description="Message body content")
    fields: Optional[str] = Field(None, description="fields")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[Dict[str, Any]] = Field(None, description="Message")
    event_id: Optional[Dict[str, Any]] = Field(None, description="Event")
    filters_notice: Optional[str] = Field(None, description="Fetching a lot of messages may take a long time. Consider using filters to speed things up")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[Dict[str, Any]] = Field(None, description="Contact")


class MicrosoftoutlookCreateTool(BaseTool):
    name = "microsoftoutlook_create"
    description = "Tool for microsoftOutlook create operation - create operation"
    
    def __init__(self, credentials: Optional[MicrosoftoutlookCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftOutlook create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftOutlook create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftOutlook create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftOutlook create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
