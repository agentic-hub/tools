from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LemlistCredentials

class LemlistGetToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="ID of the campaign to create the lead under. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    email: Optional[str] = Field(None, description="Email of the lead to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class LemlistGetTool(BaseTool):
    name: str = "lemlist_get"
    connector_id: str = "nodes-base.lemlist"
    description: str = "Tool for lemlist get operation - get operation"
    args_schema: type[BaseModel] | None = LemlistGetToolInput
    credentials: Optional[LemlistCredentials] = None
