from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FlowtriggerDefaultToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource that triggers the webhook")
    listIds: Optional[str] = Field(None, description="Lists IDs, perhaps known better as \"Projects\" separated by a comma (,)")
    taskIds: Optional[str] = Field(None, description="Task IDs separated by a comma (,)")


class FlowtriggerDefaultTool(BaseTool):
    name = "flowtrigger_default"
    description = "Tool for flowTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the flowTrigger default operation."""
        # Implement the tool logic here
        return f"Running flowTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the flowTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
