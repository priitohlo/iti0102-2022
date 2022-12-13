"""Alchemy."""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """Init."""
        self.name = name

    def __repr__(self):
        """Repr."""
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.storage = list()

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.storage.append(element)
        else:
            raise TypeError

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        for i, e in enumerate(reversed(self.storage)):
            if e.name == element_name:
                return self.storage.pop(-i - 1)
        return None

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        return_list = self.storage.copy()
        self.storage.clear()
        return return_list

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        content_dict = dict()
        return_string = "Content:\n"

        if len(self.storage) == 0:
            return return_string + " Empty."

        for e in self.storage:
            if e.name not in content_dict:
                content_dict[e.name] = 1
            else:
                content_dict[e.name] += 1

        for k, v in sorted(content_dict.items()):
            return_string += f" * {k} x {v}\n"

        return return_string[:-1]


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.recipes = dict()

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        components = frozenset([first_component_name, second_component_name])
        if len({first_component_name, second_component_name, product_name}) < 3:
            raise DuplicateRecipeNamesException
        elif components in self.recipes:
            raise RecipeOverlapException

        self.recipes[components] = product_name

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str or None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        components = frozenset([first_component_name, second_component_name])
        try:
            return self.recipes[components]
        except KeyError:
            return None

    def get_component_names(self, product_name: str) -> tuple[str, str] or None:
        for k, v in self.recipes.items():
            if v == product_name:
                return tuple(k)
        return None


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        super().__init__()
        self.recipes = recipes
        self.result = []

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.storage.append(element)
        else:
            raise TypeError

        while any([x.issubset(frozenset([x.name for x in self.storage])) for x in self.recipes.recipes.keys()])\
                and not any([x.uses == 0 for x in [y for y in self.storage if type(y) == Catalyst]]):
            for k, v in self.recipes.recipes.items():
                if k.issubset(frozenset([x.name for x in reversed(self.storage)])):
                    self.result = []
                    for i, e in reversed(list(enumerate(self.storage))):
                        if len(self.result) == 2:
                            break
                        if e.name in k and e.name not in self.result:
                            if type(e) == Catalyst:
                                if e.uses > 0:
                                    e.uses -= 1
                                    self.result.append(e)
                                else:
                                    continue
                            else:
                                self.result.append(self.storage.pop(i))

                    if len(self.result) == 2:
                        self.storage.append(AlchemicalElement(self.recipes.get_product_name(*[x.name for x in self.result])))
                    else:
                        self.storage += self.result
                    break



class Catalyst(AlchemicalElement):
    """Catalyst class."""

    def __init__(self, name: str, uses: int):
        """
        Initialize the Catalyst class.

        :param name: The name of the Catalyst.
        :param uses: The number of uses the Catalyst has.
        """
        self.name = name
        self.uses = uses

    def __repr__(self) -> str:
        """
        Representation of the Catalyst class.

        Example:
            catalyst = Catalyst("Philosophers' stone", 3)
            print(catalyst) # -> <C: Philosophers' stone (3)>

        :return: String representation of the Catalyst.
        """
        return f"<C: {self.name} ({self.uses})>"


class Purifier(AlchemicalStorage):
    """
    Purifier class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Purifier class."""
        self.storage = list()
        self.recipes = recipes

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can be split into anything.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            purifier = Purifier(recipes)
            purifier.add(AlchemicalElement('Ice'))
            purifier.extract() # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.storage.append(element)
        else:
            raise TypeError

        while any([x in [y.name for y in self.storage] for x in self.recipes.recipes.values()]):
            for k, v in self.recipes.recipes.items():
                if v in [x.name for x in self.storage]:
                    for i, e in reversed(list(enumerate(self.storage))):
                        if e.name == v:
                            self.storage.pop(i)
                            self.storage += [AlchemicalElement(x) for x in self.recipes.get_component_names(e.name)]


if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Earth', 'Fire', 'Iron')
    recipes.add_recipe("Philosophers' stone", 'Iron', 'Silver')
    recipes.add_recipe("Philosophers' stone", 'Silver', 'Gold')
    recipes.add_recipe('Iron', 'Crystal', 'Talisman')
    # ((Earth + Fire) + Philosophers' stone) + Philosophers' stone) = Gold

    cauldron = Cauldron(recipes)
    cauldron.add(Catalyst("Philosophers' stone", 2))
    cauldron.add(AlchemicalElement('Fire'))
    print(cauldron.get_content())
    # Content:
    #  * Fire x 1
    #  * Philosophers' stone x 1

    cauldron.add(AlchemicalElement('Earth'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Gold>]

    purifier = Purifier(recipes)
    purifier.add(AlchemicalElement('Talisman'))
    print(purifier.extract())  # -> [<AE: Earth>, <AE: Fire>, <AE: Crystal>]  (in any order)
