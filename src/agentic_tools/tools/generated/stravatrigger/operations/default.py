from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StravatriggerDefaultToolInput(BaseModel):
    resolveData: Optional[bool] = Field(None, description="By default the webhook-data only contain the Object ID. If this option gets activated, it will resolve the data automatically.")
    event: Optional[str] = Field(None, description="Event")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    object: Optional[str] = Field(None, description="Object")


class StravatriggerDefaultTool(BaseTool):
    name = "stravatrigger_default"
    description = "Tool for stravaTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the stravaTrigger default operation."""
        # Implement the tool logic here
        return f"Running stravaTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stravaTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
