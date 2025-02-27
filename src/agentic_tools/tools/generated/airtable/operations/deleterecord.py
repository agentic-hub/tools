from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AirtableCredentials

class AirtableDeleterecordToolInput(BaseModel):
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


class AirtableDeleterecordTool(BaseTool):
    name: str = "airtable_deleterecord"
    description: str = "Tool for airtable deleteRecord operation - deleteRecord operation"
    args_schema: type[BaseModel] | None = AirtableDeleterecordToolInput
    credentials: Optional[AirtableCredentials] = None
