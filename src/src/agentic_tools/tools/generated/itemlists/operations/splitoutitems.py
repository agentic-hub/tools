from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsSplitoutitemsToolInput(BaseModel):
    fieldToSplitOut: Optional[str] = Field(None, description="The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary.")
    fieldsToExclude: Optional[str] = Field(None, description="Fields To Exclude")
    fieldsToSplitBy: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fieldsToInclude: Optional[str] = Field(None, description="Fields in the input items to aggregate together")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Whether to copy any other fields into the new items")


class ItemlistsSplitoutitemsTool(BaseTool):
    name = "itemlists_splitoutitems"
    description = "Tool for itemLists splitOutItems operation - splitOutItems operation"
    
    def _run(self, **kwargs):
        """Run the itemLists splitOutItems operation."""
        # Implement the tool logic here
        return f"Running itemLists splitOutItems operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the itemLists splitOutItems operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
