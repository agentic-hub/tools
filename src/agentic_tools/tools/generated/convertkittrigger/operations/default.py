from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConvertkittriggerDefaultToolInput(BaseModel):
    courseId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    tagId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    event: Optional[str] = Field(None, description="The events that can trigger the webhook and whether they are enabled")
    productId: Optional[str] = Field(None, description="Product ID")
    link: Optional[str] = Field(None, description="The URL of the initiating link")
    formId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class ConvertkittriggerDefaultTool(BaseTool):
    name = "convertkittrigger_default"
    description = "Tool for convertKitTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the convertKitTrigger default operation."""
        # Implement the tool logic here
        return f"Running convertKitTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the convertKitTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
