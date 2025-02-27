from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WiseCredentials

class WiseCreateToolInput(BaseModel):
    quote_id: Optional[str] = Field(None, description="ID of the quote based on which to create the transfer")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    target_currency: Optional[str] = Field(None, description="Code of the currency to receive for the quote to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    source_currency: Optional[str] = Field(None, description="Code of the currency to send for the quote to create")
    transfer_id: Optional[str] = Field(None, description="ID of the transfer to delete")
    target_account_id: Optional[str] = Field(None, description="ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    amount_type: Optional[str] = Field(None, description="Whether the amount is to be sent or received")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    profile_id: Optional[str] = Field(None, description="ID of the user profile to create the quote under. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    file_name: Optional[str] = Field(None, description="Name of the file that will be downloaded")
    amount: Optional[float] = Field(None, description="Amount of funds for the quote to create")


class WiseCreateTool(BaseTool):
    name: str = "wise_create"
    connector_id: str = "nodes-base.wise"
    description: str = "Tool for wise create operation - create operation"
    args_schema: type[BaseModel] | None = WiseCreateToolInput
    credentials: Optional[WiseCredentials] = None
