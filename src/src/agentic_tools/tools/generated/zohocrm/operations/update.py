from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZohocrmUpdateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    invoiceId: Optional[str] = Field(None, description="ID of the invoice to update")
    salesOrderId: Optional[str] = Field(None, description="ID of the sales order to update")
    Product_Details: Optional[List[Any]] = Field(None, description="Products")
    quoteId: Optional[str] = Field(None, description="ID of the quote to update")
    vendorId: Optional[str] = Field(None, description="ID of the vendor to update")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    lastName: Optional[str] = Field(None, description="Last Name")
    subject: Optional[str] = Field(None, description="Subject or title of the invoice")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="ID of the account to update. Can be found at the end of the URL.")
    dealName: Optional[str] = Field(None, description="Deal Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    accountName: Optional[str] = Field(None, description="Account Name")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    Company: Optional[str] = Field(None, description="Company at which the lead works")
    dealId: Optional[str] = Field(None, description="ID of the deal to update")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    purchaseOrderId: Optional[str] = Field(None, description="ID of the purchase order to update")
    contactId: Optional[str] = Field(None, description="ID of the contact to update")
    vendorName: Optional[str] = Field(None, description="Vendor Name")
    leadId: Optional[str] = Field(None, description="ID of the lead to update")
    productName: Optional[str] = Field(None, description="Product Name")
    productId: Optional[str] = Field(None, description="ID of the product to update")


class ZohocrmUpdateTool(BaseTool):
    name = "zohocrm_update"
    description = "Tool for zohoCrm update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the zohoCrm update operation."""
        # Implement the tool logic here
        return f"Running zohoCrm update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zohoCrm update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
