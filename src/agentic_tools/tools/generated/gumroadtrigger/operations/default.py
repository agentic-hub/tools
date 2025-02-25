from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GumroadtriggerDefaultToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="The resource is gonna fire the event")


class GumroadtriggerDefaultTool(BaseTool):
    name = "gumroadtrigger_default"
    description = "Tool for gumroadTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the gumroadTrigger default operation."""
        # Implement the tool logic here
        return f"Running gumroadTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gumroadTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
