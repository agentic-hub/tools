from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WorkabletriggerDefaultToolInput(BaseModel):
    triggerOn: Optional[str] = Field(None, description="Trigger On")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")


class WorkabletriggerDefaultTool(BaseTool):
    name = "workabletrigger_default"
    description = "Tool for workableTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the workableTrigger default operation."""
        # Implement the tool logic here
        return f"Running workableTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the workableTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
