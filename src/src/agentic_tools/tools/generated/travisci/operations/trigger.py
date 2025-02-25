from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TravisciTriggerToolInput(BaseModel):
    buildId: Optional[str] = Field(None, description="Value uniquely identifying the build")
    slug: Optional[str] = Field(None, description="Same as {ownerName}/{repositoryName}")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    branch: Optional[str] = Field(None, description="Branch requested to be built")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciTriggerTool(BaseTool):
    name = "travisci_trigger"
    description = "Tool for travisCi trigger operation - trigger operation"
    
    def _run(self, **kwargs):
        """Run the travisCi trigger operation."""
        # Implement the tool logic here
        return f"Running travisCi trigger operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the travisCi trigger operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
