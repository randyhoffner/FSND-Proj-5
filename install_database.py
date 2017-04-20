from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, User, MenuItem

engine = create_engine('sqlite:///catalog.db')

# Bind engine to metadata of the Base class.
Base.metadata.bind = engine

DBSDession = sessionmaker(bind=engine)
session = DBSDession()

# Create dummy user.
User1 = User(name="Mr Boozehound", email="boozy@randyhoffner.com", picture="http:/Bee/static/boozehound.png")
session.add(User1)
session.commit()

# Catgegory for Scotch
category1 = Category(user_id=1, name="Scotch", description="Made in Scotland from barley malt.")

session.add(category1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Johnny Walker Blue Label", description="The best blended scotch money ($$$) can buy", category=category1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Laphroaig", description="Islay single malt scotch.  Tastes like fish.", category=category1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Lagavulin", description="Southern Islay single malt that has a strong peaty taste.", category=category1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Glenmorangie", description="Highland single malt scotch.", category=category1)

session.add(menuItem4)
session.commit()


# Category for bourbon
category2 = Category(user_id=1, name="Bourbon", description="Made in Kentucky.  More than 50 percent corn.  Aged in new oak barrels.")

session.add(category2)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Eagle Rare", description="Good sipping bourbon.", category=category2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Michter's", description="Excellent small batch bourbon.", category=category2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Old Forester 1920 Prohibition Style", description="Very good specialty bourbon, 115 proof.", category=category2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Blanton's Single Barrel", description="Great bourbon, high price.", category=category2)

session.add(menuItem4)
session.commit()


# Category for gin.
category3 = Category(user_id=1, name="Gin", description="Derives its primary flavor from juniper berries.")

session.add(category3)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Beefeater London Dry Gin", description="An excellent dry gin perfect for making gin and tonic.", category=category3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Monopolowa Dry Gin", description="Made in Austria from pototatoes.  As good as Beefeater but cheaper.", category=category3)

session.add(menuItem2)
session.commit()


# Category for tequila

category4 = Category(user_id=1, name="Tequila", description="Made in Mexico from blue agave.")

session.add(category4)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Patron Silver", description="One of the best tequilas available.", category=category4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Don Julio Real", description="Extra Anejo tequila.  You can't afford it.", category=category4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="1800 Silver 100 Proof", description="Strong silver tequila.", category=category4)

session.add(menuItem3)
session.commit()


# Category for mescal
category5 = Category(user_id=1, name="Mezcal", description="Made in Mexico from any kind of agave.  Smoky flavor.")

session.add(category5)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Monte Alban Mezcal con Gusamo", description="That's right: with worm.", category=category5)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Pierde Almas Espadin", description="Smoky.", category=category5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Mescal Tosba Pechuga", description="Triple distilled.", category=category5)

session.add(menuItem3)
session.commit()

print "added liquors!"





