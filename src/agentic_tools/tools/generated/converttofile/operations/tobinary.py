from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileTobinaryToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    source_property: Optional[str] = Field(None, description="The name of the input field that contains the base64 string to convert to a file. Use dot-notation for deep fields (e.g. 'level1.level2.currentKey').")


class ConverttofileTobinaryTool(BaseTool):
    name: str = "converttofile_tobinary"
    description: str = "Tool for convertToFile toBinary operation - toBinary operation"
    args_schema: type[BaseModel] | None = ConverttofileTobinaryToolInput
