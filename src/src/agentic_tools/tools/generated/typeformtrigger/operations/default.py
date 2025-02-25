from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TypeformtriggerDefaultToolInput(BaseModel):
    simplifyAnswers: Optional[bool] = Field(None, description="Whether to convert the answers to a key:value pair (\"FIELD_TITLE\":\"USER_ANSER\") to be easily processable")
    authentication: Optional[str] = Field(None, description="Authentication")
    onlyAnswers: Optional[bool] = Field(None, description="Whether to return only the answers of the form and not any of the other data")
    formId: Optional[str] = Field(None, description="Form which should trigger workflow on submission. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class TypeformtriggerDefaultTool(BaseTool):
    name = "typeformtrigger_default"
    description = "Tool for typeformTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the typeformTrigger default operation."""
        # Implement the tool logic here
        return f"Running typeformTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the typeformTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
