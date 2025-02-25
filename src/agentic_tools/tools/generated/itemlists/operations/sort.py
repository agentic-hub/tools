from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsSortToolInput(BaseModel):
    fields_to_exclude: Optional[str] = Field(None, description="Fields To Exclude")
    type: Optional[str] = Field(None, description="The fields of the input items to compare to see if they are the same")
    fields_to_split_by: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_include: Optional[str] = Field(None, description="Fields To Include")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Include")
    sort_fields_ui: Optional[Dict[str, Any]] = Field(None, description="The fields of the input items to compare to see if they are the same")
    code: Optional[str] = Field(None, description="Javascript code to determine the order of any two items")


class ItemlistsSortTool(BaseTool):
    name = "itemlists_sort"
    description = "Tool for itemLists sort operation - sort operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the itemLists sort operation."""
        # Implement the tool logic here
        return f"Running itemLists sort operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the itemLists sort operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
