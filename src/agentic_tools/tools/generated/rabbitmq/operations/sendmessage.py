from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RabbitmqCredentials

class RabbitmqSendmessageToolInput(BaseModel):
    exchange: Optional[str] = Field(None, description="Name of the exchange to publish to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    send_input_data: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON")
    message: Optional[str] = Field(None, description="The message to be sent")
    exchange_type: Optional[str] = Field(None, description="Type of exchange")
    routing_key: Optional[str] = Field(None, description="The routing key for the message")
    queue: Optional[str] = Field(None, description="Name of the queue to publish to")
    mode: Optional[str] = Field(None, description="To where data should be moved")
    operation: Optional[str] = Field(None, description="Operation")


class RabbitmqSendmessageTool(BaseTool):
    name: str = "rabbitmq_sendmessage"
    connector_id: str = "nodes-base.rabbitmq"
    description: str = "Tool for rabbitmq sendMessage operation - sendMessage operation"
    args_schema: type[BaseModel] | None = RabbitmqSendmessageToolInput
    credentials: Optional[RabbitmqCredentials] = None
