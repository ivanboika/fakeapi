from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    companyName = Column(String)
    stateCadastrCode = Column(String)
    legalAddress = Column(String)
    companyRating = Column(Float)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    productName = Column(String)
    group = Column(String)
    description = Column(String)
    photoCode = Column(String)
    amountInStock = Column(Integer)
    price = Column(Float)


class Contact(Base):
    __tablename__ = 'contacts'

    contactID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('users.id'))
    contactName = Column(String)
    contactPhone = Column(String)
    contactEmail = Column(String)


class Cart(Base):
    __tablename__ = 'carts'

    cartID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('users.id'))


class CartItem(Base):
    __tablename__ = 'cartItems'

    cartItemID = Column(Integer, primary_key=True, index=True)
    cartID = Column(Integer, ForeignKey('carts.cartID'))
    productID = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
