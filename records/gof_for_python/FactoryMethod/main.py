from framework import Factory, Product
from idcard import IDCard, IDCardFactory

def main():
  factory: Factory = IDCardFactory()
  card1: Product = factory.create("a")
  card2: Product = factory.create("b")
  card3: Product = factory.create("c")
  card1.use()
  card2.use()
  card3.use()
  print(factory.getOwners())

if __name__ == '__main__':
    main()