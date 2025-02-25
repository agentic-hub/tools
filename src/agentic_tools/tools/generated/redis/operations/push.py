from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RedisPushToolInput(BaseModel):
    list: Optional[str] = Field(None, description="Name of the list in Redis")
    messageData: Optional[str] = Field(None, description="Data to push")
    keyType: Optional[str] = Field(None, description="The type of the key to get")
    valueIsJSON: Optional[bool] = Field(None, description="Whether the value is JSON or key value pairs")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    expire: Optional[bool] = Field(None, description="Whether to set a timeout on key")
    tail: Optional[bool] = Field(None, description="Whether to push or pop data from the end of the list")
    key: Optional[str] = Field(None, description="Name of the key to delete from Redis")
    ttl: Optional[float] = Field(None, description="Number of seconds before key expiration")
    operation: Optional[str] = Field(None, description="Operation")
    propertyName: Optional[str] = Field(None, description="Name of the property to write received data to. Supports dot-notation. Example: \"data.person[0].name\".")


class RedisPushTool(BaseTool):
    name = "redis_push"
    description = "Tool for redis push operation - push operation"
    
    def _run(self, **kwargs):
        """Run the redis push operation."""
        # Implement the tool logic here
        return f"Running redis push operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the redis push operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
