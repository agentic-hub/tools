from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwilioCredentials(BaseModel):
    """Credentials for twilio authentication."""
    twilio_api: Optional[Dict[str, Any]] = Field(None, description="twilioApi")

class TwilioSendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TwilioCredentials] = Field(None, description="Custom credentials for authentication")
    to: Optional[str] = Field(None, description="The number to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    to_whatsapp: Optional[bool] = Field(None, description="Whether the message should be sent to WhatsApp")
    operation: Optional[str] = Field(None, description="Operation")


class TwilioSendTool(BaseTool):
    name = "twilio_send"
    description = "Tool for twilio send operation - send operation"
    
    def __init__(self, credentials: Optional[TwilioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the twilio send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running twilio send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running twilio send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twilio send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
