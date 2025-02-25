from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TravisciGetToolInput(BaseModel):
    buildId: Optional[str] = Field(None, description="Value uniquely identifying the build")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciGetTool(BaseTool):
    name = "travisci_get"
    description = "Tool for travisCi get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the travisCi get operation."""
        # Implement the tool logic here
        return f"Running travisCi get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the travisCi get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
