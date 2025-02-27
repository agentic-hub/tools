from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CockpitCredentials

class CockpitGetToolInput(BaseModel):
    json_data_fields: Optional[bool] = Field(None, description="Whether new entry fields should be set via the value-key pair UI or JSON")
    form: Optional[str] = Field(None, description="Name of the form to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    singleton: Optional[str] = Field(None, description="Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    collection: Optional[str] = Field(None, description="Name of the collection to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    data_fields_ui: Optional[Dict[str, Any]] = Field(None, description="Entry data to send")
    data_fields_json: Optional[str] = Field(None, description="Entry data to send as JSON")
    operation: Optional[str] = Field(None, description="Operation")


class CockpitGetTool(BaseTool):
    name: str = "cockpit_get"
    description: str = "Tool for cockpit get operation - get operation"
    args_schema: type[BaseModel] | None = CockpitGetToolInput
    credentials: Optional[CockpitCredentials] = None
