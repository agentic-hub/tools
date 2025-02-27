from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WebflowCredentials

class WebflowGetallToolInput(BaseModel):
    live: Optional[bool] = Field(None, description="Whether the item should be published on the live site")
    item_id: Optional[str] = Field(None, description="ID of the item to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    site_id: Optional[str] = Field(None, description="ID of the site containing the collection whose items to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    collection_id: Optional[str] = Field(None, description="ID of the collection whose items to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields")


class WebflowGetallTool(BaseTool):
    name: str = "webflow_getall"
    connector_id: str = "nodes-base.webflow"
    description: str = "Tool for webflow getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = WebflowGetallToolInput
    credentials: Optional[WebflowCredentials] = None
