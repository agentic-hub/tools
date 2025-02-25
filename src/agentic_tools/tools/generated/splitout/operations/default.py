from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SplitoutDefaultToolInput(BaseModel):
    include: Optional[str] = Field(None, description="Whether to copy any other fields into the new items")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    field_to_split_out: Optional[str] = Field(None, description="The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary.")
    fields_to_include: Optional[str] = Field(None, description="Fields in the input items to aggregate together")


class SplitoutDefaultTool(BaseTool):
    name = "splitout_default"
    description = "Tool for splitOut default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the splitOut default operation."""
        # Implement the tool logic here
        return f"Running splitOut default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the splitOut default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
