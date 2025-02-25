from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NocodbCreateToolInput(BaseModel):
    table: Optional[str] = Field(None, description="The table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    primaryKey: Optional[str] = Field(None, description="Primary Key Type")
    workspaceId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    inputsToIgnore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    id: Optional[str] = Field(None, description="The value of the ID field")
    operation: Optional[str] = Field(None, description="Operation")
    downloadFieldNames: Optional[str] = Field(None, description="Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive.")
    dataToSend: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    version: Optional[str] = Field(None, description="API Version")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    customPrimaryKey: Optional[str] = Field(None, description="Field Name")
    resource: Optional[str] = Field(None, description="Resource")
    downloadAttachments: Optional[bool] = Field(None, description="Whether the attachment fields define in 'Download Fields' will be downloaded")
    projectId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    authentication: Optional[str] = Field(None, description="Authentication")
    info: Optional[str] = Field(None, description="In this mode, make sure the incoming data fields are named the same as the columns in NocoDB. (Use an 'Edit Fields' node before this node to change them if required.)")


class NocodbCreateTool(BaseTool):
    name = "nocodb_create"
    description = "Tool for nocoDb create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the nocoDb create operation."""
        # Implement the tool logic here
        return f"Running nocoDb create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nocoDb create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
