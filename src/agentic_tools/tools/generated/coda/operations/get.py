from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CodaCredentials

class CodaGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    doc_id: Optional[str] = Field(None, description="ID of the doc. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    table_id: Optional[str] = Field(None, description="The table to create the row in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    formula_id: Optional[str] = Field(None, description="The formula to get the row from")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    column_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    control_id: Optional[str] = Field(None, description="The control to get the row from")
    row_id: Optional[str] = Field(None, description="ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected")
    operation: Optional[str] = Field(None, description="Operation")
    view_id: Optional[str] = Field(None, description="The view to get the row from")


class CodaGetTool(BaseTool):
    name: str = "coda_get"
    description: str = "Tool for coda get operation - get operation"
    args_schema: type[BaseModel] | None = CodaGetToolInput
    credentials: Optional[CodaCredentials] = None
