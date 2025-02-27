from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LemlistCredentials

class LemlistCreateToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="ID of the campaign to create the lead under. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="Email of the lead to create")
    operation: Optional[str] = Field(None, description="Operation")


class LemlistCreateTool(BaseTool):
    name: str = "lemlist_create"
    connector_id: str = "nodes-base.lemlist"
    description: str = "Tool for lemlist create operation - create operation"
    args_schema: type[BaseModel] | None = LemlistCreateToolInput
    credentials: Optional[LemlistCredentials] = None
