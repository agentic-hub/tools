from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IntervalDefaultToolInput(BaseModel):
    interval: Optional[float] = Field(None, description="Interval value")
    unit: Optional[str] = Field(None, description="Unit of the interval value")
    notice: Optional[str] = Field(None, description="This workflow will run on the schedule you define here once you <a data-key=\"activate\">activate</a> it.<br><br>For testing, you can also trigger it manually: by going back to the canvas and clicking 'test workflow'")


class IntervalDefaultTool(BaseTool):
    name = "interval_default"
    description = "Tool for interval default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the interval default operation."""
        # Implement the tool logic here
        return f"Running interval default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the interval default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
