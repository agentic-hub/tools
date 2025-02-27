from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NotionCredentials

class NotionGetToolInput(BaseModel):
    database_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Database to get")
    page_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Database Page to get")
    text: Optional[str] = Field(None, description="The text to search for")
    user_id: Optional[str] = Field(None, description="User ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    block_ui: Optional[Dict[str, Any]] = Field(None, description="Blocks")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    block_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Block to append blocks to")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    properties_ui: Optional[Dict[str, Any]] = Field(None, description="Properties")
    title: Optional[str] = Field(None, description="Page title. Appears at the top of the page and can be found via Quick Find.")
    notion_notice: Optional[str] = Field(None, description="In Notion, make sure to <a href=\"https://www.notion.so/help/add-and-manage-connections-with-the-api\" target=\"_blank\">add your connection</a> to the pages you want to access.")


class NotionGetTool(BaseTool):
    name: str = "notion_get"
    description: str = "Tool for notion get operation - get operation"
    args_schema: type[BaseModel] | None = NotionGetToolInput
    credentials: Optional[NotionCredentials] = None
