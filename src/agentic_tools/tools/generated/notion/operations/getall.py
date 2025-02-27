from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NotionCredentials

class NotionGetallToolInput(BaseModel):
    database_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Database to operate on")
    fetch_nested_blocks: Optional[bool] = Field(None, description="Also Fetch Nested Blocks")
    page_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Database Page to update")
    text: Optional[str] = Field(None, description="The text to search for")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://developers.notion.com/reference/post-database-query#post-database-query-filter\" target=\"_blank\">Notion guide</a> to creating filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    block_ui: Optional[Dict[str, Any]] = Field(None, description="Blocks")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    block_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Block to get all children from")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    simplify_output: Optional[bool] = Field(None, description="Simplify Output")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    properties_ui: Optional[Dict[str, Any]] = Field(None, description="Properties")
    filter_type: Optional[str] = Field(None, description="Filter")
    title: Optional[str] = Field(None, description="Page title. Appears at the top of the page and can be found via Quick Find.")
    notion_notice: Optional[str] = Field(None, description="In Notion, make sure to <a href=\"https://www.notion.so/help/add-and-manage-connections-with-the-api\" target=\"_blank\">add your connection</a> to the pages you want to access.")
    match_type: Optional[str] = Field(None, description="Must Match")


class NotionGetallTool(BaseTool):
    name: str = "notion_getall"
    connector_id: str = "nodes-base.notion"
    description: str = "Tool for notion getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = NotionGetallToolInput
    credentials: Optional[NotionCredentials] = None
