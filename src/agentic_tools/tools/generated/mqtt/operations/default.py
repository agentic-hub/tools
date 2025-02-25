from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MqttDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to publish")
    sendInputData: Optional[bool] = Field(None, description="Whether to send the the data the node receives as JSON")
    topic: Optional[str] = Field(None, description="The topic to publish to")


class MqttDefaultTool(BaseTool):
    name = "mqtt_default"
    description = "Tool for mqtt default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the mqtt default operation."""
        # Implement the tool logic here
        return f"Running mqtt default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mqtt default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
