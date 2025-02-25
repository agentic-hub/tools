from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KafkaCredentials(BaseModel):
    """Credentials for kafka authentication."""
    kafka: Optional[Dict[str, Any]] = Field(None, description="kafka")

class KafkaDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[KafkaCredentials] = Field(None, description="Custom credentials for authentication")
    use_key: Optional[bool] = Field(None, description="Whether to use a message key")
    event_name: Optional[str] = Field(None, description="Namespace and Name of Schema in Schema Registry (namespace.name)")
    header_parameters_json: Optional[str] = Field(None, description="Header parameters as JSON (flat object)")
    message: Optional[str] = Field(None, description="The message to be sent")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON to Kafka")
    schema_registry_url: Optional[str] = Field(None, description="URL of the schema registry")
    headers_ui: Optional[Dict[str, Any]] = Field(None, description="Headers")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    use_schema_registry: Optional[bool] = Field(None, description="Whether to use Confluent Schema Registry")
    topic: Optional[str] = Field(None, description="Name of the queue of topic to publish to")
    key: Optional[str] = Field(None, description="The message key")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class KafkaDefaultTool(BaseTool):
    name = "kafka_default"
    description = "Tool for kafka default operation - default operation"
    
    def __init__(self, credentials: Optional[KafkaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the kafka default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running kafka default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running kafka default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the kafka default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
