from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileRtfToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileRtfTool(BaseTool):
    name: str = "extractfromfile_rtf"
    description: str = "Tool for extractFromFile rtf operation - rtf operation"
    args_schema: type[BaseModel] | None = ExtractfromfileRtfToolInput
