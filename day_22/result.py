class Result:
    def __init__(self, outcome, cost) -> None:
        self.outcome=outcome
        self.cost=int(cost)

    
    def __str__(self) -> str:
        return f'{self.outcome}, cost={self.cost}'
    
    def __repr__(self) -> str:
        return repr((self.outcome, self.cost))

