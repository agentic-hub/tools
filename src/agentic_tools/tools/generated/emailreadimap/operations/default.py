from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EmailreadimapCredentials(BaseModel):
    """Credentials for emailReadImap authentication."""
    imap: Optional[Dict[str, Any]] = Field(None, description="imap")

class EmailreadimapDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[EmailreadimapCredentials] = Field(None, description="Custom credentials for authentication")
    data_property_attachments_prefix_name: Optional[str] = Field(None, description="Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is \"attachment_\" the first attachment is saved to \"attachment_0\"")
    post_process_action: Optional[str] = Field(None, description="What to do after the email has been received. If \"nothing\" gets selected it will be processed multiple times.")
    mailbox: Optional[str] = Field(None, description="Mailbox Name")
    download_attachments: Optional[bool] = Field(None, description="Whether attachments of emails should be downloaded. Only set if needed as it increases processing.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    format: Optional[str] = Field(None, description="The format to return the message in")


class EmailreadimapDefaultTool(BaseTool):
    name = "emailreadimap_default"
    description = "Tool for emailReadImap default operation - default operation"
    
    def __init__(self, credentials: Optional[EmailreadimapCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the emailReadImap default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running emailReadImap default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running emailReadImap default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the emailReadImap default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
