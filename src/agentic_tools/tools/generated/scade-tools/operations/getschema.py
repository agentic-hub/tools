from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Scade-toolsCredentials

class Scade-toolsGetschemaToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    workflow_id: Optional[Dict[str, Any]] = Field(None, description="Workflow to filter the executions by")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    workflow_object: Optional[str] = Field(None, description="A valid JSON object with required fields: 'name', 'nodes', 'connections' and 'settings'. More information can be found in the <a href=\"https://docs.n8n.io/api/api-reference/#tag/Workflow/paths/~1workflows/post\">documentation</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    credential_type_name: Optional[str] = Field(None, description="The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'.")
    execution_id: Optional[str] = Field(None, description="Execution ID")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    operation: Optional[str] = Field(None, description="Operation")


class Scade-toolsGetschemaTool(BaseTool):
    name: str = "scade-tools_getschema"
    connector_id: str = "nodes-base.scade-tools"
    description: str = "Tool for scade-tools getSchema operation - getSchema operation"
    args_schema: type[BaseModel] | None = Scade-toolsGetschemaToolInput
    credentials: Optional[Scade-toolsCredentials] = None
