from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RemoveduplicatesDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_compare: Optional[str] = Field(None, description="Fields in the input to add to the comparison")
    compare: Optional[str] = Field(None, description="The fields of the input items to compare to see if they are the same")
    fields_to_exclude: Optional[str] = Field(None, description="Fields in the input to exclude from the comparison")


class RemoveduplicatesDefaultTool(BaseTool):
    name: str = "removeduplicates_default"
    connector_id: str = "nodes-base.removeDuplicates"
    description: str = "Tool for removeDuplicates default operation - default operation"
    args_schema: type[BaseModel] | None = RemoveduplicatesDefaultToolInput
