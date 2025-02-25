from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SortDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    code: Optional[str] = Field(None, description="Javascript code to determine the order of any two items")
    sortFieldsUi: Optional[Dict[str, Any]] = Field(None, description="The fields of the input items to compare to see if they are the same")
    type: Optional[str] = Field(None, description="The fields of the input items to compare to see if they are the same")


class SortDefaultTool(BaseTool):
    name = "sort_default"
    description = "Tool for sort default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the sort default operation."""
        # Implement the tool logic here
        return f"Running sort default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sort default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
