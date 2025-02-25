from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FormiotriggerDefaultToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    projectId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    events: Optional[str] = Field(None, description="events")
    formId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class FormiotriggerDefaultTool(BaseTool):
    name = "formiotrigger_default"
    description = "Tool for formIoTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the formIoTrigger default operation."""
        # Implement the tool logic here
        return f"Running formIoTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the formIoTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
