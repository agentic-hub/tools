from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StopanderrorDefaultToolInput(BaseModel):
    errorMessage: Optional[str] = Field(None, description="Error Message")
    errorType: Optional[str] = Field(None, description="Type of error to throw")
    errorObject: Optional[str] = Field(None, description="Object containing error properties")


class StopanderrorDefaultTool(BaseTool):
    name = "stopanderror_default"
    description = "Tool for stopAndError default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the stopAndError default operation."""
        # Implement the tool logic here
        return f"Running stopAndError default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stopAndError default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
