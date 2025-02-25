from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RabbitmqtriggerDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    queue: Optional[str] = Field(None, description="The name of the queue to read from")
    laterMessageNode: Optional[str] = Field(None, description="To delete an item from the queue, insert a RabbitMQ node later in the workflow and use the 'Delete from queue' operation")


class RabbitmqtriggerDefaultTool(BaseTool):
    name = "rabbitmqtrigger_default"
    description = "Tool for rabbitmqTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the rabbitmqTrigger default operation."""
        # Implement the tool logic here
        return f"Running rabbitmqTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rabbitmqTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
