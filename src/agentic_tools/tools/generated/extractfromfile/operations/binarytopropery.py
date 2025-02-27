from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileBinarytoproperyToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    destination_key: Optional[str] = Field(None, description="The name of the output field that will contain the extracted data")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileBinarytoproperyTool(BaseTool):
    name: str = "extractfromfile_binarytopropery"
    connector_id: str = "nodes-base.extractFromFile"
    description: str = "Tool for extractFromFile binaryToPropery operation - binaryToPropery operation"
    args_schema: type[BaseModel] | None = ExtractfromfileBinarytoproperyToolInput
