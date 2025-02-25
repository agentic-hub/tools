from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GotowebinarCredentials(BaseModel):
    """Credentials for goToWebinar authentication."""
    go_to_webinar_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="goToWebinarOAuth2Api")

class GotowebinarCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GotowebinarCredentials] = Field(None, description="Custom credentials for authentication")
    organizer_key: Optional[str] = Field(None, description="The co-organizer's organizer key for the webinar")
    panelist_key: Optional[str] = Field(None, description="Key of the panelist to delete")
    details: Optional[str] = Field(None, description="The details to retrieve for the attendee")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last name of the registrant to create")
    email: Optional[str] = Field(None, description="The co-organizer's email address")
    webinar_key: Optional[str] = Field(None, description="Key of the webinar that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subject: Optional[str] = Field(None, description="Subject")
    session_key: Optional[str] = Field(None, description="Key of the session that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    coorganizer_key: Optional[str] = Field(None, description="Key of the co-organizer to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the panelist to create")
    registrant_key: Optional[str] = Field(None, description="Registrant key of the attendee at the webinar session")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    given_name: Optional[str] = Field(None, description="The co-organizer's given name")
    is_external: Optional[bool] = Field(None, description="Whether the co-organizer has no GoToWebinar account")
    first_name: Optional[str] = Field(None, description="First name of the registrant to create")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    times: Optional[Dict[str, Any]] = Field(None, description="Time Range")


class GotowebinarCreateTool(BaseTool):
    name = "gotowebinar_create"
    description = "Tool for goToWebinar create operation - create operation"
    
    def __init__(self, credentials: Optional[GotowebinarCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the goToWebinar create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running goToWebinar create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running goToWebinar create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the goToWebinar create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
