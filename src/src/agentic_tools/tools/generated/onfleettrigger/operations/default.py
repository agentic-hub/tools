from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnfleettriggerDefaultToolInput(BaseModel):
    triggerOn: Optional[str] = Field(None, description="Trigger On")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class OnfleettriggerDefaultTool(BaseTool):
    name = "onfleettrigger_default"
    description = "Tool for onfleetTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the onfleetTrigger default operation."""
        # Implement the tool logic here
        return f"Running onfleetTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the onfleetTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
