from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RabbitmqDeletemessageToolInput(BaseModel):
    deleteMessage: Optional[str] = Field(None, description="Will delete an item from the queue triggered earlier in the workflow by a RabbitMQ Trigger node")
    exchange: Optional[str] = Field(None, description="Name of the exchange to publish to")
    message: Optional[str] = Field(None, description="The message to be sent")
    exchangeType: Optional[str] = Field(None, description="Type of exchange")
    routingKey: Optional[str] = Field(None, description="The routing key for the message")
    queue: Optional[str] = Field(None, description="Name of the queue to publish to")
    mode: Optional[str] = Field(None, description="To where data should be moved")
    operation: Optional[str] = Field(None, description="Operation")


class RabbitmqDeletemessageTool(BaseTool):
    name = "rabbitmq_deletemessage"
    description = "Tool for rabbitmq deleteMessage operation - deleteMessage operation"
    
    def _run(self, **kwargs):
        """Run the rabbitmq deleteMessage operation."""
        # Implement the tool logic here
        return f"Running rabbitmq deleteMessage operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rabbitmq deleteMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
