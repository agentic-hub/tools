from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MandrillCredentials(BaseModel):
    """Credentials for mandrill authentication."""
    mandrill_api: Optional[Dict[str, Any]] = Field(None, description="mandrillApi")

class MandrillSendhtmlToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MandrillCredentials] = Field(None, description="Custom credentials for authentication")
    headers_json: Optional[str] = Field(None, description="Optional extra headers to add to the message (most headers are allowed)")
    metadata_ui: Optional[Dict[str, Any]] = Field(None, description="Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.")
    resource: Optional[str] = Field(None, description="Resource")
    merge_vars_ui: Optional[Dict[str, Any]] = Field(None, description="Per-recipient merge variables")
    merge_vars_json: Optional[str] = Field(None, description="Global merge variables")
    to_email: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    attachments_ui: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    headers_ui: Optional[Dict[str, Any]] = Field(None, description="Optional extra headers to add to the message (most headers are allowed)")
    metadata_json: Optional[str] = Field(None, description="Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.")
    from_email: Optional[str] = Field(None, description="Email address of the sender optional with name")
    operation: Optional[str] = Field(None, description="Operation")
    attachments_json: Optional[str] = Field(None, description="An array of supported attachments to add to the message")


class MandrillSendhtmlTool(BaseTool):
    name = "mandrill_sendhtml"
    description = "Tool for mandrill sendHtml operation - sendHtml operation"
    
    def __init__(self, credentials: Optional[MandrillCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mandrill sendHtml operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mandrill sendHtml operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mandrill sendHtml operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mandrill sendHtml operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
