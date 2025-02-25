from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwilioCredentials(BaseModel):
    """Credentials for twilio authentication."""
    twilio_api: Optional[Dict[str, Any]] = Field(None, description="twilioApi")

class TwilioMakeToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TwilioCredentials] = Field(None, description="Custom credentials for authentication")
    to: Optional[str] = Field(None, description="The number to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    twiml: Optional[bool] = Field(None, description="Whether to use the <a href=\"https://www.twilio.com/docs/voice/twiml\">Twilio Markup Language</a> in the message")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class TwilioMakeTool(BaseTool):
    name = "twilio_make"
    description = "Tool for twilio make operation - make operation"
    
    def __init__(self, credentials: Optional[TwilioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the twilio make operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running twilio make operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running twilio make operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twilio make operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
