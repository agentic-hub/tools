from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailjettriggerDefaultToolInput(BaseModel):
    event: Optional[str] = Field(None, description="Determines which resource events the webhook is triggered for")


class MailjettriggerDefaultTool(BaseTool):
    name = "mailjettrigger_default"
    description = "Tool for mailjetTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the mailjetTrigger default operation."""
        # Implement the tool logic here
        return f"Running mailjetTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailjetTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
