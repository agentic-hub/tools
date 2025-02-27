from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileOdsToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileOdsTool(BaseTool):
    name: str = "extractfromfile_ods"
    connector_id: str = "nodes-base.extractFromFile"
    description: str = "Tool for extractFromFile ods operation - ods operation"
    args_schema: type[BaseModel] | None = ExtractfromfileOdsToolInput
