from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RedisCredentials

class RedisSetToolInput(BaseModel):
    message_data: Optional[str] = Field(None, description="Data to publish")
    key_type: Optional[str] = Field(None, description="The type of the key to set")
    value_is_json: Optional[bool] = Field(None, description="Whether the value is JSON or key value pairs")
    value: Optional[str] = Field(None, description="The value to write in Redis")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    expire: Optional[bool] = Field(None, description="Whether to set a timeout on key")
    key: Optional[str] = Field(None, description="Name of the key to set in Redis")
    ttl: Optional[float] = Field(None, description="Number of seconds before key expiration")
    operation: Optional[str] = Field(None, description="Operation")
    property_name: Optional[str] = Field(None, description="Name of the property to write received data to. Supports dot-notation. Example: \"data.person[0].name\".")


class RedisSetTool(BaseTool):
    name: str = "redis_set"
    description: str = "Tool for redis set operation - set operation"
    args_schema: type[BaseModel] | None = RedisSetToolInput
    credentials: Optional[RedisCredentials] = None
