from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoingeckoMarketchartToolInput(BaseModel):
    baseCurrency: Optional[str] = Field(None, description="The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    days: Optional[str] = Field(None, description="Return data for this many days in the past from now")
    resource: Optional[str] = Field(None, description="Resource")
    contractAddress: Optional[str] = Field(None, description="Token's contract address")
    searchBy: Optional[str] = Field(None, description="Search by coin ID or contract address")
    baseCurrencies: Optional[str] = Field(None, description="baseCurrencies")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    platformId: Optional[str] = Field(None, description="The ID of the platform issuing tokens")
    quoteCurrencies: Optional[str] = Field(None, description="quoteCurrencies")
    quoteCurrency: Optional[str] = Field(None, description="The second currency in the pair. For BTC:ETH this is ETH. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    coinId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CoingeckoMarketchartTool(BaseTool):
    name = "coingecko_marketchart"
    description = "Tool for coinGecko marketChart operation - marketChart operation"
    
    def _run(self, **kwargs):
        """Run the coinGecko marketChart operation."""
        # Implement the tool logic here
        return f"Running coinGecko marketChart operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the coinGecko marketChart operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
