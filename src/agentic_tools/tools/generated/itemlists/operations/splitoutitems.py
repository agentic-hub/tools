from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsSplitoutitemsToolInput(BaseModel):
    field_to_split_out: Optional[str] = Field(None, description="The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary.")
    fields_to_exclude: Optional[str] = Field(None, description="Fields To Exclude")
    fields_to_split_by: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_include: Optional[str] = Field(None, description="Fields in the input items to aggregate together")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Whether to copy any other fields into the new items")


class ItemlistsSplitoutitemsTool(BaseTool):
    name = "itemlists_splitoutitems"
    description = "Tool for itemLists splitOutItems operation - splitOutItems operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the itemLists splitOutItems operation."""
        # Implement the tool logic here
        return f"Running itemLists splitOutItems operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the itemLists splitOutItems operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
