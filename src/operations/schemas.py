from datetime import datetime

from pydantic import BaseModel

class OperationSchemaRead(BaseModel):
    id:               int        
    quantity:         int        
    figi:             str        
    instrument_type:  str | None
    date:             datetime  
    type:             str     
    created_at:       datetime
    updated_at:       datetime
    
class OperationSchemaCreate(BaseModel):
    quantity:         int        
    figi:             str        
    instrument_type:  str | None
    date:             datetime  
    type:             str     
    

