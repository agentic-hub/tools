from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileFromicsToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    destination_key: Optional[str] = Field(None, description="The name of the output field that will contain the extracted data")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileFromicsTool(BaseTool):
    name: str = "extractfromfile_fromics"
    description: str = "Tool for extractFromFile fromIcs operation - fromIcs operation"
    args_schema: type[BaseModel] | None = ExtractfromfileFromicsToolInput
