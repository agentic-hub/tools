from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FormstacktriggerDefaultToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    authentication: Optional[str] = Field(None, description="Authentication")
    formId: Optional[str] = Field(None, description="The Formstack form to monitor for new submissions. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class FormstacktriggerDefaultTool(BaseTool):
    name = "formstacktrigger_default"
    description = "Tool for formstackTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the formstackTrigger default operation."""
        # Implement the tool logic here
        return f"Running formstackTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the formstackTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
