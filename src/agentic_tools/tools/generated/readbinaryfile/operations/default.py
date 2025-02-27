from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ReadbinaryfileDefaultToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="Path of the file to read")
    data_property_name: Optional[str] = Field(None, description="Name of the binary property to which to write the data of the read file")


class ReadbinaryfileDefaultTool(BaseTool):
    name: str = "readbinaryfile_default"
    description: str = "Tool for readBinaryFile default operation - default operation"
    args_schema: type[BaseModel] | None = ReadbinaryfileDefaultToolInput
