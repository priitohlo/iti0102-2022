class Factory:
    def __init__(self):
        self.cakes_baked = list()
        self.cakes_baked_last = list()

    def bake_cake(self, toppings: int, base: int) -> int:
        self.cakes_baked_last.clear()
        ingredients_amount = toppings if toppings == base else max(toppings, base)
        for i in (5, 2, 1):
            while ingredients_amount >= i:
                self.cakes_baked.append(Cake(i, i))
                self.cakes_baked_last.append(Cake(i, i))
                ingredients_amount -= i

        return len(self.cakes_baked_last)

    def get_last_cakes(self, n: int) -> list:
        return self.cakes_baked_last[-n:] if n != 0 else []

    def get_cakes_baked(self) -> list:
        return self.cakes_baked

    def __str__(self):
        return f"Factory with {len(self.cakes_baked)} cakes." if len(self.cakes_baked) != 1 else "Factory with 1 cake."

    def __repr__(self):
        return f"{len(self.cakes_baked_last)} cakes"


class Cake:

    def __init__(self, base_amount, toppings_amount):
        match (base_amount, toppings_amount):
            case (1, 1):
                self.type = "basic"
            case (2, 2):
                self.type = "medium"
            case (5, 5):
                self.type = "large"
            case other:
                raise WrongIngredientsAmountException

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def __repr__(self):
        match self.type:
            case "basic":
                return "Cake(basic)"
            case "medium":
                return "Cake(medium)"
            case "large":
                return "Cake(large)"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.type == other.type


class WrongIngredientsAmountException(Exception):
    pass
