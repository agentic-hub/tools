from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WekanCredentials

class WekanDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    checklist_item_id: Optional[str] = Field(None, description="The ID of the checklistItem item to get. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    checklist_id: Optional[str] = Field(None, description="The ID of the checklist to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    comment_id: Optional[str] = Field(None, description="The ID of the comment to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    author_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    swimlane_id: Optional[str] = Field(None, description="The swimlane ID of the new card. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    board_id: Optional[str] = Field(None, description="The ID of the board to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    card_id: Optional[str] = Field(None, description="The ID of the card to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    title: Optional[str] = Field(None, description="The title of the board")


class WekanDeleteTool(BaseTool):
    name: str = "wekan_delete"
    description: str = "Tool for wekan delete operation - delete operation"
    args_schema: type[BaseModel] | None = WekanDeleteToolInput
    credentials: Optional[WekanCredentials] = None
