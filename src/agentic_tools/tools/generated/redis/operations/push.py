from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RedisCredentials

class RedisPushToolInput(BaseModel):
    list: Optional[str] = Field(None, description="Name of the list in Redis")
    message_data: Optional[str] = Field(None, description="Data to push")
    key_type: Optional[str] = Field(None, description="The type of the key to get")
    value_is_json: Optional[bool] = Field(None, description="Whether the value is JSON or key value pairs")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    expire: Optional[bool] = Field(None, description="Whether to set a timeout on key")
    tail: Optional[bool] = Field(None, description="Whether to push or pop data from the end of the list")
    key: Optional[str] = Field(None, description="Name of the key to delete from Redis")
    ttl: Optional[float] = Field(None, description="Number of seconds before key expiration")
    operation: Optional[str] = Field(None, description="Operation")
    property_name: Optional[str] = Field(None, description="Name of the property to write received data to. Supports dot-notation. Example: \"data.person[0].name\".")


class RedisPushTool(BaseTool):
    name: str = "redis_push"
    connector_id: str = "nodes-base.redis"
    description: str = "Tool for redis push operation - push operation"
    args_schema: type[BaseModel] | None = RedisPushToolInput
    credentials: Optional[RedisCredentials] = None
