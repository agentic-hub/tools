from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ShopifytriggerDefaultToolInput(BaseModel):
    topic: Optional[str] = Field(None, description="Trigger On")
    authentication: Optional[str] = Field(None, description="Authentication")


class ShopifytriggerDefaultTool(BaseTool):
    name = "shopifytrigger_default"
    description = "Tool for shopifyTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the shopifyTrigger default operation."""
        # Implement the tool logic here
        return f"Running shopifyTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the shopifyTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
