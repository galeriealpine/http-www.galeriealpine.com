import sys
sys.path.append('/Users/lee/working/InstaPy/assets')

from instapy import InstaPy

insta_username = ''
insta_password = ''

for line in open( '/Users/lee/working/.ga_instagram_bot.cred' ):
    if insta_username == '':
        insta_username = line.rstrip()
    else:
        insta_password = line.rstrip()

# set headless_browser=True if you want to run InstaPy on a server
session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=True
)
session.login()

# don't use the relationship bounds check
session.set_relationship_bounds(
    enabled=False
)

session.set_delimit_liking(
    enabled=True,
    max_likes=2000,
    min_likes=0
)

# follow everyone we like
session.set_do_follow(
    enabled=True,
    percentage=25,
    times=2
)

# unfollow users who don't follow us
session.unfollow_users(
    amount=100,
    instapy_followed_enabled=True,
    style="RANDOM",
    sleep_delay=60,
)

# note - keep sum of all likes to < 300 per hour

# like anything posted here
session.like_by_locations(
    [
        # actual places
        '216921418/villars/',
        '241218410/villars-vaud-switzerland/',
        '670455/villars-sur-ollon/',
        '261044104/sur-les-pistes-villars/',
        '293286136/bretaye/',
        '256352451/gryon-switzerland/',
        '564436973/gare-bvb-de-villars-sur-ollon/',
        '1026860107/arveyes/',
        '220496208/les-diablerets/',
        '155754398365410/cookiedeli/',
        '518992906/le-chamossaire/',
        '1024081980/piste-de-ski-de-villars/',
        '540331631/villars-gryon-les-chaux/',
        '177560976483953/telecabine-roc-dorsay-villars/',
        '353973872/villars-gryon-alpes-vaudoises/',

        # restaurants, hotels, schools, etc
        '324654486/refuge-de-solalex/',
        '1020387703/givengain-foundation/',
        '1027509796/villars-ski-school/',
        '186149958596417/les-mazots-du-clos-luxury-guesthouse-spa/',
        '221256543/chalet-royalp-hotel-spa/',
        '304782561/restaurant-lalchimiste/',
        '321774021624847/villars-vanguard-live-music-club/',
        '577417879055907/eurotel-victoria-villars/',
        '664786822/vieux-villars/',
    ],
    amount=19,
    skip_top_posts=True
)

# like all photos with these tags (note, no ollon or bex as too many
# false positives from outside the area in those, ditto aigle)
session.like_by_tags(
    [
        'villars',
        'villarssurollon',
        'villarsgryon',
        'villarsgryondiablerets',
        'villarsurollon',
        'villarsskischool',
        'bretaye',
    ],
    skip_top_posts=True,
    amount=19
)

# end the bot session
session.end()
