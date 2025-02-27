from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CodaCredentials

class CodaDeleteviewrowToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    doc_id: Optional[str] = Field(None, description="ID of the doc. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    table_id: Optional[str] = Field(None, description="The table to create the row in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    column_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    row_id: Optional[str] = Field(None, description="The view to get the row from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    view_id: Optional[str] = Field(None, description="The view to get the row from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class CodaDeleteviewrowTool(BaseTool):
    name: str = "coda_deleteviewrow"
    description: str = "Tool for coda deleteViewRow operation - deleteViewRow operation"
    args_schema: type[BaseModel] | None = CodaDeleteviewrowToolInput
    credentials: Optional[CodaCredentials] = None
