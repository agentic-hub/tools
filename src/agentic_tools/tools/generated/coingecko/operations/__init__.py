# coinGecko operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all coinGecko operation tools."""
    tools = []
    from .candlestick import CoingeckoCandlestickTool
    tools.append(CoingeckoCandlestickTool())
    from .get import CoingeckoGetTool
    tools.append(CoingeckoGetTool())
    from .getall import CoingeckoGetallTool
    tools.append(CoingeckoGetallTool())
    from .history import CoingeckoHistoryTool
    tools.append(CoingeckoHistoryTool())
    from .market import CoingeckoMarketTool
    tools.append(CoingeckoMarketTool())
    from .marketchart import CoingeckoMarketchartTool
    tools.append(CoingeckoMarketchartTool())
    from .price import CoingeckoPriceTool
    tools.append(CoingeckoPriceTool())
    from .ticker import CoingeckoTickerTool
    tools.append(CoingeckoTickerTool())
    from .getall import CoingeckoGetallTool
    tools.append(CoingeckoGetallTool())
    return tools
