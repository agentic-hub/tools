from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KeaptriggerDefaultToolInput(BaseModel):
    rawData: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    eventId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class KeaptriggerDefaultTool(BaseTool):
    name = "keaptrigger_default"
    description = "Tool for keapTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the keapTrigger default operation."""
        # Implement the tool logic here
        return f"Running keapTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the keapTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
