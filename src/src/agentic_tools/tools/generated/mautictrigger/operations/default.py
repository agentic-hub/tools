from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MautictriggerDefaultToolInput(BaseModel):
    eventsOrder: Optional[str] = Field(None, description="Order direction for queued events in one webhook. Can be “DESC” or “ASC”.")
    authentication: Optional[str] = Field(None, description="Authentication")
    events: Optional[str] = Field(None, description="events")


class MautictriggerDefaultTool(BaseTool):
    name = "mautictrigger_default"
    description = "Tool for mauticTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the mauticTrigger default operation."""
        # Implement the tool logic here
        return f"Running mauticTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mauticTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
