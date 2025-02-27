from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhantombusterCredentials

class PhantombusterGetallToolInput(BaseModel):
    resolve_data: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agent_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterGetallTool(BaseTool):
    name: str = "phantombuster_getall"
    connector_id: str = "nodes-base.phantombuster"
    description: str = "Tool for phantombuster getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = PhantombusterGetallToolInput
    credentials: Optional[PhantombusterCredentials] = None
