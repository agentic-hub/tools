from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailjetCredentials(BaseModel):
    """Credentials for mailjet authentication."""
    mailjet_email_api: Optional[Dict[str, Any]] = Field(None, description="mailjetEmailApi")
    mailjet_sms_api: Optional[Dict[str, Any]] = Field(None, description="mailjetSmsApi")

class MailjetSendtemplateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MailjetCredentials] = Field(None, description="Custom credentials for authentication")
    template_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    variables_json: Optional[str] = Field(None, description="HTML text message of email")
    to_email: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    variables_ui: Optional[Dict[str, Any]] = Field(None, description="Variables")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    text: Optional[str] = Field(None, description="Plain text message of email")
    from_email: Optional[str] = Field(None, description="The title for the email")
    operation: Optional[str] = Field(None, description="Operation")


class MailjetSendtemplateTool(BaseTool):
    name = "mailjet_sendtemplate"
    description = "Tool for mailjet sendTemplate operation - sendTemplate operation"
    
    def __init__(self, credentials: Optional[MailjetCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mailjet sendTemplate operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mailjet sendTemplate operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mailjet sendTemplate operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailjet sendTemplate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
