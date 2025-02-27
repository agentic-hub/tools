from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SetDefaultToolInput(BaseModel):
    json_output: Optional[str] = Field(None, description="JSON Output")
    duplicate_warning: Optional[str] = Field(None, description="Item duplication is set in the node settings. This option will be ignored when the workflow runs automatically.")
    exclude_fields: Optional[str] = Field(None, description="Comma-separated list of the field names you want to exclude from the output. You can drag the selected fields from the input panel.")
    include: Optional[str] = Field(None, description="How to select the fields you want to include in your output items")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    mode: Optional[str] = Field(None, description="Mode")
    include_fields: Optional[str] = Field(None, description="Comma-separated list of the field names you want to include in the output. You can drag the selected fields from the input panel.")
    duplicate_item: Optional[bool] = Field(None, description="Duplicate Item")
    fields: Optional[Dict[str, Any]] = Field(None, description="Edit existing fields or add new ones to modify the output data")
    duplicate_count: Optional[float] = Field(None, description="How many times the item should be duplicated, mainly used for testing and debugging")


class SetDefaultTool(BaseTool):
    name: str = "set_default"
    description: str = "Tool for set default operation - default operation"
    args_schema: type[BaseModel] | None = SetDefaultToolInput
