from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CodaCredentials

class CodaUpdateviewrowToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    doc_id: Optional[str] = Field(None, description="ID of the doc. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    table_id: Optional[str] = Field(None, description="The table to create the row in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    key_name: Optional[str] = Field(None, description="The view to get the row from")
    column_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    row_id: Optional[str] = Field(None, description="The view to get the row from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    view_id: Optional[str] = Field(None, description="The view to get the row from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class CodaUpdateviewrowTool(BaseTool):
    name: str = "coda_updateviewrow"
    description: str = "Tool for coda updateViewRow operation - updateViewRow operation"
    args_schema: type[BaseModel] | None = CodaUpdateviewrowToolInput
    credentials: Optional[CodaCredentials] = None
