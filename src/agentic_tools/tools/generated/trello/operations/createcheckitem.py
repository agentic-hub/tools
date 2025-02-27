from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TrelloCredentials

class TrelloCreatecheckitemToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    check_item_id: Optional[str] = Field(None, description="The ID of the checklist item to delete")
    description: Optional[str] = Field(None, description="The description of the board")
    checklist_id: Optional[str] = Field(None, description="The ID of the checklist to update")
    comment_id: Optional[str] = Field(None, description="The ID of the comment to delete")
    text: Optional[str] = Field(None, description="Text of the comment")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the attachment to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the new check item on the checklist")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    card_id: Optional[Dict[str, Any]] = Field(None, description="The ID of the card")
    id_member: Optional[str] = Field(None, description="The ID of the member to add to the board")


class TrelloCreatecheckitemTool(BaseTool):
    name: str = "trello_createcheckitem"
    description: str = "Tool for trello createCheckItem operation - createCheckItem operation"
    args_schema: type[BaseModel] | None = TrelloCreatecheckitemToolInput
    credentials: Optional[TrelloCredentials] = None
