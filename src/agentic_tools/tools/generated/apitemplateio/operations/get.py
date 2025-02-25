from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ApitemplateioGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class ApitemplateioGetTool(BaseTool):
    name = "apitemplateio_get"
    description = "Tool for apiTemplateIo get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the apiTemplateIo get operation."""
        # Implement the tool logic here
        return f"Running apiTemplateIo get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the apiTemplateIo get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
