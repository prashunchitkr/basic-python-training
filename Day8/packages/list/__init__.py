# using relative imports
from .fruits import add_fruit, remove_fruit
from .vegetables import add_vegetable, remove_vegetable

# list of objects to be exported while other modules import with *
__all__ = ['add_fruit', 'add_vegetable']
