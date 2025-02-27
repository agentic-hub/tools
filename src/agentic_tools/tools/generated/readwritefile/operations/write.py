from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ReadwritefileWriteToolInput(BaseModel):
    data_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    file_name: Optional[str] = Field(None, description="Path and name of the file that should be written. Also include the file extension.")
    operation: Optional[str] = Field(None, description="Operation")
    info: Optional[str] = Field(None, description="Use this node to read and write files on the same computer running n8n. To handle files between different computers please use other nodes (e.g. FTP, HTTP Request, AWS).")


class ReadwritefileWriteTool(BaseTool):
    name: str = "readwritefile_write"
    connector_id: str = "nodes-base.readWriteFile"
    description: str = "Tool for readWriteFile write operation - write operation"
    args_schema: type[BaseModel] | None = ReadwritefileWriteToolInput
