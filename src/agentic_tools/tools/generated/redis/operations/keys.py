from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RedisCredentials

class RedisKeysToolInput(BaseModel):
    message_data: Optional[str] = Field(None, description="Data to publish")
    key_type: Optional[str] = Field(None, description="The type of the key to get")
    key_pattern: Optional[str] = Field(None, description="The key pattern for the keys to return")
    value_is_json: Optional[bool] = Field(None, description="Whether the value is JSON or key value pairs")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    expire: Optional[bool] = Field(None, description="Whether to set a timeout on key")
    get_values: Optional[bool] = Field(None, description="Whether to get the value of matching keys")
    key: Optional[str] = Field(None, description="Name of the key to delete from Redis")
    ttl: Optional[float] = Field(None, description="Number of seconds before key expiration")
    operation: Optional[str] = Field(None, description="Operation")
    property_name: Optional[str] = Field(None, description="Name of the property to write received data to. Supports dot-notation. Example: \"data.person[0].name\".")


class RedisKeysTool(BaseTool):
    name: str = "redis_keys"
    connector_id: str = "nodes-base.redis"
    description: str = "Tool for redis keys operation - keys operation"
    args_schema: type[BaseModel] | None = RedisKeysToolInput
    credentials: Optional[RedisCredentials] = None
