from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HelpscoutCredentials(BaseModel):
    """Credentials for helpScout authentication."""
    help_scout_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="helpScoutOAuth2Api")

class HelpscoutCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HelpscoutCredentials] = Field(None, description="Custom credentials for authentication")
    mailbox_id: Optional[str] = Field(None, description="ID of a mailbox where the conversation is being created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    customer_id: Optional[str] = Field(None, description="Customer ID")
    emails_ui: Optional[Dict[str, Any]] = Field(None, description="Emails")
    text: Optional[str] = Field(None, description="The chat text")
    type: Optional[str] = Field(None, description="Conversation type")
    resolve_data: Optional[bool] = Field(None, description="By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    social_profiles_ui: Optional[Dict[str, Any]] = Field(None, description="Social Profiles")
    websites_ui: Optional[Dict[str, Any]] = Field(None, description="Websites")
    subject: Optional[str] = Field(None, description="Conversation’s subject")
    address_ui: Optional[Dict[str, Any]] = Field(None, description="Address")
    operation: Optional[str] = Field(None, description="Operation")
    phones_ui: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversation_id: Optional[str] = Field(None, description="Conversation ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Conversation status")
    attachments_ui: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    threads_ui: Optional[Dict[str, Any]] = Field(None, description="Threads")
    chats_ui: Optional[Dict[str, Any]] = Field(None, description="Chat Handles")


class HelpscoutCreateTool(BaseTool):
    name = "helpscout_create"
    description = "Tool for helpScout create operation - create operation"
    
    def __init__(self, credentials: Optional[HelpscoutCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the helpScout create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running helpScout create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running helpScout create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the helpScout create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
