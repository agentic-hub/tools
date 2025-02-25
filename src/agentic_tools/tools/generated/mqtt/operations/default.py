from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MqttCredentials(BaseModel):
    """Credentials for mqtt authentication."""
    mqtt: Optional[Dict[str, Any]] = Field(None, description="mqtt")

class MqttDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MqttCredentials] = Field(None, description="Custom credentials for authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to publish")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON")
    topic: Optional[str] = Field(None, description="The topic to publish to")


class MqttDefaultTool(BaseTool):
    name = "mqtt_default"
    description = "Tool for mqtt default operation - default operation"
    
    def __init__(self, credentials: Optional[MqttCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mqtt default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mqtt default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mqtt default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mqtt default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
