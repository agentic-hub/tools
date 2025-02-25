from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AmqptriggerDefaultToolInput(BaseModel):
    clientname: Optional[str] = Field(None, description="Leave empty for non-durable topic subscriptions or queues")
    subscription: Optional[str] = Field(None, description="Leave empty for non-durable topic subscriptions or queues")
    sink: Optional[str] = Field(None, description="Name of the queue of topic to listen to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")


class AmqptriggerDefaultTool(BaseTool):
    name = "amqptrigger_default"
    description = "Tool for amqpTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the amqpTrigger default operation."""
        # Implement the tool logic here
        return f"Running amqpTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the amqpTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
