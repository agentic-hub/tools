from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ReadwritefileReadToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    file_selector: Optional[str] = Field(None, description="Specify a file's path or path pattern to read multiple files")
    operation: Optional[str] = Field(None, description="Operation")
    info: Optional[str] = Field(None, description="Use this node to read and write files on the same computer running n8n. To handle files between different computers please use other nodes (e.g. FTP, HTTP Request, AWS).")


class ReadwritefileReadTool(BaseTool):
    name: str = "readwritefile_read"
    connector_id: str = "nodes-base.readWriteFile"
    description: str = "Tool for readWriteFile read operation - read operation"
    args_schema: type[BaseModel] | None = ReadwritefileReadToolInput
