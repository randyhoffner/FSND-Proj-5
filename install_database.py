from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

from database_setup import Category, Base, User, Item

engine = create_engine('sqlite:///catalog.db')

# Bind engine to metadata of the Base class.
Base.metadata.bind = engine

DBSDession = sessionmaker(bind=engine)
session = DBSDession()

# Create dummy user.
User1 = User(name="Mr Boozehound", email="boozy@randyhoffner.com", picture="static/boozehound.png")
session.add(User1)
session.commit()

# Catgegory for Scotch
category1 = Category(user_id=1, name="Scotch")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Johnny Walker Blue Label", description="The best blended scotch money ($$$) can buy", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Laphroaig", description="Islay single malt scotch.  Tastes like fish.", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Lagavulin", description="Southern Islay single malt that has a strong peaty taste.", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Glenmorangie", description="Highland single malt scotch.")

session.add(item4)
session.commit()


# Category for bourbon
category2 = Category(user_id=1, name="Bourbon")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Eagle Rare", description="Good sipping bourbon.", category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Michter's", description="Excellent small batch bourbon.", category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Old Forester 1920 Prohibition Style", description="Very good specialty bourbon, 115 proof.", category=category2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Blanton's Single Barrel", description="Great bourbon, high price.")

session.add(item4)
session.commit()


# Category for gin.
category3 = Category(user_id=1, name="Gin")

session.add(category3)
session.commit()

item1 = Item(user_id=1, name="Beefeater London Dry Gin", description="An excellent dry gin perfect for making gin and tonic.", category=category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Monopolowa Dry Gin", description="Made in Austria from pototatoes.  As good as Beefeater but cheaper.", category=category3)

session.add(item2)
session.commit()


# Category for tequila

category4 = Category(user_id=1, name="Tequila")

session.add(category4)
session.commit()

item1 = Item(user_id=1, name="Patron Silver", description="One of the best tequilas available.", category=category4)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Don Julio Real", description="Extra Anejo tequila.  You can't afford it.")

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="1800 Silver 100 Proof", description="Strong silver tequila.", category=category4)

session.add(item3)
session.commit()


# Category for mescal
category5 = Category(user_id=1, name="Mezcal")

session.add(category5)
session.commit()

item1 = Item(user_id=1, name="Monte Alban Mezcal con Gusamo", description="That's right: with worm.", category=category5)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Pierde Almas Espadin", description="Smoky.", category=category5)

session.add(item2)
session.commit()

item3 = Item(user_id, name="Mescal Tosba Pechuga", description="Triple distilled.", category=category5)

session.add(item3)
session.commit()

print "added liquors!"





