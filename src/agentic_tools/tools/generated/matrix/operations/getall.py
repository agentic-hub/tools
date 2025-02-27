from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MatrixCredentials

class MatrixGetallToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="The token to start returning events from. This token can be obtained from a prev_batch token returned for each room by the sync API. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    user_id: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    other_options: Optional[Dict[str, Any]] = Field(None, description="Other Options")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filtering options")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixGetallTool(BaseTool):
    name: str = "matrix_getall"
    connector_id: str = "nodes-base.matrix"
    description: str = "Tool for matrix getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MatrixGetallToolInput
    credentials: Optional[MatrixCredentials] = None
