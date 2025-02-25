from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TravisciCancelToolInput(BaseModel):
    buildId: Optional[str] = Field(None, description="Value uniquely identifying the build")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciCancelTool(BaseTool):
    name = "travisci_cancel"
    description = "Tool for travisCi cancel operation - cancel operation"
    
    def _run(self, **kwargs):
        """Run the travisCi cancel operation."""
        # Implement the tool logic here
        return f"Running travisCi cancel operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the travisCi cancel operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
