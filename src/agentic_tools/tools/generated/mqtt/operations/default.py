from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MqttCredentials

class MqttDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to publish")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON")
    topic: Optional[str] = Field(None, description="The topic to publish to")


class MqttDefaultTool(BaseTool):
    name: str = "mqtt_default"
    description: str = "Tool for mqtt default operation - default operation"
    args_schema: type[BaseModel] | None = MqttDefaultToolInput
    credentials: Optional[MqttCredentials] = None
