from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LemlistCredentials

class LemlistGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="ID of the campaign to create the lead under. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    email: Optional[str] = Field(None, description="Email of the lead to create")
    operation: Optional[str] = Field(None, description="Operation")


class LemlistGetallTool(BaseTool):
    name: str = "lemlist_getall"
    connector_id: str = "nodes-base.lemlist"
    description: str = "Tool for lemlist getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = LemlistGetallToolInput
    credentials: Optional[LemlistCredentials] = None
