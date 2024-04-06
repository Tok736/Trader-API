from datetime import datetime

from pydantic import BaseModel

class OperationSchemaRead(BaseModel):
    __tablename__ = "operation"

    id:               int        
    quantinity:       int        
    figi:             str        
    instrument_type:  str | None
    date:             datetime  
    type:             str     
    created_at:       datetime
    updated_at:       datetime
    
class OperationSchemaCreate(BaseModel):
    __tablename__ = "operation"

    quantinity:       int        
    figi:             str        
    instrument_type:  str | None
    date:             datetime  
    type:             str     
    

