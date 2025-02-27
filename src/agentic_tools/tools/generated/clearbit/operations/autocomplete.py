from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ClearbitCredentials

class ClearbitAutocompleteToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name is the partial name of the company")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class ClearbitAutocompleteTool(BaseTool):
    name: str = "clearbit_autocomplete"
    connector_id: str = "nodes-base.clearbit"
    description: str = "Tool for clearbit autocomplete operation - autocomplete operation"
    args_schema: type[BaseModel] | None = ClearbitAutocompleteToolInput
    credentials: Optional[ClearbitCredentials] = None
