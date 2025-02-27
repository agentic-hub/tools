from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhantombusterCredentials

class Phantombuster__custom_api_call__ToolInput(BaseModel):
    resolve_data: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agent_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class Phantombuster__custom_api_call__Tool(BaseTool):
    name: str = "phantombuster___custom_api_call__"
    description: str = "Tool for phantombuster __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Phantombuster__custom_api_call__ToolInput
    credentials: Optional[PhantombusterCredentials] = None
