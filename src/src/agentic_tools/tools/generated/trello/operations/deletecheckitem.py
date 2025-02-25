from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TrelloDeletecheckitemToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    checkItemId: Optional[str] = Field(None, description="The ID of the checklist item to delete")
    description: Optional[str] = Field(None, description="The description of the board")
    commentId: Optional[str] = Field(None, description="The ID of the comment to delete")
    text: Optional[str] = Field(None, description="Text of the comment")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the attachment to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the board")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    cardId: Optional[Dict[str, Any]] = Field(None, description="The ID of the card")
    idMember: Optional[str] = Field(None, description="The ID of the member to add to the board")


class TrelloDeletecheckitemTool(BaseTool):
    name = "trello_deletecheckitem"
    description = "Tool for trello deleteCheckItem operation - deleteCheckItem operation"
    
    def _run(self, **kwargs):
        """Run the trello deleteCheckItem operation."""
        # Implement the tool logic here
        return f"Running trello deleteCheckItem operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the trello deleteCheckItem operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
