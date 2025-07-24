from .Locations import prices_ints

from .Constants import *

def can_play_song(song, state, player):
    return state.has(song, player) and state.has("Ocarina of Time", player)

def can_get_magic_beans(state, player):
    return (state.has("Magic Bean", player) and 
            state.has("Deku Mask", player) and 
            state.can_reach("Deku Palace", 'Region', player))

def has_bombchus(state, player):
    return state.has("Progressive Bombchu Bag", player)

def has_explosives(state, player):
    return (state.has("Progressive Bomb Bag", player) or 
            has_bombchus(state, player) or 
            state.has("Blast Mask", player))

def has_hard_projectiles(state, player):
    return (state.has("Progressive Bow", player) or 
            state.has("Zora Mask", player) or 
            state.has("Hookshot", player))

def has_projectiles(state, player):
    return ((state.has("Deku Mask", player) and state.has("Progressive Magic", player)) or 
            has_hard_projectiles(state, player))

def can_smack_hard(state, player):
    return (state.has("Progressive Sword", player) or 
            state.has("Fierce Deity's Mask", player) or 
            state.has("Great Fairy Sword", player) or 
            state.has("Goron Mask", player) or 
            state.has("Zora Mask", player))

def can_smack(state, player):
    return can_smack_hard(state, player) or state.has("Deku Mask", player)

def can_clear_woodfall(state, player):
    return state.can_reach("Woodfall Temple Odolwa's Remains", 'Location', player)
    
def can_clear_snowhead(state, player):
    return state.can_reach("Snowhead Temple Goht's Remains", 'Location', player)
    
def can_clear_greatbay(state, player):
    return state.can_reach("Great Bay Temple Gyorg's Remains", 'Location', player)
    
def can_clear_stonetower(state, player):
    return state.can_reach("Stone Tower Temple Inverted Twinmold's Remains", 'Location', player)

def has_paper(state, player):
    return (state.has("Land Title Deed", player) or 
            state.has("Swamp Title Deed", player) or 
            state.has("Mountain Title Deed", player) or 
            state.has("Ocean Title Deed", player) or 
            state.has("Letter to Kafei", player) or 
            state.has("Priority Mail", player))

def can_get_cow_milk(state, player):
    return (has_bottle(state, player) and 
            can_play_song("Epona's Song", state, player) and 
            (has_explosives(state, player) or 
             can_use_powder_keg(state, player) or 
             state.has("Hookshot", player) or 
             (state.has("Gibdo Mask", player) and 
              has_bottle(state, player) and 
              can_plant_beans(state, player) and 
              state.can_reach("Twin Islands Hot Water Grotto Chest", 'Location', player) or 
              can_use_light_arrows(state, player) and 
              (state.can_reach("Twin Islands Hot Water Grotto Chest", 'Location', player) or 
               (state.has("Goron Mask", player) and 
                state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player)) or 
               state.can_reach("Ikana Well Invisible Chest", 'Location', player)))))

def has_bottle(state, player, need_count=1):
    bottle_count = 0
    if state.has("Bottle", player, 2):
        bottle_count += 2
    elif state.has("Bottle", player):
        bottle_count += 1
    if state.has("Bottle of Milk", player):
        bottle_count += 1
    if state.has("Bottle of Chateau Romani", player):
        bottle_count += 1
    if state.has("Bottle of Red Potion", player):
        bottle_count += 1
    return bottle_count >= need_count

def can_plant_beans(state, player):
    return (can_get_magic_beans(state, player) and 
            (has_bottle(state, player) or can_play_song("Song of Storms", state, player)))

def can_use_powder_keg(state, player):
    return state.has("Powder Keg", player) and state.has("Goron Mask", player)

def can_use_magic_arrow(item, state, player):
    return (state.has(item, player) and 
            state.has("Progressive Bow", player) and 
            state.has("Progressive Magic", player))

def can_use_fire_arrows(state, player):
    return can_use_magic_arrow("Fire Arrow", state, player)

def can_use_ice_arrows(state, player):
    return can_use_magic_arrow("Ice Arrow", state, player)

def can_use_light_arrows(state, player):
    return can_use_magic_arrow("Light Arrow", state, player)

def has_gilded_sword(state, player):
    return state.has("Progressive Sword", player, 3)

def has_mirror_shield(state, player):
    return state.has("Progressive Shield", player, 2)

def can_use_lens(state, player):
    return state.has("Lens of Truth", player) and state.has("Progressive Magic", player)

def can_bring_to_player(state, player):
    return state.has("Hookshot", player) or state.has("Zora Mask", player)

def can_reach_scarecrow(state, player):
    return (state.can_reach("Astral Observatory", 'Region', player) or 
            state.can_reach("Trading Post", 'Region', player))

def can_reach_seahorse(state, player):
    return (state.can_reach("Fisherman's House", 'Region', player) and 
            state.has("Zora Mask", player) and 
            state.has("Pictograph Box", player) and 
            (state.has("Hookshot", player) or state.has("Goron Mask", player)))

def can_afford_price(state, player, price):
    if price > 200:
        return state.has("Progressive Wallet", player, 2)
    elif price > 99:
        return state.has("Progressive Wallet", player)
    return True

def can_purchase(state, player, price_index):
    price = prices_ints[price_index]
    if price > 200:
        return state.has("Progressive Wallet", player, 2)
    elif price > 99:
        return state.has("Progressive Wallet", player)
    return True

def has_enough_remains(state, player, need_count):
    remains_count = 0
    if state.has("Odolwa's Remains", player):
        remains_count += 1
    if state.has("Goht's Remains", player):
        remains_count += 1
    if state.has("Gyorg's Remains", player):
        remains_count += 1
    if state.has("Twinmold's Remains", player):
        remains_count += 1
    return remains_count >= need_count

def get_region_rules(player, options):
    return {
        "Clock Town -> The Moon":
            lambda state: (
                state.has("Ocarina of Time", player) and 
                state.has("Oath to Order", player) and 
                has_enough_remains(state, player, options.moon_remains_required.value)
            ),
        "Southern Swamp -> Southern Swamp (Deku Palace)":
            lambda state: (
                state.has("Bottle of Red Potion", player) or 
                (
                    has_hard_projectiles(state, player) and 
                    state.has("Deku Mask", player)
                ) or 
                (
                    state.has("Pictograph Box", player) and 
                    state.has("Deku Mask", player)
                )
            ),
        "Southern Swamp (Deku Palace) -> Swamp Spider House":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp (Deku Palace) -> Deku Palace":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp (Deku Palace) -> Woodfall":
            lambda state: state.has("Deku Mask", player),
        "Woodfall -> Woodfall Temple":
            lambda state: can_play_song("Sonata of Awakening", state, player),
        "Termina Field -> Path to Mountain Village":
            lambda state: state.has("Progressive Bow", player),
        "Path to Mountain Village -> Mountain Village":
            lambda state: (
                state.has("Goron Mask", player) or 
                has_explosives(state, player) or 
                can_use_fire_arrows(state, player)
            ),
        "Path to Snowhead -> Snowhead":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_play_song("Goron Lullaby", state, player) and 
                state.has("Progressive Magic", player)
            ),
        "Snowhead -> Snowhead Temple": lambda state: (
                state.has("Goron Mask", player) and 
                can_play_song("Goron Lullaby", state, player) and 
                state.has("Progressive Magic", player)
            ),            
        "Termina Field -> Great Bay":
            lambda state: can_play_song("Epona's Song", state, player),
        "Great Bay -> Ocean Spider House":
            lambda state: has_explosives(state, player),
        "Great Bay -> Pirates' Fortress":
            lambda state: state.has("Zora Mask", player),
        "Pirates' Fortress -> Pirates' Fortress Sewers":
            lambda state: state.has("Goron Mask", player) or state.has("Hookshot", player),
        "Pirates' Fortress Sewers -> Pirates' Fortress (Interior)":
            lambda state: state.has("Goron Mask", player) or state.has("Hookshot", player),
        "Zora Cape -> Zora Hall":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape -> Great Bay Temple":
            lambda state: (
                can_play_song("New Wave Bossa Nova", state, player) and 
                state.has("Hookshot", player) and 
                state.has("Zora Mask", player)
            ),
        "Road to Ikana -> Ikana Graveyard":
            lambda state: can_play_song("Epona's Song", state, player),
        "Road to Ikana -> Ikana Canyon":
            lambda state: (
                (
                    state.has("Garo Mask", player) and 
                    can_play_song("Epona's Song", state, player) and 
                    state.has("Hookshot", player)
                ) or 
                (
                    state.has("Gibdo Mask", player) and 
                    can_play_song("Epona's Song", state, player) and 
                    state.has("Hookshot", player)
                )
            ),
        "Ikana Canyon -> Secret Shrine":
            lambda state: can_use_light_arrows(state, player),
        "Ikana Canyon -> Beneath the Well":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                state.has("Hookshot", player) and 
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player)
            ),
        "Ikana Canyon -> Ikana Castle":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                state.has("Hookshot", player) and 
                (
                    can_use_light_arrows(state, player) or 
                    has_mirror_shield(state, player)
                )
            ),
        "Stone Tower -> Stone Tower Temple":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_play_song("Elegy of Emptiness", state, player) and 
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player)
            ),
        "Stone Tower -> Stone Tower (Inverted)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and 
                can_use_light_arrows(state, player) and 
                can_play_song("Elegy of Emptiness", state, player)
            ),
        "Stone Tower (Inverted) -> Stone Tower Temple (Inverted)":
            lambda state: True,    
    }

def get_location_rules(player, options):
    return {
        "Keaton Quiz":
            lambda state: state.has("Keaton Mask", player),
        "Clock Town Postbox":
            lambda state: state.has("Postman's Hat", player),
        "Top of Clock Tower (Ocarina of Time)":
            lambda state: has_projectiles(state, player),
        "Top of Clock Tower (Song of Time)":
            lambda state: has_projectiles(state, player),
        
        "North Clock Town Deku Playground Any Day":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Deku Playground All Days":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Save Old Lady":
            lambda state: (
                state.has("Progressive Sword", player) or 
                state.has("Great Fairy Sword", player) or 
                state.has("Zora Mask", player) or 
                state.has("Goron Mask", player)
            ),
        "North Clock Town Great Fairy Reward (Has Transformation Mask)":
            lambda state: (
                state.has("Stray Fairy (Clock Town)", player) and 
                (
                    state.has("Deku Mask", player) or 
                    state.has("Goron Mask", player) or 
                    state.has("Zora Mask", player)
                )
            ),
        "North Clock Town Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Clock Town)", player),
        "Clock Town Hide-and-Seek":
            lambda state: has_projectiles(state, player),
        
        "South Clock Town Moon's Tear Trade":
            lambda state: state.has("Moon's Tear", player),
        "South Clock Town Corner Chest":
            lambda state: state.has("Hookshot", player),
        "South Clock Town Final Day Tower Chest":
            lambda state: (
                state.has("Hookshot", player) or 
                (
                    state.has("Deku Mask", player) and 
                    state.has("Moon's Tear", player)
                )
            ),
        "Clock Tower Happy Mask Salesman #1":
            lambda state: True,
        "Clock Tower Happy Mask Salesman #2":
            lambda state: True,
        
        "East Clock Town Couples Mask on Mayor":
            lambda state: state.has("Couple's Mask", player),
        "East Clock Town Shooting Gallery 40-49 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Shooting Gallery Perfect 50 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Honey and Darling Any Day":
            lambda state: (
                state.has("Progressive Bow", player) or 
                (
                    state.has("Progressive Bomb Bag", player) or 
                    has_bombchus(state, player)
                ) or 
                (
                    state.has("Deku Mask", player) and 
                    state.has("Progressive Magic", player)
                )
            ),
        "East Clock Town Honey and Darling All Days":
            lambda state: (
                state.has("Progressive Bow", player) and 
                state.has("Progressive Bomb Bag", player) and 
                has_bombchus(state, player)
            ),
        "East Clock Town Treasure Game Chest (Human)":
            lambda state: True,
        "East Clock Town Treasure Game Chest (Deku)":
            lambda state: state.has("Deku Mask", player),
        "East Clock Town Treasure Game Chest (Goron)":
            lambda state: state.has("Goron Mask", player),
        "East Clock Town Treasure Game Chest (Zora)":
            lambda state: state.has("Zora Mask", player),
        "Bomber's Hideout Chest":
            lambda state: (
                state.can_reach("Clock Town Hide-and-Seek", 'Location', player) and 
                has_explosives(state, player)
            ),
        "Bomber's Hideout Astral Observatory":
            lambda state: has_projectiles(state, player),
        "Milk Bar Show":
            lambda state: (
                state.has("Romani Mask", player) and 
                state.has("Deku Mask", player) and 
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and 
                state.has("Ocarina of Time", player)
            ),
        "Milk Bar Priority Mail to Aroma":
            lambda state: (
                state.has("Romani Mask", player) and 
                state.has("Kafei's Mask", player) and 
                state.has("Priority Mail", player)
            ),
        "East Clock Town Milk Bar Milk Purchase":
            lambda state: (
                state.has("Romani Mask", player) and 
                can_afford_price(state, player, 40)
            ),
        "East Clock Town Milk Bar Chateau Romani Purchase":
            lambda state: (
                state.has("Romani Mask", player) and 
                can_afford_price(state, player, 200)
            ),
        
        "West Clock Town Swordsman Expert Course":
            lambda state: state.has("Progressive Sword", player),
        "West Clock Town Postman Counting":
            lambda state: state.has("Bunny Hood", player),
        "West Clock Town Dancing Sisters":
            lambda state: state.has("Kamaro Mask", player),
        "West Clock Town Bank 200 Rupees":
            lambda state: True,
        "West Clock Town Bank 500 Rupees":
            lambda state: state.has("Progressive Wallet", player),
        "West Clock Town Bank 1000 Rupees":
            lambda state: state.has("Progressive Wallet", player, 2),
        "West Clock Town Priority Mail to Postman":
            lambda state: state.has("Priority Mail", player),
        "Clock Town Trading Post Shop Item 1":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_1),
        "Clock Town Trading Post Shop Item 2":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_2),
        "Clock Town Trading Post Shop Item 3":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_3),
        "Clock Town Trading Post Shop Item 4":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_4),
        "Clock Town Trading Post Shop Item 5":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_5),
        "Clock Town Trading Post Shop Item 6":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_6),
        "Clock Town Trading Post Shop Item 7":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_7),
        "Clock Town Trading Post Shop Item 8":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_8),
        "Clock Town Trading Post Shop (Night) Item 1":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_1),
        "Clock Town Trading Post Shop (Night) Item 2":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_2),
        "Clock Town Trading Post Shop (Night) Item 3":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_3),
        "Clock Town Trading Post Shop (Night) Item 4":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_4),
        "Clock Town Trading Post Shop (Night) Item 5":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_5),
        "Clock Town Trading Post Shop (Night) Item 6":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_6),
        "Clock Town Trading Post Shop (Night) Item 7":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_7),
        "Clock Town Trading Post Shop (Night) Item 8":
            lambda state: can_purchase(state, player, SHOP_ID_TRADING_POST_NIGHT_8),
        "Clock Town Bomb Shop Item 1":
            lambda state: can_purchase(state, player, SHOP_ID_BOMB_SHOP_1),
        "Clock Town Bomb Shop Item 2":
            lambda state: can_purchase(state, player, SHOP_ID_BOMB_SHOP_2),
        "Clock Town Bomb Shop Item 3":
            lambda state: can_purchase(state, player, SHOP_ID_BOMB_SHOP_3),
        "Clock Town Bomb Shop Powder Keg Goron":
            lambda state: state.has("Goron Mask", player) and state.has("Powder Keg", player),
        "Clock Town Bomb Shop Item 3 (Stop Thief)":
            lambda state: (
                state.can_reach("North Clock Town Save Old Lady", 'Location', player) and 
                can_purchase(state, player, SHOP_ID_BOMB_SHOP_3_UPGRADE)
            ),
        "Curiosity Shop Blue Rupee Trade":
            lambda state: (
                has_bottle(state, player) and 
                (
                    state.has("Mask of Scents", player) or 
                    can_get_cow_milk(state, player)
                )
            ),
        "Curiosity Shop Red Rupee Trade":
            lambda state: has_bottle(state, player),
        "Curiosity Shop Purple Rupee Trade":
            lambda state: (
                has_bottle(state, player) and 
                state.can_reach("Stone Tower Temple Inverted Death Armos Maze Chest", 'Location', player)
            ),
        "Curiosity Shop Gold Rupee Trade":
            lambda state: (
                has_bottle(state, player) and 
                (
                    (
                        state.can_reach("Graveyard Day 3 Dampe Big Poe Chest", 'Location', player) or 
                        (
                            state.can_reach("Ikana Well Rightside Torch Chest", 'Location', player) and 
                            state.has("Progressive Bomb Bag", player)
                        )
                    ) or 
                    (
                        state.has("Romani Mask", player) and 
                        can_afford_price(state, player, 200)
                    ) or 
                    state.can_reach("Goron Racetrack Prize", 'Location', player)
                )
            ),
        "Curiosity Shop Night 3 (Stop Thief)":
            lambda state: (
                can_purchase(state, player, SHOP_ID_CURIOSITY_SHOP_MASK) and 
                state.can_reach("North Clock Town Save Old Lady", 'Location', player)
            ),
        "Curiosity Shop Night 3 Thief Stolen Item":
            lambda state: can_purchase(state, player, SHOP_ID_CURIOSITY_SHOP_BOMB_BAG),
        
        "Stock Pot Inn Midnight Meeting":
            lambda state: (
                state.has("Kafei's Mask", player) and 
                (
                    state.has("Deku Mask", player) or 
                    state.has("Room Key", player)
                )
            ),
        "Stock Pot Inn Upstairs Middle Room Chest":
            lambda state: state.has("Room Key", player),
        "Stock Pot Inn Midnight Toilet Hand":
            lambda state: has_paper(state, player),
        "Stock Pot Inn Granny Story #1":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Granny Story #2":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Anju and Kafei":
            lambda state: (
                state.has("Kafei's Mask", player) and 
                can_play_song("Epona's Song", state, player) and 
                state.has("Letter to Kafei", player) and 
                state.has("Pendant of Memories", player) and 
                state.has("Hookshot", player) and 
                (
                    state.has("Garo Mask", player) or 
                    state.has("Gibdo Mask", player)
                )
            ),
        
        "Laundry Pool Kafei's Request":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Curiosity Shop Salesman #1":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Curiosity Shop Salesman #2":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Musician":
            lambda state: True,

        "Termina Tall Grass Chest":
            lambda state: True,
        "Termina Tall Grass Grotto Chest":
            lambda state: True,
        "Termina Stump Chest":
            lambda state: (
                state.has("Hookshot", player) or 
                can_plant_beans(state, player)
            ),
        "Termina Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Termina Peahat Grotto Chest":
            lambda state: True,
        "Termina Dodongo Grotto Chest":
            lambda state: True,
        "Termina Bio Baba Grotto HP":
            lambda state: (
                (
                    has_explosives(state, player) or 
                    state.has("Goron Mask", player)
                ) and 
                state.has("Zora Mask", player)
            ),
        "Termina Northern Midnight Dancer":
            lambda state: (
                state.has("Ocarina of Time", player) and 
                state.has("Song of Healing", player)
            ),
        "Termina Gossip Stones HP":
            lambda state: (
                (
                    has_explosives(state, player) or 
                    state.has("Goron Mask", player)
                ) and 
                (
                    (
                        state.has("Deku Mask", player) and 
                        can_play_song("Sonata of Awakening", state, player)
                    ) or 
                    (
                        state.has("Goron Mask", player) and 
                        can_play_song("Goron Lullaby", state, player)
                    ) or 
                    (
                        state.has("Zora Mask", player) and 
                        can_play_song("New Wave Bossa Nova", state, player)
                    )
                )
            ),
        "Termina Moon's Tear Scrub HP":
            lambda state: (
                (
                    state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player) and 
                    state.has("Ocarina of Time", player) and 
                    can_afford_price(state, player, 100)
                ) or 
                (
                    state.has("Deku Mask", player) and 
                    state.has("Ocarina of Time", player) and 
                    can_afford_price(state, player, 100)
                )
            ),
        "Termina Log Bombable Grotto Left Cow":
            lambda state: (
                has_explosives(state, player) and 
                can_play_song("Epona's Song", state, player)
            ),
        "Termina Log Bombable Grotto Right Cow":
            lambda state: (
                has_explosives(state, player) and 
                can_play_song("Epona's Song", state, player)
            ),

        "Milk Road Gorman Ranch Race":
            lambda state: (
                state.has("Ocarina of Time", player) and 
                state.has("Epona's Song", player)
            ),
        "Milk Road Gorman Ranch Purchase":
            lambda state: True,
        "Tingle Romani Ranch Map Purchase":
            lambda state: (
                has_projectiles(state, player) or 
                (
                    state.can_reach("Milk Road", 'Region', player) or 
                    state.can_reach("Twin Islands", 'Region', player)
                )
            ),
            
        "Road to Swamp Tree HP":
            lambda state: has_projectiles(state, player),
        "Tingle Woodfall Map Purchase":
            lambda state: (
                has_projectiles(state, player) or 
                (
                    state.can_reach("Southern Swamp", 'Region', player) or 
                    state.can_reach("Clock Town", 'Region', player)
                )
            ),
        "Swamp Shooting Gallery 2120 Points":
            lambda state: state.has("Progressive Bow", player),
        "Swamp Shooting Gallery 2180 Points":
            lambda state: state.has("Progressive Bow", player),

        "Southern Swamp Deku Scrub Purchase Beans":
            lambda state: (
                (
                    state.has("Deku Mask", player) and 
                    can_plant_beans(state, player)
                ) or 
                (
                    state.has("Land Title Deed", player) and 
                    state.has("Moon's Tear", player) and 
                    can_plant_beans(state, player)
                )
            ),
        "Southern Swamp Deku Trade":
            lambda state: state.has("Land Title Deed", player),
        "Southern Swamp Deku Trade Freestanding HP":
            lambda state: (
                state.has("Land Title Deed", player) and 
                state.has("Deku Mask", player)
            ),
        "Southern Swamp Tour Witch Gift":
            lambda state: has_bottle(state, player),
        "Southern Swamp Tour Guide Winning Picture":
            lambda state: state.has("Pictograph Box", player),
        "Southern Swamp Tour Guide Good Picture":
            lambda state: state.has("Pictograph Box", player),
        "Southern Swamp Tour Guide Okay Picture":
            lambda state: state.has("Pictograph Box", player),
        "Southern Swamp Near Swamp Spider House Grotto Chest":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp Song Tablet":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp Mystery Woods Day 2 Grotto Chest":
            lambda state: True,
        "Southern Swamp Witch Shop Item 1":
            lambda state: (
                state.has("Mask of Scents", player) and 
                has_bottle(state, player) and 
                can_purchase(state, player, SHOP_ID_WITCH_POTION_1)
            ),
        "Southern Swamp Witch Shop Item 2":
            lambda state: can_purchase(state, player, SHOP_ID_WITCH_POTION_2),
        "Southern Swamp Witch Shop Item 3":
            lambda state: can_purchase(state, player, SHOP_ID_WITCH_POTION_3),

        "Swamp Spider House First Room Pot Near Entrance Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House First Room Crawling In Water Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House First Room Crawling Right Column Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House First Room Crawling Left Column Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House First Room Against Far Wall Token":
            lambda state: (
                (
                    can_bring_to_player(state, player) and 
                    has_projectiles(state, player)
                ) or 
                (
                    state.has("Deku Mask", player) and 
                    state.has("Progressive Magic", player)
                ) or 
                (
                    state.has("Deku Mask", player) and 
                    state.has("Progressive Bow", player)
                )
            ),
        "Swamp Spider House First Room Lower Left Bugpatch Token":
            lambda state: (
                can_smack(state, player) and 
                has_bottle(state, player)
            ),
        "Swamp Spider House First Room Lower Right Bugpatch Token":
            lambda state: (
                can_smack(state, player) and 
                has_bottle(state, player)
            ),
        "Swamp Spider House First Room Upper Right Bugpatch Token":
            lambda state: (
                can_smack(state, player) and 
                has_bottle(state, player)
            ),
        "Swamp Spider House Monument Room Left Crate Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Monument Room Right Crate Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Monument Room Crawling Wall Token":
            lambda state: (
                can_bring_to_player(state, player) or 
                (
                    can_smack(state, player) and 
                    can_plant_beans(state, player) and 
                    (
                        has_explosives(state, player) or 
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Swamp Spider House Monument Room Crawling On Monument Token":
            lambda state: (
                can_smack(state, player) and 
                can_bring_to_player(state, player) and 
                has_projectiles(state, player)
            ),
        "Swamp Spider House Monument Room Behind Torch Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Beehive #1 Token":
            lambda state: (
                can_smack(state, player) and 
                has_projectiles(state, player)
            ),
        "Swamp Spider House Pottery Room Beehive #2 Token":
            lambda state: (
                can_smack(state, player) and 
                has_projectiles(state, player)
            ),
        "Swamp Spider House Pottery Room Small Pot Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Left Large Pot Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Right Large Pot Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Behind Vines Token":
            lambda state: (
                state.has("Progressive Sword", player) or 
                state.has("Great Fairy Sword", player) or 
                state.has("Fierce Deity's Mask", player)
            ),
        "Swamp Spider House Pottery Room Upper Wall Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Golden Room Crawling Left Wall Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Golden Room Crawling Right Column Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Golden Room Against Far Wall Token":
            lambda state: (
                can_smack(state, player) and 
                (
                    can_bring_to_player(state, player) or 
                    can_plant_beans(state, player)
                )
            ),
        "Swamp Spider House Golden Room Beehive Token":
            lambda state: (
                can_smack(state, player) and 
                has_projectiles(state, player)
            ),
        "Swamp Spider House Tree Room Tall Grass #1 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tall Grass #2 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tree #1 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tree #2 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tree #3 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Beehive Token":
            lambda state: (
                can_smack(state, player) and 
                has_projectiles(state, player)
            ),
        "Swamp Spider House Reward":
            lambda state: state.has("Swamp Skulltula Token", player, 30),

        "Deku Palace Bean Seller":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Chest":
            lambda state: (
                can_plant_beans(state, player) or 
                state.has("Hookshot", player)
            ),
        "Deku Palace Monkey Song":
            lambda state: (
                state.has("Ocarina of Time", player) and 
                can_plant_beans(state, player) and 
                state.has("Deku Mask", player)
            ),
        "Deku Palace Butler Race":
            lambda state: (
                can_clear_woodfall(state, player) and 
                has_bottle(state, player) and 
                (
                    state.has("Progressive Sword", player) or 
                    state.has("Great Fairy Sword", player) or 
                    state.has("Fierce Deity's Mask", player)
                )
            ),

        "Woodfall Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Woodfall)", player, 15),
        "Woodfall Near Owl Statue Chest":
            lambda state: state.has("Deku Mask", player),
        "Woodfall After Great Fairy Cave Chest":
            lambda state: state.has("Deku Mask", player),
        "Woodfall Near Swamp Entrance Chest":
            lambda state: state.has("Deku Mask", player),

        "Woodfall Temple Dragonfly Chest":
            lambda state: (
                state.has("Small Key (Woodfall)", player) or 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Black Boe Room Chest":
            lambda state: (
                state.has("Small Key (Woodfall)", player) or 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Wooden Flower Switch Chest":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Dinolfos Chest":
            lambda state: (
                (
                    state.has("Small Key (Woodfall)", player) and 
                    can_smack(state, player)
                ) or 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Boss Key Chest":
            lambda state: (
                state.has("Progressive Bow", player) and 
                can_smack(state, player)
            ),
        "Woodfall Temple Wooden Flower Bubble SF":
            lambda state: (
                (
                    state.has("Progressive Bow", player) and 
                    state.has("Great Fairy Mask", player)
                ) or 
                can_use_fire_arrows(state, player)
            ),
        "Woodfall Temple Moving Flower Platform Room Beehive SF":
            lambda state: (
                (
                    state.has("Progressive Bow", player) or 
                    (
                        state.has("Deku Mask", player) and 
                        state.has("Progressive Magic", player)
                    )
                ) or 
                (
                    state.has("Great Fairy Mask", player) and 
                    (
                        state.has("Hookshot", player) or 
                        state.has("Zora Mask", player)
                    )
                )
            ),
        "Woodfall Temple Push Block Skulltula SF":
            lambda state: (
                (
                    state.has("Small Key (Woodfall)", player) and 
                    can_smack(state, player)
                ) or 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Push Block Bubble SF":
            lambda state: (
                state.has("Great Fairy Mask", player) and 
                (
                    (
                        state.has("Small Key (Woodfall)", player) and 
                        has_projectiles(state, player)
                    ) or 
                    state.has("Progressive Bow", player)
                )
            ),
        "Woodfall Temple Push Block Beehive SF":
            lambda state: (
                state.has("Great Fairy Mask", player) and 
                (
                    (
                        state.has("Small Key (Woodfall)", player) and 
                        has_projectiles(state, player)
                    ) or 
                    state.has("Progressive Bow", player)
                )
            ),
        "Woodfall Temple Final Room Right Lower Platform SF":
            lambda state: (
                state.has("Progressive Bow", player) or 
                can_use_fire_arrows(state, player)
            ),
        "Woodfall Temple Final Room Right Upper Platform SF":
            lambda state: (
                state.has("Progressive Bow", player) or 
                can_use_fire_arrows(state, player)
            ),
        "Woodfall Temple Final Room Left Upper Platform SF":
            lambda state: (
                state.has("Progressive Bow", player) or 
                can_use_fire_arrows(state, player)
            ),
        "Woodfall Temple Final Room Bubble SF":
            lambda state: (
                state.has("Progressive Bow", player) or 
                can_use_fire_arrows(state, player)
            ),
        "Woodfall Temple Heart Container":
            lambda state: (
                can_smack(state, player) and 
                state.has("Progressive Bow", player) and 
                (
                    state.has("Boss Key (Woodfall)", player) or 
                    (
                        state.has("Odolwa's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Woodfall Temple Odolwa's Remains":
            lambda state: (
                can_smack(state, player) and 
                state.has("Progressive Bow", player) and 
                (
                    state.has("Boss Key (Woodfall)", player) or 
                    (
                        state.has("Odolwa's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
            
        "Tour Witch Target Shooting":
            lambda state: (
                can_clear_woodfall(state, player) and 
                has_bottle(state, player) and 
                state.has("Progressive Bow", player)
            ),
            
        "Mountain Village Invisible Ladder Cave Healing Invisible Goron":
            lambda state: (
                can_use_lens(state, player) and 
                can_play_song("Song of Healing", state, player)
            ),
        "Mountain Village Feeding Freezing Goron":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                (
                    can_play_song("Goron Lullaby", state, player) or 
                    can_use_fire_arrows(state, player)
                )
            ),
        "Mountain Village Spring Waterfall Chest":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Ramp Grotto":
            lambda state: can_clear_snowhead(state, player),
        "Don Gero Mask Frog Song HP":
            lambda state: (
                state.has("Don Gero Mask", player) and 
                can_clear_snowhead(state, player) and 
                state.can_reach("Woodfall Temple Boss Key Chest", 'Location', player) and 
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Mountain Village Smithy Upgrade":
            lambda state: (
                can_afford_price(state, player, 100) and 
                (
                    can_use_fire_arrows(state, player) or 
                    state.can_reach("Twin Islands Hot Water Grotto Chest", 'Location', player) or 
                    can_clear_snowhead(state, player)
                )
            ),
        "Mountain Village Smithy Gold Dust Upgrade":
            lambda state: (
                state.can_reach("Mountain Village Smithy Upgrade", 'Location', player) and 
                state.can_reach("Goron Racetrack Prize", 'Location', player) and 
                has_bottle(state, player)
            ),
            
        "Tingle Snowhead Map Purchase":
            lambda state: (
                has_projectiles(state, player) and 
                (
                    state.can_reach("Twin Islands", 'Region', player) or 
                    state.can_reach("Southern Swamp", 'Region', player)
                )
            ),
        "Twin Islands Ramp Grotto Chest":
            lambda state: (
                has_explosives(state, player) and 
                (
                    state.has("Goron Mask", player) or 
                    state.has("Hookshot", player)
                )
            ),
        "Twin Islands Goron Elder Request":
            lambda state: (
                state.has("Goron Mask", player) and 
                (
                    can_use_fire_arrows(state, player) or 
                    (
                        (
                            state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) or 
                            (
                                state.can_reach("Ikana Well Invisible Chest", 'Location', player) and 
                                can_play_song("Song of Soaring", state, player)
                            )
                        ) and 
                        has_bottle(state, player)
                    )
                )
            ),
        "Twin Islands Hot Water Grotto Chest":
            lambda state: (
                (
                    has_explosives(state, player) and 
                    can_use_fire_arrows(state, player)
                ) or 
                (
                    state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and 
                    has_bottle(state, player) and 
                    state.has("Goron Mask", player) and 
                    has_explosives(state, player)
                ) or 
                (
                    can_clear_snowhead(state, player) or 
                    (
                        state.can_reach("Ikana Well Invisible Chest", 'Location', player) and 
                        can_play_song("Song of Soaring", state, player)
                    )
                )
            ),
        "Twin Islands Spring Underwater Cave Chest":
            lambda state: (
                state.has("Zora Mask", player) and 
                can_clear_snowhead(state, player)
            ),
        "Twin Islands Spring Underwater Near Ramp Chest":
            lambda state: (
                state.has("Zora Mask", player) and 
                can_clear_snowhead(state, player)
            ),
        "Goron Racetrack Prize":
            lambda state: (
                (
                    can_use_powder_keg(state, player) or 
                    state.can_reach("Powder Keg Goron Reward", 'Location', player)
                ) and 
                can_clear_snowhead(state, player)
            ),
            
        "Goron Village Lens Cave Rock Chest":
            lambda state: has_explosives(state, player),
        "Goron Village Lens Cave Invisible Chest":
            lambda state: True,
        "Goron Village Lens Cave Center Chest":
            lambda state: True,
        "Goron Village Deku Scrub Purchase Bomb Bag":
            lambda state: (
                can_afford_price(state, player, 200) and 
                (
                    state.has("Goron Mask", player) or 
                    (
                        state.can_reach("Goron Village Deku Trade Freestanding HP", 'Location', player) and 
                        state.can_reach("Southern Swamp Deku Trade Freestanding HP", 'Location', player) and 
                        state.has("Moon's Tear", player)
                    )
                )
            ),
        "Goron Village Deku Trade":
            lambda state: (
                state.has("Deku Mask", player) and 
                state.has("Swamp Title Deed", player)
            ),
        "Goron Village Deku Trade Freestanding HP":
            lambda state: (
                state.can_reach("Goron Village Deku Trade", 'Location', player)
            ),
        "Powder Keg Goron Reward":
            lambda state: (
                can_clear_snowhead(state, player) or 
                (
                    can_use_fire_arrows(state, player) and 
                    state.has("Goron Mask", player)
                )
            ),
        "Goron Village Baby Goron Lullaby":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_play_song("Goron Lullaby", state, player)
            ),
        "Goron Village Shop Item 1":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_purchase(state, player, SHOP_ID_GORON_SHOP_1)
            ),
        "Goron Village Shop Item 2":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_purchase(state, player, SHOP_ID_GORON_SHOP_2)
            ),
        "Goron Village Shop Item 3":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_purchase(state, player, SHOP_ID_GORON_SHOP_3)
            ),
        "Goron Village Shop (Spring) Item 1":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_purchase(state, player, SHOP_ID_GORON_SHOP_SPRING_1) and 
                can_clear_snowhead(state, player)
            ),
        "Goron Village Shop (Spring) Item 2":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_purchase(state, player, SHOP_ID_GORON_SHOP_SPRING_2) and 
                can_clear_snowhead(state, player)
            ),
        "Goron Village Shop (Spring) Item 3":
            lambda state: (
                state.has("Goron Mask", player) and 
                can_purchase(state, player, SHOP_ID_GORON_SHOP_SPRING_3) and 
                can_clear_snowhead(state, player)
            ),
        "Goron Village Deku Trade Freestanding HP (Spring)":
            lambda state: (
                can_clear_snowhead(state, player) and 
                state.has("Deku Mask", player) and 
                state.has("Swamp Title Deed", player)
            ),

        "Path to Snowhead Grotto Chest":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path to Snowhead Scarecrow Pillar HP":
            lambda state: (
                can_reach_scarecrow(state, player) and 
                state.has("Goron Mask", player) and 
                can_use_lens(state, player) and 
                state.has("Hookshot", player)
            ),
            
        "Snowhead Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Snowhead)", player, 15),
            
        "Snowhead Temple Initial Runway Under Platform Bubble SF":
            lambda state: (
                state.has("Progressive Bow", player) and 
                state.has("Great Fairy Mask", player)
            ),
        "Snowhead Temple Initial Runway Tower Bubble SF":
            lambda state: (
                state.has("Progressive Bow", player) and 
                state.has("Great Fairy Mask", player)
            ),
        "Snowhead Temple Grey Door Near Bombable Stairs Box SF":
            lambda state: (
                (
                    state.has("Small Key (Snowhead)", player) and 
                    state.has("Great Fairy Mask", player) and 
                    has_explosives(state, player)
                ) or 
                (
                    state.has("Hookshot", player) and 
                    state.can_reach("Snowhead Temple Initial Runway Tower Bubble SF", 'Location', player) and 
                    has_explosives(state, player)
                )
            ),
        "Snowhead Temple Timed Switch Room Bubble SF":
            lambda state: (
                (
                    state.has("Small Key (Snowhead)", player, 2) and 
                    state.has("Great Fairy Mask", player) and 
                    state.has("Progressive Bow", player) and 
                    can_use_lens(state, player) and 
                    has_explosives(state, player)
                ) or 
                (
                    can_reach_scarecrow(state, player) and 
                    state.has("Hookshot", player) and 
                    state.has("Great Fairy Mask", player) and 
                    state.has("Progressive Bow", player) and 
                    can_use_lens(state, player)
                ) or 
                (
                    can_use_fire_arrows(state, player) and 
                    state.has("Great Fairy's Mask", player) and 
                    can_use_lens(state, player)
                )
            ),
        "Snowhead Temple Snowmen Bubble SF":
            lambda state: (
                state.has("Small Key (Snowhead)", player) and 
                can_use_fire_arrows(state, player) and 
                state.has("Great Fairy Mask", player)
            ),
        "Snowhead Temple Dinolfos Room First SF":
            lambda state: (
                state.has("Small Key (Snowhead)", player) and 
                can_use_fire_arrows(state, player)
            ),
        "Snowhead Temple Dinolfos Room Second SF":
            lambda state: (
                state.has("Small Key (Snowhead)", player) and 
                can_use_fire_arrows(state, player)
            ),
        "Snowhead Temple Initial Runway Ice Blowers Chest":
            lambda state: (
                can_use_fire_arrows(state, player) or 
                state.has("Hookshot", player)
            ),
        "Snowhead Temple Green Door Ice Blowers Chest":
            lambda state: can_use_fire_arrows(state, player),
        "Snowhead Temple Orange Door Upper Chest":
            lambda state: (
                state.has("Hookshot", player) or 
                (
                    state.has("Small Key (Snowhead)", player) and 
                    can_use_fire_arrows(state, player)
                )
            ),
        "Snowhead Temple Orange Door Behind Block Chest":
            lambda state: True,
        "Snowhead Temple Light Blue Door Center Chest":
            lambda state: (
                state.has("Small Key (Snowhead)", player) or 
                state.has("Hookshot", player)
            ),
        "Snowhead Temple Light Blue Door Upper Chest":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player) or 
                    state.has("Hookshot", player)
                )
            ),
        "Snowhead Temple Upstairs 2F Icicle Room Hidden Chest":
            lambda state: (
                can_use_lens(state, player) and 
                has_explosives(state, player) and 
                state.has("Progressive Bow", player) and 
                (
                    state.has("Small Key (Snowhead)", player) or 
                    state.has("Hookshot", player)
                )
            ),
        "Snowhead Temple Upstairs 2F Icicle Room Snowball Chest":
            lambda state: (
                has_explosives(state, player) and 
                (
                    (
                        state.has("Small Key (Snowhead)", player) and 
                        state.has("Progressive Bow", player)
                    ) or 
                    state.has("Hookshot", player)
                )
            ),
        "Snowhead Temple Elevator Room Invisible Platform Chest":
            lambda state: (
                (
                    can_use_lens(state, player) and 
                    state.has("Small Key (Snowhead)", player, 2) and 
                    has_explosives(state, player)
                ) or 
                (
                    can_use_lens(state, player) and 
                    can_use_fire_arrows(state, player)
                ) or 
                (
                    can_use_lens(state, player) and 
                    state.has("Hookshot", player)
                )
            ),
        "Snowhead Temple Elevator Room Lower Chest":
            lambda state: True,
        "Snowhead Temple 1st Wizzrobe Chest":
            lambda state: (
                (
                    state.has("Small Key (Snowhead)", player, 2) and 
                    has_explosives(state, player)
                ) or 
                can_use_fire_arrows(state, player)
            ),
        "Snowhead Temple Column Room 2F Hidden Chest":
            lambda state: (
                (
                    state.has("Small Key (Snowhead)", player, 3) and 
                    can_use_fire_arrows(state, player) and 
                    can_use_lens(state, player) and 
                    has_explosives(state, player) and 
                    state.has("Deku Mask", player)
                ) or 
                (
                    can_use_fire_arrows(state, player) and 
                    can_reach_scarecrow(state, player) and 
                    state.has("Hookshot", player) and 
                    can_use_lens(state, player)
                )
            ),
        "Snowhead Temple 2nd Wizzrobe Chest":
            lambda state: (
                (
                    state.has("Small Key (Snowhead)", player, 3) and 
                    can_use_fire_arrows(state, player) and 
                    has_explosives(state, player)
                ) or 
                (
                    state.has("Small Key (Snowhead)", player, 1) and 
                    can_use_fire_arrows(state, player) and 
                    state.has("Deku Mask", player)
                )
            ),
        "Snowhead Temple Heart Container":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    (
                        state.has("Small Key (Snowhead)", player, 1) and 
                        state.has("Boss Key (Snowhead)", player)
                    ) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Snowhead Temple Goht's Remains":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    (
                        state.has("Small Key (Snowhead)", player, 1) and 
                        state.has("Boss Key (Snowhead)", player)
                    ) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),

        "Romani Ranch Bremen Mask March Baby Cuccos":
            lambda state: state.has("Bremen Mask", player),
        "Romani Ranch Helping Cremia":
            lambda state: (
                can_use_powder_keg(state, player) and 
                state.has("Progressive Bow", player)
            ),
        "Romani Ranch Doggy Racetrack Rooftop Chest":
            lambda state: (
                state.has("Hookshot", player) or 
                can_plant_beans(state, player) or 
                state.has("Zora Mask", player)
            ),
        "Romani Ranch Doggy Race":
            lambda state: state.has("Mask of Truth", player),
        "Romani Ranch Romani Game":
            lambda state: (
                can_use_powder_keg(state, player) and 
                state.has("Progressive Bow", player)
            ),
        "Romani Ranch Defended Against Aliens":
            lambda state: (
                can_use_powder_keg(state, player) and 
                state.has("Progressive Bow", player)
            ),
        "Romani Ranch Barn Free Cow":
            lambda state: (
                can_use_powder_keg(state, player) and 
                can_play_song("Epona's Song", state, player)
            ),
        "Romani Ranch Barn Stables Front Cow":
            lambda state: (
                can_use_powder_keg(state, player) and 
                can_play_song("Epona's Song", state, player)
            ),
        "Romani Ranch Barn Stables Back Cow":
            lambda state: (
                can_use_powder_keg(state, player) and 
                can_play_song("Epona's Song", state, player)
            ),

        "Great Bay Healing Zora":
            lambda state: can_play_song("Song of Healing", state, player),
        "Great Bay Scarecrow Ledge HP":
            lambda state: (
                can_plant_beans(state, player) and 
                can_reach_scarecrow(state, player) and 
                state.has("Hookshot", player)
            ),
        "Tingle Great Bay Map Purchase":
            lambda state: (
                has_projectiles(state, player) and 
                (
                    state.can_reach("Great Bay", 'Region', player) or 
                    state.can_reach("Milk Road", 'Region', player)
                )
            ),
        "Great Bay Ledge Grotto Left Cow":
            lambda state: (
                state.has("Hookshot", player) and 
                can_play_song("Epona's Song", state, player)
            ),
        "Great Bay Ledge Grotto Right Cow":
            lambda state: (
                state.has("Hookshot", player) and 
                can_play_song("Epona's Song", state, player)
            ),
        "Pinnacle Rock HP":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Upper Eel Chest":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Lower Eel Chest":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Great Bay Marine Research Lab Zora Egg Delivery Song":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player, 3) and 
                state.can_reach("Pirates' Fortress Leader's Room Chest", "Location", player)
            ),
        "Great Bay Marine Research Lab Feeding Fish":
            lambda state: has_bottle(state, player),
        "Great Bay (Cleared) Fisherman Island Game HP":
            lambda state: can_clear_greatbay(state, player),
        
        "Ocean Spider House Ramp Upper Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Ramp Lower Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Lobby Ceiling Token":
            lambda state: (
                state.has("Hookshot", player) and 
                can_use_fire_arrows(state, player)
            ),
        "Ocean Spider House First Room Rafter Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Open Pot #1 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Open Pot #2 Token":
            lambda state: (
                state.has("Hookshot", player) and 
                can_use_fire_arrows(state, player)
            ),
        "Ocean Spider House First Room Wall Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Top Bookcase Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Passage Behind Bookcase Front Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Passage Behind Bookcase Rear Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Libary Painting #1 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Painting #2 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Rafter Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Bookshelf Hole Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Rafter Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Open Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Behind Staircase Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Crate Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Wall Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Open Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Painting Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Ceiling Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Chandelier #1 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Chandelier #2 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Chandelier #3 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Web Token":
            lambda state: (
                state.has("Hookshot", player) and 
                can_use_fire_arrows(state, player)
            ),
        "Ocean Spider House Storage Room North Wall Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Crate Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Hidden Hole Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Ceiling Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Coloured Mask Sequence HP":
            lambda state: (
                state.has("Hookshot", player) and 
                state.has("Captain's Hat", player) and 
                state.has("Progressive Bow", player)
            ),
        "Ocean Spider House Reward":
            lambda state: state.has("Ocean Skulltula Token", player, 30),
        
        "Pirates' Fortress Exterior Underwater Log Chest":
            lambda state: state.has("Zora Mask", player),
        "Pirates' Fortress Exterior Underwater Near Entrance Chest":
            lambda state: state.has("Zora Mask", player),
        "Pirates' Fortress Exterior Underwater Corner Near Fortress Chest":
            lambda state: state.has("Zora Mask", player),
        
        "Pirates' Fortress Sewers Push Block Maze Chest":
            lambda state: state.has("Goron Mask", player),
        "Pirates' Fortress Sewers Cage HP":
            lambda state: state.has("Goron Mask", player),
        "Pirates' Fortress Sewers Underwater Upper Chest":
            lambda state: state.has("Goron Mask", player),
        "Pirates' Fortress Sewers Underwater Lower Chest":
            lambda state: state.has("Goron Mask", player),
        
        "Pirates' Fortress Hub Lower Chest":
            lambda state: True,
        "Pirates' Fortress Hub Upper Chest":
            lambda state: state.has("Hookshot", player),
        "Pirates' Fortress Leader's Room Chest":
            lambda state: (
                (
                    state.has("Hookshot", player) or 
                    state.has("Goron Mask", player)
                ) and 
                (
                    state.has("Progressive Bow", player) or 
                    (
                        state.has("Deku Mask", player) and 
                        state.has("Progressive Magic", player)
                    )
                )
            ),
        "Pirates' Fortress Near Egg Chest":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        "Pirates' Fortress Pirates Surrounding Chest":
            lambda state: state.has("Hookshot", player),
            
        "Zora Cape Near Great Fairy Grotto Chest":
            lambda state: (
                state.has("Goron Mask", player) or 
                has_explosives(state, player)
            ),
        "Zora Cape Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Underwater Like-Like HP":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Pot Game Silver Rupee":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Upper Chest":
            lambda state: state.has("Hookshot", player),
        "Zora Cape Tree Chest":
            lambda state: (
                state.has("Hookshot", player) and 
                state.has("Deku Mask", player)
            ),
        "Beaver Bros. Race Bottle Reward":
            lambda state: (
                state.has("Hookshot", player) and 
                state.has("Zora Mask", player)
            ),
        "Beaver Bros. Race HP":
            lambda state: (
                state.has("Hookshot", player) and 
                state.has("Zora Mask", player)
            ),
            
        "Zora Hall Piano Zora Song":
            lambda state: state.has("Zora Mask", player),
        "Zora Hall Torches Reward":
            lambda state: (
                state.has("Zora Mask", player) and 
                can_use_fire_arrows(state, player)
            ),
        "Zora Hall Good Picture of Lulu":
           lambda state: (
               state.has("Pictograph Box", player) and 
               state.has("Zora Mask", player)
           ),
        "Zora Hall Bad Picture of Lulu":
           lambda state: (
               state.has("Pictograph Box", player) and 
               state.has("Zora Mask", player)
           ),
        "Zora Hall Deku Scrub Purchase Green Potion":
            lambda state: (
                state.has("Zora Mask", player) and 
                has_bottle(state, player)
            ),
        "Zora Hall Goron Scrub Trade":
            lambda state: (
                state.has("Zora Mask", player) and 
                state.has("Mountain Title Deed", player) and 
                state.has("Goron Mask", player)
            ),
        "Zora Hall Goron Scrub Trade Freestanding HP":
            lambda state: (
                state.has("Deku Mask", player) and 
                state.can_reach("Zora Hall Goron Scrub Trade", 'Location', player)
            ),
        "Zora Hall Shop Item 1":
            lambda state: (
                state.has("Zora Mask", player) and 
                can_purchase(state, player, SHOP_ID_ZORA_SHOP_1)
            ),
        "Zora Hall Shop Item 2":
            lambda state: (
                state.has("Zora Mask", player) and 
                can_purchase(state, player, SHOP_ID_ZORA_SHOP_2)
            ),
        "Zora Hall Shop Item 3":
            lambda state: (
                state.has("Zora Mask", player) and 
                can_purchase(state, player, SHOP_ID_ZORA_SHOP_3)
            ),

        "Great Bay Great Fairy Reward":
            lambda state: (
                state.has("Stray Fairy (Great Bay)", player, 15) and 
                state.has("Hookshot", player)
            ),
            
        "Great Bay Temple Four Torches Chest":
            lambda state: True,
        "Great Bay Temple Waterwheel Room Skulltula SF":
            lambda state: can_smack_hard(state, player),
        "Great Bay Temple Waterwheel Room Bubble Under Platform SF":
            lambda state: (
                state.has("Zora Mask", player) or 
                (
                    has_projectiles(state, player) and 
                    state.has("Great Fairy Mask", player)
                )
            ),
        "Great Bay Temple Blender Room Barrel SF":
            lambda state: True,
        "Great Bay Temple Pot At Bottom Of Blender SF":
            lambda state: True,
        "Great Bay Temple Red-Green Pipe First Room Chest":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Red-Green Pipe First Room Pot SF":
            lambda state: (
                can_use_ice_arrows(state, player) or 
                (
                    has_projectiles(state, player) and 
                    state.has("Great Fairy Mask", player)
                ) or 
                state.has("Deku Mask", player)
            ),
        "Great Bay Temple Bio-Baba Hall Chest":
            lambda state: True,
        "Great Bay Temple Froggy Entrance Room Pot SF":
            lambda state: True,
        "Great Bay Temple Froggy Entrance Room Upper Chest":
            lambda state: True,
        "Great Bay Temple Froggy Entrance Room Caged Chest":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Froggy Entrance Room Underwater Chest":
            lambda state: True,
        "Great Bay Temple Behind Locked Door Chest":
            lambda state: (
                (
                    state.has("Small Key (Great Bay)", player) and 
                    can_smack_hard(state, player)
                ) or 
                (
                    state.has("Small Key (Great Bay)", player) and 
                    has_explosives(state, player)
                ) or 
                (
                    state.has("Small Key (Great Bay)", player) and 
                    state.has("Progressive Bow", player)
                )
            ),
        "Great Bay Temple Room Behind Waterfall Ceiling Chest":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Green Pipe Freezable Waterwheel Upper Chest":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Freezable Waterwheel Lower Chest":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Seesaw Room Underwater Barrel SF":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Seesaw Room Chest":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Before Boss Room Underneath Platform Bubble SF":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Before Boss Room Exit Tunnel Bubble SF":
            lambda state: state.can_reach("Great Bay Temple Before Boss Room Underneath Platform Bubble SF", 'Location', player),
        "Great Bay Temple Heart Container":
            lambda state: (
                state.has("Hookshot", player) and 
                (
                    (
                        state.can_reach("Great Bay Temple Before Boss Room Underneath Platform Bubble SF", 'Location', player) and 
                        state.has("Boss Key (Great Bay)", player)
                    ) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg's Remains":
            lambda state: (
                state.has("Hookshot", player) and 
                (
                    (
                        state.can_reach("Great Bay Temple Before Boss Room Underneath Platform Bubble SF", 'Location', player) and 
                        state.has("Boss Key (Great Bay)", player)
                    ) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        
        "Road to Ikana Pillar Chest":
            lambda state: state.has("Hookshot", player),
        "Road to Ikana Rock Grotto Chest":
            lambda state: state.has("Goron Mask", player),
        "Road to Ikana Invisible Soldier":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Bottle of Red Potion", player) and 
                can_use_lens(state, player)
            ),
            
        "Ikana Graveyard Bombable Grotto Chest":
            lambda state: has_explosives(state, player),
        "Graveyard Day 1 Bats Chest":
            lambda state: (
                state.has("Captain's Hat", player) and 
                can_smack(state, player)
            ),
        "Graveyard Day 2 Dampe Bats":
            lambda state: has_projectiles(state, player),
        "Graveyard Day 2 Iron Knuckle Chest":
            lambda state: (
                state.has("Captain's Hat", player) and 
                can_smack_hard(state, player) and 
                has_explosives(state, player) and 
                can_use_lens(state, player)
            ),
        "Graveyard Day 3 Dampe Big Poe Chest":
            lambda state: (
                (
                    state.has("Captain's Hat", player) and 
                    state.has("Progressive Bow", player)
                ) or 
                (
                    state.has("Captain's Hat", player) and 
                    state.has("Zora Mask", player)
                )
            ),
        "Graveyard Sonata To Wake Sleeping Skeleton Chest":
            lambda state: (
                can_play_song("Sonata of Awakening", state, player) and 
                can_smack_hard(state, player)
            ),
        "Graveyard Day 1 Iron Knuckle Song":
            lambda state: (
                state.has("Captain's Hat", player) and 
                can_smack_hard(state, player)
            ),

        "Tingle Stone Tower Map Purchase":
            lambda state: (
                has_projectiles(state, player) and 
                (
                    (
                        state.can_reach("Ikana Canyon", 'Region', player) and 
                        can_use_ice_arrows(state, player) and 
                        state.has("Hookshot", player)
                    ) or 
                    state.can_reach("Great Bay", 'Region', player)
                )
            ),
        "Ikana Canyon Spirit House":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ikana Canyon Music Box Mummy":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                can_play_song("Song of Healing", state, player) and 
                can_play_song("Song of Storms", state, player)
            ),
        "Ikana Canyon Deku Scrub Purchase Blue Potion":
            lambda state: (
                has_bottle(state, player) and 
                can_afford_price(state, player, 100)
            ),
        "Ikana Canyon Zora Scrub Trade":
            lambda state: (
                state.has("Zora Mask", player) and 
                state.has("Ocean Title Deed", player)
            ),
        "Ikana Canyon Zora Trade Freestanding HP":
            lambda state: (
                state.has("Deku Mask", player) and 
                state.has("Zora Mask", player) and 
                state.has("Ocean Title Deed", player)
            ),
        "Ikana Canyon Grotto Chest":
            lambda state: True,

        "Stone Tower Great Fairy Reward":
            lambda state: (
                state.has("Stray Fairy (Stone Tower)", player, 15) and 
                can_use_ice_arrows(state, player)
            ),
            
        "Secret Shrine Left Chest":
            lambda state: (
                can_smack_hard(state, player) and 
                can_use_light_arrows(state, player)
            ),
        "Secret Shrine Middle-Left Chest":
            lambda state: (
                can_smack_hard(state, player) and 
                can_use_light_arrows(state, player)
            ),
        "Secret Shrine Middle-Right Chest":
            lambda state: (
                can_smack_hard(state, player) and 
                can_use_light_arrows(state, player)
            ),
        "Secret Shrine Right Chest":
            lambda state: (
                can_use_light_arrows(state, player) and 
                can_smack_hard(state, player)
            ),
        "Secret Shrine Center Chest":
            lambda state: (
                state.can_reach("Secret Shrine Left Chest", 'Location', player) and 
                state.can_reach("Secret Shrine Middle-Left Chest", 'Location', player) and 
                state.can_reach("Secret Shrine Middle-Right Chest", 'Location', player) and 
                state.can_reach("Secret Shrine Right Chest", 'Location', player)
            ),
            
        "Ikana Well Rightside Torch Chest":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Ikana Well Invisible Chest":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_afford_price(state, player, 100) or 
                    state.has("Mask of Scents", player)
                )
            ),
        "Ikana Well Final Chest":
            lambda state: (
                (
                    state.has("Gibdo Mask", player) and 
                    has_bottle(state, player) and 
                    can_plant_beans(state, player) and 
                    (
                        state.has("Progressive Bomb Bag", player) or 
                        (
                            state.has("Captain's Hat", player) and 
                            state.has("Progressive Bow", player)
                        )
                    )
                ) or 
                (
                    can_use_light_arrows(state, player) and 
                    can_use_fire_arrows(state, player)
                )
            ),
        "Ikana Well Cow":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_play_song("Epona's Song", state, player) and 
                    (
                        can_plant_beans(state, player) or 
                        can_use_light_arrows(state, player)
                    ) and 
                    (
                        (
                            can_play_song("Song of Soaring", state, player) and 
                            (
                                (
                                    state.can_reach("Twin Islands", 'Region', player) and 
                                    can_use_fire_arrows(state, player)
                                ) or 
                                (
                                    state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and 
                                    state.has("Goron Mask", player)
                                )
                            )
                        ) or 
                        state.can_reach("Ikana Well Invisible Chest", 'Location', player)
                    )
                )
            ),
            
        "Ikana Castle Pillar Freestanding HP":
            lambda state: (
                state.has("Deku Mask", player) and 
                can_use_lens(state, player) and 
                can_use_fire_arrows(state, player)
            ),
        "Ikana Castle King Song":
            lambda state: (
                (
                    state.has("Deku Mask", player) and 
                    can_use_lens(state, player) and 
                    can_use_fire_arrows(state, player) and 
                    state.has("Powder Keg", player) and 
                    state.has("Goron Mask", player) and 
                    has_mirror_shield(state, player)
                ) or 
                (
                    can_use_fire_arrows(state, player) and 
                    has_mirror_shield(state, player) and 
                    can_use_light_arrows(state, player)
                )
            ),

        "Stone Tower Inverted Outside Left Chest":
            lambda state: can_plant_beans(state, player),
        "Stone Tower Inverted Outside Middle Chest":
            lambda state: can_plant_beans(state, player),
        "Stone Tower Inverted Outside Right Chest":
            lambda state: can_plant_beans(state, player),
        
        "Stone Tower Temple Entrance Room Eye Switch Chest":
            lambda state: state.has("Progressive Bow", player),
        "Stone Tower Temple Entrance Room Lower Chest":
            lambda state: (
                state.has("Small Key (Stone Tower)", player, 4) and 
                state.has("Deku Mask", player) and 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Temple Armos Room Back Chest":
            lambda state: (
                (
                    has_explosives(state, player) and 
                    has_mirror_shield(state, player)
                ) or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Temple Armos Room Upper Chest":
            lambda state: state.has("Hookshot", player),
        "Stone Tower Temple Armos Room Lava Chest":
            lambda state: (
                (
                    has_explosives(state, player) and 
                    has_mirror_shield(state, player)
                ) or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Temple Eyegore Room Switch Chest":
            lambda state: can_use_light_arrows(state, player),
        "Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest":
            lambda state: (
                state.has("Small Key (Stone Tower)", player) or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Temple Eastern Water Room Underwater Chest":
            lambda state: can_use_light_arrows(state, player),
        "Stone Tower Temple Eastern Water Room Sun Block Chest":
            lambda state: (
                can_use_light_arrows(state, player) or 
                (
                    state.has("Small Key (Stone Tower)", player) and 
                    has_mirror_shield(state, player)
                )
            ),
        "Stone Tower Temple Mirror Room Sun Block Chest":
            lambda state: (
                (
                    state.has("Small Key (Stone Tower)", player, 2) and 
                    has_mirror_shield(state, player)
                ) or 
                (
                    can_use_light_arrows(state, player) and 
                    state.has("Small Key (Stone Tower)", player, 1)
                )
            ),
        "Stone Tower Temple Mirror Room Sun Face Chest":
            lambda state: (
                (
                    state.has("Small Key (Stone Tower)", player, 2) and 
                    has_mirror_shield(state, player)
                ) or 
                (
                    can_use_light_arrows(state, player) and 
                    state.has("Small Key (Stone Tower)", player, 1)
                )
            ),
        "Stone Tower Temple Air Gust Room Side Chest":
            lambda state: (
                (
                    state.has("Small Key (Stone Tower)", player, 2) and 
                    has_mirror_shield(state, player) and 
                    state.has("Deku Mask", player)
                ) or 
                (
                    can_use_light_arrows(state, player) and 
                    state.has("Small Key (Stone Tower)", player, 1) and 
                    state.has("Deku Mask", player)
                )
            ),
        "Stone Tower Temple Air Gust Room Goron Switch Chest":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and 
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Garo Master Chest":
            lambda state: (
                (
                    state.has("Small Key (Stone Tower)", player, 2) and 
                    has_mirror_shield(state, player) and 
                    state.has("Deku Mask", player) and 
                    can_smack_hard(state, player)
                ) or 
                (
                    can_use_light_arrows(state, player) and 
                    state.has("Small Key (Stone Tower)", player, 1) and 
                    can_smack_hard(state, player)
                )
            ),
        "Stone Tower Temple After Garo Upside Down Chest":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Stone Tower Temple Eyegore Chest":
            lambda state: state.can_reach("Stone Tower Temple Garo Master Chest", 'Location', player),
        "Stone Tower Temple Inverted Entrance Room Sun Face Chest":
            lambda state: can_use_light_arrows(state, player),
        "Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest":
            lambda state: (
                state.has("Deku Mask", player) and 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Temple Inverted Eastern Air Gust Room Ice Eye Switch Chest":
            lambda state: (
                can_use_light_arrows(state, player) and 
                state.has("Deku Mask", player) and 
                can_use_fire_arrows(state, player)
            ),
        "Stone Tower Temple Inverted Eastern Air Gust Room Hall Floor Switch Chest":
            lambda state: (
                can_use_light_arrows(state, player) and 
                state.has("Deku Mask", player)
            ),
        "Stone Tower Temple Inverted Wizzrobe Chest":
            lambda state: (
                can_use_light_arrows(state, player) and 
                state.has("Deku Mask", player) and 
                state.has("Small Key (Stone Tower)", player, 3)
            ),
        "Stone Tower Temple Inverted Death Armos Maze Chest":
            lambda state: state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player),
        "Stone Tower Temple Inverted Gomess Chest":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player) and 
                can_use_light_arrows(state, player) and 
                can_smack_hard(state, player)
            ),
        "Stone Tower Temple Inverted Eyegore Chest":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player) and 
                state.has("Small Key (Stone Tower)", player, 4)
            ),
        "Stone Tower Temple Inverted Heart Container":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player) and 
                (
                    state.has("Progressive Bow", player) or 
                    state.has("Fierce Deity's Mask", player) or 
                    (
                        state.has("Giant's Mask", player) and 
                        state.has("Progressive Magic", player) and 
                        state.has("Progressive Sword", player)
                    )
                ) and 
                (
                    state.has("Boss Key (Stone Tower)", player) or 
                    (
                        state.has("Twinmold's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Stone Tower Temple Inverted Twinmold's Remains":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player) and 
                (
                    state.has("Progressive Bow", player) or 
                    state.has("Fierce Deity's Mask", player) or 
                    (
                        state.has("Giant's Mask", player) and 
                        state.has("Progressive Magic", player) and 
                        state.has("Progressive Sword", player)
                    )
                ) and 
                (
                    state.has("Boss Key (Stone Tower)", player) or 
                    (
                        state.has("Twinmold's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),

        "Oath to Order":
            lambda state: (
                can_clear_woodfall(state, player) or 
                can_clear_snowhead(state, player) or 
                can_clear_greatbay(state, player) or 
                can_clear_stonetower(state, player)
            ),

        "Moon Deku Trial HP":
            lambda state: state.has("Deku Mask", player),
        "Moon Goron Trial HP":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player)
            ),
        "Moon Zora Trial HP":
            lambda state: state.has("Zora Mask", player),
        "Moon Link Trial Garo Master Chest":
            lambda state: (
                can_smack_hard(state, player) and 
                state.has("Hookshot", player)
            ),
        "Moon Link Trial Iron Knuckle Chest":
            lambda state: state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player),
        "Moon Link Trial HP":
            lambda state: (
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and 
                has_bombchus(state, player) and 
                state.has("Progressive Bow", player)
            ),
        "Moon Trade All Masks":
            lambda state: (
                state.can_reach("Moon Deku Trial HP", 'Location', player) and 
                state.can_reach("Moon Goron Trial HP", 'Location', player) and 
                state.can_reach("Moon Zora Trial HP", 'Location', player) and 
                state.can_reach("Moon Link Trial HP", 'Location', player) and 
                can_use_fire_arrows(state, player) and 
                state.has("Captain's Hat", player) and 
                state.has("Giant's Mask", player) and 
                state.has("All-Night Mask", player) and 
                state.has("Bunny Hood", player) and 
                state.has("Keaton Mask", player) and 
                state.has("Garo Mask", player) and 
                state.has("Romani Mask", player) and 
                state.has("Circus Leader's Mask", player) and 
                state.has("Postman's Hat", player) and 
                state.has("Couple's Mask", player) and 
                state.has("Great Fairy Mask", player) and 
                state.has("Gibdo Mask", player) and 
                state.has("Don Gero Mask", player) and 
                state.has("Kamaro Mask", player) and 
                state.has("Mask of Truth", player) and 
                state.has("Stone Mask", player) and 
                state.has("Bremen Mask", player) and 
                state.has("Blast Mask", player) and 
                state.has("Mask of Scents", player) and 
                state.has("Kafei's Mask", player)
            ),
        "Defeat Majora":
            lambda state: (
                can_smack_hard(state, player) and 
                (
                    (
                        (
                            state.has("Zora Mask", player) or 
                            has_mirror_shield(state, player)
                        ) and 
                        can_use_light_arrows(state, player)
                    ) or 
                    (
                        state.has("Fierce Deity's Mask", player) and 
                        state.has("Progressive Magic", player)
                    )
                ) and 
                has_enough_remains(state, player, options.majora_remains_required.value)
            ),

            # Grass Location Rules
        "North Clock Town Keaton Grass (1)":
            lambda state: True,
        "North Clock Town Keaton Grass (2)":
            lambda state: True,
        "North Clock Town Keaton Grass (3)":
            lambda state: True,
        "North Clock Town Keaton Grass (4)":
            lambda state: True,
        "North Clock Town Keaton Grass (5)":
            lambda state: True,
        "North Clock Town Keaton Grass (6)":
            lambda state: True,
        "North Clock Town Keaton Grass (7)":
            lambda state: True,
        "North Clock Town Keaton Grass (8)":
            lambda state: True,
        "North Clock Town Keaton Grass (9)":
            lambda state: True,
                                                                              
        # Termina Field Grass Group 0
        "Termina Field Grass Group 0 (0)":
            lambda state: True,
        "Termina Field Grass Group 0 (1)":
            lambda state: True,
        "Termina Field Grass Group 0 (2)":
            lambda state: True,
        "Termina Field Grass Group 0 (3)":
            lambda state: True,
        "Termina Field Grass Group 0 (4)":
            lambda state: True,
        "Termina Field Grass Group 0 (5)":
            lambda state: True,
        "Termina Field Grass Group 0 (6)":
            lambda state: True,
        "Termina Field Grass Group 0 (7)":
            lambda state: True,
        "Termina Field Grass Group 0 (8)":
            lambda state: True,
        "Termina Field Grass Group 0 (9)":
            lambda state: True,
        "Termina Field Grass Group 0 (10)":
            lambda state: True,
        "Termina Field Grass Group 0 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 1
        "Termina Field Grass Group 1 (0)":
            lambda state: True,
        "Termina Field Grass Group 1 (1)":
            lambda state: True,
        "Termina Field Grass Group 1 (2)":
            lambda state: True,
        "Termina Field Grass Group 1 (3)":
            lambda state: True,
        "Termina Field Grass Group 1 (4)":
            lambda state: True,
        "Termina Field Grass Group 1 (5)":
            lambda state: True,
        "Termina Field Grass Group 1 (6)":
            lambda state: True,
        "Termina Field Grass Group 1 (7)":
            lambda state: True,
        "Termina Field Grass Group 1 (8)":
            lambda state: True,
        "Termina Field Grass Group 1 (9)":
            lambda state: True,
        "Termina Field Grass Group 1 (10)":
            lambda state: True,
        "Termina Field Grass Group 1 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 2
        "Termina Field Grass Group 2 (0)":
            lambda state: True,
        "Termina Field Grass Group 2 (1)":
            lambda state: True,
        "Termina Field Grass Group 2 (2)":
            lambda state: True,
        "Termina Field Grass Group 2 (3)":
            lambda state: True,
        "Termina Field Grass Group 2 (4)":
            lambda state: True,
        "Termina Field Grass Group 2 (5)":
            lambda state: True,
        "Termina Field Grass Group 2 (6)":
            lambda state: True,
        "Termina Field Grass Group 2 (7)":
            lambda state: True,
        "Termina Field Grass Group 2 (8)":
            lambda state: True,
        "Termina Field Grass Group 2 (9)":
            lambda state: True,
        "Termina Field Grass Group 2 (10)":
            lambda state: True,
        "Termina Field Grass Group 2 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 3
        "Termina Field Grass Group 3 (0)":
            lambda state: True,
        "Termina Field Grass Group 3 (1)":
            lambda state: True,
        "Termina Field Grass Group 3 (2)":
            lambda state: True,
        "Termina Field Grass Group 3 (3)":
            lambda state: True,
        "Termina Field Grass Group 3 (4)":
            lambda state: True,
        "Termina Field Grass Group 3 (5)":
            lambda state: True,
        "Termina Field Grass Group 3 (6)":
            lambda state: True,
        "Termina Field Grass Group 3 (7)":
            lambda state: True,
        "Termina Field Grass Group 3 (8)":
            lambda state: True,
        "Termina Field Grass Group 3 (9)":
            lambda state: True,
        "Termina Field Grass Group 3 (10)":
            lambda state: True,
        "Termina Field Grass Group 3 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 4
        "Termina Field Grass Group 4 (0)":
            lambda state: True,
        "Termina Field Grass Group 4 (1)":
            lambda state: True,
        "Termina Field Grass Group 4 (2)":
            lambda state: True,
        "Termina Field Grass Group 4 (3)":
            lambda state: True,
        "Termina Field Grass Group 4 (4)":
            lambda state: True,
        "Termina Field Grass Group 4 (5)":
            lambda state: True,
        "Termina Field Grass Group 4 (6)":
            lambda state: True,
        "Termina Field Grass Group 4 (7)":
            lambda state: True,
        "Termina Field Grass Group 4 (8)":
            lambda state: True,
        "Termina Field Grass Group 4 (9)":
            lambda state: True,
        "Termina Field Grass Group 4 (10)":
            lambda state: True,
        "Termina Field Grass Group 4 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 5
        "Termina Field Grass Group 5 (0)":
            lambda state: True,
        "Termina Field Grass Group 5 (1)":
            lambda state: True,
        "Termina Field Grass Group 5 (2)":
            lambda state: True,
        "Termina Field Grass Group 5 (3)":
            lambda state: True,
        "Termina Field Grass Group 5 (4)":
            lambda state: True,
        "Termina Field Grass Group 5 (5)":
            lambda state: True,
        "Termina Field Grass Group 5 (6)":
            lambda state: True,
        "Termina Field Grass Group 5 (7)":
            lambda state: True,
        "Termina Field Grass Group 5 (8)":
            lambda state: True,
        "Termina Field Grass Group 5 (9)":
            lambda state: True,
        "Termina Field Grass Group 5 (10)":
            lambda state: True,
        "Termina Field Grass Group 5 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 6
        "Termina Field Grass Group 6 (0)":
            lambda state: True,
        "Termina Field Grass Group 6 (1)":
            lambda state: True,
        "Termina Field Grass Group 6 (2)":
            lambda state: True,
        "Termina Field Grass Group 6 (3)":
            lambda state: True,
        "Termina Field Grass Group 6 (4)":
            lambda state: True,
        "Termina Field Grass Group 6 (5)":
            lambda state: True,
        "Termina Field Grass Group 6 (6)":
            lambda state: True,
        "Termina Field Grass Group 6 (7)":
            lambda state: True,
        "Termina Field Grass Group 6 (8)":
            lambda state: True,
        "Termina Field Grass Group 6 (9)":
            lambda state: True,
        "Termina Field Grass Group 6 (10)":
            lambda state: True,
        "Termina Field Grass Group 6 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 7
        "Termina Field Grass Group 7 (0)":
            lambda state: True,
        "Termina Field Grass Group 7 (1)":
            lambda state: True,
        "Termina Field Grass Group 7 (2)":
            lambda state: True,
        "Termina Field Grass Group 7 (3)":
            lambda state: True,
        "Termina Field Grass Group 7 (4)":
            lambda state: True,
        "Termina Field Grass Group 7 (5)":
            lambda state: True,
        "Termina Field Grass Group 7 (6)":
            lambda state: True,
        "Termina Field Grass Group 7 (7)":
            lambda state: True,
        "Termina Field Grass Group 7 (8)":
            lambda state: True,
        "Termina Field Grass Group 7 (9)":
            lambda state: True,
        "Termina Field Grass Group 7 (10)":
            lambda state: True,
        "Termina Field Grass Group 7 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 8
        "Termina Field Grass Group 8 (0)":
            lambda state: True,
        "Termina Field Grass Group 8 (1)":
            lambda state: True,
        "Termina Field Grass Group 8 (2)":
            lambda state: True,
        "Termina Field Grass Group 8 (3)":
            lambda state: True,
        "Termina Field Grass Group 8 (4)":
            lambda state: True,
        "Termina Field Grass Group 8 (5)":
            lambda state: True,
        "Termina Field Grass Group 8 (6)":
            lambda state: True,
        "Termina Field Grass Group 8 (7)":
            lambda state: True,
        "Termina Field Grass Group 8 (8)":
            lambda state: True,
        "Termina Field Grass Group 8 (9)":
            lambda state: True,
        "Termina Field Grass Group 8 (10)":
            lambda state: True,
        "Termina Field Grass Group 8 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 9
        "Termina Field Grass Group 9 (0)":
            lambda state: True,
        "Termina Field Grass Group 9 (1)":
            lambda state: True,
        "Termina Field Grass Group 9 (2)":
            lambda state: True,
        "Termina Field Grass Group 9 (3)":
            lambda state: True,
        "Termina Field Grass Group 9 (4)":
            lambda state: True,
        "Termina Field Grass Group 9 (5)":
            lambda state: True,
        "Termina Field Grass Group 9 (6)":
            lambda state: True,
        "Termina Field Grass Group 9 (7)":
            lambda state: True,
        "Termina Field Grass Group 9 (8)":
            lambda state: True,
        "Termina Field Grass Group 9 (9)":
            lambda state: True,
        "Termina Field Grass Group 9 (10)":
            lambda state: True,
        "Termina Field Grass Group 9 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 10
        "Termina Field Grass Group 10 (0)":
            lambda state: True,
        "Termina Field Grass Group 10 (1)":
            lambda state: True,
        "Termina Field Grass Group 10 (2)":
            lambda state: True,
        "Termina Field Grass Group 10 (3)":
            lambda state: True,
        "Termina Field Grass Group 10 (4)":
            lambda state: True,
        "Termina Field Grass Group 10 (5)":
            lambda state: True,
        "Termina Field Grass Group 10 (6)":
            lambda state: True,
        "Termina Field Grass Group 10 (7)":
            lambda state: True,
        "Termina Field Grass Group 10 (8)":
            lambda state: True,
        "Termina Field Grass Group 10 (9)":
            lambda state: True,
        "Termina Field Grass Group 10 (10)":
            lambda state: True,
        "Termina Field Grass Group 10 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 11
        "Termina Field Grass Group 11 (0)":
            lambda state: True,
        "Termina Field Grass Group 11 (1)":
            lambda state: True,
        "Termina Field Grass Group 11 (2)":
            lambda state: True,
        "Termina Field Grass Group 11 (3)":
            lambda state: True,
        "Termina Field Grass Group 11 (4)":
            lambda state: True,
        "Termina Field Grass Group 11 (5)":
            lambda state: True,
        "Termina Field Grass Group 11 (6)":
            lambda state: True,
        "Termina Field Grass Group 11 (7)":
            lambda state: True,
        "Termina Field Grass Group 11 (8)":
            lambda state: True,
        "Termina Field Grass Group 11 (9)":
            lambda state: True,
        "Termina Field Grass Group 11 (10)":
            lambda state: True,
        "Termina Field Grass Group 11 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 12
        "Termina Field Grass Group 12 (0)":
            lambda state: True,
        "Termina Field Grass Group 12 (1)":
            lambda state: True,
        "Termina Field Grass Group 12 (2)":
            lambda state: True,
        "Termina Field Grass Group 12 (3)":
            lambda state: True,
        "Termina Field Grass Group 12 (4)":
            lambda state: True,
        "Termina Field Grass Group 12 (5)":
            lambda state: True,
        "Termina Field Grass Group 12 (6)":
            lambda state: True,
        "Termina Field Grass Group 12 (7)":
            lambda state: True,
        "Termina Field Grass Group 12 (8)":
            lambda state: True,
        "Termina Field Grass Group 12 (9)":
            lambda state: True,
        "Termina Field Grass Group 12 (10)":
            lambda state: True,
        "Termina Field Grass Group 12 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 13
        "Termina Field Grass Group 13 (0)":
            lambda state: True,
        "Termina Field Grass Group 13 (1)":
            lambda state: True,
        "Termina Field Grass Group 13 (2)":
            lambda state: True,
        "Termina Field Grass Group 13 (3)":
            lambda state: True,
        "Termina Field Grass Group 13 (4)":
            lambda state: True,
        "Termina Field Grass Group 13 (5)":
            lambda state: True,
        "Termina Field Grass Group 13 (6)":
            lambda state: True,
        "Termina Field Grass Group 13 (7)":
            lambda state: True,
        "Termina Field Grass Group 13 (8)":
            lambda state: True,
        "Termina Field Grass Group 13 (9)":
            lambda state: True,
        "Termina Field Grass Group 13 (10)":
            lambda state: True,
        "Termina Field Grass Group 13 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 14
        "Termina Field Grass Group 14 (0)":
            lambda state: True,
        "Termina Field Grass Group 14 (1)":
            lambda state: True,
        "Termina Field Grass Group 14 (2)":
            lambda state: True,
        "Termina Field Grass Group 14 (3)":
            lambda state: True,
        "Termina Field Grass Group 14 (4)":
            lambda state: True,
        "Termina Field Grass Group 14 (5)":
            lambda state: True,
        "Termina Field Grass Group 14 (6)":
            lambda state: True,
        "Termina Field Grass Group 14 (7)":
            lambda state: True,
        "Termina Field Grass Group 14 (8)":
            lambda state: True,
        "Termina Field Grass Group 14 (9)":
            lambda state: True,
        "Termina Field Grass Group 14 (10)":
            lambda state: True,
        "Termina Field Grass Group 14 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 15
        "Termina Field Grass Group 15 (0)":
            lambda state: True,
        "Termina Field Grass Group 15 (1)":
            lambda state: True,
        "Termina Field Grass Group 15 (2)":
            lambda state: True,
        "Termina Field Grass Group 15 (3)":
            lambda state: True,
        "Termina Field Grass Group 15 (4)":
            lambda state: True,
        "Termina Field Grass Group 15 (5)":
            lambda state: True,
        "Termina Field Grass Group 15 (6)":
            lambda state: True,
        "Termina Field Grass Group 15 (7)":
            lambda state: True,
        "Termina Field Grass Group 15 (8)":
            lambda state: True,
        "Termina Field Grass Group 15 (9)":
            lambda state: True,
        "Termina Field Grass Group 15 (10)":
            lambda state: True,
        "Termina Field Grass Group 15 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 16
        "Termina Field Grass Group 16 (0)":
            lambda state: True,
        "Termina Field Grass Group 16 (1)":
            lambda state: True,
        "Termina Field Grass Group 16 (2)":
            lambda state: True,
        "Termina Field Grass Group 16 (3)":
            lambda state: True,
        "Termina Field Grass Group 16 (4)":
            lambda state: True,
        "Termina Field Grass Group 16 (5)":
            lambda state: True,
        "Termina Field Grass Group 16 (6)":
            lambda state: True,
        "Termina Field Grass Group 16 (7)":
            lambda state: True,
        "Termina Field Grass Group 16 (8)":
            lambda state: True,
        "Termina Field Grass Group 16 (9)":
            lambda state: True,
        "Termina Field Grass Group 16 (10)":
            lambda state: True,
        "Termina Field Grass Group 16 (11)":
            lambda state: True,
        
        # Termina Field Grass Group 17
        "Termina Field Grass Group 17 (0)":
            lambda state: True,
        "Termina Field Grass Group 17 (1)":
            lambda state: True,
        "Termina Field Grass Group 17 (2)":
            lambda state: True,
        "Termina Field Grass Group 17 (3)":
            lambda state: True,
        "Termina Field Grass Group 17 (4)":
            lambda state: True,
        "Termina Field Grass Group 17 (5)":
            lambda state: True,
        "Termina Field Grass Group 17 (6)":
            lambda state: True,
        "Termina Field Grass Group 17 (7)":
            lambda state: True,
        "Termina Field Grass Group 17 (8)":
            lambda state: True,
        "Termina Field Grass Group 17 (9)":
            lambda state: True,
        "Termina Field Grass Group 17 (10)":
            lambda state: True,
        "Termina Field Grass Group 17 (11)":
            lambda state: True,
        
        # Termina Field Grass Grotto Grass
        "Termina Field Grass Grotto Grass (1)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (2)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (3)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (4)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (5)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (6)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (7)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (8)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (9)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (10)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (11)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (12)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (13)":
            lambda state: True,
        "Termina Field Grass Grotto Grass (14)":
            lambda state: True,
        
        # Termina Field Cow Grotto Grass Groups
        "Termina Field Cow Grotto Grass Group 1 (1)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (2)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (3)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (4)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (5)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (6)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (7)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (8)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (9)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (10)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (11)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 1 (12)":
            lambda state: has_explosives(state, player),
        
        "Termina Field Cow Grotto Grass Group 2 (1)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (2)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (3)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (4)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (5)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (6)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (7)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (8)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (9)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (10)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (11)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 2 (12)":
            lambda state: has_explosives(state, player),
        
        "Termina Field Cow Grotto Grass Group 3 (1)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (2)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (3)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (4)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (5)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (6)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (7)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (8)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (9)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (10)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (11)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 3 (12)":
            lambda state: has_explosives(state, player),
        
        "Termina Field Cow Grotto Grass Group 4 (1)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (2)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (3)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (4)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (5)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (6)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (7)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (8)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (9)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (10)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (11)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 4 (12)":
            lambda state: has_explosives(state, player),
        
        "Termina Field Cow Grotto Grass Group 5 (1)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (2)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (3)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (4)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (5)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (6)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (7)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (8)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (9)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (10)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (11)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 5 (12)":
            lambda state: has_explosives(state, player),
        
        "Termina Field Cow Grotto Grass Group 6 (1)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (2)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (3)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (4)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (5)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (6)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (7)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (8)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (9)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (10)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (11)":
            lambda state: has_explosives(state, player),
        "Termina Field Cow Grotto Grass Group 6 (12)":
            lambda state: has_explosives(state, player),
        
        # Termina Field Peahat Grotto Grass
        "Termina Field Peahat Grotto Grass Group 1 (1)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (2)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (3)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (4)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (5)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (6)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (7)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (8)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (9)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (10)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (11)":
            lambda state: True,
        "Termina Field Peahat Grotto Grass Group 1 (12)":
            lambda state: True,
        
        # Termina Field Bio Baba Grotto Grass
        "Termina Field Bio Baba Grotto Grass (1)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Termina Field Bio Baba Grotto Grass (2)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        
        # Termina Field Eastern Gossip Grotto Grass
        "Termina Field Eastern Gossip Grotto Grass (1)":
            lambda state: True,
        "Termina Field Eastern Gossip Grotto Grass (2)":
            lambda state: True,
        "Termina Field Eastern Gossip Grotto Grass (3)":
            lambda state: True,
        "Termina Field Eastern Gossip Grotto Grass (4)":
            lambda state: True,
        "Termina Field Eastern Gossip Grotto Grass (5)":
            lambda state: True,
        
        # Termina Field Eastern Pillar Grotto Grass
        "Termina Field Eastern Pillar Grotto Grass (1)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (2)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (3)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (4)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (5)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (6)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (7)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (8)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (9)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (10)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (11)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (12)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (13)":
            lambda state: True,
        "Termina Field Eastern Pillar Grotto Grass (14)":
            lambda state: True,
        
        # Termina Field Bombable Rock Grass 
        "Termina Field Bombable Rock Grass (1)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Termina Field Bombable Rock Grass (2)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Termina Field Bombable Rock Grass (3)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Termina Field Bombable Rock Grass (4)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Termina Field Bombable Rock Grass (5)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        # Road To Southern Swamp Grass
        "Road to Southern Swamp Outside Archery Grass (1)":
            lambda state: True,
        "Road to Southern Swamp Outside Archery Grass (2)":
            lambda state: True,
        
        # Road to Southern Swamp Grass Group 0
        "Road to Southern Swamp Grass Group 0 (0)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (1)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (2)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (3)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (4)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (5)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (6)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (7)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 0 (8)":
            lambda state: True,
        
        # Road to Southern Swamp Grass Group 1
        "Road to Southern Swamp Grass Group 1 (0)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (1)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (2)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (3)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (4)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (5)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (6)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (7)":
            lambda state: True,
        "Road to Southern Swamp Grass Group 1 (8)":
            lambda state: True,
        "Road to Southern Swamp Grotto Grass (0)":
            lambda state: True,
        "Road to Southern Swamp Grotto Grass (1)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (2)":
            lambda state: True,   
        "Road to Southern Swamp Grotto Grass (3)":
            lambda state: True, 
        "Road to Southern Swamp Grotto Grass (4)":
            lambda state: True,
        "Road to Southern Swamp Grotto Grass (5)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (6)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (7)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (8)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (9)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (10)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (11)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (12)":
            lambda state: True,  
        "Road to Southern Swamp Grotto Grass (13)":
            lambda state: True,              

        # Southern Swamp Grass
        "Southern Swamp Owl Grass (1)":
            lambda state: True,
        "Southern Swamp Owl Grass (2)":
            lambda state: True,
        
        # Southern Swamp Grass Group 0
        "Southern Swamp Grass Group 0 (0)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (1)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (2)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (3)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (4)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (5)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (6)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (7)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (8)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (9)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (10)":
            lambda state: True,
        "Southern Swamp Grass Group 0 (11)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (0)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (1)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (2)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (3)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (4)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (5)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (6)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (7)":
            lambda state: True,
        "Southern Swamp Grass Group 1 (8)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (0)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (1)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (2)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (3)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (4)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (5)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (6)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (7)":
            lambda state: True,
        "Southern Swamp Grass Group 2 (8)":
            lambda state: True,
        "Southern Near Gossip Stone Grass (1)":
            lambda state: True,
        "Southern Near Gossip Stone Grass (2)":
            lambda state: True,            
        # Woods of Mystery Grass
        "Woods of Mystery Grass (0)":
            lambda state: True,
        "Woods of Mystery Grass (1)":
            lambda state: True,
        "Woods of Mystery Grass (2)":
            lambda state: True,
        "Woods of Mystery Grass (3)":
            lambda state: True,
        "Woods of Mystery Grass (4)":
            lambda state: True,
        "Woods of Mystery Grass (5)":
            lambda state: True,
        "Woods of Mystery Grass (6)":
            lambda state: True,
        "Woods of Mystery Grass (7)":
            lambda state: True,
        "Woods of Mystery Grass (8)":
            lambda state: True,
        "Woods of Mystery Grass (9)":
            lambda state: True,
        "Woods of Mystery Grass (10)":
            lambda state: True,
        "Woods of Mystery Grass (11)":
            lambda state: True,
        "Woods of Mystery Grass (12)":
            lambda state: True,
        "Woods of Mystery Grass (13)":
            lambda state: True,
        "Woods of Mystery Grass (14)":
            lambda state: True,
        "Woods of Mystery Grass (15)":
            lambda state: True,
        "Woods of Mystery Grass (16)":
            lambda state: True,
        "Woods of Mystery Grass (17)":
            lambda state: True,
        "Woods of Mystery Grass (18)":
            lambda state: True,
        "Woods of Mystery Grass (19)":
            lambda state: True,
        
        # Woods of Mystery Day-specific Grass
        "Woods of Mystery Day 2 Unique Grass":
            lambda state: True,
        "Woods of Mystery Day 3 Unique Grass (0)":
            lambda state: True,
        "Woods of Mystery Day 3 Unique Grass (1)":
            lambda state: True,
        
        # Woods of Mystery Day 2 Grotto Grass
        "Woods of Mystery Day 2 Grotto Grass (0)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (1)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (2)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (3)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (4)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (5)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (6)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (7)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (8)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (9)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (10)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (11)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (12)":
            lambda state: True,
        "Woods of Mystery Day 2 Grotto Grass (13)":
            lambda state: True,
        
        # Southern Swamp Grotto Grass - Requires access to Swamp Spider House
        "Southern Swamp Grotto Grass (1)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (2)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (3)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (4)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (5)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (6)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (7)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (8)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (9)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (10)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (11)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (12)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (13)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        "Southern Swamp Grotto Grass (14)":
            lambda state: (
                state.has("Deku Mask", player) and
                (
                    state.has("Bottle of Red Potion", player) or 
                    (
                        has_hard_projectiles(state, player) and 
                        state.has("Deku Mask", player)
                    ) or 
                    (
                        state.has("Pictograph Box", player) and 
                        state.has("Deku Mask", player)
                    )
                )
            ),
        
        # Deku Palace Bean Grotto Grass
        "Deku Palace Bean Grotto Grass Group 0 (0)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (1)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (2)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (3)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (4)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (5)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (6)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (7)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (8)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (9)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (10)":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Grass Group 0 (11)":
            lambda state: state.has("Deku Mask", player),
        
        # Woodfall Grass
        "Woodfall Grass (1)":
            lambda state: True,
        "Woodfall Grass (2)":
            lambda state: True,
        "Woodfall Grass (3)":
            lambda state: True,
        "Woodfall Grass (4)":
            lambda state: True,
        "Woodfall Grass (5)":
            lambda state: True,
        "Woodfall Grass (6)":
            lambda state: True,
        
        # Southern Swamp Owl Post Dungeon Grass
        "Southern Swamp Owl Post Dungeon Grass (1)":
            lambda state: can_clear_woodfall(state, player),
        "Southern Swamp Owl Post Dungeon Grass (2)":
            lambda state: can_clear_woodfall(state, player),

        # Milk Road Owl Grass
        "Milk Road Owl Grass (1)":
            lambda state: True,
        "Milk Road Owl Grass (2)":
            lambda state: True,
        "Milk Road Owl Grass (3)":
            lambda state: True,
        
        # Milk Road Keaton Grass
        "Milk Road Keaton Grass (1)":
            lambda state: True,
        "Milk Road Keaton Grass (2)":
            lambda state: True,
        "Milk Road Keaton Grass (3)":
            lambda state: True,
        "Milk Road Keaton Grass (4)":
            lambda state: True,
        "Milk Road Keaton Grass (5)":
            lambda state: True,
        "Milk Road Keaton Grass (6)":
            lambda state: True,
        "Milk Road Keaton Grass (7)":
            lambda state: True,
        "Milk Road Keaton Grass (8)":
            lambda state: True,
        "Milk Road Keaton Grass (9)":
            lambda state: True,
        
        # Milk Road Gorman Racetrack Grass Group 1 - Requires Epona's Song
        "Milk Road Gorman Racetrack Grass Group 1 (1)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (2)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (3)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (4)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (5)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (6)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (7)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (8)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (9)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (10)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (11)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 1 (12)":
            lambda state: can_play_song("Epona's Song", state, player),
        
        # Milk Road Gorman Racetrack Grass Group 2 - Requires Epona's Song
        "Milk Road Gorman Racetrack Grass Group 2 (1)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (2)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (3)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (4)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (5)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (6)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (7)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (8)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (9)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (10)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (11)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Milk Road Gorman Racetrack Grass Group 2 (12)":
            lambda state: can_play_song("Epona's Song", state, player),

        # Romani Ranch Grass Group 1
        "Romani Ranch Grass Group 1 (1)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (2)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (3)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (4)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (5)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (6)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (7)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (8)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (9)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (10)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (11)":
            lambda state: True,
        "Romani Ranch Grass Group 1 (12)":
            lambda state: True,
        
        # Romani Ranch Grass Group 2
        "Romani Ranch Grass Group 2 (1)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (2)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (3)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (4)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (5)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (6)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (7)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (8)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (9)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (10)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (11)":
            lambda state: True,
        "Romani Ranch Grass Group 2 (12)":
            lambda state: True,
        
        # Romani Ranch Grass Group 3
        "Romani Ranch Grass Group 3 (1)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (2)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (3)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (4)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (5)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (6)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (7)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (8)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (9)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (10)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (11)":
            lambda state: True,
        "Romani Ranch Grass Group 3 (12)":
            lambda state: True,
        
        # Romani Ranch Grass Group 4
        "Romani Ranch Grass Group 4 (1)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (2)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (3)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (4)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (5)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (6)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (7)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (8)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (9)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (10)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (11)":
            lambda state: True,
        "Romani Ranch Grass Group 4 (12)":
            lambda state: True,
        
        # Romani Ranch Grass Group 5
        "Romani Ranch Grass Group 5 (1)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (2)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (3)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (4)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (5)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (6)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (7)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (8)":
            lambda state: True,
        "Romani Ranch Grass Group 5 (9)":
            lambda state: True,

        # Twin Isles Grotto Grass - Requires 
        "Twin Isles Grotto Grass (1)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (2)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (3)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (4)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (5)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (6)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (7)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (8)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (9)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (10)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (11)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (12)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (13)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        "Twin Isles Grotto Grass (14)":
            lambda state: (
                (state.has("Goron Mask", player) and has_explosives(state, player)) or
                (state.has("Hookshot", player) and has_explosives(state, player))
            ),
        
        # Twin Islands Springtime Grass - Requires clearing Snowhead
        "Twin Islands Springtime Grass Group 1 (1)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (2)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (3)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (4)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (5)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (6)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (7)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (8)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (9)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (10)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (11)":
            lambda state: can_clear_snowhead(state, player),
        "Twin Islands Springtime Grass Group 1 (12)":
            lambda state: can_clear_snowhead(state, player),

        # Goron Village Lens Cave Grass Group 1
        "Goron Village Lens Cave Grass Group 1 (1)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (2)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (3)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (4)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (5)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (6)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (7)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (8)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (9)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (10)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (11)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 1 (12)":
            lambda state: True,
        
        # Goron Village Lens Cave Grass Group 2
        "Goron Village Lens Cave Grass Group 2 (1)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (2)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (3)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (4)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (5)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (6)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (7)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (8)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (9)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (10)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (11)":
            lambda state: True,
        "Goron Village Lens Cave Grass Group 2 (12)":
            lambda state: True,

        # Path To Snowhead Grotto Grass - Requires Goron Mask, Magic, and Explosives
        "Path To Snowhead Grotto Grass (1)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (2)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (3)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (4)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (5)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (6)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (7)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (8)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (9)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (10)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (11)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (12)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (13)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),
        "Path To Snowhead Grotto Grass (14)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Progressive Magic", player) and 
                has_explosives(state, player)
            ),

        # Mountain Village Springtime Grass
        "Mountain Village Springtime Grass (1)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (2)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (3)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (4)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (5)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (6)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (7)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (8)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (9)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (10)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (11)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (12)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (13)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (14)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (15)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (16)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (17)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (18)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (19)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (20)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (21)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (22)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (23)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (24)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (25)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (26)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (27)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (28)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (29)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Grass (30)":
            lambda state: can_clear_snowhead(state, player),
        
        # Mountain Village Springtime Keaton Grass
        "Mountain Village Keaton Grass (0)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (1)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (2)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (3)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (4)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (5)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (6)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (7)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Keaton Grass (8)":
            lambda state: can_clear_snowhead(state, player),
        
        # Mountain Village Spring Grotto Grass
        "Mountain Village Spring Grotto Grass (1)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (2)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (3)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (4)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (5)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (6)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (7)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (8)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (9)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (10)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (11)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (12)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (13)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Grotto Grass (14)":
            lambda state: can_clear_snowhead(state, player),

        # Great Bay Coast Grotto Grass - Requires Epona's Song
        "Great Bay Coast Grotto Grass (0)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (1)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (2)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (3)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (4)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (5)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (6)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (7)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (8)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (9)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (10)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (11)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (12)":
            lambda state: can_play_song("Epona's Song", state, player),  
        "Great Bay Coast Grotto Grass (13)":
            lambda state: can_play_song("Epona's Song", state, player),  

        # Great Bay Coast Grass - Requires Epona's Song                                                                                                                                                                      
        "Great Bay Coast Grass (1)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Great Bay Coast Grass (2)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Great Bay Coast Grass (3)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Great Bay Coast Grass (4)":
            lambda state: can_play_song("Epona's Song", state, player),
        "Great Bay Coast Grass (5)":
            lambda state: can_play_song("Epona's Song", state, player),
        
        # Great Bay Coast Cow Grotto Grass Group 1 - Requires Epona's Song and Hookshot
        "Great Bay Coast Cow Grotto Grass Group 1 (1)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (2)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (3)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (4)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (5)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (6)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (7)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (8)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (9)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (10)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (11)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 1 (12)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Great Bay Coast Cow Grotto Grass Group 2
        "Great Bay Coast Cow Grotto Grass Group 2 (1)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (2)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (3)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (4)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (5)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (6)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (7)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (8)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (9)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (10)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (11)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 2 (12)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Great Bay Coast Cow Grotto Grass Group 3
        "Great Bay Coast Cow Grotto Grass Group 3 (1)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (2)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (3)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (4)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (5)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (6)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (7)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (8)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (9)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (10)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (11)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 3 (12)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Great Bay Coast Cow Grotto Grass Group 4
        "Great Bay Coast Cow Grotto Grass Group 4 (1)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (2)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (3)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (4)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (5)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (6)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (7)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (8)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (9)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (10)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (11)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 4 (12)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Great Bay Coast Cow Grotto Grass Group 5
        "Great Bay Coast Cow Grotto Grass Group 5 (1)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (2)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (3)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (4)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (5)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (6)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (7)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (8)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (9)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (10)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (11)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 5 (12)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Great Bay Coast Cow Grotto Grass Group 6
        "Great Bay Coast Cow Grotto Grass Group 6 (1)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (2)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (3)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (4)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (5)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (6)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (7)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (8)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (9)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (10)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (11)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),
        "Great Bay Coast Cow Grotto Grass Group 6 (12)":
            lambda state: (
                can_play_song("Epona's Song", state, player) and 
                state.has("Hookshot", player)
            ),            

        # Zora Cape Grotto Grass - Requires explosives or Goron Mask
        "Zora Cape Grotto Grass (0)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (1)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (2)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (3)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (4)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (5)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (6)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (7)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (8)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (9)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (10)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (11)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        "Zora Cape Grotto Grass (12)":
            lambda state: (
                has_explosives(state, player) or 
                state.has("Goron Mask", player)
            ),
        # Road To Ikana Grotto Grass - Requires Goron Mask
        "Road To Ikana Grotto Grass (1)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (2)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (3)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (4)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (5)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (6)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (7)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (8)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (9)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (10)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (11)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (12)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (13)":
            lambda state: state.has("Goron Mask", player),
        "Road To Ikana Grotto Grass (14)":
            lambda state: state.has("Goron Mask", player),                 
        # Ikana Graveyard Lower Grass
        "Ikana Graveyard Lower Grass (1)":
            lambda state: True,
        "Ikana Graveyard Lower Grass (2)":
            lambda state: True,
        "Ikana Graveyard Lower Grass (3)":
            lambda state: True,
        "Ikana Graveyard Lower Grass (4)":
            lambda state: True,
        "Ikana Graveyard Lower Grass (5)":
            lambda state: True,
        
        # Ikana Graveyard Upper Grass
        "Ikana Graveyard Upper Grass (1)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (2)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (3)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (4)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (5)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (6)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (7)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (8)":
            lambda state: True,
        "Ikana Graveyard Upper Grass (9)":
            lambda state: True,
        
        # Ikana Graveyard Bombable Grotto Grass - Requires explosives
        "Ikana Graveyard Bombable Grotto Grass (1)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (2)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (3)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (4)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (5)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (6)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (7)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (8)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (9)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (10)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (11)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (12)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (13)":
            lambda state: has_explosives(state, player),
        "Ikana Graveyard Bombable Grotto Grass (14)":
            lambda state: has_explosives(state, player),
        # Ikana Canyon Grass - Requires Ice Arrows and Hookshot
        "Ikana Canyon Grass (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ikana Canyon Grass (2)":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ikana Canyon Grass (3)":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ikana Canyon Grass (4)":
            lambda state: (
                can_use_ice_arrows(state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Ikana Canyon Grotto Grass
        "Ikana Canyon Grotto Grass (1)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (2)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (3)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (4)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (5)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (6)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (7)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (8)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (9)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (10)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (11)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (12)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (13)":
            lambda state: True,
        "Ikana Canyon Grotto Grass (14)":
            lambda state: True, 

        # Secret Shrine Entrance Grass
        "Secret Shrine Entrance Grass (1)":
            lambda state: True,
        "Secret Shrine Entrance Grass (2)":
            lambda state: True,
        "Secret Shrine Entrance Grass (3)":
            lambda state: True,
        "Secret Shrine Entrance Grass (4)":
            lambda state: True,
        "Secret Shrine Entrance Grass (5)":
            lambda state: True,
        "Secret Shrine Entrance Grass (6)":
            lambda state: True,
        
        # Secret Shrine Dinolfos Grass - Requires Light Arrows
        "Secret Shrine Dinolfos Grass (0)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Dinolfos Grass (1)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Dinolfos Grass (2)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Dinolfos Grass (3)":
            lambda state: can_use_light_arrows(state, player),
        
        # Secret Shrine Wizzrobe Grass - Requires Light Arrows
        "Secret Shrine Wizzrobe Grass (0)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wizzrobe Grass (1)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wizzrobe Grass (2)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wizzrobe Grass (3)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wizzrobe Grass (4)":
            lambda state: can_use_light_arrows(state, player),
        
        # Secret Shrine Wart Grass - Requires Light Arrows
        "Secret Shrine Wart Grass (0)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wart Grass (1)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wart Grass (2)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wart Grass (3)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wart Grass (4)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wart Grass (5)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wart Grass (6)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Wart Grass (7)":
            lambda state: can_use_light_arrows(state, player),
        
        # Secret Shrine Garo Master Grass - Requires Light Arrows
        "Secret Shrine Garo Master Grass (0)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Garo Master Grass (1)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Garo Master Grass (2)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Garo Master Grass (3)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Garo Master Grass (4)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Garo Master Grass (5)":
            lambda state: can_use_light_arrows(state, player),   

        # Beneath the Well Left Side Back Room Grass - Matches Invisible Chest rules
        "Beneath the Well Left Side Back Room Grass (0)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_afford_price(state, player, 100) or 
                    state.has("Mask of Scents", player)
                )
            ),
        "Beneath the Well Left Side Back Room Grass (1)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_afford_price(state, player, 100) or 
                    state.has("Mask of Scents", player)
                )
            ),
        
        # Beneath the Well Right Side Before Big Poe and Cow Grass 
        "Beneath the Well Right Side Before Big Poe and Cow Grass (0)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Beneath the Well Right Side Before Big Poe and Cow Grass (1)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Beneath the Well Right Side Before Big Poe and Cow Grass (2)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Beneath the Well Right Side Before Big Poe and Cow Grass (3)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        
        # Beneath the Well Right Side Cow Grass 
        "Beneath the Well Right Side Cow Grass (0)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_play_song("Epona's Song", state, player) and 
                    (
                        can_plant_beans(state, player) or 
                        can_use_light_arrows(state, player)
                    ) and 
                    (
                        (
                            can_play_song("Song of Soaring", state, player) and 
                            (
                                (
                                    state.can_reach("Twin Islands", 'Region', player) and 
                                    can_use_fire_arrows(state, player)
                                ) or 
                                (
                                    state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and 
                                    state.has("Goron Mask", player)
                                )
                            )
                        ) or 
                        state.can_reach("Ikana Well Invisible Chest", 'Location', player)
                    )
                )
            ),
        "Beneath the Well Right Side Cow Grass (1)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_play_song("Epona's Song", state, player) and 
                    (
                        can_plant_beans(state, player) or 
                        can_use_light_arrows(state, player)
                    ) and 
                    (
                        (
                            can_play_song("Song of Soaring", state, player) and 
                            (
                                (
                                    state.can_reach("Twin Islands", 'Region', player) and 
                                    can_use_fire_arrows(state, player)
                                ) or 
                                (
                                    state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and 
                                    state.has("Goron Mask", player)
                                )
                            )
                        ) or 
                        state.can_reach("Ikana Well Invisible Chest", 'Location', player)
                    )
                )
            ),
        "Beneath the Well Right Side Cow Grass (2)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_play_song("Epona's Song", state, player) and 
                    (
                        can_plant_beans(state, player) or 
                        can_use_light_arrows(state, player)
                    ) and 
                    (
                        (
                            can_play_song("Song of Soaring", state, player) and 
                            (
                                (
                                    state.can_reach("Twin Islands", 'Region', player) and 
                                    can_use_fire_arrows(state, player)
                                ) or 
                                (
                                    state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and 
                                    state.has("Goron Mask", player)
                                )
                            )
                        ) or 
                        state.can_reach("Ikana Well Invisible Chest", 'Location', player)
                    )
                )
            ),
        
        # Beneath the Well Right Side Back Room Grass
        "Beneath the Well Right Side Back Room Grass (0)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Beneath the Well Right Side Back Room Grass (1)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Beneath the Well Right Side Back Room Grass (2)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Beneath the Well Right Side Back Room Grass (3)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        "Beneath the Well Right Side Back Room Grass (4)":
            lambda state: (
                state.has("Gibdo Mask", player) and 
                has_bottle(state, player) and 
                (
                    can_plant_beans(state, player) or 
                    can_use_light_arrows(state, player)
                )
            ),
        # Ikana Castle Grass - Requires Mirror Shield or Light Arrows
        "Ikana Castle Grass (1)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (2)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (3)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (4)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (5)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (6)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (7)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (8)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (9)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (10)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (11)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        "Ikana Castle Grass (12)":
            lambda state: (
                has_mirror_shield(state, player) or 
                can_use_light_arrows(state, player)
            ),
        # Snowhead Temple Basement Grass
        "Snowhead Temple Basement Grass (0)":
            lambda state: True,
        "Snowhead Temple Basement Grass (1)":
            lambda state: True,
        "Snowhead Temple Basement Grass (2)":
            lambda state: True,
        "Snowhead Temple Basement Grass (3)":
            lambda state: True,
        "Snowhead Temple Basement Grass (4)":
            lambda state: True,
        "Snowhead Temple Basement Grass (5)":
            lambda state: True,
        "Snowhead Temple Basement Grass (6)":
            lambda state: True,
        "Snowhead Temple Basement Grass (7)":
            lambda state: True,
        "Snowhead Temple Basement Grass (8)":
            lambda state: True,
        "Snowhead Temple Basement Grass (9)":
            lambda state: True,
        # Stone Tower Temple Entrance Room Grass
        "Stone Tower Temple Entrance Room Grass (0)":
            lambda state: True,
        "Stone Tower Temple Entrance Room Grass (1)":
            lambda state: True,
        "Stone Tower Temple Entrance Room Grass (2)":
            lambda state: True,
        
        # Stone Tower Temple Elegy Maze Grass - Requires Goron, Zora, and Elegy
        "Stone Tower Temple Elegy Maze Grass (0)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and 
                can_play_song("Elegy of Emptiness", state, player)
            ),
        "Stone Tower Temple Elegy Maze Grass (1)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and 
                can_play_song("Elegy of Emptiness", state, player)
            ),
        "Stone Tower Temple Elegy Maze Grass (2)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and 
                can_play_song("Elegy of Emptiness", state, player)
            ),
        "Stone Tower Temple Elegy Maze Grass (3)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and 
                can_play_song("Elegy of Emptiness", state, player)
            ),
        "Stone Tower Temple Elegy Maze Grass (4)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and 
                can_play_song("Elegy of Emptiness", state, player)
            ),
        "Stone Tower Temple Elegy Maze Grass (5)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and 
                can_play_song("Elegy of Emptiness", state, player)
            ),

        # Clock Town Pots
        "Trading Post Pot":
            lambda state: True,

        # Sword School Night 3 Midnight Pots - Requires Progressive Sword
        "Sword School Night 3 Midnight Pots (0)":
            lambda state: state.has("Progressive Sword", player),
        "Sword School Night 3 Midnight Pots (1)":
            lambda state: state.has("Progressive Sword", player),
        "Sword School Night 3 Midnight Pots (2)":
            lambda state: state.has("Progressive Sword", player),
        "Sword School Night 3 Midnight Pots (3)":
            lambda state: state.has("Progressive Sword", player),
        "Sword School Night 3 Midnight Pots (4)":
            lambda state: state.has("Progressive Sword", player),

        # Clock Tower Pots Night 3
        "Top Of Clock Tower Pots (0)":
            lambda state: True,
        "Top Of Clock Tower Pots (1)":
            lambda state: True,
        "Top Of Clock Tower Pots (2)":
            lambda state: True,
        "Top Of Clock Tower Pots (3)":
            lambda state: True,                                    

        # Bombers Hideout Pots - Requires access to Bomber's Hideout Astral Observatory
        "Bombers Hideout Pots (0)":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player),
        "Bombers Hideout Pots (1)":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player),
        "Bombers Hideout Pots (2)":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player),
        "Bombers Hideout Pots (3)":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player),
        
        # Astral Observatory Pots - Requires access to Bomber's Hideout Astral Observatory
        "Astral Observatory Pots (0)":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player),
        "Astral Observatory Pots (1)":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player),
        "Astral Observatory Pots (2)":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player),

        # Termina Field Pots
        
        # Termina Field Eastern Pillar Pot
        "Termina Field Eastern Pillar Pot":
            lambda state: has_projectiles(state, player),
        
        # Termina Field Deku Business Scrub Grotto Pot
        "Termina Field Deku Business Scrub Grotto Pot":
            lambda state: True,
        # Southern Swamp Pots
        
        # Road To Southern Swamp Outside Archery Pots
        "Road To Southern Swamp Outside Archery Pots (0)":
            lambda state: True,
        "Road To Southern Swamp Outside Archery Pots (1)":
            lambda state: True,
        
        # Southern Swamp Beneath Witch Shop Pots
        "Southern Swamp Beneath Witch Shop Pots (0)":
            lambda state: True,
        "Southern Swamp Beneath Witch Shop Pots (1)":
            lambda state: True,
        "Southern Swamp Beneath Witch Shop Pots (2)":
            lambda state: True,
        
        # Swamp Spider House Pots
        
        # Swamp Spider House Main Room Pots
        "Swamp Spider House Main Room Pots (0)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Main Room Pots (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Main Room Pots (2)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Main Room Pots (3)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Main Room Pots (4)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Main Room Pots (5)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Main Room Pots (6)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Main Room Pots (7)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),  

        # Swamp Spider House Tablet Room Pots
        "Swamp Spider House Tablet Room Pots (0)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Tablet Room Pots (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player), 

        # Swamp Spider House Giant Jar Room Pots
        "Swamp Spider House Giant Jar Room Pots (0)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Giant Jar Room Pots (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Giant Jar Room Pots (2)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Giant Jar Room Pots (3)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Giant Jar Room Pots (4)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Giant Jar Room Pots (5)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Giant Jar Room Pots (6)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Giant Jar Room Pots (7)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),            
        
        # Swamp Spider House Gold Room Pots
        "Swamp Spider House Gold Room Pots (0)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Gold Room Pots (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Gold Room Pots (2)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Gold Room Pots (3)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Gold Room Pots (4)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Gold Room Pots (5)":    
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        # Deku Palace Pots
        
        # Deku Palace Right Side Upper Pots
        "Deku Palace Right Side Upper Pots (0)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Upper Pots (1)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        
        # Deku Butler Race Pots
        "Deku Butler Race Pots (0)":
            lambda state: (
                can_clear_woodfall(state, player) and 
                state.has("Progressive Sword", player) and 
                has_bottle(state, player)
            ),
        "Deku Butler Race Pots (1)":
            lambda state: (
                can_clear_woodfall(state, player) and 
                state.has("Progressive Sword", player) and 
                has_bottle(state, player)
            ),
        # Woodfall Pots
        
        # Woodfall Owl Pots - Requires access to Woodfall region as Deku
        "Woodfall Owl Pots (0)":
            lambda state: (
                state.can_reach("Woodfall", 'Region', player) and 
                state.has("Deku Mask", player)
            ),
        "Woodfall Owl Pots (1)":
            lambda state: (
                state.can_reach("Woodfall", 'Region', player) and 
                state.has("Deku Mask", player)
            ),
        "Woodfall Owl Pots (2)":
            lambda state: (
                state.can_reach("Woodfall", 'Region', player) and 
                state.has("Deku Mask", player)
            ),
        # Woodfall Temple Pots
        
        # Woodfall Temple Entrance Pot
        "Woodfall Temple Entrance Pot":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        
        # Woodfall Temple Main Room Pots
        "Woodfall Temple Main Room Pots (0)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (1)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (2)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (3)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (4)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (5)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (6)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (7)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Main Room Pots (8)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        
        # Woodfall Temple Deku Elevator Pots
        "Woodfall Temple Deku Elevator Pots (0)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Deku Elevator Pots (1)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Deku Elevator Pots (2)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        "Woodfall Temple Deku Elevator Pots (3)":
            lambda state: state.can_reach("Woodfall Temple", 'Region', player),
        
        # Woodfall Temple Frog Boss Pots - Requires bow to access this area
        "Woodfall Temple Frog Boss Pots (0)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Frog Boss Pots (1)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Frog Boss Pots (2)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Frog Boss Pots (3)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                state.has("Progressive Bow", player)
            ),
        
        # Woodfall Temple Left Side Bridge Pots - Requires small key or bow
        "Woodfall Temple Left Side Bridge Pots (0)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                (
                    state.has("Small Key (Woodfall)", player) or 
                    state.has("Progressive Bow", player)
                )
            ),
        "Woodfall Temple Left Side Bridge Pots (1)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                (
                    state.has("Small Key (Woodfall)", player) or 
                    state.has("Progressive Bow", player)
                )
            ),
        
        # Woodfall Temple Pre Boss Pots - Requires bow to reach pre-boss area
        "Woodfall Temple Pre Boss Pots (0)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Pre Boss Pots (1)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and 
                state.has("Progressive Bow", player)
            ),
        # Mountain Village Pots
        
        "Mountain Village Pots (0)":
            lambda state: True,
        "Mountain Village Pots (1)":
            lambda state: True,
        "Mountain Village Pots (2)":
            lambda state: True,
        # Goron Village Pots
        
        # Goron Racetrack Pots - Requires Goron Mask and Powder Keg
        "Goron Racetrack Pots (0)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (1)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (2)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (3)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (4)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (5)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (6)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (7)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (8)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (9)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (10)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (11)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (12)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (13)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (14)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (15)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (16)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (17)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (18)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (19)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (20)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (21)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (22)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (23)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (24)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (25)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (26)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (27)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (28)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        "Goron Racetrack Pots (29)":
            lambda state: (
                state.has("Goron Mask", player) and 
                state.has("Powder Keg", player)
            ),
        
        # Goron Shrine Pots - Requires region access
        "Goron Shrine Pots (0)":
            lambda state: True,
        "Goron Shrine Pots (1)":
            lambda state: True,
        "Goron Shrine Pots (2)":
            lambda state: True,
        "Goron Shrine Pots (3)":
            lambda state: True,
        "Goron Shrine Pots (4)":
            lambda state: True,
        "Goron Shrine Pots (5)":
            lambda state: True,
        "Goron Shrine Pots (6)":
            lambda state: True,
        "Goron Shrine Pots (7)":
            lambda state: True,
        "Goron Shrine Pots (8)":
            lambda state: True,
        "Goron Shrine Pots (9)":
            lambda state: True,
        "Goron Shrine Pots (10)":
            lambda state: True,  
                        
        # Snowhead Temple Pots
        
        # Snowhead Temple Blue Door Lava Bridge Pots 
        "Snowhead Temple Entrance Pots (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),        
        "Snowhead Temple Entrance Pots (1)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        # Snowhead Temple Pots
        
        # Snowhead Temple Blue Door Lava Bridge Pots - Basic temple access
        "Snowhead Temple Blue Door Lava Bridge Pots (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Blue Door Lava Bridge Pots (1)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Blue Door Lava Bridge Pots (2)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Blue Door Lava Bridge Pots (3)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Blue Door Lava Bridge Pots (4)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Blue Door Lava Bridge Pots (5)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Blue Door Lava Bridge Pots (6)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        
        # Snowhead Temple Main Room Pots Basement - Basic temple access
        "Snowhead Temple Main Room Pots Basement (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Main Room Pots Basement (1)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        
        # Snowhead Temple Main Room Scarecrow Pots - Requires Hookshot or Fire Arrows
        "Snowhead Temple Main Room Scarecrow Pots (0)":
            lambda state: (
   
                (
                    state.has("Hookshot", player) or 
                    can_use_fire_arrows(state, player)
                )
            ),
        "Snowhead Temple Main Room Scarecrow Pots (1)":
            lambda state: (
   
                (
                    state.has("Hookshot", player) or 
                    can_use_fire_arrows(state, player)
                )
            ),
        
        # Snowhead Temple Frozen Green Door Pots - Basic temple access (pots are at bottom)
        "Snowhead Temple Frozen Green Door Pots (0)":
            lambda state: True,
        "Snowhead Temple Frozen Green Door Pots (1)":
            lambda state: True,
        "Snowhead Temple Frozen Green Door Pots (2)":
            lambda state: True,
        "Snowhead Temple Frozen Green Door Pots (3)":
            lambda state: True,
        "Snowhead Temple Frozen Green Door Pots (4)":
            lambda state: True,
        "Snowhead Temple Frozen Green Door Pots (5)":
            lambda state: True,
        "Snowhead Temple Frozen Green Door Pots (6)":
            lambda state: True,
        "Snowhead Temple Frozen Green Door Pots (7)":
            lambda state:can_use_fire_arrows(state, player
            ),
        "Snowhead Temple Frozen Green Door Pots (8)":
            lambda state:can_use_fire_arrows(state, player
            ),
        "Snowhead Temple Frozen Green Door Pots (9)":
            lambda state:can_use_fire_arrows(state, player
            ),
        "Snowhead Temple Frozen Green Door Pots (10)":
            lambda state:can_use_fire_arrows(state, player
            ),
        "Snowhead Temple Frozen Green Door Pots (11)":
            lambda state:can_use_fire_arrows(state, player
            ),
        "Snowhead Temple Frozen Green Door Pots (12)":
            lambda state:can_use_fire_arrows(state, player
            ),
        
        # Snowhead Temple Orange Door Push Block Pots - Requires Fire Arrows and (Small Key or Hookshot)
        "Snowhead Temple Orange Door Push Block Pots (0)":
            lambda state: (can_use_fire_arrows(state, player) and
                (
                    state.has("Small Key (Snowhead)", player) or
                    state.has("Hookshot", player)
                )
            ),  
        "Snowhead Temple Orange Door Push Block Pots (1)":
            lambda state: (can_use_fire_arrows(state, player) and
                (
                    state.has("Small Key (Snowhead)", player) or
                    state.has("Hookshot", player)
                )
            ),  
        "Snowhead Temple Orange Door Push Block Ghost Pots (1)":
            lambda state: (can_use_fire_arrows(state, player) and
                (
                    state.has("Small Key (Snowhead)", player) or
                    state.has("Hookshot", player)
                )
            ),  
        "Snowhead Temple Orange Door Push Block Ghost Pots (2)":
            lambda state: (can_use_fire_arrows(state, player) and
                (
                    state.has("Small Key (Snowhead)", player) or
                    state.has("Hookshot", player)
                )
            ),                         

        # Snowhead Temple Locked Grey Door Wolfos Pots - Requires 2 Small Keys
        "Snowhead Temple Locked Grey Door Wolfos Pots (0)":
            lambda state: (
                state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Locked Grey Door Wolfos Pots (1)":
            lambda state: (
                state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Locked Grey Door Wolfos Pots (2)":
            lambda state: (
                state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Locked Grey Door Wolfos Pots (3)":
            lambda state: (
                state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Locked Grey Door Wolfos Pots (4)":
            lambda state: (
                state.has("Small Key (Snowhead)", player, 2)
            ),
        
        # Snowhead Temple Goron Pound Puzzle Pots - Requires explosives and (Goron Mask or Fire Arrows)
        "Snowhead Temple Goron Pound Puzzle Pots (0)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 2) or
                    can_use_fire_arrows(state, player)
            ),
        "Snowhead Temple Goron Pound Puzzle Pots (1)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 2) or
                    can_use_fire_arrows(state, player)
            ),
        
        # Snowhead Temple Main Room Pots 2nd Floor Bridge - Basic temple access
        "Snowhead Temple Main Room Pots 2nd Floor Bridge (0)":
            lambda state: ( 
                    state.has("Small Key (Snowhead)", player, 2) or
                    can_use_fire_arrows(state, player)
            ),        
        "Snowhead Temple Main Room Pots 2nd Floor Bridge (1)":
            lambda state: ( 
                    state.has("Small Key (Snowhead)", player, 2) or
                    can_use_fire_arrows(state, player)
            ), 
        # Snowhead Temple Main Room 4th Floor Pots - Same as Boss Key Chest requirements
        "Snowhead Temple Main Room 4th Floor Pots (0)":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        can_use_fire_arrows(state, player) and
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                )
            ),
        "Snowhead Temple Main Room 4th Floor Pots (1)":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        can_use_fire_arrows(state, player) and
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                )
            ),
        
        # Snowhead Temple 4th Floor Wizzrobe Pots - Same as Boss Key Chest requirements
        "Snowhead Temple 4th Floor Wizzrobe Pots (0)":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        can_use_fire_arrows(state, player) and
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                )
            ),
        "Snowhead Temple 4th Floor Wizzrobe Pots (1)":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        can_use_fire_arrows(state, player) and
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                )
            ),
        "Snowhead Temple 4th Floor Wizzrobe Pots (2)":
            lambda state: (
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (    
                        can_use_fire_arrows(state, player) and
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                )
            ),
        
        # Goht Boss Room Pots - Top floor requirements plus Boss Key or Remains warp
        "Goht Boss Room Pots (0)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (1)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (2)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (3)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (4)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (5)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (6)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (7)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (8)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (9)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (10)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (11)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (12)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Goht Boss Room Pots (13)":
            lambda state: (
   
                can_use_fire_arrows(state, player) and 
                (
                    state.has("Small Key (Snowhead)", player, 3) or 
                    (
                        state.has("Small Key (Snowhead)", player, 2) and 
                        state.has("Hookshot", player) and 
                        can_reach_scarecrow(state, player)
                    )
                ) and 
                (
                    state.has("Boss Key (Snowhead)", player) or 
                    (
                        state.has("Goht's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),

        "Mountain Village Springtime Pots (0)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Pots (1)":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Springtime Pots (2)":
            lambda state: can_clear_snowhead(state, player),

        # Romani Ranch Pots
        
        # Romani Ranch Baby Chickens Pots
        "Romani Ranch Baby Chickens Pots (0)":
            lambda state: True,
        "Romani Ranch Baby Chickens Pots (1)":
            lambda state: True,
        
        # Romani Ranch Doggy Racetrack Pots
        "Romani Ranch Doggy Racetrack Pots (0)":
            lambda state: True,
        "Romani Ranch Doggy Racetrack Pots (1)":
            lambda state: True,
        "Romani Ranch Doggy Racetrack Pots (2)":
            lambda state: True,
        "Romani Ranch Doggy Racetrack Pots (3)":
            lambda state: True,
# Ocean Spider House Pots - All require region access, explosives, and hookshot
        
        # Ocean Spiderhouse Bottom Of Ramp Pots
        "Ocean Spiderhouse Bottom Of Ramp Pots (0)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Bottom Of Ramp Pots (1)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Bottom Of Ramp Pots (2)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Bottom Of Ramp Pots (3)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Ocean Spiderhouse Main Room Lower Pots
        "Ocean Spiderhouse Main Room Lower Pots (0)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Main Room Lower Pots (1)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Main Room Lower Pots (2)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Main Room Lower Pots (3)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Main Room Lower Pots (4)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Ocean Spiderhouse Crate Room Pots
        "Ocean Spiderhouse Crate Room Pots (0)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Crate Room Pots (1)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Crate Room Pots (2)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Crate Room Pots (3)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Crate Room Pots (4)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Crate Room Pots (5)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Crate Room Pots (6)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Crate Room Pots (7)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        
        # Ocean Spiderhouse Coloured Skulls Room Pots
        "Ocean Spiderhouse Coloured Skulls Room Pots (0)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Coloured Skulls Room Pots (1)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and 
                has_explosives(state, player) and 
                state.has("Hookshot", player)
            ),
        # Pinnacle Rock Pots - Requires reaching seahorse, bottle, and Zora Mask
        
        "Pinnacle Rock Pots (0)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (1)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (2)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (3)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (4)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (5)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (6)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (7)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (8)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (9)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
        "Pinnacle Rock Pots (10)":
            lambda state: (
                can_reach_seahorse(state, player) and 
                has_bottle(state, player) and 
                state.has("Zora Mask", player)
            ),
# Pirates' Fortress Pots
        
        # Pirates Fortress Sewers Cage Room Pots - Requires Goron to reach cage room
        "Pirates Fortress Sewers Cage Room Pots (0)":
            lambda state: (
                state.can_reach("Pirates' Fortress Sewers", 'Region', player) and 
                state.has("Goron Mask", player)
            ),
        "Pirates Fortress Sewers Cage Room Pots (1)":
            lambda state: (
                state.can_reach("Pirates' Fortress Sewers", 'Region', player) and 
                state.has("Goron Mask", player)
            ),
        
        # Pirates Fortress Sewers After Gate Hidden Ladder Pots
        "Pirates Fortress Sewers After Gate Hidden Ladder Pots (0)":
            lambda state: (
                state.can_reach("Pirates' Fortress Sewers", 'Region', player) and 
                (state.has("Goron Mask", player) or state.has("Hookshot", player))
            ),
        "Pirates Fortress Sewers After Gate Hidden Ladder Pots (1)":
            lambda state: (
                state.can_reach("Pirates' Fortress Sewers", 'Region', player) and 
                (state.has("Goron Mask", player) or state.has("Hookshot", player))
            ),
        
        # Pirates Fortress Sewers Exit Pots
        "Pirates Fortress Sewers Exit Pots (0)":
            lambda state: (
                state.can_reach("Pirates' Fortress Sewers", 'Region', player) and 
                (state.has("Goron Mask", player) or state.has("Hookshot", player))
            ),
        "Pirates Fortress Sewers Exit Pots (1)":
            lambda state: (
                state.can_reach("Pirates' Fortress Sewers", 'Region', player) and 
                (state.has("Goron Mask", player) or state.has("Hookshot", player))
            ),
        "Pirates Fortress Sewers Exit Pots (2)":
            lambda state: (
                state.can_reach("Pirates' Fortress Sewers", 'Region', player) and 
                (state.has("Goron Mask", player) or state.has("Hookshot", player))
            ),
        
        # Pirates Fortress Interior Underwater Chest Room Pots - Requires Hookshot and can_smack_hard
        "Pirates Fortress Interior Underwater Chest Room Pots (0)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        "Pirates Fortress Interior Underwater Chest Room Pots (1)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        "Pirates Fortress Interior Underwater Chest Room Pots (2)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        
        # Pirates Fortress Interior Room Past Green Guard Pots
        "Pirates Fortress Interior Room Past Green Guard Pots (0)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        "Pirates Fortress Interior Room Past Green Guard Pots (1)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        "Pirates Fortress Interior Room Past Green Guard Pots (2)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        
        # Pirates Fortress Interior Upper Beehive Room Pots
        "Pirates Fortress Interior Upper Beehive Room Pots (0)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        "Pirates Fortress Interior Upper Beehive Room Pots (1)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        
        # Pirates Fortress Interior Room Past Pink Guard Pots
        "Pirates Fortress Interior Room Past Pink Guard Pots (0)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        "Pirates Fortress Interior Room Past Pink Guard Pots (1)":
            lambda state: (
                state.has("Hookshot", player) and 
                can_smack_hard(state, player)
            ),
        # Zora Cape Pots
        
        # Zora Cape Like Like Pool Pots - Region access only
        "Zora Cape Like Like Pool Pots (0)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Like Like Pool Pots (1)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        
        # Zora Cape Owl Pots - Requires Zora Mask
        "Zora Cape Owl Pots (0)":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Owl Pots (1)":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Owl Pots (2)":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Owl Pots (3)":
            lambda state: state.has("Zora Mask", player),
# Great Bay Temple Pots
        
        # Great Bay Temple Above Whirlpool Pots
        "Great Bay Temple Above Whirlpool Pots (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Above Whirlpool Pots (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        
        # Great Bay Temple Room Behind 1F Waterfall 
        "Great Bay Temple Room Behind 1F Waterfall (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Room Behind 1F Waterfall (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Room Behind 1F Waterfall (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Room Behind 1F Waterfall (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        
        # Great Bay Temple Red Green Pipe Tunnel Room Pots 
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (0)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (1)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (2)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (3)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (4)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (5)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (6)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (7)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (8)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (9)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (10)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Red Green Pipe Tunnel Room Pots (11)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        
        # Great Bay Temple Caged Chest Room Pots 
        "Great Bay Temple Caged Chest Room Pots (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Pots (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Pots (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Pots (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Pots (4)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Pots (5)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Pots (6)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Pots (7)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        
        # Great Bay Temple Red Valve Underwater Pots - Basic temple access
        "Great Bay Temple Red Valve Underwater Pots (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Red Valve Underwater Pots (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Red Valve Underwater Pots (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Red Valve Underwater Pots (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        
        # Great Bay Temple Behind Locked Door Pots - Requires Small Key
        "Great Bay Temple Behind Locked Door Pots (0)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (1)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (2)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (3)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (4)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (5)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (6)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (7)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (8)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (9)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (10)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Behind Locked Door Pots (11)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        
        # Great Bay Temple Floating Eye Miniboss Room Pots - Requires Small Key only
        "Great Bay Temple Floating Eye Miniboss Room Pots (0)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Floating Eye Miniboss Room Pots (1)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Floating Eye Miniboss Room Pots (2)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Floating Eye Miniboss Room Pots (3)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Floating Eye Miniboss Room Pots (4)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Floating Eye Miniboss Room Pots (5)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Floating Eye Miniboss Room Pots (6)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        "Great Bay Temple Floating Eye Miniboss Room Pots (7)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                state.has("Small Key (Great Bay)", player)
            ),
        
        # Great Bay Temple Green Pipe Frozen Waterwheel Pots - Requires Ice Arrows
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (0)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (1)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (2)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (3)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (4)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (5)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (6)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        "Great Bay Temple Green Pipe Frozen Waterwheel Pots (7)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player)
            ),
        
        # Great Bay Temple Seesaw Room Pots - Requires both Ice and Fire Arrows
        "Great Bay Temple Seesaw Room Pots (0)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Seesaw Room Pots (1)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Seesaw Room Pots (2)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        
        # Great Bay Temple Pots Underneath Boss Door Platform - Requires both Ice and Fire Arrows
        "Great Bay Temple Pots Underneath Boss Door Platform (0)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Pots Underneath Boss Door Platform (1)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Pots Underneath Boss Door Platform (2)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Pots Underneath Boss Door Platform (3)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Pots Underneath Boss Door Platform (4)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Pots Underneath Boss Door Platform (5)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Pots Underneath Boss Door Platform (6)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        "Great Bay Temple Pots Underneath Boss Door Platform (7)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                can_use_ice_arrows(state, player) and
                can_use_fire_arrows(state, player)
            ),
        
        # Great Bay Temple Gyorg Pots - Requires Boss Key or Remains warp
        "Great Bay Temple Gyorg Pots (0)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg Pots (1)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg Pots (2)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg Pots (3)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg Pots (4)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg Pots (5)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg Pots (6)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
        "Great Bay Temple Gyorg Pots (7)":
            lambda state: (
                state.can_reach("Great Bay Temple", 'Region', player) and 
                (
                    state.has("Boss Key (Great Bay)", player) or 
                    (
                        state.has("Gyorg's Remains", player) and 
                        options.remains_allow_boss_warps.value
                    )
                )
            ),
# Pot Location Rules
        
        # IKANA GRAVEYARD POTS
        "Road To Ikana Scarecrow Pillar Pot":
            lambda state: (
                can_play_song("Epona's Song", state, player) and
                state.has("Hookshot", player) and
                can_reach_scarecrow(state, player)
            ),
        
        # Ikana Graveyard Day 1 Grave Pots
        "Ikana Graveyard Day 1 Grave Pots (0)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 1 Grave Pots (1)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 1 Grave Pots (2)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 1 Grave Pots (3)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 1 Grave Pots (4)":
            lambda state: state.has("Captain's Hat", player),
        
        # Ikana Graveyard Day 2 Entrance Grave Pot
        "Ikana Graveyard Day 2 Entrance Grave Pot":
            lambda state: state.has("Captain's Hat", player),
        
        # Ikana Graveyard Day 2 Invisible Path Entryway Pots
        "Ikana Graveyard Day 2 Invisible Path Entryway Pots (0)":
            lambda state: (
                state.has("Captain's Hat", player) and
                has_explosives(state, player)
            ),
        "Ikana Graveyard Day 2 Invisible Path Entryway Pots (1)":
            lambda state: (
                state.has("Captain's Hat", player) and
                has_explosives(state, player)
            ),
        
        # Ikana Graveyard Day 2 Invisible Path Pots
        "Ikana Graveyard Day 2 Invisible Path Pots (0)":
            lambda state: (
                state.has("Captain's Hat", player) and
                has_explosives(state, player) and
                can_use_lens(state, player)
            ),
        "Ikana Graveyard Day 2 Invisible Path Pots (1)":
            lambda state: (
                state.has("Captain's Hat", player) and
                has_explosives(state, player) and
                can_use_lens(state, player)
            ),
        "Ikana Graveyard Day 2 Invisible Path Pots (2)":
            lambda state: (
                state.has("Captain's Hat", player) and
                has_explosives(state, player) and
                can_use_lens(state, player)
            ),
        "Ikana Graveyard Day 2 Invisible Path Pots (3)":
            lambda state: (
                state.has("Captain's Hat", player) and
                has_explosives(state, player) and
                can_use_lens(state, player)
            ),
        
        # Ikana Graveyard Day 3 Pots
        "Ikana Graveyard Day 3 Pots (0)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (1)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (2)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (3)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (4)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (5)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (6)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (7)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (8)":
            lambda state: state.has("Captain's Hat", player),
        "Ikana Graveyard Day 3 Pots (9)":
            lambda state: state.has("Captain's Hat", player),
        
        # SECRET SHRINE POTS
        "Secret Shrine Entrance Pots (0)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Entrance Pots (1)":
            lambda state: can_use_light_arrows(state, player),
        "Secret Shrine Entrance Pots (2)":
            lambda state: can_use_light_arrows(state, player),
        
        "Secret Shrine Underwater Pots (0)":
            lambda state: (
                can_use_light_arrows(state, player) and
                can_smack_hard(state, player) and
                state.has("Zora Mask", player),
            ),
        "Secret Shrine Underwater Pots (1)":
            lambda state: (
                can_use_light_arrows(state, player) and
                can_smack_hard(state, player) and
                state.has("Zora Mask", player),
            ),
        "Secret Shrine Underwater Pots (2)":
            lambda state: (
                can_use_light_arrows(state, player) and
                can_smack_hard(state, player) and
                state.has("Zora Mask", player),
            ),
        "Secret Shrine Underwater Pots (3)":
            lambda state: (
                can_use_light_arrows(state, player) and
                can_smack_hard(state, player) and
                state.has("Zora Mask", player),
            ),
        "Secret Shrine Underwater Pots (4)":
            lambda state: (
                can_use_light_arrows(state, player) and
                can_smack_hard(state, player) and
                state.has("Zora Mask", player),
            ),
        "Secret Shrine Underwater Pots (5)":
            lambda state: (
                can_use_light_arrows(state, player) and
                can_smack_hard(state, player) and
                state.has("Zora Mask", player),
            ),
        
        # IKANA CASTLE POTS
        "Ikana Castle Frozen Eyes Room Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                )
            ),
        "Ikana Castle Frozen Eyes Room Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                )
            ),
        
        "Ikana Castle Left Side Falling Ceiling Room Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                )
            ),
        "Ikana Castle Left Side Falling Ceiling Room Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                )
            ),
        
        "Ikana Castle Left Side Broken Floor Room Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                ) and
                state.has("Deku Mask", player)
            ),
        "Ikana Castle Left Side Broken Floor Room Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                ) and
                state.has("Deku Mask", player)
            ),
        "Ikana Castle Left Side Broken Floor Room Pots (2)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                ) and
                state.has("Deku Mask", player)
            ),
        "Ikana Castle Left Side Broken Floor Room Pots (3)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                ) and
                state.has("Deku Mask", player)
            ),
        
        "Ikana Castle Left Side Staircase Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                ) and
                state.has("Deku Mask", player)
            ),
        "Ikana Castle Left Side Staircase Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                ) and
                state.has("Deku Mask", player)
            ),
        
        "Ikana Castle Right Side Staircase Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                )
            ),
        "Ikana Castle Right Side Staircase Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                can_use_fire_arrows(state, player) and
                (
                    can_use_light_arrows(state, player) or
                    has_mirror_shield(state, player)
                )
            ),
        
        # Ikana Castle Throne Room Pots
        "Ikana Castle Throne Room Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Ikana Castle Throne Room Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Ikana Castle Throne Room Pots (2)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Ikana Castle Throne Room Pots (3)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Ikana Castle Throne Room Pots (4)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Ikana Castle Throne Room Pots (5)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Ikana Castle Throne Room Pots (6)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        "Ikana Castle Throne Room Pots (7)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                    can_use_light_arrows(state, player) or
                    (
                        has_mirror_shield(state, player) and
                        state.has("Deku Mask", player) and
                        can_use_lens(state, player) and
                        can_use_fire_arrows(state, player) and
                        state.has("Powder Keg", player) and
                        state.has("Goron Mask", player)
                    )
                )
            ),
        
        # BENEATH THE WELL POTS
        "Well Left Side Back Room Pots (0)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_afford_price(state, player, 100) or
                    state.has("Mask of Scents", player)
                )
            ),
        "Well Left Side Back Room Pots (1)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_afford_price(state, player, 100) or
                    state.has("Mask of Scents", player)
                )
            ),
        "Well Left Side Back Room Pots (2)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_afford_price(state, player, 100) or
                    state.has("Mask of Scents", player)
                )
            ),
        "Well Left Side Back Room Pots (3)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_afford_price(state, player, 100) or
                    state.has("Mask of Scents", player)
                )
            ),
        "Well Left Side Back Room Pots (4)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_afford_price(state, player, 100) or
                    state.has("Mask of Scents", player)
                )
            ),
        
        "Well Right Side Before Chest Room Pots (0)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (1)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (2)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (3)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (4)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (5)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (6)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (7)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (8)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Well Right Side Before Chest Room Pots (9)":
            lambda state: (
                state.has("Gibdo Mask", player) and
                has_bottle(state, player) and
                (
                    can_plant_beans(state, player) or
                    can_use_light_arrows(state, player)
                )
            ),
        
        # Well Big Poe Pots
        "Well Big Poe Pots (0)":
            lambda state: (
                (
                    state.has("Gibdo Mask", player) and
                    has_bottle(state, player) and
                    can_plant_beans(state, player) and
                    (
                        state.has("Progressive Bomb Bag", player) or
                        (
                            state.has("Captain's Hat", player) and
                            state.has("Progressive Bow", player)
                        )
                    )
                ) or
                (
                    can_use_light_arrows(state, player) and
                    can_use_fire_arrows(state, player)
                )
            ),
        "Well Big Poe Pots (1)":
            lambda state: (
                (
                    state.has("Gibdo Mask", player) and
                    has_bottle(state, player) and
                    can_plant_beans(state, player) and
                    (
                        state.has("Progressive Bomb Bag", player) or
                        (
                            state.has("Captain's Hat", player) and
                            state.has("Progressive Bow", player)
                        )
                    )
                ) or
                (
                    can_use_light_arrows(state, player) and
                    can_use_fire_arrows(state, player)
                )
            ),
        "Well Big Poe Pots (2)":
            lambda state: (
                (
                    state.has("Gibdo Mask", player) and
                    has_bottle(state, player) and
                    can_plant_beans(state, player) and
                    (
                        state.has("Progressive Bomb Bag", player) or
                        (
                            state.has("Captain's Hat", player) and
                            state.has("Progressive Bow", player)
                        )
                    )
                ) or
                (
                    can_use_light_arrows(state, player) and
                    can_use_fire_arrows(state, player)
                )
            ),
        "Well Big Poe Pots (3)":
            lambda state: (
                (
                    state.has("Gibdo Mask", player) and
                    has_bottle(state, player) and
                    can_plant_beans(state, player) and
                    (
                        state.has("Progressive Bomb Bag", player) or
                        (
                            state.has("Captain's Hat", player) and
                            state.has("Progressive Bow", player)
                        )
                    )
                ) or
                (
                    can_use_light_arrows(state, player) and
                    can_use_fire_arrows(state, player)
                )
            ),
        
        # STONE TOWER POTS
        #Stone Tower Climb Pots
        "Stone Tower Climb Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Climb Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player)
            ),
            #Stone Tower Lower Scarecrow Pots            
        "Stone Tower Lower Scarecrow Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (2)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (3)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (4)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (5)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (6)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (7)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (8)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (9)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (10)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Lower Scarecrow Pots (11)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and 
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
                
            ),
        
        # Stone Tower Upper Scarecrow Pots
        "Stone Tower Upper Scarecrow Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (2)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (3)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (4)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (5)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (6)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (7)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Upper Scarecrow Pots (8)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        
        # Stone Tower Owl Pots
        "Stone Tower Owl Pots (0)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Owl Pots (1)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Owl Pots (2)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        "Stone Tower Owl Pots (3)":
            lambda state: (
                can_use_ice_arrows(state, player) and
                can_play_song("Elegy of Emptiness", state, player) and
                state.has("Goron Mask", player) and
                state.has("Zora Mask", player) and
                state.has("Hookshot", player)
            ),
        
        # STONE TOWER TEMPLE POTS
        "Stone Tower Temple Entrance Pots (0)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Entrance Pots (1)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        
        "Stone Tower Temple Lower Basement Armos Pots (0)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Lower Basement Armos Pots (1)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Lower Basement Armos Pots (2)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Lower Basement Armos Pots (3)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Lower Basement Armos Pots (4)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Lower Basement Armos Pots (5)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Lower Basement Armos Pots (6)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Lower Basement Armos Pots (7)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        
        "Stone Tower Temple Right Side Near Locked Door Pots (0)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and
                (
                    state.has("Small Key (Stone Tower)", player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Stone Tower Temple Right Side Near Locked Door Pots (1)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and
                (
                    state.has("Small Key (Stone Tower)", player) or
                    can_use_light_arrows(state, player)
                )
            ),
        
        "Stone Tower Temple Right Side Underwater Pots (0)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and
                (
                    state.has("Small Key (Stone Tower)", player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Stone Tower Temple Right Side Underwater Pots (1)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and
                (
                    state.has("Small Key (Stone Tower)", player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Stone Tower Temple Right Side Underwater Pots (2)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and
                (
                    state.has("Small Key (Stone Tower)", player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Stone Tower Temple Right Side Underwater Pots (3)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and
                (
                    state.has("Small Key (Stone Tower)", player) or
                    can_use_light_arrows(state, player)
                )
            ),
        "Stone Tower Temple Right Side Underwater Pots (4)":
            lambda state: (
                state.can_reach("Stone Tower Temple", 'Region', player) and
                (
                    state.has("Small Key (Stone Tower)", player) or
                    can_use_light_arrows(state, player)
                )
            ),
        
        # Stone Tower Temple Mirror Room Pots
        "Stone Tower Temple Mirror Room Pots (0)":
            lambda state: (
                (
                    state.has("Small Key (Stone Tower)", player, 2) and
                    has_mirror_shield(state, player)
                ) or
                (
                    can_use_light_arrows(state, player) and
                    state.has("Small Key (Stone Tower)", player, 1)
                )
            ),
        "Stone Tower Temple Mirror Room Pots (1)":
            lambda state: (
                (
                    state.has("Small Key (Stone Tower)", player, 2) and
                    has_mirror_shield(state, player)
                ) or
                (
                    can_use_light_arrows(state, player) and
                    state.has("Small Key (Stone Tower)", player, 1)
                )
            ),
        
        # Stone Tower Temple Deku Updraft Pots
        "Stone Tower Temple Deku Updraft Pots (0)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Stone Tower Temple Deku Updraft Pots (1)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Stone Tower Temple Deku Updraft Pots (2)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Stone Tower Temple Deku Updraft Pots (3)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        
        # Stone Tower Temple Lower Spike Roller Pots
        "Stone Tower Temple Lower Spike Roller Pots (0)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Lower Spike Roller Pots (1)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Lower Spike Roller Pots (2)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Lower Spike Roller Pots (3)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Lower Spike Roller Pots (4)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Lower Spike Roller Pots (5)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Lower Spike Roller Pots (6)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        "Stone Tower Temple Lower Spike Roller Pots (7)":
            lambda state: (
                state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and
                state.has("Goron Mask", player)
            ),
        
        # INVERTED STONE TOWER POTS
        "Inverted Stone Tower Bean Pots (0)":
            lambda state: (
                state.can_reach("Stone Tower (Inverted)", 'Region', player) and
                can_plant_beans(state, player)
            ),
        "Inverted Stone Tower Bean Pots (1)":
            lambda state: (
                state.can_reach("Stone Tower (Inverted)", 'Region', player) and
                can_plant_beans(state, player)
            ),
        "Inverted Stone Tower Bean Pots (2)":
            lambda state: (
                state.can_reach("Stone Tower (Inverted)", 'Region', player) and
                can_plant_beans(state, player)
            ),
        "Inverted Stone Tower Bean Pots (3)":
            lambda state: (
                state.can_reach("Stone Tower (Inverted)", 'Region', player) and
                can_plant_beans(state, player)
            ),
        "Inverted Stone Tower Bean Pots (4)":
            lambda state: (
                state.can_reach("Stone Tower (Inverted)", 'Region', player) and
                can_plant_beans(state, player)
            ),
        
        # Inverted Stone Tower Temple Updraft Pots
        "Inverted Stone Tower Temple Updraft Pots (0)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Inverted Stone Tower Temple Updraft Pots (1)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Inverted Stone Tower Temple Updraft Pots (2)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Inverted Stone Tower Temple Updraft Pots (3)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Inverted Stone Tower Temple Updraft Pots (4)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        "Inverted Stone Tower Temple Updraft Pots (5)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest", 'Location', player) and
                state.has("Deku Mask", player)
            ),
        
        # Inverted Stone Tower Temple Miniboss Pots
        "Inverted Stone Tower Temple Miniboss Pots (0)":
            lambda state: (
                can_use_light_arrows(state, player) and
                state.has("Deku Mask", player) and
                state.has("Small Key (Stone Tower)", player, 3)
            ),
        "Inverted Stone Tower Temple Miniboss Pots (1)":
            lambda state: (
                can_use_light_arrows(state, player) and
                state.has("Deku Mask", player) and
                state.has("Small Key (Stone Tower)", player, 3)
            ),
        "Inverted Stone Tower Temple Miniboss Pots (2)":
            lambda state: (
                can_use_light_arrows(state, player) and
                state.has("Deku Mask", player) and
                state.has("Small Key (Stone Tower)", player, 3)
            ),
        "Inverted Stone Tower Temple Miniboss Pots (3)":
            lambda state: (
                can_use_light_arrows(state, player) and
                state.has("Deku Mask", player) and
                state.has("Small Key (Stone Tower)", player, 3)
            ),
        
        # Inverted Stone Tower Temple Lower Bridge Room Pots
        "Inverted Stone Tower Temple Lower Bridge Room Pots (0)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player),
        "Inverted Stone Tower Temple Lower Bridge Room Pots (1)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player),
        
        # Inverted Stone Tower Temple Small Poe Room Pots
        "Inverted Stone Tower Temple Small Poe Room Pots (0)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Death Armos Maze Chest", 'Location', player),
        "Inverted Stone Tower Temple Small Poe Room Pots (1)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Death Armos Maze Chest", 'Location', player),
        "Inverted Stone Tower Temple Small Poe Room Pots (2)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Death Armos Maze Chest", 'Location', player),
        "Inverted Stone Tower Temple Small Poe Room Pots (3)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Death Armos Maze Chest", 'Location', player),
        
        # Inverted Stone Tower Temple Wizzrobe Room Pots
        "Inverted Stone Tower Temple Wizzrobe Room Pots (0)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Gomess Chest", 'Location', player) and
                can_smack_hard(state, player)
            ),
        "Inverted Stone Tower Temple Wizzrobe Room Pots (1)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Gomess Chest", 'Location', player) and
                can_smack_hard(state, player)
            ),
        "Inverted Stone Tower Temple Wizzrobe Room Pots (2)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Gomess Chest", 'Location', player) and
                can_smack_hard(state, player)
            ),
        "Inverted Stone Tower Temple Wizzrobe Room Pots (3)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Gomess Chest", 'Location', player) and
                can_smack_hard(state, player)
            ),
        "Inverted Stone Tower Temple Wizzrobe Room Pots (4)":
            lambda state: (
                state.can_reach("Stone Tower Temple Inverted Gomess Chest", 'Location', player) and
                can_smack_hard(state, player)
            ),
        
        # Inverted Stone Tower Temple Pre Boss Pots (Flying)
        "Inverted Stone Tower Temple Pre Boss Pots (Flying) (0)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (Flying) (1)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (Flying) (2)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (Flying) (3)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        
        # Inverted Stone Tower Temple Pre Boss Pots
        "Inverted Stone Tower Temple Pre Boss Pots (0)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (1)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (2)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (3)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (4)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (5)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (6)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Inverted Stone Tower Temple Pre Boss Pots (7)":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        
        # MOON POTS
        "Moon Goron Trial Pots (0)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (1)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (2)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (3)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (4)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (5)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (6)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (7)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (8)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (9)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (10)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (11)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (12)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (13)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        "Moon Goron Trial Pots (14)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),
        
        # Moon Link Trial Pots
        "Moon Link Trial Pots (0)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        "Moon Link Trial Pots (1)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        "Moon Link Trial Pots (2)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        "Moon Link Trial Pots (3)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        "Moon Link Trial Pots (4)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        "Moon Link Trial Pots (5)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        "Moon Link Trial Pots (6)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        "Moon Link Trial Pots (7)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) and
                has_bombchus(state, player) and
                state.has("Progressive Bow", player)
            ),
        
        # Majora Arena Pots
        "Majora Arena Pots (0)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                can_smack_hard(state, player) and
                (
                    (
                        state.has("Zora Mask", player) or
                        has_mirror_shield(state, player)
                    ) and
                    can_use_light_arrows(state, player) or
                    (
                        state.has("Fierce Deity's Mask", player) and
                        state.has("Progressive Magic", player)
                    )
                ) and
                has_enough_remains(state, player, options.majora_remains_required.value)
            ),
        "Majora Arena Pots (1)":
            lambda state: (
                state.can_reach("The Moon", 'Region', player) and
                can_smack_hard(state, player) and
                (
                    (
                        state.has("Zora Mask", player) or
                        has_mirror_shield(state, player)
                    ) and
                    can_use_light_arrows(state, player) or
                    (
                        state.has("Fierce Deity's Mask", player) and
                        state.has("Progressive Magic", player)
                    )
                ) and
                has_enough_remains(state, player, options.majora_remains_required.value)
            ),
        
        # Termina Field Hitspots Logic
        # Clock Town Hitspots Logic

        # South Clock Town Targets Hitspot
        "South Clock Town Targets Hitspot (0)":
            lambda state: has_projectiles(state, player),
        "South Clock Town Targets Hitspot (1)":
            lambda state: has_projectiles(state, player),
        "South Clock Town Targets Hitspot (2)":
            lambda state: has_projectiles(state, player),

        # East Clock Town Targets And Basket Hitspots
        "East Clock Town Targets And Basket Hitspots (0)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (1)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (2)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (3)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (4)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (5)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (6)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (7)":
            lambda state: True,
        "East Clock Town Targets And Basket Hitspots (8)":
            lambda state: True,

        # Sword School Gong
        "Sword School Gong":
            lambda state: state.has("Progressive Sword", player),

        # Stock Pot Inn Mask Hitspot
        "Stock Pot Inn Mask Hitspot (0)":
            lambda state:(             
                state.has("Zora Mask", player) and 
                state.has("Progressive Magic", player)),
        "Stock Pot Inn Mask Hitspot (1)":
            lambda state:(             
                state.has("Zora Mask", player) and 
                state.has("Progressive Magic", player)),
        "Stock Pot Inn Mask Hitspot (2)":
            lambda state:(             
                state.has("Zora Mask", player) and 
                state.has("Progressive Magic", player)),

        # Termina Field West Wall Hitspot
        "Termina Field West Wall Hitspot (0)":
            lambda state: True,
        "Termina Field West Wall Hitspot (1)":
            lambda state: True,
        "Termina Field West Wall Hitspot (2)":
            lambda state: True,

        # Termina Field Above West Clock Town Entry Hitspot
        "Termina Field Above West Clock Town Entry Hitspot (0)":
            lambda state: has_projectiles(state, player),
        "Termina Field Above West Clock Town Entry Hitspot (1)":
            lambda state: has_projectiles(state, player),
        "Termina Field Above West Clock Town Entry Hitspot (2)":
            lambda state: has_projectiles(state, player),

        # Skull Kid Drawing Hitspot
        "Skull Kid Drawing Hitspot (0)":
            lambda state: True,
        "Skull Kid Drawing Hitspot (1)":
            lambda state: True,
        "Skull Kid Drawing Hitspot (2)":
            lambda state: True,
        
        # Romani Ranch Hitspots
        "Romani Ranch Baby Cuccoos Hitspots (0)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Romani Ranch Baby Cuccoos Hitspots (1)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Romani Ranch Baby Cuccoos Hitspots (2)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Romani Ranch Baby Cuccoos Hitspots (3)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Romani Ranch Baby Cuccoos Hitspots (4)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Romani Ranch Baby Cuccoos Hitspots (5)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_projectiles(state, player)
            ),
        
        # Swamp Spider House Hitspots
        "Swamp Spiderhouse Totem Eye Hitspots (0)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (1)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (2)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (3)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (4)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (5)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (6)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (7)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (8)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (9)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (10)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Swamp Spiderhouse Totem Eye Hitspots (11)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_projectiles(state, player)
            ),
        
        # Ocean Spider House Hitspots
        "Ocean Spiderhouse Mask Hitspots (0)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (1)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (2)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (3)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (4)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (5)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (6)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (7)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Ocean Spiderhouse Mask Hitspots (8)":
            lambda state: (
                state.can_reach("Ocean Spider House", 'Region', player) and
                state.has("Hookshot", player)
            ),
        
        # Pirates Fortress Interior Hitspots
        "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (0)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (1)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (2)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (3)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (4)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (5)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        
        "Pirates Fortress Interior Indoor Pirate Flag Eye Hitspot (0)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Pirates Fortress Interior Indoor Pirate Flag Eye Hitspot (1)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Pirates Fortress Interior Indoor Pirate Flag Eye Hitspot (2)":
            lambda state: (
                state.can_reach("Pirates' Fortress (Interior)", 'Region', player) and
                has_projectiles(state, player)
            ),
        
        # Ikana Graveyard Hitspots
        "Ikana Graveyard Lantern Hitspots (0)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (1)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (2)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (3)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (4)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (5)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (6)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (7)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (8)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (9)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (10)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),
        "Ikana Graveyard Lantern Hitspots (11)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_projectiles(state, player)
            ),

        # FREESTANDING RUPEES

        # Termina Field Song Wall

        "Termina Field 6am Songwall (0)":
        lambda state: True,
        "Termina Field 6am Songwall (1)":
            lambda state: True,
        "Termina Field 6am Songwall (2)":
            lambda state: True,
        "Termina Field 7am Songwall (0)":
            lambda state: True,
        "Termina Field 7am Songwall (1)":
            lambda state: True,
        "Termina Field 7am Songwall (2)":
            lambda state: True,
        "Termina Field 8am Songwall (0)":
            lambda state: True,
        "Termina Field 8am Songwall (1)":
            lambda state: True,
        "Termina Field 8am Songwall (2)":
            lambda state: True,
        "Termina Field 9am Songwall (0)":
            lambda state: True,
        "Termina Field 9am Songwall (1)":
            lambda state: True,
        "Termina Field 9am Songwall (2)":
            lambda state: True,
        "Termina Field 10am Songwall (0)":
            lambda state: True,
        "Termina Field 10am Songwall (1)":
            lambda state: True,
        "Termina Field 10am Songwall (2)":
            lambda state: True,
        "Termina Field 11am Songwall (0)":
            lambda state: True,
        "Termina Field 11am Songwall (1)":
            lambda state: True,
        "Termina Field 11am Songwall (2)":
            lambda state: True,
        "Termina Field 12pm Songwall (0)":
            lambda state: True,
        "Termina Field 12pm Songwall (1)":
            lambda state: True,
        "Termina Field 12pm Songwall (2)":
            lambda state: True,
        "Termina Field 1pm Songwall (0)":
            lambda state: True,
        "Termina Field 1pm Songwall (1)":
            lambda state: True,
        "Termina Field 1pm Songwall (2)":
            lambda state: True,
        "Termina Field 2pm Songwall (0)":
            lambda state: True,
        "Termina Field 2pm Songwall (1)":
            lambda state: True,
        "Termina Field 2pm Songwall (2)":
            lambda state: True,
        "Termina Field 3pm Songwall (0)":
            lambda state: True,
        "Termina Field 3pm Songwall (1)":
            lambda state: True,
        "Termina Field 3pm Songwall (2)":
            lambda state: True,
        "Termina Field 4pm Songwall (0)":
            lambda state: True,
        "Termina Field 4pm Songwall (1)":
            lambda state: True,
        "Termina Field 4pm Songwall (2)":
            lambda state: True,
        "Termina Field 5pm Songwall (0)":
            lambda state: True,
        "Termina Field 5pm Songwall (1)":
            lambda state: True,
        "Termina Field 5pm Songwall (2)":
            lambda state: True,
        "Termina Field 6pm Songwall (0)":
            lambda state: True,
        "Termina Field 6pm Songwall (1)":
            lambda state: True,
        "Termina Field 6pm Songwall (2)":
            lambda state: True,
        "Termina Field 7pm Songwall (0)":
            lambda state: True,
        "Termina Field 7pm Songwall (1)":
            lambda state: True,
        "Termina Field 7pm Songwall (2)":
            lambda state: True,
        "Termina Field 8pm Songwall (0)":
            lambda state: True,
        "Termina Field 8pm Songwall (1)":
            lambda state: True,
        "Termina Field 8pm Songwall (2)":
            lambda state: True,
        "Termina Field 9pm Songwall (0)":
            lambda state: True,
        "Termina Field 9pm Songwall (1)":
            lambda state: True,
        "Termina Field 9pm Songwall (2)":
            lambda state: True,
        "Termina Field 10pm Songwall (0)":
            lambda state: True,
        "Termina Field 10pm Songwall (1)":
            lambda state: True,
        "Termina Field 10pm Songwall (2)":
            lambda state: True,
        "Termina Field 11pm Songwall (0)":
            lambda state: True,
        "Termina Field 11pm Songwall (1)":
            lambda state: True,
        "Termina Field 11pm Songwall (2)":
            lambda state: True,
        "Termina Field 12am Songwall (0)":
            lambda state: True,
        "Termina Field 12am Songwall (1)":
            lambda state: True,
        "Termina Field 12am Songwall (2)":
            lambda state: True,
        "Termina Field 1am Songwall (0)":
            lambda state: True,
        "Termina Field 1am Songwall (1)":
            lambda state: True,
        "Termina Field 1am Songwall (2)":
            lambda state: True,
        "Termina Field 2am Songwall (0)":
            lambda state: True,
        "Termina Field 2am Songwall (1)":
            lambda state: True,
        "Termina Field 2am Songwall (2)":
            lambda state: True,
        "Termina Field 3am Songwall (0)":
            lambda state: True,
        "Termina Field 3am Songwall (1)":
            lambda state: True,
        "Termina Field 3am Songwall (2)":
            lambda state: True,
        "Termina Field 4am Songwall (0)":
            lambda state: True,
        "Termina Field 4am Songwall (1)":
            lambda state: True,
        "Termina Field 4am Songwall (2)":
            lambda state: True,
        "Termina Field 5am Songwall (0)":
            lambda state: True,
        "Termina Field 5am Songwall (1)":
            lambda state: True,
        "Termina Field 5am Songwall (2)":
            lambda state: True,

        # Laundry Pool Night 2 Rupees
        "Laundry Pool Night 2 Rupees (0)":
            lambda state: True,
        "Laundry Pool Night 2 Rupees (1)":
            lambda state: True,
        "Laundry Pool Night 2 Rupees (2)":
            lambda state: True,


        # Termina Field Easter Pillar Rupees
        "Termina Field Easter Pillar Rupees":
            lambda state: state.can_reach("Termina Field", 'Region', player),

        # Termina Field Tree Rupees
        "Termina Field Tree Rupees (0)":
            lambda state: state.can_reach("Termina Field", 'Region', player),
        "Termina Field Tree Rupees (1)":
            lambda state: state.can_reach("Termina Field", 'Region', player),

        # Termina Field Song Guay Rupees
        "Termina Field Song Guay Rupees (0)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (1)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (2)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (3)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (4)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (5)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (6)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (7)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (8)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (9)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (10)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (11)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (12)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (13)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (14)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (15)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (16)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (17)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (18)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),
        "Termina Field Song Guay Rupees (19)":
            lambda state: (
                state.can_reach("Termina Field", 'Region', player) and
                (can_play_song("Sonata of Awakening", state, player) or
                 can_play_song("Goron Lullaby", state, player) or
                 can_play_song("New Wave Bossa Nova", state, player))
            ),

        # Termina Field Song Guay Goron/Epona Rupees
        "Termina Field Song Guay Goron/Epona Rupees (0)":
            lambda state: state.can_reach("Termina Field", 'Region', player),
        "Termina Field Song Guay Goron/Epona Rupees (1)":
            lambda state: state.can_reach("Termina Field", 'Region', player),
        "Termina Field Song Guay Goron/Epona Rupees (2)":
            lambda state: state.can_reach("Termina Field", 'Region', player),

        # Deku PlayGround Day 1 Rupees
        "Deku PlayGround Day 1 Rupees (0)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 1 Rupees (1)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 1 Rupees (2)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 1 Rupees (3)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 1 Rupees (4)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 1 Rupees (5)":
            lambda state: state.has("Deku Mask", player),

        # Deku PlayGround Day 2 Rupees
        "Deku PlayGround Day 2 Rupees (0)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 2 Rupees (1)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 2 Rupees (2)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 2 Rupees (3)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 2 Rupees (4)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 2 Rupees (5)":
            lambda state: state.has("Deku Mask", player),

        # Deku PlayGround Day 3 Rupees
        "Deku PlayGround Day 3 Rupees (0)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 3 Rupees (1)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 3 Rupees (2)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 3 Rupees (3)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 3 Rupees (4)":
            lambda state: state.has("Deku Mask", player),
        "Deku PlayGround Day 3 Rupees (5)":
            lambda state: state.has("Deku Mask", player),

        # Southern Swamp Flower Rupees
        "Southern Swamp Flower Rupees (0)":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp Flower Rupees (1)":
            lambda state: state.has("Deku Mask", player),

        "Southern Swamp Witch Shop Rupee (1)":
            lambda state: True,            

        # Deku Palace Right Side Rupees
        "Deku Palace Right Side Rupees (0)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (1)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (2)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (3)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (4)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (5)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (6)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (7)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (8)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (9)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (10)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (11)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Right Side Rupees (12)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),

        # Deku Palace Left Side Rupees
        "Deku Palace Left Side Rupees (0)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (1)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (2)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (3)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (4)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (5)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (6)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (7)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (8)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (9)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),
        "Deku Palace Left Side Rupees (10)":
            lambda state: state.can_reach("Deku Palace", 'Region', player),

        # Deku Butler Rupees
        "Deku Butler Rupees (0)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (1)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (2)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (3)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (4)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (5)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (6)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (7)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (8)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (9)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (10)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (11)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (12)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (13)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (14)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (15)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (16)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (17)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (18)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (19)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (20)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (21)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (22)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (23)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (24)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (25)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (26)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (27)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (28)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),
        "Deku Butler Rupees (29)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                can_clear_woodfall(state, player) and
                state.has("Progressive Sword", player) and
                has_bottle(state, player)
            ),

        # Woodfall Stump Rupee
        "Woodfall Stump Rupee":
            lambda state: state.can_reach("Woodfall", 'Region', player),

        # Romani Ranch Haystack Rupees
        "Romani Ranch Haystack Rupees (0)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),
        "Romani Ranch Haystack Rupees (1)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),

        # Woodfall Temple Pre Boss Rupees 
        "Woodfall Temple Pre Boss Rupees (0)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Pre Boss Rupees (1)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Pre Boss Rupees (2)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Pre Boss Rupees (3)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Pre Boss Rupees (4)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and
                state.has("Progressive Bow", player)
            ),
        "Woodfall Temple Pre Boss Rupees (5)":
            lambda state: (
                state.can_reach("Woodfall Temple", 'Region', player) and
                state.has("Progressive Bow", player)
            ),

        # Snowhead Temple Icicle Rupees
        "Snowhead Temple Icicle Rupees (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Icicle Rupees (1)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Icicle Rupees (2)":
            lambda state: has_explosives(state, player),

        # Mountain Village Spring Boulder Under Smithy Rupee
        "Mountain Village Spring Boulder Under Smithy Rupee":
            lambda state: can_clear_snowhead(state, player),

        # Twin Islands Spring Underwater Rupees
        "Twin Islands Spring Underwater Rupees (0)":
            lambda state: (
                state.can_reach("Twin Islands", 'Region', player) and
                can_clear_snowhead(state, player) and
                state.has("Zora Mask", player)
            ),
        "Twin Islands Spring Underwater Rupees (1)":
            lambda state: (
                state.can_reach("Twin Islands", 'Region', player) and
                can_clear_snowhead(state, player) and
                state.has("Zora Mask", player)
            ),
        "Twin Islands Spring Underwater Rupees (2)":
            lambda state: (
                state.can_reach("Twin Islands", 'Region', player) and
                can_clear_snowhead(state, player) and
                state.has("Zora Mask", player)
            ),
        "Twin Islands Spring Underwater Rupees (3)":
            lambda state: (
                state.can_reach("Twin Islands", 'Region', player) and
                can_clear_snowhead(state, player) and
                state.has("Zora Mask", player)
            ),

        # Great Bay Temple Waterwheel Rupees
        "Great Bay Temple Waterwheel Rupees (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Waterwheel Rupees (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Waterwheel Rupees (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Waterwheel Rupees (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Waterwheel Rupees (4)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),

        # Great Bay Temple Caged Chest Room Underwater Rupees
        "Great Bay Temple Caged Chest Room Underwater Rupees (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Caged Chest Room Underwater Rupees (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),

        # Ikana Graveyard Day 2 Rupees
        "Ikana Graveyard Day 2 Rupees (0)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Day 2 Rupees (1)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Day 2 Rupees (2)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Day 2 Rupees (3)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Day 2 Rupees (4)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Day 2 Rupees (5)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Day 2 Rupees (6)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),

        # Secret Shrine Rupees
        "Secret Shrine Rupees (0)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (1)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (2)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (3)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (4)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (5)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (6)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (7)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (8)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (9)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (10)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (11)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (12)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (13)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (14)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (15)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),
        "Secret Shrine Rupees (16)":
            lambda state: (
                state.can_reach("Ikana Canyon", 'Region', player) and
                (state.has("Zora Mask", player) or can_plant_beans(state, player))
            ),

        # Stone Tower Bridge Room Rupees
        "Stone Tower Bridge Room Rupees (0)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Bridge Room Rupees (1)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Bridge Room Rupees (2)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Bridge Room Rupees (3)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Bridge Room Rupees (4)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Bridge Room Rupees (5)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Bridge Room Rupees (6)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Bridge Room Rupees (7)":
            lambda state: (state.has("Stone Tower Temple Small Key", player, 2) and 
                has_mirror_shield(state, player)
                or 
                can_use_light_arrows(state, player)
            ),
        # Stone Tower Eyegore Room Light Block Rupees
        "Stone Tower Eyegore Room Light Block Rupees (0)":
            lambda state: (
                can_use_light_arrows(state, player)
            ),
        "Stone Tower Eyegore Room Light Block Rupees (1)":
            lambda state: (
                can_use_light_arrows(state, player)
            ),

        # Inverted Stone Tower Right Side Light Block Rupees
        "Inverted Stone Tower Right Side Light Block Rupees (0)":
            lambda state: True,
        "Inverted Stone Tower Right Side Light Block Rupees (1)":
            lambda state: True,
        # Inverted Stone Tower Dexihand Rupees
        "Inverted Stone Tower Dexihand Rupees (0)":
            lambda state: True,
        "Inverted Stone Tower Dexihand Rupees (1)":
            lambda state: True,
        "Inverted Stone Tower Dexihand Rupees (2)":
            lambda state: True,

        # Inverted Stone Tower Pre Boss Rupees
        "Inverted Stone Tower Pre Boss Rupees (0)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (1)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (2)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (3)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (4)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (5)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (6)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (7)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (8)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (9)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),
        "Inverted Stone Tower Pre Boss Rupees (10)":
            lambda state: (
                state.has("Stone Tower Temple Small Key", player, 3) and
                state.has("Deku Mask", player),
            ),

        # INVISIBLE RUPEES

        # Termina Field Invisible Rupee Over Ramp Near Fountains
        "Termina Field Invisible Rupee Over Ramp Near Fountains":
            lambda state: True,

        # Termina Field Fountain Rupees
        "Termina Field Fountain Rupees (0)":
            lambda state: True,
        "Termina Field Fountain Rupees (1)":
            lambda state: True,

        # Termina Field Invisible Rupee Over Water
        "Termina Field Invisible Rupee Over Water":
            lambda state: True,

        # Termina Field Invisible Rupee Over Stump
        "Termina Field Invisible Rupee Over Stump":
            lambda state: (
                state.has("Deku Mask", player) or
                (state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player))
            ),

        # Termina Field Invisible Rupees In Long Grass
        "Termina Field Invisible Rupees In Long Grass (0)":
            lambda state: True,
        "Termina Field Invisible Rupees In Long Grass (1)":
            lambda state: True,
        "Termina Field Invisible Rupees In Long Grass (2)":
            lambda state: True,
        "Termina Field Invisible Rupees In Long Grass (3)":
            lambda state: True,
        "Termina Field Invisible Rupees In Long Grass (4)":
            lambda state: True,

        # Termina Field Invisible Rupee Over Northern Ramp
        "Termina Field Invisible Rupee Over Northern Ramp":
            lambda state: (
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player)
            ),

        # Romani Ranch Invisible Fence Rupees
        "Romani Ranch Invisible Fence Rupees (0)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),
        "Romani Ranch Invisible Fence Rupees (1)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),
        "Romani Ranch Invisible Fence Rupees (2)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),
        "Romani Ranch Invisible Fence Rupees (3)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),
        "Romani Ranch Invisible Fence Rupees (4)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),
        "Romani Ranch Invisible Fence Rupees (5)":
            lambda state: state.can_reach("Romani Ranch", 'Region', player),

        # Swamp Spiderhouse Invisible Rupees Above Giant Jars
        "Swamp Spiderhouse Invisible Rupees Above Giant Jars (0)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spiderhouse Invisible Rupees Above Giant Jars (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spiderhouse Invisible Rupees Above Giant Jars (2)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spiderhouse Invisible Rupees Above Giant Jars (3)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spiderhouse Invisible Rupees Above Giant Jars (4)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),    
        
        # SOILS

        # Termina Field Stump Soil
        "Termina Field Stump Soil":
            lambda state: has_bottle(state, player),

        # Termina Field Wall Soil
        "Termina Field Wall Soil (0)":
            lambda state: has_bottle(state, player),
        "Termina Field Wall Soil (1)":
            lambda state: has_bottle(state, player),
        "Termina Field Wall Soil (2)":
            lambda state: has_bottle(state, player),

        # Termina Field Eastern Soil
        "Termina Field Eastern Soil":
            lambda state: has_bottle(state, player),

        # Termina Field Observatory Soil
        "Termina Field Observatory Soil (0)":
            lambda state: has_bottle(state, player),
        "Termina Field Observatory Soil (1)":
            lambda state: has_bottle(state, player),
        "Termina Field Observatory Soil (2)":
            lambda state: has_bottle(state, player),

        # Swamp Spider House Rock Soil
        "Swamp Spider House Rock Soil (0)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_bottle(state, player)
            ),
        "Swamp Spider House Rock Soil (1)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_bottle(state, player)
            ),
        "Swamp Spider House Rock Soil (2)":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_bottle(state, player)
            ),

        # Swamp Spider House Gold Room Soil
        "Swamp Spider House Gold Room Soil":
            lambda state: (
                state.can_reach("Swamp Spider House", 'Region', player) and
                has_bottle(state, player)
            ),

        # Deku Palace Bean Seller Soil
        "Deku Palace Bean Seller Soil (0)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                has_bottle(state, player)
            ),
        "Deku Palace Bean Seller Soil (1)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                has_bottle(state, player)
            ),
        "Deku Palace Bean Seller Soil (2)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                has_bottle(state, player)
            ),

        # Deku Palace Exterior Soil
        "Deku Palace Exterior Soil (0)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                has_bottle(state, player)
            ),
        "Deku Palace Exterior Soil (1)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                has_bottle(state, player)
            ),
        "Deku Palace Exterior Soil (2)":
            lambda state: (
                state.can_reach("Deku Palace", 'Region', player) and
                has_bottle(state, player)
            ),

        # Romani Ranch Day 1 Soil
        "Romani Ranch Day 1 Soil":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_bottle(state, player) and
                state.has("Goron Mask", player) and
                can_use_powder_keg(state, player)
            ),

        # Romani Ranch Day 2/3 Soil
        "Romani Ranch Day 2/3 Soil (0)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_bottle(state, player)
            ),
        "Romani Ranch Day 2/3 Soil (1)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_bottle(state, player)
            ),
        "Romani Ranch Day 2/3 Soil (2)":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_bottle(state, player)
            ),

        # Romani Ranch Doggy Racetrack Soil
        "Romani Ranch Doggy Racetrack Soil":
            lambda state: (
                state.can_reach("Romani Ranch", 'Region', player) and
                has_bottle(state, player)
            ),

        # Great Bay Coast Soil
        "Great Bay Coast Soil":
            lambda state: (
                state.can_reach("Great Bay", 'Region', player) and
                has_bottle(state, player)
            ),

        # Secret Shrine Soil
        "Secret Shrine Soil (0)":
            lambda state: (
                state.can_reach("Secret Shrine", 'Region', player) and
                has_bottle(state, player)
            ),
        "Secret Shrine Soil (1)":
            lambda state: (
                state.can_reach("Secret Shrine", 'Region', player) and
                has_bottle(state, player)
            ),
        "Secret Shrine Soil (2)":
            lambda state: (
                state.can_reach("Secret Shrine", 'Region', player) and
                has_bottle(state, player)
            ),

        # Stone Tower Inverted Soils
        "Stone Tower Inverted Soils (0)":
            lambda state: (
                state.can_reach("Stone Tower (Inverted)", 'Region', player) and
                has_bottle(state, player)
            ),
        "Stone Tower Inverted Soils (1)":
            lambda state: (
                state.can_reach("Stone Tower (Inverted)", 'Region', player) and
                has_bottle(state, player) and
                can_plant_beans(state, player)
            ),    

        # SNOWBALLS

        # Path to Mountains Snowballs
        "Path to Mountains Snowballs (0)":
            lambda state: True,
        "Path to Mountains Snowballs (1)":
            lambda state: True,
        "Path to Mountains Snowballs (2)":
            lambda state: True,
        "Path to Mountains Snowballs (3)":
            lambda state: True,
        "Path to Mountains Snowballs (4)":
            lambda state: True,
        "Path to Mountains Snowballs (5)":
            lambda state: True,
        "Path to Mountains Snowballs (6)":
            lambda state: True,
        "Path to Mountains Snowballs (7)":
            lambda state: True,
        "Path to Mountains Snowballs (8)":
            lambda state: True,
        "Path to Mountains Snowballs (9)":
            lambda state: True,
        "Path to Mountains Snowballs (10)":
            lambda state: True,
        "Path to Mountains Snowballs (11)":
            lambda state: True,
        "Path to Mountains Snowballs (12)":
            lambda state: True,
        "Path to Mountains Snowballs (13)":
            lambda state: True,
        "Path to Mountains Snowballs (14)":
            lambda state: True,

        # Mountain Village Day 1 Snowballs
        "Mountain Village Day 1 Snowballs (0)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (1)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (2)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (3)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (4)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (5)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (6)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (7)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (8)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (9)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (10)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (11)":
            lambda state: True,
        "Mountain Village Day 1 Snowballs (12)":
            lambda state: True,

        # Snowballs Outside Goron Graveyard
        "Snowballs Outside Goron Graveyard (0)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                state.has("Progressive Magic", player) and
                state.has("Lens of Truth", player)
            ),
        "Snowballs Outside Goron Graveyard (1)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                state.has("Progressive Magic", player) and
                state.has("Lens of Truth", player)
            ),

        # Twin Islands Day 1 Snowballs
        "Twin Islands Day 1 Snowballs (0)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (1)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (2)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (3)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (4)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (5)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (6)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (7)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (8)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (9)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (10)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (11)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (12)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (13)":
            lambda state: True,
        "Twin Islands Day 1 Snowballs (14)":
            lambda state: True,

        # Twin Isles Snowballs Near Grotto
        "Twin Isles Snowballs Near Grotto (0)":
            lambda state: True,
        "Twin Isles Snowballs Near Grotto (1)":
            lambda state: True,
        "Twin Isles Snowballs Near Grotto (2)":
            lambda state: True,

        # Goron Village Snowballs
        "Goron Village Snowballs (0)":
            lambda state: True,
        "Goron Village Snowballs (1)":
            lambda state: True,
        "Goron Village Snowballs (2)":
            lambda state: True,
        "Goron Village Snowballs (3)":
            lambda state: True,
        "Goron Village Snowballs (4)":
            lambda state: True,
        "Goron Village Snowballs (5)":
            lambda state: True,
        "Goron Village Snowballs (6)":
            lambda state: True,
        "Goron Village Snowballs (7)":
            lambda state: True,
        "Goron Village Snowballs (8)":
            lambda state: True,
        "Goron Village Snowballs (9)":
            lambda state: True,
        "Goron Village Snowballs (10)":
            lambda state: True,
        "Goron Village Snowballs (11)":
            lambda state: True,
        "Goron Village Snowballs (12)":
            lambda state: True,
        "Goron Village Snowballs (13)":
            lambda state: True,
        "Goron Village Snowballs (14)":
            lambda state: True,
        "Goron Village Snowballs (15)":
            lambda state: True,
        "Goron Village Snowballs (16)":
            lambda state: True,
        "Goron Village Snowballs (17)":
            lambda state: True,
        "Goron Village Snowballs (18)":
            lambda state: True,
        "Goron Village Snowballs (19)":
            lambda state: True,

        # Path to Snowhead Snowballs
        "Path to Snowhead Snowballs (0)":
            lambda state: (
                state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player)
        ),
        "Path to Snowhead Snowballs (1)":
            lambda state: (
                state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player)
        ),
        "Path to Snowhead Snowballs (2)":
            lambda state: (
                state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player)
        ),
        "Path to Snowhead Snowballs (3)":
            lambda state: (
                state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player)
        ),
        "Path to Snowhead Snowballs (4)":
            lambda state: (
                state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player)
        ),
        "Path to Snowhead Snowballs (5)":
            lambda state: (
                state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player)
        ),
        "Path to Snowhead Snowballs (6)":
            lambda state: (
                state.has("Goron Mask", player) and
                 state.has("Progressive Magic", player)
        ),
        # Outside Snowhead Temple Snowballs
        "Outside Snowhead Temple Snowballs (0)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (1)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (2)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (3)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (4)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (5)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (6)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (7)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (8)":
             lambda state: True,
        "Outside Snowhead Temple Snowballs (9)":
             lambda state: True,

        # Snowhead Temple Lower Runway Room Snowballs             
        "Snowhead Temple Lower Runway Room Snowballs (0)":
            lambda state: True,
        "Snowhead Temple Lower Runway Room Snowballs (1)":
        lambda state: True,
        
        # Snowhead Temple Icicle Room Snowballs
        "Snowhead Temple Icicle Room Snowballs (0)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 1) or
                state.has("Hookshot", player)
            ),
        "Snowhead Temple Icicle Room Snowballs (1)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 1) or
                state.has("Hookshot", player)
            ),
        "Snowhead Temple Icicle Room Snowballs (2)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 1) or
                state.has("Hookshot", player)
            ),
        "Snowhead Temple Icicle Room Snowballs (3)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 1) or
                state.has("Hookshot", player)
            ),
        "Snowhead Temple Icicle Room Snowballs (4)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 1) or
                state.has("Hookshot", player)
            ),
        "Snowhead Temple Icicle Room Snowballs (5)":
            lambda state: (
                has_explosives(state, player) and
                state.has("Small Key (Snowhead)", player, 1) or
                state.has("Hookshot", player)
            ),

        # Snowhead Temple Main Room 2nd Floor Snowballs
        "Snowhead Temple Main Room 2nd Floor Snowballs (0)":
            lambda state: (
                can_use_fire_arrows(state, player) or
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Main Room 2nd Floor Snowballs (1)":
            lambda state: (
                can_use_fire_arrows(state, player) or
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Main Room 2nd Floor Snowballs (2)":
            lambda state: (
                can_use_fire_arrows(state, player) or
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Main Room 2nd Floor Snowballs (3)":
            lambda state: (
                can_use_fire_arrows(state, player) or
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Main Room 2nd Floor Snowballs (4)":
            lambda state: (
                can_use_fire_arrows(state, player) or
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple Main Room 2nd Floor Snowballs (5)":
            lambda state: (
                can_use_fire_arrows(state, player) or
                 state.has("Small Key (Snowhead)", player, 2)
            ),

        # Snowhead Temple 3rd Floor Bridge Snowballs
        "Snowhead Temple 3rd Floor Bridge Snowballs (0)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Bridge Snowballs (1)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Bridge Snowballs (2)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Bridge Snowballs (3)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),

        # Snowhead Temple 3rd Floor Behind Locked Door Snowballs
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (0)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (1)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (2)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (3)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (4)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (5)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (6)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),
        "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (7)":
            lambda state: (
                can_use_fire_arrows(state, player) and
                 state.has("Small Key (Snowhead)", player, 2)
            ),

        # Mountain Village Spring Snowballs
        "Mountain Village Spring Snowballs (0)":
            lambda state: (
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Snowballs (1)":
            lambda state: (
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Snowballs (2)":
            lambda state: (
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Snowballs (3)":
            lambda state: (
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Snowballs (4)":
            lambda state: (
                can_clear_snowhead(state, player)
            ),    
        # ROCKS

        # Termina Field Kamaro Rock Circle
        "Termina Field Kamaro Rock Circle (0)":
            lambda state: True,
        "Termina Field Kamaro Rock Circle (1)":
            lambda state: True,
        "Termina Field Kamaro Rock Circle (2)":
            lambda state: True,
        "Termina Field Kamaro Rock Circle (3)":
            lambda state: True,
        "Termina Field Kamaro Rock Circle (4)":
            lambda state: True,
        "Termina Field Kamaro Rock Circle (5)":
            lambda state: True,
        "Termina Field Kamaro Rock Circle (6)":
            lambda state: True,
        "Termina Field Kamaro Rock Circle (7)":
            lambda state: True,

        # Termina Field North West Rock Wall
        "Termina Field North West Rock Wall (0)":
            lambda state: has_explosives(state, player),
        "Termina Field North West Rock Wall (1)":
            lambda state: has_explosives(state, player),
        "Termina Field North West Rock Wall (2)":
            lambda state: has_explosives(state, player),
        "Termina Field North West Rock Wall (3)":
            lambda state: has_explosives(state, player),
        "Termina Field North West Rock Wall (4)":
            lambda state: has_explosives(state, player),

        # Termina Field Rock Behind Coast Wall
        "Termina Field Rock Behind Coast Wall":
            lambda state: can_play_song("Epona's Song", state, player),

        # South West Rock Wall
        "South West Rock Wall (0)":
            lambda state: has_explosives(state, player),
        "South West Rock Wall (1)":
            lambda state: has_explosives(state, player),
        "South West Rock Wall (2)":
            lambda state: has_explosives(state, player),
        "South West Rock Wall (3)":
            lambda state: has_explosives(state, player),

        # Swamp Spider Entry Rocks
        "Swamp Spider Entry Rocks (0)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider Entry Rocks (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),

        # Swamp Spider Large Pots Rock
        "Swamp Spider Large Pots Rock":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),

        # Goron Shrine Rocks
        "Goron Shrine Rocks (0)":
            lambda state: True,
        "Goron Shrine Rocks (1)":
            lambda state: True,
        "Goron Shrine Rocks (2)":
            lambda state: True,
        "Goron Shrine Rocks (3)":
            lambda state: True,
        "Goron Shrine Rocks (4)":
            lambda state: True,
        "Goron Shrine Rocks (5)":
            lambda state: True,
        "Goron Shrine Rocks (6)":
            lambda state: True,
        "Goron Shrine Rocks (7)":
            lambda state: True,
        "Goron Shrine Rocks (8)":
            lambda state: True,
        "Goron Shrine Rocks (9)":
            lambda state: True,
        "Goron Shrine Rocks (10)":
            lambda state: True,
        "Goron Shrine Rocks (11)":
            lambda state: True,
        "Goron Shrine Rocks (12)":
            lambda state: True,
        "Goron Shrine Rocks (13)":
            lambda state: True,
        "Goron Shrine Rocks (14)":
            lambda state: True,
        "Goron Shrine Rocks (15)":
            lambda state: True,

        # Mountain Village Spring Rock Triangle
        "Mountain Village Spring Rock Triangle (0)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Rock Triangle (1)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Rock Triangle (2)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Rock Triangle (3)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Rock Triangle (4)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                can_clear_snowhead(state, player)
            ),

        # Mountain Village Spring Outside Goron Graveyard
        "Mountain Village Spring Outside Goron Graveyard Rocks (0)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                can_clear_snowhead(state, player)
            ),
        "Mountain Village Spring Outside Goron Graveyard Rocks (1)":
            lambda state: (
                state.can_reach("Mountain Village", 'Region', player) and
                can_clear_snowhead(state, player)
            ),

        # Twin Isles Spring Above Grotto Rocks
        "Twin Isles Spring Above Grotto Rocks (0)":
            lambda state: True,
        "Twin Isles Spring Above Grotto Rocks (1)":
            lambda state: True,
        "Twin Isles Spring Above Grotto Rocks (2)":
            lambda state: True,

        # Great Bay Coast Scattered Beach Rocks
        "Great Bay Coast Scattered Beach Rocks (0)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Great Bay Coast Scattered Beach Rocks (1)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Great Bay Coast Scattered Beach Rocks (2)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Great Bay Coast Scattered Beach Rocks (3)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Great Bay Coast Scattered Beach Rocks (4)":
            lambda state: state.can_reach("Great Bay", 'Region', player),

        # Great Bay Coast Rock Wall Rocks
        "Great Bay Coast Rock Wall Rocks (0)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Great Bay Coast Rock Wall Rocks (1)":
            lambda state: state.can_reach("Great Bay", 'Region', player),

        # Great Bay Coast Underwater Rocks (Bombchus only)
        "Great Bay Coast Underwater Rocks (Bombchus only) (0)":
            lambda state: (
                state.can_reach("Great Bay", 'Region', player) and
                has_bombchus(state, player)
            ),
        "Great Bay Coast Underwater Rocks (Bombchus only) (1)":
            lambda state: (
                state.can_reach("Great Bay", 'Region', player) and
                has_bombchus(state, player)
            ),
        "Great Bay Coast Underwater Rocks (Bombchus only) (2)":
            lambda state: (
                state.can_reach("Great Bay", 'Region', player) and
                has_bombchus(state, player)
            ),
        "Great Bay Coast Underwater Rocks (Bombchus only) (3)":
            lambda state: (
                state.can_reach("Great Bay", 'Region', player) and
                has_bombchus(state, player)        
            ),                

        # Rocks Underwater Easy to get
        "Rocks Underwater Easy to get (0)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Rocks Underwater Easy to get (1)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Rocks Underwater Easy to get (2)":
            lambda state: state.can_reach("Great Bay", 'Region', player),
        "Rocks Underwater Easy to get (3)":
            lambda state: state.can_reach("Great Bay", 'Region', player),

        # Zora Cape Beach Rocks
        "Zora Cape Beach Rocks (0)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (1)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (2)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (3)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (4)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (5)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (6)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (7)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (8)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),
        "Zora Cape Beach Rocks (9)":
            lambda state: state.can_reach("Zora Cape", 'Region', player),

        # Zora Cape Island Rocks (Req Hook)
        "Zora Cape Island Rocks (0)":
            lambda state: (
                state.can_reach("Zora Cape", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Zora Cape Island Rocks (1)":
            lambda state: (
                state.can_reach("Zora Cape", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Zora Cape Island Rocks (2)":
            lambda state: (
                state.can_reach("Zora Cape", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Zora Cape Island Rocks (3)":
            lambda state: (
                state.can_reach("Zora Cape", 'Region', player) and
                state.has("Hookshot", player)
            ),
        "Zora Cape Island Rocks (4)":
            lambda state: (
                state.can_reach("Zora Cape", 'Region', player) and
                state.has("Hookshot", player)
            ),

        # Road To Ikana Rock Circle
        "Road To Ikana Rock Circle (0)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),
        "Road To Ikana Rock Circle (1)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),
        "Road To Ikana Rock Circle (2)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),
        "Road To Ikana Rock Circle (3)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),
        "Road To Ikana Rock Circle (4)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),
        "Road To Ikana Rock Circle (5)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),
        "Road To Ikana Rock Circle (6)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),
        "Road To Ikana Rock Circle (7)":
            lambda state: state.can_reach("Road to Ikana", 'Region', player),

        # Ikana Graveyard Rock Circle
        "Ikana Graveyard Rock Circle (0)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Rock Circle (1)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Rock Circle (2)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Rock Circle (3)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Rock Circle (4)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Rock Circle (5)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Rock Circle (6)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),
        "Ikana Graveyard Rock Circle (7)":
            lambda state: state.can_reach("Ikana Graveyard", 'Region', player),

        # Ikana Graveyard Captain Rockwall
        "Ikana Graveyard Captain Rockwall (0)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_explosives(state, player) and
                can_play_song("Sonata of Awakening", state, player)
            ),
        "Ikana Graveyard Captain Rockwall (1)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_explosives(state, player) and
                can_play_song("Sonata of Awakening", state, player)
            ),
        "Ikana Graveyard Captain Rockwall (2)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_explosives(state, player) and
                can_play_song("Sonata of Awakening", state, player)
            ),
        "Ikana Graveyard Captain Rockwall (3)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_explosives(state, player) and
                can_play_song("Sonata of Awakening", state, player)
            ),
        "Ikana Graveyard Captain Rockwall (4)":
            lambda state: (
                state.can_reach("Ikana Graveyard", 'Region', player) and
                has_explosives(state, player) and
                can_play_song("Sonata of Awakening", state, player)
            ),

        # Inverted Stone Lower Tower Rocks
        "Inverted Stone Lower Tower Rocks (0)":
            lambda state: state.can_reach("Stone Tower (Inverted)", 'Region', player),
        "Inverted Stone Lower Tower Rocks (1)":
            lambda state: state.can_reach("Stone Tower (Inverted)", 'Region', player),

        # Woodsanity (Crates/Barrels/Bonk Boards)
        # Clock Town
        "Laundry Pool Crate (0)":
            lambda state: True,
        "East Clock Town Crates (0)":
            lambda state: True,
        "East Clock Town Crates (1)":
            lambda state: True,
        "Termina Field Business Scrub Grotto Crate (1)":
            lambda state: True,

        # Romani Ranch Crates

        "Romani Ranch Crate Next To Romani (1)":
            lambda state: True,
        "Romani Ranch Baby Cuccoo Crates (0)":
            lambda state: True,
        "Romani Ranch Baby Cuccoo Crates (1)":
            lambda state: True,
        "Romani Ranch Baby Cuccoo Crates (2)":
            lambda state: True,

        # Swamp Spider House

        "Swamp Spider House Monument Room Crates (0)":
             lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Monument Room Crates (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Monument Room Crates (2)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Monument Room Crates (3)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Monument Room Crates (4)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Monument Room Crates (5)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Gold Room Crates (0)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),
        "Swamp Spider House Gold Room Crates (1)":
            lambda state: state.can_reach("Swamp Spider House", 'Region', player),

        # Goron Village

        "Goron Village Keg Goron Crate (1)":
            lambda state: can_use_fire_arrows(state,player),

        # Ocean Spider House

        "Ocean Spiderhouse Basement Crate (1)":
            lambda state: state.can_reach("Ocean Spider House", 'Region', player) and
                            state.has("Hookshot", player),

        # Pirates' Fortress Related

        "Pirates Fortress Entrance Bonk Board (0)":
            lambda state: state.can_reach("Great Bay", 'Region', player) and
                            state.has("Zora Mask", player),
        "Pirates Fortress Entrance Bonk Board (1)":
            lambda state: state.can_reach("Great Bay", 'Region', player) and
                          state.has("Zora Mask", player),
        "Pirates Fortress Entrance Bonk Board (2)":
            lambda state: state.can_reach("Great Bay", 'Region', player) and
                          state.has("Zora Mask", player),
        "Pirates Fortress Entrance Bonk Board (3)":
            lambda state: state.can_reach("Great Bay", 'Region', player) and
                          state.has("Zora Mask", player),

        "Pirates Fortress Sewers Bonk Board (0)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates Fortress Sewers Bonk Board (1)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates Fortress Sewers Bonk Board (2)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),

        # Pirate Fortress Sewers Barrels/Crates

        "Pirates' Fortress Sewers Barrel (0)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (1)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (2)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (3)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (4)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (5)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (6)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (7)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (8)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (9)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (10)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (11)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),
        "Pirates' Fortress Sewers Barrel (12)":
            lambda state: state.can_reach("Pirates' Fortress Sewers", 'Region', player),

        # Pirates' Fortress Interior Crates

        "Pirates Fortress' Interior Crates (0)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player),
        "Pirates Fortress' Interior Crates (1)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player),
        "Pirates Fortress' Interior Crates (2)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player),
        "Pirates Fortress' Exterior Balcony Barrel (1)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player) and
                            state.has("Hookshot", player),
        "Pirates' Fortress Leader's Room Crate (0)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player) and
                            state.has("Progressive Bow", player),
        "Pirates' Fortress Leader's Room Crate (1)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player) and
                          state.has("Progressive Bow", player),
        "Pirates' Fortress Guarded Bridge Barrel (0)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player) and
                          state.has("Hookshot", player),
        "Pirates Fortress Interior Room Past Pink Guard Barrel (0)":
            lambda state: state.can_reach("Pirates' Fortress Interior", 'Region', player) and
                          state.has("Hookshot", player),

        # Dungeon Woodsanity

        # Snowhead

        "Snowhead Temple Lava Bridge Room Crate (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Elevator Room Crates (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Elevator Room Crates (1)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Elevator Room Crates (2)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Elevator Room Crates (3)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Elevator Room Crates (4)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),

        "Snowhead Temple Timed Switch Puzzle Room Crate (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player) and
                            has_explosives(state, player),
        "Snowhead Temple Timed Switch Puzzle Room Crate (1)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player) and
                          has_explosives(state, player),

        # Great Bay

        "Great Bay Temple Entrance Barrels (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Entrance Barrels (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Entrance Barrels (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Entrance Barrels (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Entrance Barrels (4)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Entrance Barrels (5)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Entrance Barrels (6)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Entrance Barrels (7)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player),
        "Great Bay Temple Room Behind 1F Waterfall Barrels (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                            can_use_ice_arrows(state, player),
        "Great Bay Temple Room Behind 1F Waterfall Barrels (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple Room Behind 1F Waterfall Barrels (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),

        "Great Bay Temple 1F Red Valve Room Barrels (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Barrels (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Barrels (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Barrels (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Barrels (4)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Crates (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Crates (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Crates (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Crates (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),
        "Great Bay Temple 1F Red Valve Room Crates (4)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player),

        "Great Bay Temple 1F Frog Miniboss Crates (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (4)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (5)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (6)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (7)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (8)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (9)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (10)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (11)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (12)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (13)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (14)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple 1F Frog Miniboss Crates (15)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),

        "Great Bay Temple Seesaw Room Crates (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Crates (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Crates (2)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Crates (3)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Crates (4)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Crates (5)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Crates (6)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Green Pipe Frozen Waterwheel Crates (0)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),
        "Great Bay Temple Green Pipe Frozen Waterwheel Crates (1)":
            lambda state: state.can_reach("Great Bay Temple", 'Region', player) and
                          can_use_ice_arrows(state, player) and
                          can_use_fire_arrows(state, player),

        # Stone Tower Temple

        "Stone Tower Temple Entrance Room Crates (0)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Entrance Room Crates (1)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),

        "Stone Tower Temple Mirror Room Crates (0)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          (can_use_light_arrows(state, player) or
                           state.has("Mirror Shield", player)),
        "Stone Tower Temple Mirror Room Crates (1)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          (can_use_light_arrows(state, player) or
                           state.has("Mirror Shield", player)),
        "Stone Tower Temple Eyegore Room Crates (0)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Eyegore Room Crates (1)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Eyegore Room Crates (2)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player),

        "Stone Tower Temple Behind Bombable Wall Crates (0)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                            has_explosives(state, player),
        "Stone Tower Temple Behind Bombable Wall Crates (1)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          has_explosives(state, player),
        "Stone Tower Temple Behind Bombable Wall Crates (2)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          has_explosives(state, player),
        "Stone Tower Temple Behind Bombable Wall Crates (3)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          has_explosives(state, player),
        "Stone Tower Temple Behind Bombable Wall Crates (4)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          has_explosives(state, player),
        "Stone Tower Temple Behind Bombable Wall Crates (5)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          has_explosives(state, player),
        "Stone Tower Temple Behind Bombable Wall Crates (6)":
            lambda state: state.can_reach("Stone Tower Temple", 'Region', player) and
                          has_explosives(state, player),

        # Inverted Stone Tower

        "Stone Tower Temple Inverted Entry Crates (0)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Inverted Entry Crates (1)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Inverted Entry Crates (2)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Inverted Entry Crates (3)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player),
        "Stone Tower Temple Inverted Entry Crates (4)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player),

        "Stone Tower Temple Inverted Thin Hallway Crates (0)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player) and
                          state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Thin Hallway Crates (1)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player) and
                          state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Thin Hallway Crates (2)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player) and
                          state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Thin Hallway Crates (3)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player) and
                          state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Thin Hallway Crates (4)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player) and
                          state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Thin Hallway Crates (5)":
            lambda state: state.can_reach("Inverted Stone Tower Temple", 'Region', player) and
                          state.has("Deku Mask", player),

        # Icicles (ice ice baby)

        # Snowhead Temple

        "Snowhead Temple Entry Block Icicles (0)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Entry Block Icicles (1)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Entry Block Icicles (2)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Entry Block Icicles (3)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),
        "Snowhead Temple Entry Block Icicles (4)":
            lambda state: state.can_reach("Snowhead Temple", 'Region', player),

        "Snowhead Temple Grey Door Icicles (0)":
            lambda state: True,
        "Snowhead Temple Grey Door Icicles (1)":
            lambda state: True,

        "Snowhead Temple 3F Behind Locked Door Icicles (0)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and
                          (
                          state.has("Hookshot", player) or
                          can_use_fire_arrows(state, player)
                          ),


        "Snowhead Temple 3F Behind Locked Door Icicles (1)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and
                          (
                                  state.has("Hookshot", player) or
                                  can_use_fire_arrows(state, player)
                          ),

        "Snowhead Temple 3F Behind Locked Door Icicles (2)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and
                          (
                                  state.has("Hookshot", player) or
                                  can_use_fire_arrows(state, player)
                          ),

        "Snowhead Temple 4F Outside Wizzrobe Icicles (0)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and
                          (
                                  state.has("Hookshot", player) or
                                  can_use_fire_arrows(state, player)
                          ),
        "Snowhead Temple 4F Outside Wizzrobe Icicles (1)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and
                          (
                                  state.has("Hookshot", player) or
                                  can_use_fire_arrows(state, player)
                          ),

        "Snowhead Temple Outside Boss Door Icicles (0)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and can_use_fire_arrows(state, player),
        "Snowhead Temple Outside Boss Door Icicles (1)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and can_use_fire_arrows(state, player),
        "Snowhead Temple Outside Boss Door Icicles (2)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and can_use_fire_arrows(state, player),
        "Snowhead Temple Outside Boss Door Icicles (3)":
            lambda state: state.has("Small Key (Snowhead)", player, 1) and can_use_fire_arrows(state, player),

        # Great Bay Temple

        "Great Bay Temple Outside Frog Miniboss Door Icicles (0)":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Outside Frog Miniboss Door Icicles (1)":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Outside Frog Miniboss Door Icicles (2)":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Outside Frog Miniboss Door Icicles (3)":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Outside Frog Miniboss Door Icicles (4)":
            lambda state: can_use_ice_arrows(state, player),

        # Goron Trial

        "Goron Trial Icicles (0)":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic", player),
        "Goron Trial Icicles (1)":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic", player),
        "Goron Trial Icicles (2)":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic", player),
        "Goron Trial Icicles (3)":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic", player),

        # Hivesanity

        # Termina Field

        "Termina Field Bombable Rock Grotto Hive (0)":
            lambda state: has_explosives(state, player) and state.has("Zora Mask", player),
        "Termina Field Bombable Rock Grotto Hive (1)":
            lambda state: has_explosives(state, player) and state.has("Zora Mask", player),
        "Termina Field Bombable Rock Grotto Hive (2)":
            lambda state: has_explosives(state, player) and state.has("Zora Mask", player),

        # Southern Swamp Hive

        "Southern Swamp Hive Near Frog (0)":
            lambda state: has_projectiles(state, player),

        # Swamp Spider House

        "Swamp Spider House Giant Pot Room Hives (0)":
            lambda state: has_projectiles(state, player),
        "Swamp Spider House Giant Pot Room Hives (1)":
            lambda state: has_projectiles(state, player),
        "Swamp Spider House Giant Pot Room Hives (2)":
            lambda state: has_projectiles(state, player),

        "Swamp Spider House Gold Room Hives (0)":
            lambda state: has_projectiles(state, player),
        "Swamp Spider House Gold Room Hives (1)":
            lambda state: has_projectiles(state, player),

        "Swamp Spider Tree Room Hives (0)":
            lambda state: has_projectiles(state, player),
        "Swamp Spider Tree Room Hives (1)":
            lambda state: has_projectiles(state, player),
        "Swamp Spider Tree Room Hives (2)":
            lambda state: has_projectiles(state, player),

        # Woodfall Temple Hives

        "Woodfall Temple Entrance Hive (0)":
            lambda state: has_projectiles(state, player),

        "Woodfall Temple Push Block Hive (0)":
            lambda state: has_projectiles(state, player),

        # Mountain Village Spring Hives

        "Mountain Village Spring Tree Hive (0)":
            lambda state: can_clear_snowhead(state, player),

        # Real Fairysanity/Gossip Faires/Butterly Fairies

        # Termina Field Gossip Fairies

        "Termina Field Southern Tree Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player),
        "Termina Field Near Thieving Bird Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),
        "Termina Field Near Bombable Rock Grotto Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),
        "Termina Field Gossip Grotto Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),
        "Termina Field Near Songwall Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),
        "Termina Field Eastern Corner Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Road to Southern Swamp Gossip Fairy

        "Road To Southern Swamp Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Southern Swamp Gossip Fairies

        "Southern Swamp Near Witch Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        "Swamp Spider House Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Milk Road Gossip Fairy

        "Milk Road Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Romani Ranch Gossip Fairies

        "Romani Ranch Entry Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),
        "Romani Ranch Tree Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),
        "Romani Ranch Near Barn Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                      can_play_song("Epona's Song", state, player),
        "Romani Ranch Baby Cuccoos Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                      can_play_song("Epona's Song", state, player),
        "Romani Ranch Doggy Racetrack Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                      can_play_song("Epona's Song", state, player),

        # Path to Mountain Village Gossip Fairy

        "Path To Mountain Village Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Mountain Village Gossip Fairies

        "Mountain Village Spring Waterfall Gossip Fairy":
            lambda state: can_clear_snowhead(state, player) and
                          (
                              can_play_song("Song of Healing", state, player) or
                              can_play_song("Epona's Song", state, player)
                          ),
        "Mountain Village Spring Ramps To Goron Graveyard Gossip Fairy":
            lambda state: can_clear_snowhead(state, player) and
                          (
                                  can_play_song("Song of Healing", state, player) or
                                  can_play_song("Epona's Song", state, player)
                          ),

        # Great Bay Coast Gossip Fairy

        "Great Bay Coast Rock Wall Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Zora Cape

        "Zora Cape Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Road to Ikana Gossip Fairy

        "Road To Ikana Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        # Ikana Canyon Gossip Fairy

        "Ikana Canyon Near Octoroks Gossip Fairy":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),

        "Ikana Canyon Across Ocean Deed Ravine Gossip Fairy":
            lambda state:
            (
                state.has("Zora Mask", player) and
                state.has("Ocean Title Deed", player) and
                state.has("Deku Mask", player) and
                (
                        can_play_song("Song of Healing", state, player) or
                        can_play_song("Epona's Song", state, player)
                  )
            )
        "Ikana Canyon Near Ghost House Gossip Fairy":
            lambda state:
            (
                can_use_ice_arrows(state, player) and
                state.has("Hookshot", player) and
                (
                        can_play_song("Song of Healing", state, player) or
                        can_play_song("Epona's Song", state, player)
                )
            )

        # Moon Gossip Fairies

        "Deku Trial Front Left Gossip":
            lambda state:
        (
            state.has("Deku Mask", player) and
            (
                    can_play_song("Song of Healing", state, player) or
                    can_play_song("Epona's Song", state, player)
            )
        )
        "Deku Trial Back Left Gossip":
            lambda state:
            (
                    state.has("Deku Mask", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Deku Trial Front Right Gossip":
            lambda state:
            (
                    state.has("Deku Mask", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Deku Trial Back Right Gossip":
            lambda state:
            (
                    state.has("Deku Mask", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Deku Trial Furthest Back Gossip":
            lambda state:
            (
                    state.has("Deku Mask", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )

        # Goron Trial Gossip Fairies

        "Goron Trial 1st Gazebo Gossip (0)":
            lambda state:
            (
                state.has("Goron Mask", player) and
                state.has("Progressive Magic", player) and
                (
                        can_play_song("Song of Healing", state, player) or
                        can_play_song("Epona's Song", state, player)
                )
            )
        "Goron Trial 1st Gazebo Gossip (1)":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Goron Trial 2nd Gazebo Gossip (0)":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Goron Trial 2nd Gazebo Gossip (1)":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Goron Trial Near Heart Piece Gossip (1)":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )

        # Zora Trial
        "Zora Trial RRR Path Gossip":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Zora Trial RRL Path Gossip":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Zora Trial LRR Path Gossip":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Zora Trial LRLL Path Gossip":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )
        "Zora Trial LLL Path Gossip":
            lambda state:
            (
                    state.has("Goron Mask", player) and
                    state.has("Progressive Magic", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            )

        # Link Trial Gossip Fairies

        "Link Trial Gossip (1)":
            lambda state: can_play_song("Song of Healing", state, player) or
                          can_play_song("Epona's Song", state, player),
        "Link Trial Gossip (2)":
            lambda state:
            (
                state.has("Hookshot", player) and
                (
                        can_play_song("Song of Healing", state, player) or
                        can_play_song("Epona's Song", state, player)
                )
            ),

        "Link Trial Gossip (3)":
            lambda state:
            (
                    state.has("Hookshot", player) and
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            ),
        "Link Trial Gossip (4)":
            lambda state:
            (
                    state.can_reach("Link Trial Gossip (3)") and
                    can_use_fire_arrows(state, player) and
                    has_bombchus(state, player)
                        (
                        can_play_song("Song of Healing", state, player) or
                        can_play_song("Epona's Song", state, player)
                    )
            ),

        "Link Trial Gossip (5)":
            lambda state:
            (
                    state.can_reach("Link Trial Gossip (3)") and
                    can_use_fire_arrows(state, player) and
                    has_bombchus(state, player)
                    (
                            can_play_song("Song of Healing", state, player) or
                            can_play_song("Epona's Song", state, player)
                    )
            ),


        # Well Fairies

        "Fairy Fountain Left Side Well (0)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),
        "Fairy Fountain Left Side Well (1)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),

        "Fairy Fountain Left Side Well (2)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),

        "Fairy Fountain Left Side Well (3)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),

        "Fairy Fountain Left Side Well (4)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),

        "Fairy Fountain Left Side Well (5)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),

        "Fairy Fountain Left Side Well (6)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),

        "Fairy Fountain Left Side Well (7)":
            lambda state:
            (
                    (
                            state.has("Mask of Scents", player) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
                    or
                    (
                            can_afford_price(state, player, 100) and
                            has_bottle(state, player, 1) and
                            state.has("Gibdo Mask", player)
                    )
            ),

        # Butterfly Fairies

        "Termina Field Near Peahat Grotto Butterfly Fairy (0)":
            lambda state: True,

        "Termina Field Cow Grotto Butterfly Fairy (0)":
            lambda state: has_explosives(state, player),

        "Termina Field Bombable Rock Grotto Butterfly Fairy (0)":
            lambda state: has_explosives(state, player),

        # Deku Palace Butterflies

        "Deku Palace Bean Seller Butterfly Fairy (0)":
            lambda state: True,

        # Great Bay Coast Butterflies

        "Great Bay Coast Outside Fisherman Hut Butterfly Fairy (0)":
            lambda state: True,

        "Great Bay Coast cow Grotto Butterfly Fairy (0)":
            lambda state: state.has("Hookshot", player),

        # Moon Butterflies

        "Moon Butterfly Fairy (0)":
            lambda state: True,
        "Moon Butterfly Fairy (1)":
            lambda state: True,
        "Moon Butterfly Fairy (2)":
            lambda state: True,
        "Moon Butterfly Fairy (3)":
            lambda state: True,
        "Moon Butterfly Fairy (4)":
            lambda state: True,
        "Moon Butterfly Fairy (5)":
            lambda state: True,
        "Moon Butterfly Fairy (6)":
            lambda state: True,
        "Moon Butterfly Fairy (7)":
            lambda state: True,
        "Moon Butterfly Fairy (8)":
            lambda state: True,
        "Moon Butterfly Fairy (9)":
            lambda state: True,
        "Moon Butterfly Fairy (10)":
            lambda state: True,
        "Moon Butterfly Fairy (11)":
            lambda state: True,
        "Moon Butterfly Fairy (12)":
            lambda state: True,

    }
