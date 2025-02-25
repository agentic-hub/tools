from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoingeckoGetToolInput(BaseModel):
    baseCurrency: Optional[str] = Field(None, description="The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    contractAddress: Optional[str] = Field(None, description="Token's contract address")
    searchBy: Optional[str] = Field(None, description="Search by coin ID or contract address")
    baseCurrencies: Optional[str] = Field(None, description="baseCurrencies")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    platformId: Optional[str] = Field(None, description="The ID of the platform issuing tokens")
    quoteCurrencies: Optional[str] = Field(None, description="quoteCurrencies")
    coinId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CoingeckoGetTool(BaseTool):
    name = "coingecko_get"
    description = "Tool for coinGecko get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the coinGecko get operation."""
        # Implement the tool logic here
        return f"Running coinGecko get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the coinGecko get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
