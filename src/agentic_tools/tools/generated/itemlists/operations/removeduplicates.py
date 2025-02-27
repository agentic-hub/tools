from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsRemoveduplicatesToolInput(BaseModel):
    fields_to_compare: Optional[str] = Field(None, description="Fields in the input to add to the comparison")
    fields_to_exclude: Optional[str] = Field(None, description="Fields in the input to exclude from the comparison")
    fields_to_split_by: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_include: Optional[str] = Field(None, description="Fields To Include")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Include")
    compare: Optional[str] = Field(None, description="The fields of the input items to compare to see if they are the same")


class ItemlistsRemoveduplicatesTool(BaseTool):
    name: str = "itemlists_removeduplicates"
    connector_id: str = "nodes-base.itemLists"
    description: str = "Tool for itemLists removeDuplicates operation - removeDuplicates operation"
    args_schema: type[BaseModel] | None = ItemlistsRemoveduplicatesToolInput
