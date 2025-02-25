from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SsetriggerDefaultToolInput(BaseModel):
    url: Optional[str] = Field(None, description="The URL to receive the SSE from")


class SsetriggerDefaultTool(BaseTool):
    name = "ssetrigger_default"
    description = "Tool for sseTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the sseTrigger default operation."""
        # Implement the tool logic here
        return f"Running sseTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sseTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
