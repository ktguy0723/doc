class Product:
  def use(self):
    pass


class Factory(Product):
  def create(self, owner: str) -> Product:
    p:Product = self._createProduct(owner)
    self._registerProduct(p)
    return p

  def _createProduct(self, owner: str) -> Product:
    pass

  def _registerProduct(product: Product):
    pass



