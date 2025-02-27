from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AirtableCredentials

class AirtableGetmanyToolInput(BaseModel):
    table: Optional[str] = Field(None, description="By URL")
    base: Optional[Dict[str, Any]] = Field(None, description="Base")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    id: Optional[str] = Field(None, description="ID of the record to delete. <a href=\"https://support.airtable.com/docs/record-id\" target=\"_blank\">More info</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="columns")


class AirtableGetmanyTool(BaseTool):
    name: str = "airtable_getmany"
    connector_id: str = "nodes-base.airtable"
    description: str = "Tool for airtable getMany operation - getMany operation"
    args_schema: type[BaseModel] | None = AirtableGetmanyToolInput
    credentials: Optional[AirtableCredentials] = None
