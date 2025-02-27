from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MetabaseCredentials

class Metabase__custom_api_call__ToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class Metabase__custom_api_call__Tool(BaseTool):
    name: str = "metabase___custom_api_call__"
    connector_id: str = "nodes-base.metabase"
    description: str = "Tool for metabase __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Metabase__custom_api_call__ToolInput
    credentials: Optional[MetabaseCredentials] = None
