from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JiratriggerDefaultToolInput(BaseModel):
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    incomingAuthentication: Optional[str] = Field(None, description="If authentication should be activated for the webhook (makes it more secure)")
    events: Optional[str] = Field(None, description="events")
    jiraVersion: Optional[str] = Field(None, description="Jira Version")


class JiratriggerDefaultTool(BaseTool):
    name = "jiratrigger_default"
    description = "Tool for jiraTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the jiraTrigger default operation."""
        # Implement the tool logic here
        return f"Running jiraTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jiraTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
