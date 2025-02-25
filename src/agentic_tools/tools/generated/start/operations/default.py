from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StartDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="This node is where a manual workflow execution starts. To make one, go back to the canvas and click ‘execute workflow’")


class StartDefaultTool(BaseTool):
    name = "start_default"
    description = "Tool for start default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the start default operation."""
        # Implement the tool logic here
        return f"Running start default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the start default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
