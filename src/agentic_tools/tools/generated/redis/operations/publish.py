from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RedisCredentials(BaseModel):
    """Credentials for redis authentication."""
    redis: Optional[Dict[str, Any]] = Field(None, description="redis")

class RedisPublishToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RedisCredentials] = Field(None, description="Custom credentials for authentication")
    message_data: Optional[str] = Field(None, description="Data to publish")
    key_type: Optional[str] = Field(None, description="The type of the key to get")
    value_is_json: Optional[bool] = Field(None, description="Whether the value is JSON or key value pairs")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    expire: Optional[bool] = Field(None, description="Whether to set a timeout on key")
    channel: Optional[str] = Field(None, description="Channel name")
    key: Optional[str] = Field(None, description="Name of the key to delete from Redis")
    ttl: Optional[float] = Field(None, description="Number of seconds before key expiration")
    operation: Optional[str] = Field(None, description="Operation")
    property_name: Optional[str] = Field(None, description="Name of the property to write received data to. Supports dot-notation. Example: \"data.person[0].name\".")


class RedisPublishTool(BaseTool):
    name = "redis_publish"
    description = "Tool for redis publish operation - publish operation"
    
    def __init__(self, credentials: Optional[RedisCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the redis publish operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running redis publish operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running redis publish operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the redis publish operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
