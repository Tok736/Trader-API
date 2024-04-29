from sqlalchemy import Select

class Paginator:
    ''' Class to paginate select queries from db '''
    def __init__(self, limit: int = 10, offset: int = 0) -> None:
        self.limit = limit
        self.offset = offset

    def __call__(self, statement: Select):
        ''' 
        Overriding call method. Using: 
        paginator = Paginator(limit=20, offset=5)

        statement = select(User)
        statement = paginator(statement)
        '''
        return statement.offset(self.offset).limit(self.limit)