from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LimitDefaultToolInput(BaseModel):
    keep: Optional[str] = Field(None, description="When removing items, whether to keep the ones at the start or the ending")
    max_items: Optional[float] = Field(None, description="If there are more items than this number, some are removed")


class LimitDefaultTool(BaseTool):
    name = "limit_default"
    description = "Tool for limit default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the limit default operation."""
        # Implement the tool logic here
        return f"Running limit default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the limit default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
