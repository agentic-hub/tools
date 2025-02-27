from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssqsCredentials

class AwssqsSendmessageToolInput(BaseModel):
    queue_type: Optional[str] = Field(None, description="Queue Type")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message to send to the queue")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the data the node receives as JSON to SQS")
    message_group_id: Optional[str] = Field(None, description="Tag that specifies that a message belongs to a specific message group. Applies only to FIFO (first-in-first-out) queues.")
    queue: Optional[str] = Field(None, description="Queue to send a message to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class AwssqsSendmessageTool(BaseTool):
    name: str = "awssqs_sendmessage"
    description: str = "Tool for awsSqs sendMessage operation - sendMessage operation"
    args_schema: type[BaseModel] | None = AwssqsSendmessageToolInput
    credentials: Optional[AwssqsCredentials] = None
