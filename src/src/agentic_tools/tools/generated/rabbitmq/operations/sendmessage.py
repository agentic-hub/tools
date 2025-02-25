from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RabbitmqSendmessageToolInput(BaseModel):
    exchange: Optional[str] = Field(None, description="Name of the exchange to publish to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sendInputData: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON")
    message: Optional[str] = Field(None, description="The message to be sent")
    exchangeType: Optional[str] = Field(None, description="Type of exchange")
    routingKey: Optional[str] = Field(None, description="The routing key for the message")
    queue: Optional[str] = Field(None, description="Name of the queue to publish to")
    mode: Optional[str] = Field(None, description="To where data should be moved")
    operation: Optional[str] = Field(None, description="Operation")


class RabbitmqSendmessageTool(BaseTool):
    name = "rabbitmq_sendmessage"
    description = "Tool for rabbitmq sendMessage operation - sendMessage operation"
    
    def _run(self, **kwargs):
        """Run the rabbitmq sendMessage operation."""
        # Implement the tool logic here
        return f"Running rabbitmq sendMessage operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rabbitmq sendMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
