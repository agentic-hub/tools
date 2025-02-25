from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsLimitToolInput(BaseModel):
    fieldsToExclude: Optional[str] = Field(None, description="Fields To Exclude")
    fieldsToSplitBy: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fieldsToInclude: Optional[str] = Field(None, description="Fields To Include")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Include")
    keep: Optional[str] = Field(None, description="When removing items, whether to keep the ones at the start or the ending")
    maxItems: Optional[float] = Field(None, description="If there are more items than this number, some are removed")


class ItemlistsLimitTool(BaseTool):
    name = "itemlists_limit"
    description = "Tool for itemLists limit operation - limit operation"
    
    def _run(self, **kwargs):
        """Run the itemLists limit operation."""
        # Implement the tool logic here
        return f"Running itemLists limit operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the itemLists limit operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
