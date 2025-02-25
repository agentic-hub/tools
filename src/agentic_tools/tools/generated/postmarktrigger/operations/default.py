from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostmarktriggerDefaultToolInput(BaseModel):
    events: Optional[str] = Field(None, description="events")
    firstOpen: Optional[bool] = Field(None, description="Only fires on first open for event \"Open\"")
    includeContent: Optional[bool] = Field(None, description="Whether to include message content for events \"Bounce\" and \"Spam Complaint\"")


class PostmarktriggerDefaultTool(BaseTool):
    name = "postmarktrigger_default"
    description = "Tool for postmarkTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the postmarkTrigger default operation."""
        # Implement the tool logic here
        return f"Running postmarkTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the postmarkTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
