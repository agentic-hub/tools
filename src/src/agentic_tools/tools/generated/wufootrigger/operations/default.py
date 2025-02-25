from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WufootriggerDefaultToolInput(BaseModel):
    form: Optional[str] = Field(None, description="The form upon which will trigger this node when a new entry is made. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    onlyAnswers: Optional[bool] = Field(None, description="Whether to return only the answers of the form and not any of the other data")


class WufootriggerDefaultTool(BaseTool):
    name = "wufootrigger_default"
    description = "Tool for wufooTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the wufooTrigger default operation."""
        # Implement the tool logic here
        return f"Running wufooTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the wufooTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
