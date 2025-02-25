from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailgunCredentials(BaseModel):
    """Credentials for mailgun authentication."""
    mailgun_api: Optional[Dict[str, Any]] = Field(None, description="mailgunApi")

class MailgunDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MailgunCredentials] = Field(None, description="Custom credentials for authentication")
    html: Optional[str] = Field(None, description="HTML text message of email")
    to_email: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    bcc_email: Optional[str] = Field(None, description="Bcc Email address of the recipient. Multiple ones can be separated by comma.")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    text: Optional[str] = Field(None, description="Plain text message of email")
    from_email: Optional[str] = Field(None, description="Email address of the sender optional with name")
    cc_email: Optional[str] = Field(None, description="Cc Email address of the recipient. Multiple ones can be separated by comma.")
    attachments: Optional[str] = Field(None, description="Name of the binary properties which contain data which should be added to email as attachment. Multiple ones can be comma-separated.")


class MailgunDefaultTool(BaseTool):
    name = "mailgun_default"
    description = "Tool for mailgun default operation - default operation"
    
    def __init__(self, credentials: Optional[MailgunCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mailgun default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mailgun default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mailgun default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailgun default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
