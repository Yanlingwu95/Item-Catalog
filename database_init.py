from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(name="Yanling Wu",
              email="nbaynom0@skype.com",
              picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
session.add(User1)
session.commit()

## User2 = User(name="Renado Gress",
##               email="rgress1@t.co",
##               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
## session.add(User2)
## session.commit()

## User3 = User(name="Prinz Blakemore",
##               email="pblakemore2@bluehost.com",
##               picture='http://dummyimage.com/200x200.png/5fa2dd/ffffff')
## session.add(User3)
## session.commit()

# Create fake categories
Category1 = Category(name="Football",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Cars",
                      user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Snacks",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Gadgets",
                      user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Food",
                      user_id=1)
session.add(Category5)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Football Boots",
               date=datetime.datetime.now(),
               description="Shoes to play football in.",
               picture= "https://images-na.ssl-images-amazon.com/images/I/71rzMNbfa%2BL._UL1300_.jpg",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Football Shirt",
               date=datetime.datetime.now(),
               description="Shirt to play football in.",
               picture="https://images.sportsdirect.com/images/products/37764221_l.jpg",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Football",
               date=datetime.datetime.now(),
               description="A Football.",
               picture="http://shihuo.hupucdn.com/ucditor/20180129/500x308_034cac31646d0068a964130368e5cd9e.jpeg",
               category_id=1,
               user_id=1)
session.add(Item3)
session.commit()

Item1 = Items(name="Tesla Roadster",
               date=datetime.datetime.now(),
               description="Dream car",
               picture= "https://cdn.teslarati.com/wp-content/uploads/2017/11/Roadster_Front_34_1-e1512593855725.jpg",
               category_id=2,
               user_id=1)
session.add(Item1)
session.commit()

Item1 = Items(name="Wa Haha",
               date=datetime.datetime.now(),
               description="My favorite Snacks",
               picture= "https://cdn.shopify.com/s/files/1/1138/5788/products/AD__asianmama.ca2_500x.jpg?v=1501486144",
               category_id=3,
               user_id=1)
session.add(Item1)
session.commit()

Item1 = Items(name="Switch",
               date=datetime.datetime.now(),
               description="An Interesting Game Tool",
               picture= "https://i.ebayimg.com/00/s/NTEyWDEwMjQ=/z/YWQAAOSws-tbDTHg/$_86.JPG",
               category_id=4,
               user_id=1)
session.add(Item1)
session.commit()

Item1 = Items(name="Healthy food",
               date=datetime.datetime.now(),
               description="Healthy and delicious dinner",
               picture= "https://cp1.douguo.com/upload/caiku/0/d/e/yuan_0d3eb0af3f56e1375db0fb9ae60addee.jpg",
               category_id=5,
               user_id=1)
session.add(Item1)
session.commit()

print "Your database has been populated with fake data!"