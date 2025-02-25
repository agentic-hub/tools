from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoppertriggerDefaultToolInput(BaseModel):
    event: Optional[str] = Field(None, description="The event to listen to")
    resource: Optional[str] = Field(None, description="The resource which will fire the event")


class CoppertriggerDefaultTool(BaseTool):
    name = "coppertrigger_default"
    description = "Tool for copperTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the copperTrigger default operation."""
        # Implement the tool logic here
        return f"Running copperTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the copperTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
