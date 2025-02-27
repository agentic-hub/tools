from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WritebinaryfileDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    file_name: Optional[str] = Field(None, description="Path to which the file should be written")
    data_property_name: Optional[str] = Field(None, description="Name of the binary property which contains the data for the file to be written")


class WritebinaryfileDefaultTool(BaseTool):
    name: str = "writebinaryfile_default"
    connector_id: str = "nodes-base.writeBinaryFile"
    description: str = "Tool for writeBinaryFile default operation - default operation"
    args_schema: type[BaseModel] | None = WritebinaryfileDefaultToolInput
