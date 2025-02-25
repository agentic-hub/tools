from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AsanatriggerDefaultToolInput(BaseModel):
    workspace: Optional[str] = Field(None, description="The workspace ID the resource is registered under. This is only required if you want to allow overriding existing webhooks. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="The resource ID to subscribe to. The resource can be a task or project.")
    authentication: Optional[str] = Field(None, description="Authentication")


class AsanatriggerDefaultTool(BaseTool):
    name = "asanatrigger_default"
    description = "Tool for asanaTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the asanaTrigger default operation."""
        # Implement the tool logic here
        return f"Running asanaTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the asanaTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
