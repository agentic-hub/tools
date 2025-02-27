from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileXlsToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileXlsTool(BaseTool):
    name: str = "extractfromfile_xls"
    description: str = "Tool for extractFromFile xls operation - xls operation"
    args_schema: type[BaseModel] | None = ExtractfromfileXlsToolInput
