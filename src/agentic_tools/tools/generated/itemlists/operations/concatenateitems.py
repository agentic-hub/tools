from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ItemlistsConcatenateitemsToolInput(BaseModel):
    aggregate: Optional[str] = Field(None, description="Aggregate")
    fields_to_exclude: Optional[str] = Field(None, description="Fields To Exclude")
    fields_to_split_by: Optional[str] = Field(None, description="The name of the input fields that you want to split the summary by")
    operation: Optional[str] = Field(None, description="Operation")
    fields_to_aggregate: Optional[Dict[str, Any]] = Field(None, description="Fields To Aggregate")
    destination_field_name: Optional[str] = Field(None, description="The name of the output field to put the data in")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_include: Optional[str] = Field(None, description="Fields To Include")
    resource: Optional[str] = Field(None, description="Resource")
    include: Optional[str] = Field(None, description="Include")


class ItemlistsConcatenateitemsTool(BaseTool):
    name: str = "itemlists_concatenateitems"
    description: str = "Tool for itemLists concatenateItems operation - concatenateItems operation"
    args_schema: type[BaseModel] | None = ItemlistsConcatenateitemsToolInput
