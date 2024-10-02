from typing import Optional
from sqlmodel import SQLModel, Field, select
from pydantic import validator
from statistics import mean
from datetime import datetime

class Beer(SQLModel, table_name="beers", table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    date: datetime = Field(default_factory=datetime.now)
#    ibu: int
    rate: int = 0

    @validator("flavor", "image", "cost", pre=True)
    def validate_ratings(cls, v: int, field) -> Optional[int]:
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean(
            [
                values["flavor"], 
                values["image"],
                values["cost"]
            ]
        )
        return int(rate)
"""        
try:
    brewdog = Beer(name="BrewDog", style="EIPA", flavor=6, cost=8, image=8)
    print(brewdog)
except RuntimeError as e:
    print(str(e) + " Zicou tudo !!!")
"""