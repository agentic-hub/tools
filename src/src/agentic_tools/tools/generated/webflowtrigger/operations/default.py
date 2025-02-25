from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WebflowtriggerDefaultToolInput(BaseModel):
    event: Optional[str] = Field(None, description="Event")
    authentication: Optional[str] = Field(None, description="Authentication")
    site: Optional[str] = Field(None, description="Site that will trigger the events. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class WebflowtriggerDefaultTool(BaseTool):
    name = "webflowtrigger_default"
    description = "Tool for webflowTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the webflowTrigger default operation."""
        # Implement the tool logic here
        return f"Running webflowTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the webflowTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
