from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_config import Category, Base, Item, User

engine = create_engine('sqlite:///itemcataloguewithusers.db')
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


# Create dummy user
User1 = User(
    name="Dummy User",
    email="dummy_user@example.com",
    picture='https://s3-ap-southeast-1.amazonaws.com/static.gig88.com/img/empty_user_male.png')
session.add(User1)
session.commit()

# items for Category Baseball
category1 = Category(user_id=1, name="Baseball")

session.add(category1)
session.commit()

item1 = Item(
    user_id=1, title="Rawlings Players Right Hand Glove", description="The Rawlings Players Right Hand Glove is"
    "a great accessory for those who are looking to start out in T-Ball or baseball. The glove is worn on the non-dominant"
    "hand - leaving your dominant left hand to throw and perfect your passes. Featuring a hook and loop strap for an adjustable"
    "and secure fit, and a basket web pattern that makes it a very flexible web.", category=category1)

session.add(item1)
session.commit()

item2 = Item(
    user_id=1, title="Wilson Ash 225 Baseball Bat", description="Knock it out of the park with "
    "the Wilson Ash 225 Baseball Bat. Constructed with Professional grade Alleghany Ash and featuring a synthetic"
    "grip for a firm grasp on the field. The balanced design offers efficient swings, while the laser engraved"
    "barrel delivers an official look.", category=category1)

session.add(item2)
session.commit()

item3 = Item(
    user_id=1,
    title="Worth 12\" Official NCAA Softball Ball",
    description="The Worth 12 Official\" NCAA Softball Ball"
    "is designed for the practice pitch with a soft polycore centre to help prevent injury. The raised red seams"
    "enhance your grip on the ball; while the ProTac synthetic leather makes the ball more durable.",
    category=category1)

session.add(item3)
session.commit()


# items for Category Basketball
category2 = Category(user_id=1, name="Basketball")

session.add(category2)
session.commit()

item1 = Item(
    user_id=1, title="adidas Dual Threat Junior Basketball Shoes", description="Step up your game and sink some hoops"
    "with the adidas Dual Threat Junior Basketball Shoes. The shoes feature an adidas BOUNCE cushioning system to"
    "deliver protection for your feet and cushioned comfort every time you hit the court. The synthetic leather mesh upper"
    "allows optimum breathability and airflow to help keep your feet cool as the game heats up while the molded foam collar"
    "provides premium comfort for your ankles. On-court traction and grip won't be a problem thanks to the full-length herringbone"
    "pattern on the outsole while also adding durability for long-lasting wear. Go hard at the ring and hit the big shots for your team"
    "in comfort thanks to the adidas Dual Threat Junior Basketball Shoes.", category=category2)

session.add(item1)
session.commit()

item2 = Item(
    user_id=1,
    title="Nike Dominate Basketball",
    description="The Nike Dominate Basketball is perfect for outdoor use and ideal for"
    "perfecting your passes. Constructed with a soft touch rubber and featuring a deep pebble texture for superior grip and handling"
    "when you need it most.",
    category=category2)

session.add(item2)
session.commit()

# items for Category Boxing
category3 = Category(user_id=1, name="Boxing")

session.add(category3)
session.commit()

item1 = Item(
    user_id=1,
    title="Adidas Women's Speed 100 Boxing Glove",
    description="Optimize your speed and performance with the Adidas"
    "Women's Speed 100 Glove. Specifically designed for Women, the narrower tapered fit ensures a comfortable and sleek design."
    "Constructed with a PU overlay material and rigid hook and loop elastic closing system, allows for a quick and firm adjustment."
    "Ideal for Boxfit and fitness classes, break through to the next level with the Adidas Women's Speed 100 Glove.",
    category=category3)

session.add(item1)
session.commit()

item2 = Item(
    user_id=1,
    title="Everlast 108\" Hand Wraps",
    description="Get your hands on the Everlast 108\""
    "Hand Wraps. Crafted from a polyester and nylon blend, these wraps have Everlast's EverFresh anti-microbial"
    "treatment that prevents the growth of odour causing bacteria, keeping them fresher for longer. Engineered"
    "for hand protection and support, the thumb strap that helps hold them in place, and a hook and loop closure"
    "that delivers a secure and stay put fit. The length of these wraps is 108 inches, ideal for smaller hands and"
    "MMA workouts. Stop pulling your punches and uppercut, hook and jab without holding back with the Everlast 108\" Hand Wraps.",
    category=category3)

session.add(item2)
session.commit()

item3 = Item(
    user_id=1, title="Everlast Chain & Swivel Set", description="Get your punching bag ready for war with"
    "the Everlast Chain & Swivel Set. Perfect for heavy bags with web strapping, this will allow you to work on your power,"
    "coordination and technique, from the comfort of your home. Featuring carabiners & a spot-welded chain construction provides"
    "a more secure hold, while the built in eye swivel allows for freedom of bag movement during after each punch; let the Everlast"
    "Chain & Swivel Set help you get fight day ready", category=category3)

session.add(item3)
session.commit()


# items for Category Golf
category4 = Category(user_id=1, name="Golf")

session.add(category4)
session.commit()
item1 = Item(
    user_id=1, title="Under Armour Men's Core Golf Visor", description="Perfect for sunny days on the golf course,"
    "the Under Armour Men's Core Gold Visor features a pre-curved bill designed to shield your eyes from harsh sun glare."
    "The built in HeatGear sweatband absorbs and wicks moisture away from the skin keeping sweat out of the eyes for"
    "focused performance; while a flexible stretch fit construction and an adjustable strap provides a customand secure fit. Eliminate"
    "all minor distraction and keep your eye on the ball in the Under Armour Men's Core Golf Visor.", category=category4)

session.add(item1)
session.commit()
item2 = Item(
    user_id=1,
    title="Srixon Soft Feel 12 PK Golf Balls",
    description="Built for the golfer looking for distance"
    "off the tee, the SrixonSoft Feel 12 PK Golf Balls feature a high velocity core to deliver extra range, while offering"
    "a softer feel around the greens..",
    category=category4)

session.add(item2)
session.commit()


# items for Category Hockey
category5 = Category(user_id=1, name="Hockey")

session.add(category5)
session.commit()

item1 = Item(
    user_id=1,
    title="Kookaburra Revoke Hockey Hand Guard",
    description="the Kookaburra Revoke Hockey Hand Guard delivers superior quality,"
    "comfort and protection. This left hand guard has an open palm design to aid stick control and feel, with an ergonomic plastic shell"
    "that provides lightweight backhand protection. With a lightweight and unrestrictive design, this hand guard also has a 2 inch elasticated"
    "embossed wristband for a secure fit every time.",
    category=category5)

session.add(item1)
session.commit()

item2 = Item(
    user_id=1,
    title="Kookaburra Feud M-Bow Senior Hockey Stick",
    description="The Kookaburra Feud M-Bow Senior Hockey Stick"
    "is a great choice for hockey players wanting to develop and improve core skills. Made with a Dual Core construction"
    "that delivers high power, and a maxi head shape for excellent control and easier pushing. The M-Bow places the optimum point of the bow"
    "in the mid-section of the stick which enhances ball control and sweep hitting techniques, whilst specialising in the strike.",
    category=category5)

session.add(item2)
session.commit()


print "added menu items!"
