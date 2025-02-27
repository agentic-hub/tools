from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileCsvToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileCsvTool(BaseTool):
    name: str = "converttofile_csv"
    connector_id: str = "nodes-base.convertToFile"
    description: str = "Tool for convertToFile csv operation - csv operation"
    args_schema: type[BaseModel] | None = ConverttofileCsvToolInput
