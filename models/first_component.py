from pydantic import BaseModel

class TickerData(BaseModel):
  name: str
  open: float
  close: float
  change: float
  
  def json(self) -> dict[str, str | float]:
    return {"name": self.name, "open": self.open, "close": self.close, "change": self.change}

class TickerDataList(BaseModel):
  logs: list[TickerData]

  def json(self) -> list[TickerData]:
    return {"logs": [ticker.json() for ticker in self.logs]}
    