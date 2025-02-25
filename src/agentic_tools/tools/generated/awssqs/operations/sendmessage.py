from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwssqsSendmessageToolInput(BaseModel):
    queueType: Optional[str] = Field(None, description="Queue Type")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message to send to the queue")
    sendInputData: Optional[bool] = Field(None, description="Whether to send the data the node receives as JSON to SQS")
    messageGroupId: Optional[str] = Field(None, description="Tag that specifies that a message belongs to a specific message group. Applies only to FIFO (first-in-first-out) queues.")
    queue: Optional[str] = Field(None, description="Queue to send a message to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class AwssqsSendmessageTool(BaseTool):
    name = "awssqs_sendmessage"
    description = "Tool for awsSqs sendMessage operation - sendMessage operation"
    
    def _run(self, **kwargs):
        """Run the awsSqs sendMessage operation."""
        # Implement the tool logic here
        return f"Running awsSqs sendMessage operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsSqs sendMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
