from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WiseCredentials

class WiseGetToolInput(BaseModel):
    quote_id: Optional[str] = Field(None, description="ID of the quote to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    target: Optional[str] = Field(None, description="Code of the target currency to retrieve the exchange rate for")
    transfer_id: Optional[str] = Field(None, description="ID of the transfer to retrieve")
    target_account_id: Optional[str] = Field(None, description="ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    source: Optional[str] = Field(None, description="Code of the source currency to retrieve the exchange rate for")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    profile_id: Optional[str] = Field(None, description="ID of the user profile to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    file_name: Optional[str] = Field(None, description="Name of the file that will be downloaded")
    download_receipt: Optional[bool] = Field(None, description="Whether to download the transfer receipt as a PDF file. Only for executed transfers, having status 'Outgoing Payment Sent'.")


class WiseGetTool(BaseTool):
    name: str = "wise_get"
    connector_id: str = "nodes-base.wise"
    description: str = "Tool for wise get operation - get operation"
    args_schema: type[BaseModel] | None = WiseGetToolInput
    credentials: Optional[WiseCredentials] = None
