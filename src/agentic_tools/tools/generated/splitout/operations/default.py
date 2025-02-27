from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SplitoutDefaultToolInput(BaseModel):
    include: Optional[str] = Field(None, description="Whether to copy any other fields into the new items")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    field_to_split_out: Optional[str] = Field(None, description="The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary.")
    fields_to_include: Optional[str] = Field(None, description="Fields in the input items to aggregate together")


class SplitoutDefaultTool(BaseTool):
    name: str = "splitout_default"
    connector_id: str = "nodes-base.splitOut"
    description: str = "Tool for splitOut default operation - default operation"
    args_schema: type[BaseModel] | None = SplitoutDefaultToolInput
