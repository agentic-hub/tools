from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileXlsxToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileXlsxTool(BaseTool):
    name: str = "converttofile_xlsx"
    description: str = "Tool for convertToFile xlsx operation - xlsx operation"
    args_schema: type[BaseModel] | None = ConverttofileXlsxToolInput
