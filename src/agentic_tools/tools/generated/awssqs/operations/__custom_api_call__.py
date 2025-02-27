from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssqsCredentials

class Awssqs__custom_api_call__ToolInput(BaseModel):
    queue_type: Optional[str] = Field(None, description="Queue Type")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the data the node receives as JSON to SQS")
    message_group_id: Optional[str] = Field(None, description="Tag that specifies that a message belongs to a specific message group. Applies only to FIFO (first-in-first-out) queues.")
    operation: Optional[str] = Field(None, description="Operation")


class Awssqs__custom_api_call__Tool(BaseTool):
    name: str = "awssqs___custom_api_call__"
    description: str = "Tool for awsSqs __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awssqs__custom_api_call__ToolInput
    credentials: Optional[AwssqsCredentials] = None
