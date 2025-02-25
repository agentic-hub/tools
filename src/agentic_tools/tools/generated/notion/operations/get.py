from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NotionGetToolInput(BaseModel):
    databaseId: Optional[Dict[str, Any]] = Field(None, description="The Notion Database to get")
    pageId: Optional[Dict[str, Any]] = Field(None, description="The Notion Database Page to get")
    text: Optional[str] = Field(None, description="The text to search for")
    userId: Optional[str] = Field(None, description="User ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    blockUi: Optional[Dict[str, Any]] = Field(None, description="Blocks")
    operation: Optional[str] = Field(None, description="Operation")
    Credentials: Optional[str] = Field(None, description="Credentials")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    blockId: Optional[Dict[str, Any]] = Field(None, description="The Notion Block to append blocks to")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    propertiesUi: Optional[Dict[str, Any]] = Field(None, description="Properties")
    title: Optional[str] = Field(None, description="Page title. Appears at the top of the page and can be found via Quick Find.")
    notionNotice: Optional[str] = Field(None, description="In Notion, make sure to <a href=\"https://www.notion.so/help/add-and-manage-connections-with-the-api\" target=\"_blank\">add your connection</a> to the pages you want to access.")


class NotionGetTool(BaseTool):
    name = "notion_get"
    description = "Tool for notion get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the notion get operation."""
        # Implement the tool logic here
        return f"Running notion get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the notion get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
