from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RabbitmqCredentials(BaseModel):
    """Credentials for rabbitmq authentication."""
    rabbitmq: Optional[Dict[str, Any]] = Field(None, description="rabbitmq")

class RabbitmqSendmessageToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RabbitmqCredentials] = Field(None, description="Custom credentials for authentication")
    exchange: Optional[str] = Field(None, description="Name of the exchange to publish to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON")
    message: Optional[str] = Field(None, description="The message to be sent")
    exchange_type: Optional[str] = Field(None, description="Type of exchange")
    routing_key: Optional[str] = Field(None, description="The routing key for the message")
    queue: Optional[str] = Field(None, description="Name of the queue to publish to")
    mode: Optional[str] = Field(None, description="To where data should be moved")
    operation: Optional[str] = Field(None, description="Operation")


class RabbitmqSendmessageTool(BaseTool):
    name = "rabbitmq_sendmessage"
    description = "Tool for rabbitmq sendMessage operation - sendMessage operation"
    
    def __init__(self, credentials: Optional[RabbitmqCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the rabbitmq sendMessage operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running rabbitmq sendMessage operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running rabbitmq sendMessage operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rabbitmq sendMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
