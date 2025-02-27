from agentic_tools.tools import BaseTool, BaseModel, Field
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
    name: str = "itemlists_sort"
    description: str = "Tool for itemLists sort operation - sort operation"
    args_schema: type[BaseModel] | None = ItemlistsSortToolInput
