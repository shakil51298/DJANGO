from pydoc import describe
from django.db import models

# Create your models here.
class Products:
    id : int
    name: str
    img : str
    desc : str
    price : float
    off : bool