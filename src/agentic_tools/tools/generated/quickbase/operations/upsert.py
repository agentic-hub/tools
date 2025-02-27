from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import QuickbaseCredentials

class QuickbaseUpsertToolInput(BaseModel):
    update_key: Optional[str] = Field(None, description="Update can use the key field on the table, or any other supported unique field")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="The table identifier")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    merge_field_id: Optional[str] = Field(None, description="<p>You're updating records in a Quick Base table with data from an external file. In order for a merge like this to work, Quick Base needs a way to match records in the source data with corresponding records in the destination table.</p><p>You make this possible by choosing the field in the app table that holds unique matching values. This is called a merge field.</p>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    report_id: Optional[str] = Field(None, description="The identifier of the report, unique to the table")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class QuickbaseUpsertTool(BaseTool):
    name: str = "quickbase_upsert"
    connector_id: str = "nodes-base.quickbase"
    description: str = "Tool for quickbase upsert operation - upsert operation"
    args_schema: type[BaseModel] | None = QuickbaseUpsertToolInput
    credentials: Optional[QuickbaseCredentials] = None
