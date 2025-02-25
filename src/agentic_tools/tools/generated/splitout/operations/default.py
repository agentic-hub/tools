from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SplitoutDefaultToolInput(BaseModel):
    include: Optional[str] = Field(None, description="Whether to copy any other fields into the new items")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fieldToSplitOut: Optional[str] = Field(None, description="The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary.")
    fieldsToInclude: Optional[str] = Field(None, description="Fields in the input items to aggregate together")


class SplitoutDefaultTool(BaseTool):
    name = "splitout_default"
    description = "Tool for splitOut default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the splitOut default operation."""
        # Implement the tool logic here
        return f"Running splitOut default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the splitOut default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
