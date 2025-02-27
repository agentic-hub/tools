from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsLimitToolInput(BaseModel):
    fields_to_exclude: Optional[str] = Field(None, description="Fields To Exclude")
    fields_to_split_by: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_include: Optional[str] = Field(None, description="Fields To Include")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Include")
    keep: Optional[str] = Field(None, description="When removing items, whether to keep the ones at the start or the ending")
    max_items: Optional[float] = Field(None, description="If there are more items than this number, some are removed")


class ItemlistsLimitTool(BaseTool):
    name: str = "itemlists_limit"
    description: str = "Tool for itemLists limit operation - limit operation"
    args_schema: type[BaseModel] | None = ItemlistsLimitToolInput
