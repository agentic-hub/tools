from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogletasksCredentials

class Googletasks__custom_api_call__ToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class Googletasks__custom_api_call__Tool(BaseTool):
    name: str = "googletasks___custom_api_call__"
    description: str = "Tool for googleTasks __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googletasks__custom_api_call__ToolInput
    credentials: Optional[GoogletasksCredentials] = None
