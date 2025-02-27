from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VeroCredentials

class VeroAliasToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    new_id: Optional[str] = Field(None, description="The new unique identifier of the user")
    tags: Optional[str] = Field(None, description="Tags to add separated by \",\"")
    data_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    data_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The old unique identifier of the user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class VeroAliasTool(BaseTool):
    name: str = "vero_alias"
    description: str = "Tool for vero alias operation - alias operation"
    args_schema: type[BaseModel] | None = VeroAliasToolInput
    credentials: Optional[VeroCredentials] = None
