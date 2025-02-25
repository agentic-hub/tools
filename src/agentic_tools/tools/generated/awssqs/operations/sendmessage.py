from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwssqsCredentials(BaseModel):
    """Credentials for awsSqs authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwssqsSendmessageToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwssqsCredentials] = Field(None, description="Custom credentials for authentication")
    queue_type: Optional[str] = Field(None, description="Queue Type")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message to send to the queue")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the data the node receives as JSON to SQS")
    message_group_id: Optional[str] = Field(None, description="Tag that specifies that a message belongs to a specific message group. Applies only to FIFO (first-in-first-out) queues.")
    queue: Optional[str] = Field(None, description="Queue to send a message to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class AwssqsSendmessageTool(BaseTool):
    name = "awssqs_sendmessage"
    description = "Tool for awsSqs sendMessage operation - sendMessage operation"
    
    def __init__(self, credentials: Optional[AwssqsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsSqs sendMessage operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsSqs sendMessage operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsSqs sendMessage operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsSqs sendMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
