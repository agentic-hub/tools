from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AirtableCredentials

class AirtableSearchToolInput(BaseModel):
    sort: Optional[Dict[str, Any]] = Field(None, description="Defines how the returned records should be ordered")
    table: Optional[str] = Field(None, description="By URL")
    base: Optional[Dict[str, Any]] = Field(None, description="Base")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options which decide which records should be returned")
    authentication: Optional[str] = Field(None, description="Authentication")
    filter_by_formula: Optional[str] = Field(None, description="The formula will be evaluated for each record, and if the result is not 0, false, \"\", NaN, [], or #Error! the record will be included in the response. <a href=\"https://support.airtable.com/docs/formula-field-reference\" target=\"_blank\">More info</a>.")
    id: Optional[str] = Field(None, description="ID of the record to delete. <a href=\"https://support.airtable.com/docs/record-id\" target=\"_blank\">More info</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="columns")


class AirtableSearchTool(BaseTool):
    name: str = "airtable_search"
    description: str = "Tool for airtable search operation - search operation"
    args_schema: type[BaseModel] | None = AirtableSearchToolInput
    credentials: Optional[AirtableCredentials] = None
