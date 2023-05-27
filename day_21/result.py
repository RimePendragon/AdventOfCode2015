class Result:
    def __init__(self, outcome, cost, items) -> None:
        self.outcome=outcome
        self.cost=int(cost)
        self.items=items

    
    def __str__(self) -> str:
        return f'{self.outcome}, cost={self.cost}, items={self.items}'
    
    def __repr__(self) -> str:
        return repr((self.outcome, self.cost, self.items))

