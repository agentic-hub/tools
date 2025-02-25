from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NotionGetallToolInput(BaseModel):
    databaseId: Optional[Dict[str, Any]] = Field(None, description="The Notion Database to operate on")
    fetchNestedBlocks: Optional[bool] = Field(None, description="Also Fetch Nested Blocks")
    pageId: Optional[Dict[str, Any]] = Field(None, description="The Notion Database Page to update")
    text: Optional[str] = Field(None, description="The text to search for")
    jsonNotice: Optional[str] = Field(None, description="See <a href=\"https://developers.notion.com/reference/post-database-query#post-database-query-filter\" target=\"_blank\">Notion guide</a> to creating filters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    blockUi: Optional[Dict[str, Any]] = Field(None, description="Blocks")
    operation: Optional[str] = Field(None, description="Operation")
    Credentials: Optional[str] = Field(None, description="Credentials")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filterJson: Optional[str] = Field(None, description="Filters (JSON)")
    blockId: Optional[Dict[str, Any]] = Field(None, description="The Notion Block to get all children from")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    simplifyOutput: Optional[bool] = Field(None, description="Simplify Output")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    propertiesUi: Optional[Dict[str, Any]] = Field(None, description="Properties")
    filterType: Optional[str] = Field(None, description="Filter")
    title: Optional[str] = Field(None, description="Page title. Appears at the top of the page and can be found via Quick Find.")
    notionNotice: Optional[str] = Field(None, description="In Notion, make sure to <a href=\"https://www.notion.so/help/add-and-manage-connections-with-the-api\" target=\"_blank\">add your connection</a> to the pages you want to access.")
    matchType: Optional[str] = Field(None, description="Must Match")


class NotionGetallTool(BaseTool):
    name = "notion_getall"
    description = "Tool for notion getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the notion getAll operation."""
        # Implement the tool logic here
        return f"Running notion getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the notion getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
