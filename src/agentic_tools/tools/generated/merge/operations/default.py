from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MergeDefaultToolInput(BaseModel):
    output: Optional[str] = Field(None, description="Output")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    combination_mode: Optional[str] = Field(None, description="Combination Mode")
    merge_by_fields: Optional[Dict[str, Any]] = Field(None, description="Fields to Match")
    join_mode: Optional[str] = Field(None, description="Output Type")
    output_data_from: Optional[str] = Field(None, description="Output Data From")
    mode: Optional[str] = Field(None, description="How data of branches should be merged")
    choose_branch_mode: Optional[str] = Field(None, description="Output Type")


class MergeDefaultTool(BaseTool):
    name: str = "merge_default"
    connector_id: str = "nodes-base.merge"
    description: str = "Tool for merge default operation - default operation"
    args_schema: type[BaseModel] | None = MergeDefaultToolInput
