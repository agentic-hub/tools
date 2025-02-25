from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JotformtriggerDefaultToolInput(BaseModel):
    resolveData: Optional[bool] = Field(None, description="By default does the webhook-data use internal keys instead of the names. If this option gets activated, it will resolve the keys automatically to the actual names.")
    form: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    onlyAnswers: Optional[bool] = Field(None, description="Whether to return only the answers of the form and not any of the other data")


class JotformtriggerDefaultTool(BaseTool):
    name = "jotformtrigger_default"
    description = "Tool for jotFormTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the jotFormTrigger default operation."""
        # Implement the tool logic here
        return f"Running jotFormTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jotFormTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
