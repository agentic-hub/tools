from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileOdsToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileOdsTool(BaseTool):
    name: str = "converttofile_ods"
    description: str = "Tool for convertToFile ods operation - ods operation"
    args_schema: type[BaseModel] | None = ConverttofileOdsToolInput
