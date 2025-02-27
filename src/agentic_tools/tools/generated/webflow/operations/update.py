from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WebflowCredentials

class WebflowUpdateToolInput(BaseModel):
    live: Optional[bool] = Field(None, description="Whether the item should be published on the live site")
    item_id: Optional[str] = Field(None, description="ID of the item to update")
    resource: Optional[str] = Field(None, description="Resource")
    site_id: Optional[str] = Field(None, description="ID of the site containing the collection whose items to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    collection_id: Optional[str] = Field(None, description="ID of the collection whose items to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields")


class WebflowUpdateTool(BaseTool):
    name: str = "webflow_update"
    connector_id: str = "nodes-base.webflow"
    description: str = "Tool for webflow update operation - update operation"
    args_schema: type[BaseModel] | None = WebflowUpdateToolInput
    credentials: Optional[WebflowCredentials] = None
