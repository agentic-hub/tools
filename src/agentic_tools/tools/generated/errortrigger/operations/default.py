from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ErrortriggerDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="This node will trigger when there is an error in another workflow, as long as that workflow is set up to do so. <a href=\"https://docs.n8n.io/integrations/core-nodes/n8n-nodes-base.errortrigger\" target=\"_blank\">More info<a>")


class ErrortriggerDefaultTool(BaseTool):
    name = "errortrigger_default"
    description = "Tool for errorTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the errorTrigger default operation."""
        # Implement the tool logic here
        return f"Running errorTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the errorTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
