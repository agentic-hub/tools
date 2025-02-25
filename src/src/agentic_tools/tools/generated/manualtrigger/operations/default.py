from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ManualtriggerDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="This node is where a manual workflow execution starts. To make one, go back to the canvas and click test workflow’")


class ManualtriggerDefaultTool(BaseTool):
    name = "manualtrigger_default"
    description = "Tool for manualTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the manualTrigger default operation."""
        # Implement the tool logic here
        return f"Running manualTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the manualTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
