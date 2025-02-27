from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RabbitmqCredentials

class RabbitmqDeletemessageToolInput(BaseModel):
    delete_message: Optional[str] = Field(None, description="Will delete an item from the queue triggered earlier in the workflow by a RabbitMQ Trigger node")
    exchange: Optional[str] = Field(None, description="Name of the exchange to publish to")
    message: Optional[str] = Field(None, description="The message to be sent")
    exchange_type: Optional[str] = Field(None, description="Type of exchange")
    routing_key: Optional[str] = Field(None, description="The routing key for the message")
    queue: Optional[str] = Field(None, description="Name of the queue to publish to")
    mode: Optional[str] = Field(None, description="To where data should be moved")
    operation: Optional[str] = Field(None, description="Operation")


class RabbitmqDeletemessageTool(BaseTool):
    name: str = "rabbitmq_deletemessage"
    connector_id: str = "nodes-base.rabbitmq"
    description: str = "Tool for rabbitmq deleteMessage operation - deleteMessage operation"
    args_schema: type[BaseModel] | None = RabbitmqDeletemessageToolInput
    credentials: Optional[RabbitmqCredentials] = None
