from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MqtttriggerDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    topics: Optional[str] = Field(None, description="Topics to subscribe to, multiple can be defined with comma. Wildcard characters are supported (+ - for single level and # - for multi level). By default all subscription used QoS=0. To set a different QoS, write the QoS desired after the topic preceded by a colom. For Example: topicA:1,topicB:2")


class MqtttriggerDefaultTool(BaseTool):
    name = "mqtttrigger_default"
    description = "Tool for mqttTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the mqttTrigger default operation."""
        # Implement the tool logic here
        return f"Running mqttTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mqttTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
