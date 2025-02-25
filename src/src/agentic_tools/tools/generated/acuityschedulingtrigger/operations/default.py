from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AcuityschedulingtriggerDefaultToolInput(BaseModel):
    resolveData: Optional[bool] = Field(None, description="By default does the webhook-data only contain the ID of the object. If this option gets activated, it will resolve the data automatically.")
    event: Optional[str] = Field(None, description="Event")
    authentication: Optional[str] = Field(None, description="Authentication")


class AcuityschedulingtriggerDefaultTool(BaseTool):
    name = "acuityschedulingtrigger_default"
    description = "Tool for acuitySchedulingTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the acuitySchedulingTrigger default operation."""
        # Implement the tool logic here
        return f"Running acuitySchedulingTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the acuitySchedulingTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
