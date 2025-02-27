from agentic_tools.tools import BaseTool, BaseModel, Field
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
    name: str = "itemlists_splitoutitems"
    description: str = "Tool for itemLists splitOutItems operation - splitOutItems operation"
    args_schema: type[BaseModel] | None = ItemlistsSplitoutitemsToolInput
