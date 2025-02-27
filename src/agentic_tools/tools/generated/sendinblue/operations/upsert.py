from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendinblueCredentials

class SendinblueUpsertToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    upsert_attributes: Optional[Dict[str, Any]] = Field(None, description="Array of attributes to be updated")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the contact")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueUpsertTool(BaseTool):
    name: str = "sendinblue_upsert"
    connector_id: str = "nodes-base.sendInBlue"
    description: str = "Tool for sendInBlue upsert operation - upsert operation"
    args_schema: type[BaseModel] | None = SendinblueUpsertToolInput
    credentials: Optional[SendinblueCredentials] = None
