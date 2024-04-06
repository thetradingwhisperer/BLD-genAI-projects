from pydantic import BaseModel, validator, ValidationError
from datetime import datetime
import pandas as pd

class GPSEntry(BaseModel):
    vessel_name: str
    timestamp: datetime
    latitude: float
    longitude: float

    @validator('latitude')
    def latitude_range(cls, v):
        if not -90 <= v <= 90:
            raise ValueError('Latitude must be between -90 and 90 degrees')
        return v

    @validator('longitude')
    def longitude_range(cls, v):
        if not -180 <= v <= 180:
            raise ValueError('Longitude must be between -180 and 180 degrees')
        return v

# Sample data points
data = [
    {"vessel_name": "Tanker A", "timestamp": "2024-04-06T12:00:00", "latitude": 25.7617, "longitude": -80.1918},
    # This entry is intentionally faulty for demonstration
    {"vessel_name": "Tanker C", "timestamp": "2024-04-06T12:10:00", "latitude": 91.0000, "longitude": -100.0000},
    {"vessel_name": "Tanker B", "timestamp": "2024-04-06T12:05:00", "latitude": 37.7749, "longitude": -122.4194},
    
]

validated_data = []

for entry in data:
    try:
        validated_entry = GPSEntry(**entry)
        validated_data.append(validated_entry)
        print(f"Validated data point: {validated_entry}")
    except ValidationError as e:
        print(f"Error validating data: {e}")
        non_validated_entry = {**entry}
        print(f"Non-validated data point: {non_validated_entry}")


# Convert the list of Pydantic models to dictionaries for DataFrame creation
df_data = [entry.dict() for entry in validated_data]
df = pd.DataFrame(df_data)

print(df)

