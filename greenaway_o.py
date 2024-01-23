class Film:
    def __init__(self, cim, ev):
        self.cim=cim
        self.ev=int(ev)

    def __str__(self) -> str:
        return f"Film címe: {self.cim}, év: {self.ev}"
