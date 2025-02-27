from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DeeplCredentials

class Deepl__custom_api_call__ToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Deepl__custom_api_call__Tool(BaseTool):
    name: str = "deepl___custom_api_call__"
    connector_id: str = "nodes-base.deepL"
    description: str = "Tool for deepL __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Deepl__custom_api_call__ToolInput
    credentials: Optional[DeeplCredentials] = None
