from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RedisSetToolInput(BaseModel):
    messageData: Optional[str] = Field(None, description="Data to publish")
    keyType: Optional[str] = Field(None, description="The type of the key to set")
    valueIsJSON: Optional[bool] = Field(None, description="Whether the value is JSON or key value pairs")
    value: Optional[str] = Field(None, description="The value to write in Redis")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    expire: Optional[bool] = Field(None, description="Whether to set a timeout on key")
    key: Optional[str] = Field(None, description="Name of the key to set in Redis")
    ttl: Optional[float] = Field(None, description="Number of seconds before key expiration")
    operation: Optional[str] = Field(None, description="Operation")
    propertyName: Optional[str] = Field(None, description="Name of the property to write received data to. Supports dot-notation. Example: \"data.person[0].name\".")


class RedisSetTool(BaseTool):
    name = "redis_set"
    description = "Tool for redis set operation - set operation"
    
    def _run(self, **kwargs):
        """Run the redis set operation."""
        # Implement the tool logic here
        return f"Running redis set operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the redis set operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
