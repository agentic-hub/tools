from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZohocrmCredentials

class ZohocrmGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    invoice_id: Optional[str] = Field(None, description="ID of the invoice to retrieve")
    sales_order_id: Optional[str] = Field(None, description="ID of the sales order to retrieve")
    product__details: Optional[List[Any]] = Field(None, description="Products")
    quote_id: Optional[str] = Field(None, description="ID of the quote to retrieve")
    vendor_id: Optional[str] = Field(None, description="ID of the vendor to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last Name")
    subject: Optional[str] = Field(None, description="Subject or title of the invoice")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="ID of the account to retrieve. Can be found at the end of the URL.")
    deal_name: Optional[str] = Field(None, description="Deal Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    account_name: Optional[str] = Field(None, description="Account Name")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    company: Optional[str] = Field(None, description="Company at which the lead works")
    deal_id: Optional[str] = Field(None, description="ID of the deal to retrieve")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    purchase_order_id: Optional[str] = Field(None, description="ID of the purchase order to retrieve")
    contact_id: Optional[str] = Field(None, description="ID of the contact to retrieve")
    vendor_name: Optional[str] = Field(None, description="Vendor Name")
    lead_id: Optional[str] = Field(None, description="ID of the lead to retrieve")
    product_name: Optional[str] = Field(None, description="Product Name")
    product_id: Optional[str] = Field(None, description="ID of the product to retrieve")


class ZohocrmGetTool(BaseTool):
    name: str = "zohocrm_get"
    connector_id: str = "nodes-base.zohoCrm"
    description: str = "Tool for zohoCrm get operation - get operation"
    args_schema: type[BaseModel] | None = ZohocrmGetToolInput
    credentials: Optional[ZohocrmCredentials] = None
