from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BitbuckettriggerDefaultToolInput(BaseModel):
    workspace: Optional[str] = Field(None, description="The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    repository: Optional[str] = Field(None, description="The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    events: Optional[str] = Field(None, description="events")


class BitbuckettriggerDefaultTool(BaseTool):
    name = "bitbuckettrigger_default"
    description = "Tool for bitbucketTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the bitbucketTrigger default operation."""
        # Implement the tool logic here
        return f"Running bitbucketTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bitbucketTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
