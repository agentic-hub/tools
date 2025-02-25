from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AmqpCredentials(BaseModel):
    """Credentials for amqp authentication."""
    amqp: Optional[Dict[str, Any]] = Field(None, description="amqp")

class AmqpDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AmqpCredentials] = Field(None, description="Custom credentials for authentication")
    sink: Optional[str] = Field(None, description="Name of the queue of topic to publish to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    header_parameters_json: Optional[str] = Field(None, description="Header parameters as JSON (flat object). Sent as application_properties in amqp-message meta info.")


class AmqpDefaultTool(BaseTool):
    name = "amqp_default"
    description = "Tool for amqp default operation - default operation"
    
    def __init__(self, credentials: Optional[AmqpCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the amqp default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running amqp default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running amqp default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the amqp default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
