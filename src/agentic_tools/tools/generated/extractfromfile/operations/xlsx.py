from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileXlsxToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileXlsxTool(BaseTool):
    name: str = "extractfromfile_xlsx"
    description: str = "Tool for extractFromFile xlsx operation - xlsx operation"
    args_schema: type[BaseModel] | None = ExtractfromfileXlsxToolInput
