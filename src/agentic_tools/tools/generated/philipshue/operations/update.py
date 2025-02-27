from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhilipshueCredentials

class PhilipshueUpdateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    on: Optional[bool] = Field(None, description="On/Off state of the light")
    light_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class PhilipshueUpdateTool(BaseTool):
    name: str = "philipshue_update"
    connector_id: str = "nodes-base.philipsHue"
    description: str = "Tool for philipsHue update operation - update operation"
    args_schema: type[BaseModel] | None = PhilipshueUpdateToolInput
    credentials: Optional[PhilipshueCredentials] = None
