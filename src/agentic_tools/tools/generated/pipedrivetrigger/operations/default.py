from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PipedrivetriggerDefaultToolInput(BaseModel):
    action: Optional[str] = Field(None, description="Type of action to receive notifications about")
    authentication: Optional[str] = Field(None, description="Authentication")
    object: Optional[str] = Field(None, description="Type of object to receive notifications about")
    incomingAuthentication: Optional[str] = Field(None, description="If authentication should be activated for the webhook (makes it more secure)")


class PipedrivetriggerDefaultTool(BaseTool):
    name = "pipedrivetrigger_default"
    description = "Tool for pipedriveTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the pipedriveTrigger default operation."""
        # Implement the tool logic here
        return f"Running pipedriveTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pipedriveTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
