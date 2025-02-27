from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import QuickbaseCredentials

class QuickbaseDownloadToolInput(BaseModel):
    update_key: Optional[str] = Field(None, description="Update can use the key field on the table, or any other supported unique field")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    table_id: Optional[str] = Field(None, description="The table identifier")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    report_id: Optional[str] = Field(None, description="The identifier of the report, unique to the table")
    field_id: Optional[str] = Field(None, description="The unique identifier of the field")
    version_number: Optional[float] = Field(None, description="The file attachment version number")
    record_id: Optional[str] = Field(None, description="The unique identifier of the record")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class QuickbaseDownloadTool(BaseTool):
    name: str = "quickbase_download"
    description: str = "Tool for quickbase download operation - download operation"
    args_schema: type[BaseModel] | None = QuickbaseDownloadToolInput
    credentials: Optional[QuickbaseCredentials] = None
