from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SortDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    code: Optional[str] = Field(None, description="Javascript code to determine the order of any two items")
    sort_fields_ui: Optional[Dict[str, Any]] = Field(None, description="The fields of the input items to compare to see if they are the same")
    type: Optional[str] = Field(None, description="The fields of the input items to compare to see if they are the same")


class SortDefaultTool(BaseTool):
    name: str = "sort_default"
    description: str = "Tool for sort default operation - default operation"
    args_schema: type[BaseModel] | None = SortDefaultToolInput
