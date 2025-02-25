from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsConcatenateitemsToolInput(BaseModel):
    aggregate: Optional[str] = Field(None, description="Aggregate")
    fieldsToExclude: Optional[str] = Field(None, description="Fields To Exclude")
    fieldsToSplitBy: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    fieldsToAggregate: Optional[Dict[str, Any]] = Field(None, description="Fields To Aggregate")
    destinationFieldName: Optional[str] = Field(None, description="The name of the output field to put the data in")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fieldsToInclude: Optional[str] = Field(None, description="Fields To Include")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Include")


class ItemlistsConcatenateitemsTool(BaseTool):
    name = "itemlists_concatenateitems"
    description = "Tool for itemLists concatenateItems operation - concatenateItems operation"
    
    def _run(self, **kwargs):
        """Run the itemLists concatenateItems operation."""
        # Implement the tool logic here
        return f"Running itemLists concatenateItems operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the itemLists concatenateItems operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
