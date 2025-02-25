from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HumanticaiGetToolInput(BaseModel):
    userId: Optional[str] = Field(None, description="This value is the same as the User ID that was provided when the analysis was created. This could be a LinkedIn URL, email ID, or a unique string in case of resume based analysis.")
    resource: Optional[str] = Field(None, description="Resource")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sendResume: Optional[bool] = Field(None, description="Whether to send a resume for a resume based analysis")
    operation: Optional[str] = Field(None, description="Operation")


class HumanticaiGetTool(BaseTool):
    name = "humanticai_get"
    description = "Tool for humanticAi get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the humanticAi get operation."""
        # Implement the tool logic here
        return f"Running humanticAi get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the humanticAi get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
