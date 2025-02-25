from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglecalendarCredentials(BaseModel):
    """Credentials for googleCalendar authentication."""
    google_calendar_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleCalendarOAuth2Api")

class GooglecalendarGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglecalendarCredentials] = Field(None, description="Custom credentials for authentication")
    use_default_reminders: Optional[bool] = Field(None, description="Use Default Reminders")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    calendar: Optional[Dict[str, Any]] = Field(None, description="Google Calendar to operate on")
    reminders_ui: Optional[Dict[str, Any]] = Field(None, description="If the event doesn't use the default reminders, this lists the reminders specific to the event")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecalendarGetallTool(BaseTool):
    name = "googlecalendar_getall"
    description = "Tool for googleCalendar getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[GooglecalendarCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleCalendar getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleCalendar getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleCalendar getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleCalendar getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
