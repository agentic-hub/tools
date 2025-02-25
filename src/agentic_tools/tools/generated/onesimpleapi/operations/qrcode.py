from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnesimpleapiCredentials(BaseModel):
    """Credentials for oneSimpleApi authentication."""
    one_simple_api: Optional[Dict[str, Any]] = Field(None, description="oneSimpleApi")

class OnesimpleapiQrcodeToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[OnesimpleapiCredentials] = Field(None, description="Custom credentials for authentication")
    download: Optional[bool] = Field(None, description="Whether to download the QR code or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The text that should be turned into a QR code - like a website URL")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiQrcodeTool(BaseTool):
    name = "onesimpleapi_qrcode"
    description = "Tool for oneSimpleApi qrCode operation - qrCode operation"
    
    def __init__(self, credentials: Optional[OnesimpleapiCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the oneSimpleApi qrCode operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running oneSimpleApi qrCode operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running oneSimpleApi qrCode operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the oneSimpleApi qrCode operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
