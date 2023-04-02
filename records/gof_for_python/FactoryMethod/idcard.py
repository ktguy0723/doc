from framework import Product, Factory

class IDCard(Product):
  def __init__(self, owner:str):
    self.owner = owner
    print(self.owner + "のカードを作ります。")

  def use(self):
    print(self.owner + "のカードを使います。")

  def getOwner(self) -> str:
    return self.owner


class IDCardFactory(Factory):
  def __init__(self):
    self.owners: list = []

  def _createProduct(self, owner: str) -> Product:
    return IDCard(owner)
  
  def _registerProduct(self, product: Product):
    self.owners.append(product.getOwner())
  
  def getOwners(self):
    return self.owners

