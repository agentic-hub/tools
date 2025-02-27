from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileXlsToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileXlsTool(BaseTool):
    name: str = "converttofile_xls"
    connector_id: str = "nodes-base.convertToFile"
    description: str = "Tool for convertToFile xls operation - xls operation"
    args_schema: type[BaseModel] | None = ConverttofileXlsToolInput
