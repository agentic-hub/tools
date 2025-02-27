from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftexcelCredentials

class MicrosoftexcelReadrowsToolInput(BaseModel):
    data: Optional[str] = Field(None, description="Raw values for the specified range as array of string arrays in JSON format")
    workbook: Optional[Dict[str, Any]] = Field(None, description="Workbook")
    table: Optional[Dict[str, Any]] = Field(None, description="Table")
    data_start_row: Optional[float] = Field(None, description="Relative to selected 'Range', first row index is 0")
    worksheet: Optional[Dict[str, Any]] = Field(None, description="Sheet")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    use_range: Optional[bool] = Field(None, description="Select a Range")
    key_row: Optional[float] = Field(None, description="Relative to selected 'Range', first row index is 0")
    raw_data: Optional[bool] = Field(None, description="Whether the data should be returned RAW instead of parsed into keys according to their header")
    operation: Optional[str] = Field(None, description="Operation")
    range: Optional[str] = Field(None, description="The sheet range to read the data from specified using a A1-style notation, has to be specific e.g A1:B5, generic ranges like A:B are not supported")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    data_property: Optional[str] = Field(None, description="The name of the property into which to write the RAW data")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Values to Send")
    data_mode: Optional[str] = Field(None, description="Data Mode")
    resource: Optional[str] = Field(None, description="Resource")
    column_to_match_on: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    value_to_match_on: Optional[str] = Field(None, description="Value of Column to Match On")
    notice: Optional[str] = Field(None, description="This node connects to the Microsoft 365 cloud platform. Use the 'Extract From File' and 'Convert to File' nodes to directly manipulate spreadsheet files (.xls, .csv, etc). <a href=\"/templates/890\" target=\"_blank\">More info</a>.")


class MicrosoftexcelReadrowsTool(BaseTool):
    name: str = "microsoftexcel_readrows"
    connector_id: str = "nodes-base.microsoftExcel"
    description: str = "Tool for microsoftExcel readRows operation - readRows operation"
    args_schema: type[BaseModel] | None = MicrosoftexcelReadrowsToolInput
    credentials: Optional[MicrosoftexcelCredentials] = None
