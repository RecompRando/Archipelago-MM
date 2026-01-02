from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class MMRLocation(Location):
    game = "Majora's Mask Recompiled"


class MMRLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None


def can_create_heart_location(shp, c_or_p, loc_index):
    if c_or_p == 0:
        starting_containers = int(shp/4) - 1
        starting_pieces = shp % 4
        shuffled_containers = int((12 - shp)/4)
        shuffled_pieces = (12 - shp) % 4
        return starting_containers + starting_pieces + shuffled_containers + shuffled_pieces >= loc_index
    else:
        return True

prices_ints = []

location_data_table: Dict[str, MMRLocationData] = {
    "Link's Inventory (Ocarina of Time)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D004C
    ),
    "Link's Inventory (Song of Time)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0067
    ),    
    "Link's Inventory (Kokiri Sword)": MMRLocationData(
        region="Clock Town",
        address=0x3469420000037
    ),
    "Link's Inventory (Hero's Shield)": MMRLocationData(
        region="Clock Town",
        address=0x3469420000032
    ),
    "Link's Inventory (Heart Item #1)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0000,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 1)
    ),
    "Link's Inventory (Heart Item #2)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0001,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 2)
    ),
    "Link's Inventory (Heart Item #3)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0002,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 3)
    ),
    "Link's Inventory (Heart Item #4)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0003,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 4)
    ),
    "Link's Inventory (Heart Item #5)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0004,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 5)
    ),
    "Link's Inventory (Heart Item #6)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0005,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 6)
    ),
    "Link's Inventory (Heart Item #7)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0006,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 7)
    ),
    "Link's Inventory (Heart Item #8)": MMRLocationData(
        region="Clock Town",
        address=0x34694200D0007,
        can_create=lambda options: can_create_heart_location(options.starting_hearts.value, options.starting_hearts_are_containers_or_pieces.value, 8)
    ),
    "Keaton Quiz": MMRLocationData(
        region="Clock Town",
        address=0x346942007028C
    ),
    "Clock Tower Happy Mask Salesman #1": MMRLocationData(
        region="Clock Town",
        address=0x3469420040068
    ),
    "Clock Tower Happy Mask Salesman #2": MMRLocationData(
        region="Clock Town",
        address=0x3469420000078
    ),
    "Before Clock Town Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420061A00,
        can_create=lambda options: options.intro_checks.value
    ),
    "Clock Town Postbox": MMRLocationData(
        region="Clock Town",
        address=0x34694200701F2
    ),
    "Clock Town Hide-and-Seek": MMRLocationData(
        region="Clock Town",
        address=0x3469420000050
    ),
    "Clock Town Trading Post Shop Item 1": MMRLocationData(
        region="Clock Town",
        address=0x346942009000A,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop Item 2": MMRLocationData(
        region="Clock Town",
        address=0x3469420090005,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop Item 3": MMRLocationData(
        region="Clock Town",
        address=0x3469420090006,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop Item 4": MMRLocationData(
        region="Clock Town",
        address=0x3469420090003,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop Item 5": MMRLocationData(
        region="Clock Town",
        address=0x3469420090007,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop Item 6": MMRLocationData(
        region="Clock Town",
        address=0x3469420090008,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop Item 7": MMRLocationData(
        region="Clock Town",
        address=0x3469420090009,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop Item 8": MMRLocationData(
        region="Clock Town",
        address=0x3469420090004,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Trading Post Shop (Night) Item 1": MMRLocationData(
        region="Clock Town",
        address=0x3469420090012,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Trading Post Shop (Night) Item 2": MMRLocationData(
        region="Clock Town",
        address=0x346942009000E,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Trading Post Shop (Night) Item 3": MMRLocationData(
        region="Clock Town",
        address=0x3469420090011,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Trading Post Shop (Night) Item 4": MMRLocationData(
        region="Clock Town",
        address=0x346942009000B,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Trading Post Shop (Night) Item 5": MMRLocationData(
        region="Clock Town",
        address=0x3469420090010,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Trading Post Shop (Night) Item 6": MMRLocationData(
        region="Clock Town",
        address=0x346942009000C,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Trading Post Shop (Night) Item 7": MMRLocationData(
        region="Clock Town",
        address=0x346942009000F,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Trading Post Shop (Night) Item 8": MMRLocationData(
        region="Clock Town",
        address=0x346942009000D,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Clock Town Bomb Shop Item 1": MMRLocationData(
        region="Clock Town",
        address=0x346942009001A,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Bomb Shop Item 2": MMRLocationData(
        region="Clock Town",
        address=0x3469420090019,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Bomb Shop Item 3": MMRLocationData(
        region="Clock Town",
        address=0x3469420090017,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Bomb Shop Item 3 (Stop Thief)": MMRLocationData(
        region="Clock Town",
        address=0x3469420090018,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Clock Town Bomb Shop Powder Keg Goron": MMRLocationData(
        region="Clock Town",
        address=0x3469420024234,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Curiosity Shop Blue Rupee Trade": MMRLocationData(
        region="Clock Town",
        address=0x346942007C402,
        can_create=lambda options: options.curiostity_shop_trades.value
    ),
    "Curiosity Shop Red Rupee Trade": MMRLocationData(
        region="Clock Town",
        address=0x346942007C404,
        can_create=lambda options: options.curiostity_shop_trades.value
    ),
    "Curiosity Shop Purple Rupee Trade": MMRLocationData(
        region="Clock Town",
        address=0x346942007C405,
        can_create=lambda options: options.curiostity_shop_trades.value
    ),
    "Curiosity Shop Gold Rupee Trade": MMRLocationData(
        region="Clock Town",
        address=0x346942007C407,
        can_create=lambda options: options.curiostity_shop_trades.value
    ),
    "Curiosity Shop Night 3 (Stop Thief)": MMRLocationData(
        region="Clock Town",
        address=0x3469420090013,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Curiosity Shop Night 3 Thief Stolen Item": MMRLocationData(
        region="Clock Town",
        address=0x3469420090015,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Laundry Pool Stray Fairy (Clock Town)": MMRLocationData(
        region="Clock Town",
        address=0x346942001007F
    ),
    "Laundry Pool Musician": MMRLocationData(
        region="Clock Town",
        address=0x346942000008C
    ),
    "Laundry Pool Kafei's Request": MMRLocationData(
        region="Clock Town",
        address=0x34694200000AB
    ),
    "Laundry Pool Curiosity Shop Salesman #1": MMRLocationData(
        region="Clock Town",
        address=0x3469420000080
    ),
    "Laundry Pool Curiosity Shop Salesman #2": MMRLocationData(
        region="Clock Town",
        address=0x34694200000A1
    ),
    "South Clock Town Moon's Tear Trade": MMRLocationData(
        region="Clock Town",
        address=0x3469420000097
    ),
    "South Clock Town Clock Tower Freestanding HP": MMRLocationData(
        region="Clock Town",
        address=0x3469420056F0A
    ),
    "South Clock Town Corner Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420066F00
    ),
    "South Clock Town Final Day Tower Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420066F01
    ),
    "East Clock Town Archery Roof Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420066C0A
    ),
    "East Clock Town Mayors Wife": MMRLocationData(
        region="Clock Town",
        address=0x346942000008F
    ),
    "East Clock Town Couples Mask on Mayor": MMRLocationData(
        region="Clock Town",
        address=0x346942007026F
    ),
    "East Clock Town Shooting Gallery 40-49 Points": MMRLocationData(
        region="Clock Town",
        address=0x3469420000023
    ),
    "East Clock Town Shooting Gallery Perfect 50 Points": MMRLocationData(
        region="Clock Town",
        address=0x346942007011D
    ),
    "East Clock Town Honey and Darling Any Day": MMRLocationData(
        region="Clock Town",
        address=0x34694200800B5
    ),
    "East Clock Town Honey and Darling All Days": MMRLocationData(
        region="Clock Town",
        address=0x34694200700B5
    ),
    "East Clock Town Treasure Game Chest (Human)": MMRLocationData(
        region="Clock Town",
        address=0x3469420061705
    ),
    "East Clock Town Treasure Game Chest (Deku)": MMRLocationData(
        region="Clock Town",
        address=0x346942006172A
    ),
    "East Clock Town Treasure Game Chest (Goron)": MMRLocationData(
        region="Clock Town",
        address=0x346942006170C
    ),
    "East Clock Town Treasure Game Chest (Zora)": MMRLocationData(
        region="Clock Town",
        address=0x3469420061704
    ),
    "Bomber's Hideout Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420062900
    ),
    "Bomber's Hideout Astral Observatory": MMRLocationData(
        region="Clock Town",
        address=0x3469420000096
    ),
    "North Clock Town Tree HP": MMRLocationData(
        region="Clock Town",
        address=0x3469420056E0A
    ),
    "North Clock Town Deku Playground Any Day": MMRLocationData(
        region="Clock Town",
        address=0x34694200801C9
    ),
    "North Clock Town Deku Playground All Days": MMRLocationData(
        region="Clock Town",
        address=0x34694200701C9
    ),
    "North Clock Town Save Old Lady": MMRLocationData(
        region="Clock Town",
        address=0x346942000008D
    ),
    "North Clock Town Great Fairy Reward": MMRLocationData(
        region="Clock Town",
        address=0x3469420030000
    ),
    "North Clock Town Great Fairy Reward (Has Transformation Mask)": MMRLocationData(
        region="Clock Town",
        address=0x3469420000086
    ),
    "West Clock Town Lottery Any Day": MMRLocationData(
        region="Clock Town",
        address=0x3469420080239
    ),
    "West Clock Town Swordsman Expert Course": MMRLocationData(
        region="Clock Town",
        address=0x34694200701EF
    ),
    "West Clock Town Postman Counting": MMRLocationData(
        region="Clock Town",
        address=0x346942007017D
    ),
    "West Clock Town Dancing Sisters": MMRLocationData(
        region="Clock Town",
        address=0x346942007027B
    ),
    "West Clock Town Bank 200 Rupees": MMRLocationData(
        region="Clock Town",
        address=0x3469420000008
    ),
    "West Clock Town Bank 500 Rupees": MMRLocationData(
        region="Clock Town",
        address=0x3469420080177
    ),
    "West Clock Town Bank 1000 Rupees": MMRLocationData(
        region="Clock Town",
        address=0x3469420070177
    ),
    "West Clock Town Priority Mail to Postman": MMRLocationData(
        region="Clock Town",
        address=0x3469420000084
    ),
    "Top of Clock Tower (Ocarina of Time)": MMRLocationData(
        region="Clock Town",
        address=0x346942000004C
    ),
    "Top of Clock Tower (Song of Time)": MMRLocationData(
        region="Clock Town",
        address=0x3469420040067
    ),
    "Stock Pot Inn Reservation": MMRLocationData(
        region="Clock Town",
        address=0x34694200000A0
    ),
    "Stock Pot Inn Midnight Meeting": MMRLocationData(
        region="Clock Town",
        address=0x34694200000AA
    ),
    "Stock Pot Inn Locked Room Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420066100
    ),
    "Stock Pot Inn Employee Room Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420066101
    ),
    "Stock Pot Inn Midnight Toilet Hand": MMRLocationData(
        region="Clock Town",
        address=0x346942007027D
    ),
    "Stock Pot Inn Granny Story #1": MMRLocationData(
        region="Clock Town",
        address=0x3469420070243
    ),
    "Stock Pot Inn Granny Story #2": MMRLocationData(
        region="Clock Town",
        address=0x3469420080243
    ),
    "Stock Pot Inn Anju and Kafei": MMRLocationData(
        region="Clock Town",
        address=0x3469420000085
    ),
    "Milk Bar Show": MMRLocationData(
        region="Clock Town",
        address=0x3469420000083
    ),
    "Milk Bar Priority Mail to Aroma": MMRLocationData(
        region="Clock Town",
        address=0x346942000006F
    ),
    "East Clock Town Milk Bar Milk Purchase": MMRLocationData(
        region="Clock Town",
        address=0x3469420026392,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "East Clock Town Milk Bar Chateau Romani Purchase": MMRLocationData(
        region="Clock Town",
        address=0x3469420000091,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Tingle Clock Town Map Purchase": MMRLocationData(
        region="Clock Town",
        address=0x34694200000B4
    ),
    "Tingle Woodfall Map Purchase": MMRLocationData(
        region="Clock Town",
        address=0x34694200000B5
    ),
    "Tingle Snowhead Map Purchase": MMRLocationData(
        region="Clock Town",
        address=0x34694200000B6
    ),
    "Tingle Romani Ranch Map Purchase": MMRLocationData(
        region="Clock Town",
        address=0x34694200000B7
    ),
    "Tingle Great Bay Map Purchase": MMRLocationData(
        region="Clock Town",
        address=0x34694200000B8
    ),
    "Tingle Stone Tower Map Purchase": MMRLocationData(
        region="Clock Town",
        address=0x34694200000B9
    ),
    "Termina Stump Chest": MMRLocationData(
        region="Termina Field",
        address=0x3469420062D02
    ),
    "Termina Grass Chest": MMRLocationData(
        region="Termina Field",
        address=0x3469420062D01
    ),
    "Termina Underwater Chest": MMRLocationData(
        region="Termina Field",
        address=0x3469420062D00
    ),
    "Termina Grass Grotto Chest": MMRLocationData(
        region="Termina Field",
        address=0x346942006071F
    ),
    "Termina Peehat Grotto Chest": MMRLocationData(
        region="Termina Field",
        address=0x3469420060704
    ),
    "Termina Dodongo Grotto Chest": MMRLocationData(
        region="Termina Field",
        address=0x3469420060700
    ),
    "Termina Log Bombable Grotto Left Cow": MMRLocationData(
        region="Termina Field",
        address=0x3469420BEEF14,
        can_create=lambda options: options.cowsanity.value
    ),
    "Termina Log Bombable Grotto Right Cow": MMRLocationData(
        region="Termina Field",
        address=0x3469420BEEF13,
        can_create=lambda options: options.cowsanity.value
    ),
    "Termina Ikana Pillar Grotto Chest": MMRLocationData(
        region="Termina Field",
        address=0x346942006071A
    ),
    "Termina Healing Kamaro": MMRLocationData(
        region="Termina Field",
        address=0x3469420000089
    ),
    "Termina Bio Baba Grotto HP": MMRLocationData(
        region="Termina Field",
        address=0x3469420050702
    ),
    "Termina Gossip Stones HP": MMRLocationData(
        region="Termina Field",
        address=0x34694200700EF
    ),
    "Termina Scrub Grotto HP": MMRLocationData(
        region="Termina Field",
        address=0x346942007024C
    ),
    "Road to Swamp Tree HP": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420054001
    ),
    "Road to Swamp Grotto Chest": MMRLocationData(
        region="Southern Swamp",
        address=0x346942006071E
    ),
    "Swamp Shooting Gallery 2120 Points": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420000024
    ),
    "Swamp Shooting Gallery 2180 Points": MMRLocationData(
        region="Southern Swamp",
        address=0x346942008011D
    ),
    "Southern Swamp Deku Trade": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420000098
    ),    
    "Southern Swamp Deku Scrub Purchase": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420090135,
        can_create=lambda options: options.scrubsanity.value
    ),
    "Southern Swamp Freestanding HP": MMRLocationData(
        region="Southern Swamp",
        address=0x346942005451E
    ),
    "Southern Swamp Kotake Item": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420000059
    ),
    "Southern Swamp Day 2 Grotto Chest": MMRLocationData(
        region="Southern Swamp",
        address=0x346942006071C
    ),
    "Southern Swamp Healing Koume": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420000043
    ),
    "Southern Swamp Winning Picture": MMRLocationData(
        region="Southern Swamp",
        address=0x34694200701C5
    ),
    "Southern Swamp Good Picture": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420071C54
    ),
    "Southern Swamp Okay Picture": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420071C52
    ),
    "Southern Swamp Witch Shop Item 1": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420090002,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Southern Swamp Witch Shop Item 2": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420090001,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Southern Swamp Witch Shop Item 3": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420090000,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Swamp Spider House First Room Pot Near Entrance Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006271E,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House First Room Crawling In Water Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062708,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House First Room Crawling Right Column Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006270F,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House First Room Crawling Left Column Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062713,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House First Room Against Far Wall Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062700,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House First Room Lower Left Bugpatch Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062709,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House First Room Lower Right Bugpatch Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006270C,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House First Room Upper Right Bugpatch Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006270B,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Monument Room Left Crate Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006270A,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Monument Room Right Crate Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006271B,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Monument Room Crawling Wall Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006270D,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Monument Room Crawling On Monument Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006270E,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Monument Room Behind Torch Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062702,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Pottery Room Beehive #1 Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062717,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Pottery Room Beehive #2 Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006271C,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Pottery Room Small Pot Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062705,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Pottery Room Left Large Pot Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062710,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Pottery Room Right Large Pot Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062711,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Pottery Room Behind Vines Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062714,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Pottery Room Upper Wall Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062716,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Golden Room Crawling Left Wall Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062719,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Golden Room Crawling Right Column Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062704,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Golden Room Against Far Wall Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062701,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Golden Room Beehive Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062712,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Tree Room Tall Grass #1 Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062707,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Tree Room Tall Grass #2 Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062706,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Tree Room Tree #1 Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062715,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Tree Room Tree #2 Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420062718,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Tree Room Tree #3 Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006271D,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Tree Room Beehive Token": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942006271A,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Swamp Spider House Reward": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942000008A
    ),
    "Southern Swamp Grotto Chest": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942006071D
    ),
    "Southern Swamp Song Tablet": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942004006A
    ),
    "Deku Palace HP": MMRLocationData(
        region="Deku Palace",
        address=0x3469420052B1E
    ),
    "Deku Palace Bean Seller": MMRLocationData(
        region="Deku Palace",
        address=0x34694200800A5
    ),
    "Deku Palace Bean Grotto Chest": MMRLocationData(
        region="Deku Palace",
        address=0x3469420060705
    ),
    "Deku Palace Monkey Song": MMRLocationData(
        region="Deku Palace",
        address=0x3469420040061
    ),
    "Deku Palace Butler Race": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942000008E
    ),
    "Woodfall Owl Statue Chest": MMRLocationData(
        region="Woodfall",
        address=0x3469420064602
    ),
    "Woodfall Bridge Chest": MMRLocationData(
        region="Woodfall",
        address=0x3469420064601
    ),
    "Woodfall Entrance Chest": MMRLocationData(
        region="Woodfall",
        address=0x3469420064600
    ),
    "Woodfall Great Fairy Reward": MMRLocationData(
        region="Woodfall",
        address=0x3469420030001
    ),
    "Woodfall Temple Entrance Chest SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B18
    ),
    "Woodfall Temple Ledge Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B01
    ),
    "Woodfall Temple Turtle Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1D
    ),
    "Woodfall Temple Dragonfly Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1C
    ),
    "Woodfall Temple Dark Room Chest SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B19
    ),
    "Woodfall Temple Switch Chest SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B17
    ),
    "Woodfall Temple Dinolfos Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1B
    ),
    "Woodfall Temple Gekko Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1E
    ),
    "Woodfall Temple Entrance Freestanding SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2B
    ),
    "Woodfall Temple Deku Baba SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2E
    ),
    "Woodfall Temple Pot SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B1C
    ),
    "Woodfall Temple Platform Hive SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B1E
    ),
    "Woodfall Temple Main Room Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B30
    ),
    "Woodfall Temple Skulltula SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B31
    ),
    "Woodfall Temple Bridge Room Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2F
    ),
    "Woodfall Temple Bridge Room Hive SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B1D
    ),
    "Woodfall Temple Pre-Boss Lower Right Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2A
    ),
    "Woodfall Temple Pre-Boss Upper Right Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B32
    ),
    "Woodfall Temple Pre-Boss Upper Left Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2C
    ),
    "Woodfall Temple Pre-Boss Pillar Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2D
    ),
    "Woodfall Temple Heart Container": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420051F00
    ),
    "Woodfall Temple Odolwa's Remains": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420000055
    ),
    "Southern Swamp Boat Archery": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420070168
    ),
    "Mountain Village Spring Waterfall Chest": MMRLocationData(
        region="Mountain Village",
        address=0x3469420065A00
    ),
    "Mountain Village Spring Ramp Grotto": MMRLocationData(
        region="Mountain Village",
        address=0x346942006071B
    ),
    "Mountain Village Healing Darmani": MMRLocationData(
        region="Mountain Village",
        address=0x3469420000079
    ),
    "Mountain Village Hungry Goron": MMRLocationData(
        region="Mountain Village",
        address=0x3469420000088
    ),
    "Mountain Village Smithy Upgrade": MMRLocationData(
        region="Mountain Village",
        address=0x3469420000038
    ),
    "Mountain Village Smithy Gold Dust Upgrade": MMRLocationData(
        region="Mountain Village",
        address=0x3469420000039
    ),
    "Mountain Village Spring Frog Choir HP": MMRLocationData(
        region="Mountain Village",
        address=0x3469420070022
    ),
    "Twin Islands Spring Underwater Cave Chest": MMRLocationData(
        region="Twin Islands",
        address=0x3469420065E00
    ),
    "Twin Islands Spring Underwater Ramp Chest": MMRLocationData(
        region="Twin Islands",
        address=0x3469420065E06
    ),
    "Twin Islands Ramp Grotto Chest": MMRLocationData(
        region="Twin Islands",
        address=0x3469420060719
    ),
    "Twin Islands Goron Elder Request": MMRLocationData(
        region="Twin Islands",
        address=0x34694200001AD
    ),
    "Twin Islands Hot Water Grotto Chest": MMRLocationData(
        region="Twin Islands",
        address=0x3469420060702
    ),
    "Goron Racetrack Prize": MMRLocationData(
        region="Twin Islands",
        address=0x346942000006A
    ),
    "Goron Village Lens Cave Rock Chest": MMRLocationData(
        region="Goron Village",
        address=0x3469420060706
    ),
    "Goron Village Lens Cave Invisible Chest": MMRLocationData(
        region="Goron Village",
        address=0x3469420060703
    ),
    "Goron Village Lens Cave Center Chest": MMRLocationData(
        region="Goron Village",
        address=0x3469420060701
    ),
    "Goron Village Baby Goron Lullaby": MMRLocationData(
        region="Goron Village",
        address=0x34694200000AD
    ),
    "Goron Village Shop Item 1": MMRLocationData(
        region="Goron Village",
        address=0x346942009001E,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Goron Village Shop Item 2": MMRLocationData(
        region="Goron Village",
        address=0x346942009001F,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Goron Village Shop Item 3": MMRLocationData(
        region="Goron Village",
        address=0x3469420090020,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Goron Village Shop (Spring) Item 1": MMRLocationData(
        region="Goron Village",
        address=0x3469420090021,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Goron Village Shop (Spring) Item 2": MMRLocationData(
        region="Goron Village",
        address=0x3469420090022,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Goron Village Shop (Spring) Item 3": MMRLocationData(
        region="Goron Village",
        address=0x3469420090023,
        can_create=lambda options: options.shopsanity.value == 2
    ),    
    "Goron Village Scrub Purchase": MMRLocationData(
        region="Goron Village",
        address=0x346942009011D,
        can_create=lambda options: options.scrubsanity.value
    ),
    "Goron Village Deku Trade": MMRLocationData(
        region="Goron Village",
        address=0x3469420000099
    ),
    "Goron Village Freestanding HP": MMRLocationData(
        region="Goron Village",
        address=0x3469420054D1E
    ),
    "Goron Village Freestanding HP (Spring)": MMRLocationData(
        region="Goron Village",
        address=0x346942005481E,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Powder Keg Goron Reward": MMRLocationData(
        region="Goron Village",
        address=0x3469420000034
    ),
    "Path to Snowhead Grotto Chest": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420060713
    ),
    "Path to Snowhead Scarecrow Pillar HP": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420055B08
    ),
    "Snowhead Great Fairy Reward": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420030002
    ),
    "Snowhead Temple Elevator Room Invisible Platform Chest SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062113
    ),
    "Snowhead Temple Lower Wizzrobe Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211B
    ),
    "Snowhead Temple Bridge Room Under Platform Bubble SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942001212F
    ),
    "Snowhead Temple Bridge Room Pillar Bubble SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420012130
    ),
    "Snowhead Temple Elevator Freestanding SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420012132
    ),
    "Snowhead Temple Bombable Stairs Crate SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942001211E
    ),
    "Snowhead Temple Timed Switch Room Bubble SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942001212C
    ),
    "Snowhead Temple Snowmen Bubble SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942001212B
    ),
    "Snowhead Temple Dinolfos Room First SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420012131
    ),
    "Snowhead Temple Dinolfos Room Second SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942001212D
    ),
    "Snowhead Temple Bridge Room Freezard Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062101
    ),
    "Snowhead Temple Elevator Room Lower Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211D
    ),
    "Snowhead Temple Basement Switch Chest SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062114
    ),
    "Snowhead Temple Freezard Torch Room Chest SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062118
    ),
    "Snowhead Temple Behind Stacked Block Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062103
    ),
    "Snowhead Temple Stacked Block Upper Chest SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062115
    ),
    "Snowhead Temple Frozen Block Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211C
    ),
    "Snowhead Temple Frozen Block Upper Chest SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062119
    ),
    "Snowhead Temple Icicle Room Hidden Chest SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062116
    ),
    "Snowhead Temple Icicle Room Snowball Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062104
    ),
    "Snowhead Temple Upper Wizzrobe Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211E
    ),
    "Snowhead Temple Main Room Wall Chest SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062117
    ),
    "Snowhead Temple Heart Container": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420054400
    ),
    "Snowhead Temple Goht's Remains": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420000056
    ),
    "Milk Road Gorman Ranch Race": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x3469420000081
    ),
    "Milk Road Gorman Ranch Purchase": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x3469420006792,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Romani Ranch Baby Cuccos March": MMRLocationData(
        region="Romani Ranch",
        address=0x346942000007F
    ),
    "Romani Ranch Doggy Racetrack Rooftop Chest": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420064100
    ),
    "Romani Ranch Doggy Race": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420070117
    ),
    "Romani Ranch Barn Free Cow": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420BEEF10,
        can_create=lambda options: options.cowsanity.value
    ),
    "Romani Ranch Barn Stables Front Cow": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420BEEF11,
        can_create=lambda options: options.cowsanity.value
    ),
    "Romani Ranch Barn Stables Back Cow": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420BEEF12,
        can_create=lambda options: options.cowsanity.value
    ),
    "Romani Ranch Romani Game": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200000A5
    ),
    "Romani Ranch Aliens": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420000060
    ),
    "Romani Ranch Helping Cremia": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420000082
    ),
    "Great Bay Healing Zora": MMRLocationData(
        region="Great Bay",
        address=0x346942000007A
    ),
    "Great Bay Fisherman's Grotto Chest": MMRLocationData(
        region="Great Bay",
        address=0x3469420060717
    ),
    "Great Bay Baby Zora Song": MMRLocationData(
        region="Great Bay",
        address=0x34694200000AC
    ),
    "Great Bay Feeding Lab Fish": MMRLocationData(
        region="Great Bay",
        address=0x34694200701D9
    ),
    "Great Bay Ledge Grotto Left Cow": MMRLocationData(
        region="Great Bay",
        address=0x3469420BEEF16,
        can_create=lambda options: options.cowsanity.value
    ),
    "Great Bay Ledge Grotto Right Cow": MMRLocationData(
        region="Great Bay",
        address=0x3469420BEEF15,
        can_create=lambda options: options.cowsanity.value
    ),
    "Great Bay Scarecrow Ledge HP": MMRLocationData(
        region="Great Bay",
        address=0x3469420053705
    ),
    "Great Bay Fisherman Game": MMRLocationData(
        region="Great Bay",
        address=0x3469420070292
    ),
    "Zora Cape Underwater Like-Like HP": MMRLocationData(
        region="Zora Cape",
        address=0x3469420053807
    ),
    "Zora Cape Underwater Chest": MMRLocationData(
        region="Zora Cape",
        address=0x3469420063800
    ),
    "Zora Cape Pot Game": MMRLocationData(
        region="Zora Cape",
        address=0x3469420072806
    ),
    "Zora Cape Deku Flower Chest": MMRLocationData(
        region="Zora Cape",
        address=0x3469420063801
    ),
    "Zora Cape Scarecrow Chest": MMRLocationData(
        region="Zora Cape",
        address=0x3469420063802
    ),
    "Zora Cape Grotto Chest": MMRLocationData(
        region="Zora Cape",
        address=0x3469420060715
    ),
    "Beaver Bros. Race 1": MMRLocationData(
        region="Zora Cape",
        address=0x346942009018D
    ),
    "Beaver Bros. Race 2 HP": MMRLocationData(
        region="Zora Cape",
        address=0x346942007018D
    ),
    "Great Bay Great Fairy Reward": MMRLocationData(
        region="Zora Cape",
        address=0x3469420030003
    ),
    "Zora Hall Shop Item 1": MMRLocationData(
        region="Zora Hall",
        address=0x346942009001B,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Zora Hall Shop Item 2": MMRLocationData(
        region="Zora Hall",
        address=0x346942009001C,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Zora Hall Shop Item 3": MMRLocationData(
        region="Zora Hall",
        address=0x346942009001D,
        can_create=lambda options: options.shopsanity.value != 0
    ),
    "Zora Hall Deku Scrub Purchase": MMRLocationData(
        region="Zora Hall",
        address=0x346942009015C,
        can_create=lambda options: options.scrubsanity.value
    ),
    "Zora Hall Goron Scrub Trade": MMRLocationData(
        region="Zora Hall",
        address=0x346942000009A
    ),
    "Zora Hall Goron Scrub Trade Freestanding HP": MMRLocationData(
        region="Zora Hall",
        address=0x3469420054C1E
    ),
    "Zora Hall Evan's Song": MMRLocationData(
        region="Zora Hall",
        address=0x3469420070241
    ),
    "Zora Hall Torches Reward": MMRLocationData(
        region="Zora Hall",
        address=0x3469420072802
    ),
    "Zora Hall Good Picture of Lulu": MMRLocationData(
        region="Zora Hall",
        address=0x3469420082284
    ),
    "Zora Hall Bad Picture of Lulu": MMRLocationData(
        region="Zora Hall",
        address=0x3469420082282
    ),
    "Pirates' Fortress Sewers Cage HP": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x346942005230C
    ),
    "Pirates' Fortress Sewers Maze Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420062301
    ),
    "Pirates' Fortress Sewers Underwater Lower Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420062306
    ),
    "Pirates' Fortress Sewers Underwater Upper Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420062304
    ),
    "Pirates' Fortress Exterior Underwater Log Chest": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420063B00
    ),
    "Pirates' Fortress Exterior Underwater Near Entrance Chest": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420063B01
    ),
    "Pirates' Fortress Exterior Underwater Corner Chest": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420063B02
    ),
    "Pirates' Fortress Interior Tank Chest": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420062300
    ),
    "Pirates' Fortress Interior Guarded Chest": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420062303
    ),
    "Pirates' Fortress Hub Lower Chest": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420061400
    ),
    "Pirates' Fortress Hub Upper Chest": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420061401
    ),
    "Pirates' Fortress Leader's Room Chest": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420062302
    ),
    "Pinnacle Rock Upper Eel Chest": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420062502
    ),
    "Pinnacle Rock Lower Eel Chest": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420062501
    ),
    "Pinnacle Rock Seahorse HP": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420070205
    ),
    "Ocean Spider House Ramp Upper Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006280C,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Ramp Lower Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006280D,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Lobby Ceiling Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006280F,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Rafter Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062806,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Open Pot #1 Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062818,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Open Pot #2 Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062817,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Wall Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006281D,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Library Top Bookcase Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062804,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Library Passage Behind Bookcase Front Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006281C,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Library Passage Behind Bookcase Rear Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062815,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Library Painting #1 Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062814,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Library Painting #2 Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062802,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Library Rafter Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062808,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Library Bookshelf Hole Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062803,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Downstairs Rafter Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062805,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Downstairs Open Pot Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006281B,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Downstairs Behind Staircase Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006281E,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Downstairs Crate Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006280B,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House First Room Downstairs Wall Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006280E,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Dining Room Open Pot Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062819,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Dining Room Painting Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062813,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Dining Room Ceiling Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062807,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Dining Room Chandelier #1 Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062810,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Dining Room Chandelier #2 Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062811,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Dining Room Chandelier #3 Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062812,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Storage Room Web Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062809,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Storage Room North Wall Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062801,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Storage Room Crate Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062816,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Storage Room Hidden Hole Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006280A,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Storage Room Ceiling Pot Token": MMRLocationData(
        region="Ocean Spider House",
        address=0x346942006281A,
        can_create=lambda options: options.skullsanity.value != 2
    ),
    "Ocean Spider House Coloured Mask Sequence HP": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420062800
    ),
    "Ocean Spider House Reward": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420000009
    ),
    "Great Bay Temple Blender Pot SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491B
    ),
    "Great Bay Temple Waterwheel Room Skulltula SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420014932
    ),
    "Great Bay Temple Waterwheel Room Bubble SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420014930
    ),
    "Great Bay Temple Blender Room Barrel SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491C
    ),
    "Great Bay Temple Before Red Valve Room Pot SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491E
    ),
    "Great Bay Temple Before Gekko Room Pot SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491D
    ),
    "Great Bay Temple Seesaw Room Underwater Barrel SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491A
    ),
    "Great Bay Temple Entrance Torches Chest SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064918
    ),
    "Great Bay Temple Behind Locked Door Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491B
    ),
    "Great Bay Temple Before Red Valve Room Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491D
    ),
    "Great Bay Temple Bio-Baba Hall Chest SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064919
    ),
    "Great Bay Temple Before Gekko Room Upper Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491C
    ),
    "Great Bay Temple Before Gekko Room Underwater Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064901
    ),
    "Great Bay Temple Mad Jellied Gekko Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491E
    ),
    "Great Bay Temple Room Behind Waterfall Ceiling Chest SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064915
    ),
    "Great Bay Temple Freezable Waterwheel Upper Chest SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064914
    ),
    "Great Bay Temple Freezable Waterwheel Lower Chest SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064917
    ),
    "Great Bay Temple Seesaw Room Chest SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064916
    ),
    "Great Bay Temple Pre-Boss Room Platform Bubble SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420014931
    ),
    "Great Bay Temple Pre-Boss Room Tunnel Bubble SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001492F
    ),
    "Great Bay Temple Heart Container": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420055F00
    ),
    "Great Bay Temple Gyorg's Remains": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420000057
    ),
    "Road to Ikana Pillar Chest": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420065300
    ),
    "Road to Ikana Rock Grotto Chest": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420060716
    ),
    "Road to Ikana Invisible Soldier": MMRLocationData(
        region="Road to Ikana",
        address=0x346942000008B
    ),
    "Ikana Graveyard Bombable Grotto Chest": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420060718
    ),
    "Graveyard Day 1 Bats Chest": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420060C03
    ),
    "Graveyard Day 1 Iron Knuckle Song": MMRLocationData(
        region="Ikana Graveyard",
        address=0x34694200000A2
    ),
    "Graveyard Day 2 Dampe Bats": MMRLocationData(
        region="Ikana Graveyard",
        address=0x34694200043CA
    ),
    "Graveyard Day 2 Iron Knuckle Chest": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420060C00
    ),
    "Graveyard Day 3 Dampe Big Poe Chest": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420063000
    ),
    "Graveyard Captain Keeta Chest": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420064300
    ),
    "Secret Shrine Dinolfos Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066000
    ),
    "Secret Shrine Wizzrobe Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066001
    ),
    "Secret Shrine Wart Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066002
    ),
    "Secret Shrine Garo Master Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066003
    ),
    "Secret Shrine Completion Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x346942006600A
    ),
    "Ikana Canyon Grotto Chest": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420060714
    ),
    "Ikana Canyon Scrub Purchase": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942009015D,
        can_create=lambda options: options.scrubsanity.value
    ),
    "Ikana Canyon Zora Scrub Trade": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420001307
    ),
    "Ikana Canyon Zora Trade Freestanding HP": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942005131E
    ),
    "Ikana Canyon Healing Pamela's Father": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420000087
    ),
    "Ikana Canyon Spirit House": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x34694200701DE
    ),
    "Stone Tower Great Fairy Reward": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420030004
    ),
    "Ikana Well Final Chest": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420064B1B
    ),
    "Ikana Well Invisible Chest": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420064B02
    ),
    "Ikana Well Rightside Torch Chest": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420064B01
    ),
    "Ikana Well Cow": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420BEEF17,
        can_create=lambda options: options.cowsanity.value
    ),
    "Ikana Castle Pillar Freestanding HP": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420051D0A
    ),
    "Ikana Castle King Song": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420040064
    ),
    # ~ "Stone Tower Temple 1F Bridge Room Underwater Switch Chest Glitched": MMRLocationData(
        # ~ region="Stone Tower Temple",
        # ~ address=0x346942006160E
    # ~ ),
    "Stone Tower Inverted Left Chest": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x346942006591F
    ),
    "Stone Tower Inverted Middle Chest": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x346942006591E
    ),
    "Stone Tower Inverted Right Chest": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x346942006591D
    ),
    "Stone Tower Temple Entrance Room Eye Switch Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061616
    ),
    "Stone Tower Temple Entrance Room Lower Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061612
    ),
    "Stone Tower Temple Armos Room Lava Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061602
    ),
    "Stone Tower Temple Armos Room Back Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x346942006161D
    ),
    "Stone Tower Temple Armos Room Upper Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061615
    ),
    "Stone Tower Temple Eyegore Room Switch Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061618
    ),
    "Stone Tower Temple Eastern Water Room Sun Block Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x346942006161C
    ),
    "Stone Tower Temple Eastern Water Room Underwater Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061617
    ),
    "Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061601
    ),
    "Stone Tower Temple Mirror Room Sun Block Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x346942006160B
    ),
    "Stone Tower Temple Mirror Room Sun Face Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x346942006160F
    ),
    "Stone Tower Temple Air Gust Room Side Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061619
    ),
    "Stone Tower Temple Air Gust Room Goron Switch Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x346942006160D
    ),
    "Stone Tower Temple Garo Master Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x346942006161B
    ),
    "Stone Tower Temple After Garo Upside Down Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420061614
    ),
    "Stone Tower Temple Eyegore Chest": MMRLocationData(
        region="Stone Tower Temple",
        address=0x346942006160C
    ),
    "Stone Tower Temple Inverted Entrance Room Sun Face Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420061810
    ),
    "Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942006180E
    ),
    "Stone Tower Temple Inverted Eastern Air Gust Room Frozen Switch Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420061813
    ),
    "Stone Tower Temple Inverted Eastern Air Gust Room Switch Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420061804
    ),
    "Stone Tower Temple Inverted Wizzrobe Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420061811
    ),
    "Stone Tower Temple Inverted Death Armos Maze Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420061805
    ),
    "Stone Tower Temple Inverted Gomess Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942006181E
    ),
    "Stone Tower Temple Inverted Eyegore Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942006181A
    ),
    "Stone Tower Temple Inverted Heart Container": MMRLocationData(
        region="Twinmold's Lair",
        address=0x3469420053600
    ),
    "Stone Tower Temple Inverted Twinmold's Remains": MMRLocationData(
        region="Twinmold's Lair",
        address=0x3469420000058
    ),
    "Oath to Order": MMRLocationData(
        region="Clock Town", # there isn't really a set location for this
        address=0x3469420040065
    ),
    "Moon Deku Trial HP": MMRLocationData(
        region="The Moon",
        address=0x3469420052A01
    ),
    "Moon Goron Trial HP": MMRLocationData(
        region="The Moon",
        address=0x3469420053F01
    ),
    "Moon Zora Trial HP": MMRLocationData(
        region="The Moon",
        address=0x3469420054701
    ),
    "Moon Link Trial Garo Master Chest": MMRLocationData(
        region="The Moon",
        address=0x3469420066601
    ),
    "Moon Link Trial Iron Knuckle Chest": MMRLocationData(
        region="The Moon",
        address=0x3469420066602
    ),
    "Moon Link Trial HP": MMRLocationData(
        region="The Moon",
        address=0x3469420056601
    ),
    "Moon Trade All Masks": MMRLocationData(
        region="The Moon",
        address=0x346942000007B
    ),
    "Defeat Majora": MMRLocationData(
        region="The Moon",
        locked_item="Victory"
    ),
    
    # Grass/Pots/Hitspots/Hidden Rupees etc past this point

    # Before Clock Town Grass
    "Before Clock Town Keaton Grass (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A09,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Keaton Grass (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A10,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),    
    "Before Clock Town Keaton Grass (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A0A,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Keaton Grass (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A0B,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Keaton Grass (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A0C,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Keaton Grass (6)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A0D,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Keaton Grass (7)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A0E,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Keaton Grass (8)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A0F,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Keaton Grass (9)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A11,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),        
    "Before Clock Town Skullkid Keaton Grass (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A00,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Skullkid Keaton Grass (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A01,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Skullkid Keaton Grass (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A02,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Skullkid Keaton Grass (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A03,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),    
    "Before Clock Town Skullkid Keaton Grass (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A04,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),    
    "Before Clock Town Skullkid Keaton Grass (6)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A05,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),    
    "Before Clock Town Skullkid Keaton Grass (7)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A06,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Skullkid Keaton Grass (8)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A07,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Before Clock Town Skullkid Keaton Grass (9)": MMRLocationData(
        region="Clock Town",
        address=0x3469420131A08,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146511,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146516,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146515,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146510,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146514,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (6)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146512,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (7)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146519,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (8)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146518,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (9)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146513,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (10)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146517,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (11)": MMRLocationData(
        region="Clock Town",
        address=0x346942014651A,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass (12)": MMRLocationData(
        region="Clock Town",
        address=0x346942014651B,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),

    "Lost Woods Grass Patch 2 (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146505,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146500,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (3)": MMRLocationData(
        region="Clock Town",
        address=0x346942014650B,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146504,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (5)": MMRLocationData(
        region="Clock Town",
        address=0x346942014650A,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (6)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146509,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (7)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146508,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (8)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146503,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (9)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146502,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (10)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146501,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (11)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146506,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Grass Patch 2 (12)": MMRLocationData(
        region="Clock Town",
        address=0x3469420146507,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136502,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136501,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136507,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136506,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136505,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (6)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136504,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (7)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136503,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (8)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136500,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Lost Woods Keaton Grass (9)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136508,
        can_create=lambda options: options.intro_checks.value and options.grasssanity.value
    ),
    "Laundry Pool Grass (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420127000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Laundry Pool Grass (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420127001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Laundry Pool Grass (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420127002,
        can_create=lambda options: options.grasssanity.value
    ),
    # North Clock Town Keaton Grass
    "North Clock Town Keaton Grass (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E00,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E01,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E02,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E03,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E04,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (6)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E05,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (7)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E06,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (8)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E07,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (9)": MMRLocationData(
        region="Clock Town",
        address=0x3469420136E08,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field 

    "Termina Field Grass Near Western Water Ramp (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Water Ramp (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri Gossip Tree (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Southwest Above Rock Ledge (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Western Fountains (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Takkuri (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Kamaro (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Peehat Grotto (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass In Front of Log (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Northern Ramp (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Grass Grotto (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Below Southeast Hill Fence (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bottom of Southeast Hill Grass (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillars (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Pillar Grotto (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Middle of Southeast Hill Grass (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Business Scrub Grotto (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Observatory Fence (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Near Eastern Gossip Grotto (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112DB,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field Grass Grotto Grass

    "Termina Field Grass Grotto Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B040,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B041,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B042,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B043,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B044,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B045,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B046,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B047,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B048,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B049,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B04A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B04B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (13)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B04C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Grotto Grass (14)": MMRLocationData(
        region="Termina Field",
        address=0x346942012B04D,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field Cow Grotto Grass

    "Termina Field Cow Grotto Grass Group 1 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (9)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (10)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100AD9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (11)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100ADA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 1 (12)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100ADB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (9)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (10)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101AD9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (11)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101ADA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 2 (12)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101ADB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (9)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (10)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102AD9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (11)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102ADA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 3 (12)": MMRLocationData(
        region="Termina Field",
        address=0x3469420102ADB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (9)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (10)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103AD9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (11)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103ADA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 4 (12)": MMRLocationData(
        region="Termina Field",
        address=0x3469420103ADB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (9)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (10)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104AD9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (11)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104ADA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 5 (12)": MMRLocationData(
        region="Termina Field",
        address=0x3469420104ADB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (9)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (10)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105AD9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (11)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105ADA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Cow Grotto Grass Group 6 (12)": MMRLocationData(
        region="Termina Field",
        address=0x3469420105ADB,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field Peehat Grotto Grass

    "Termina Field Peehat Grotto Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peehat Grotto Grass (12)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008DB,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field Bio Baba Grotto Grass

    "Termina Field Bio Baba Grotto Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128BB0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bio Baba Grotto Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128BB1,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field Eastern Gossip Grotto Grass

    "Termina Field Eastern Gossip Grotto Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128220,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Gossip Grotto Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128221,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Gossip Grotto Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128222,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Gossip Grotto Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128223,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Gossip Grotto Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128224,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field Eastern Pillar Grotto Grass
    "Termina Field Eastern Pillar Grotto Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB4D,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (13)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Eastern Pillar Grotto Grass (14)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AB4C,
        can_create=lambda options: options.grasssanity.value
    ),
    # Termina Field Bombable Rock Grass

    "Termina Field Bombable Rock Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bombable Rock Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bombable Rock Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128002,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bombable Rock Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128003,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Bombable Rock Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420128004,
        can_create=lambda options: options.grasssanity.value
    ),
    # Road to Southern Swamp
     
    "Road to Southern Swamp Outside Archery Grass (1)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420124000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Outside Archery Grass (2)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420124001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (1)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100400,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (2)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100401,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (3)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100402,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (4)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100403,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (5)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100404,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (6)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100405,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (7)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100406,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (8)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100407,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (9)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420100408,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (10)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101400,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (11)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101401,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (12)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101402,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (13)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101403,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (14)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101404,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (15)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101405,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (16)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101406,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (17)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101407,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass (18)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x3469420101408,
        can_create=lambda options: options.grasssanity.value
    ),
    # Road to Southern Swamp Grotto
    "Road to Southern Swamp Grotto Grass (1)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (2)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (3)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (4)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (5)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (6)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (7)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (8)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (9)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (10)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (11)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (12)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (13)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF4C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (14)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942012AF4D,
        can_create=lambda options: options.grasssanity.value
    ),
    # Southern Swamp

    "Southern Swamp Owl Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420124500,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Owl Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420124501,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100452,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100453,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100454,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100455,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100456,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100457,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100458,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100459,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942010045A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Tourist Centre (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942010045B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102452,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102453,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102454,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102455,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102456,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102457,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102458,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103452,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (13)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103453,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (14)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103454,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (15)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103455,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (16)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103456,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (17)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103457,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Near Witch Shop (18)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103458,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Near Gossip Stone Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420124520,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Near Gossip Stone Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420124521,
        can_create=lambda options: options.grasssanity.value
    ),              

    # Woods of Mystery

    "Woods of Mystery Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126410,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126412,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126411,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126400,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126401,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126431,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126430,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126442,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126440,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126441,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126443,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (13)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (14)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126482,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (15)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126484,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (16)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126481,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (17)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126480,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (18)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126483,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (19)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126471,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (20)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126470,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Unique Grass": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126420,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 3 Unique Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126460,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 3 Unique Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126461,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD4D,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (13)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (14)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD4C,
        can_create=lambda options: options.grasssanity.value
    ),

    # Southern Swamp Grotto
    "Southern Swamp Grotto Grass (1)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (2)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (3)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (4)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (5)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (6)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (7)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (8)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (9)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (10)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (11)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (12)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (13)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE4C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grotto Grass (14)": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942012AE4D,
        can_create=lambda options: options.grasssanity.value
    ),

    #Deku Palace Bean Grotto Grass
    "Deku Palace Bean Grotto Grass (1)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (2)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (3)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (4)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (5)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (6)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (7)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (8)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (9)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (10)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (11)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008CA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass (12)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008CB,
        can_create=lambda options: options.grasssanity.value
    ),

    # Woodfall Grass
    "Woodfall Grass (1)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124600,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Grass (2)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124601,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Grass (3)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124602,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Grass (4)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124603,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Grass (5)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124604,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Grass (6)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124605,
        can_create=lambda options: options.grasssanity.value
    ),
    # Southern Swamp After Dungeon Clear
    "Southern Swamp Owl Post Dungeon Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420120000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Owl Post Dungeon Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420120001,
        can_create=lambda options: options.grasssanity.value
    ),

    # Milk Road Owl Grass
    "Milk Road Owl Grass (1)": MMRLocationData(
        region="Milk Road",
        address=0x3469420122200,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Owl Grass (2)": MMRLocationData(
        region="Milk Road",
        address=0x3469420122201,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Owl Grass (3)": MMRLocationData(
        region="Milk Road",
        address=0x3469420122202,
        can_create=lambda options: options.grasssanity.value
    ),
    # Milk Road Keaton Grass
    "Milk Road Keaton Grass (1)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132200,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (2)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132201,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (3)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132202,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (4)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132203,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (5)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132204,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (6)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132205,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (7)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132206,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (8)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132207,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Keaton Grass (9)": MMRLocationData(
        region="Milk Road",
        address=0x3469420132208,
        can_create=lambda options: options.grasssanity.value
    ),
    # Milk Road Gorman Racetrack Grass
    "Milk Road Gorman Racetrack Grass Group 1 (1)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (2)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (3)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (4)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (5)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (6)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (7)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (8)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (9)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (10)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006A9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (11)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006AA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (12)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201006AB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (1)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (2)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (3)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (4)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (5)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (6)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (7)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (8)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (9)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (10)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016A9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (11)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016AA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (12)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694201016AB,
        can_create=lambda options: options.grasssanity.value
    ),
    # Romani Ranch Grass
    "Romani Ranch Grass In Front of Gossip Tree (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010035A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass In Front of Gossip Tree (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010035B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010135A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Gossip Tree (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010135B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010235A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Near Entrance (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010235B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010335A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Between Entrance and Barn (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010335B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Behind Barn (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104358,
        can_create=lambda options: options.grasssanity.value
    ),

    # Twin Isles Grotto Grass

    "Twin Isles Grotto Grass (1)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (2)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (3)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (4)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (5)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (6)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (7)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (8)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (9)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (10)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (11)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (12)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (13)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA4C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Isles Grotto Grass (14)": MMRLocationData(
        region="Twin Islands",
        address=0x346942012AA4D,
        can_create=lambda options: options.grasssanity.value
    ),
    # Goron Village Lens Cave Grass
    "Goron Village Lens Cave Grass (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100900,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (2)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100901,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (3)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100902,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (4)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100903,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (5)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100904,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (6)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100905,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (7)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100906,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (8)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100907,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (9)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100908,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (10)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100909,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (11)": MMRLocationData(
        region="Goron Village",
        address=0x346942010090A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (12)": MMRLocationData(
        region="Goron Village",
        address=0x346942010090B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (13)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101900,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (14)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101901,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (15)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101902,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (16)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101903,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (17)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101904,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (18)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101905,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (19)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101906,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (20)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101907,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (21)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101908,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (22)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101909,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (23)": MMRLocationData(
        region="Goron Village",
        address=0x346942010190A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass (24)": MMRLocationData(
        region="Goron Village",
        address=0x346942010190B,
        can_create=lambda options: options.grasssanity.value
    ),

    # Path To Snowhead Grotto Grass

    "Path To Snowhead Grotto Grass (1)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A440,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (2)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A441,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (3)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A442,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (4)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A443,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (5)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A444,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (6)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A445,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (7)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A446,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (8)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A447,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (9)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A448,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (10)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A449,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (11)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A44A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (12)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A44B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (13)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A44C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Path To Snowhead Grotto Grass (14)": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942012A44D,
        can_create=lambda options: options.grasssanity.value
    ),

    # Mountain Village Spring Grass

    "Mountain Village Springtime Grass (1)": MMRLocationData( 
        region="Mountain Village",
        address=0x3469420125A00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (5)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (6)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (7)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (8)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (9)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A05,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (10)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A06,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (11)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A07,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (12)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A08,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (13)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A10,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (14)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A11,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (15)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A12,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (16)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A13,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (17)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A14,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (18)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A15,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (19)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A16,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (20)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A17,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (21)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A18,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (22)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A20,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (23)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A21,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (24)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A22,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (25)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A23,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (26)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A24,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (27)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A25,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (28)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A26,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (29)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A27,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (30)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420145A28,
        can_create=lambda options: options.grasssanity.value
    ),

    # Mountain Village Keaton Grass 

    "Mountain Village Keaton Grass (0)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (5)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A05,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (6)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A06,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (7)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A07,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (8)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A08,
        can_create=lambda options: options.grasssanity.value
    ),

    # Mountain Village Spring Grotto Grass 

    "Mountain Village Spring Grotto Grass (1)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (2)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (3)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (4)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (5)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (6)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (7)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (8)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (9)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (10)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (11)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (12)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (13)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC4C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Spring Grotto Grass (14)": MMRLocationData(
        region="Mountain Village",
        address=0x346942012AC4D,
        can_create=lambda options: options.grasssanity.value
    ),

    # Twin Isles Spring Grass

    "Twin Islands Springtime Grass Group 1 (1)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (2)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (3)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (4)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (5)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (6)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (7)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (8)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (9)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (10)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005E9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (11)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005EA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Twin Islands Springtime Grass Group 1 (12)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201005EB,
        can_create=lambda options: options.grasssanity.value
    ),
    # Great Bay Coast Grotto Grass

    "Great Bay Coast Grotto Grass (1)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A840,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (2)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A841,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (3)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A842,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (4)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A843,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (5)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A844,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (6)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A845,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (7)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A846,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (8)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A847,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (9)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A848,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grotto Grass (10)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A849,
        can_create=lambda options: options.grasssanity.value
    ), 
    "Great Bay Coast Grotto Grass (11)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A84A,
        can_create=lambda options: options.grasssanity.value
    ), 
    "Great Bay Coast Grotto Grass (12)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A84B,
        can_create=lambda options: options.grasssanity.value
    ), 
    "Great Bay Coast Grotto Grass (13)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A84C,
        can_create=lambda options: options.grasssanity.value
    ), 
    "Great Bay Coast Grotto Grass (14)": MMRLocationData(
        region="Great Bay",
        address=0x346942012A84D,
        can_create=lambda options: options.grasssanity.value
    ), 

    # Great Bay Coast Grass - Requires Epona's Song
    "Great Bay Coast Grass (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420123700,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grass (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420123701,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grass (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420123702,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grass (4)": MMRLocationData(
        region="Great Bay",
        address=0x3469420123703,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Grass (5)": MMRLocationData(
        region="Great Bay",
        address=0x3469420123704,
        can_create=lambda options: options.grasssanity.value
    ),

    # Great Bay Coast Cow Grotto Grass

    "Great Bay Coast Cow Grotto Grass Group 1 (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B70,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (4)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (5)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (6)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B75,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (7)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B76,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (8)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B77,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (9)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B78,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (10)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B79,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (11)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B7A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 1 (12)": MMRLocationData(
        region="Great Bay",
        address=0x3469420100B7B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B70,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (4)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (5)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (6)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B75,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (7)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B76,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (8)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B77,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (9)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B78,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (10)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B79,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (11)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B7A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 2 (12)": MMRLocationData(
        region="Great Bay",
        address=0x3469420101B7B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B70,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (4)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (5)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (6)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B75,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (7)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B76,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (8)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B77,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (9)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B78,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (10)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B79,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (11)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B7A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 3 (12)": MMRLocationData(
        region="Great Bay",
        address=0x3469420102B7B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B70,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (4)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (5)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (6)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B75,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (7)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B76,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (8)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B77,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (9)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B78,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (10)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B79,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (11)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B7A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 4 (12)": MMRLocationData(
        region="Great Bay",
        address=0x3469420103B7B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B70,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (4)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (5)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (6)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B75,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (7)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B76,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (8)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B77,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (9)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B78,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (10)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B79,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (11)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B7A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 5 (12)": MMRLocationData(
        region="Great Bay",
        address=0x3469420104B7B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B70,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (4)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (5)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (6)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B75,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (7)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B76,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (8)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B77,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (9)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B78,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (10)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B79,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (11)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B7A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Great Bay Coast Cow Grotto Grass Group 6 (12)": MMRLocationData(
        region="Great Bay",
        address=0x3469420105B7B,
        can_create=lambda options: options.grasssanity.value
    ),

    # Zora Cape Grotto Grass

    "Zora Cape Grotto Grass (1)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A640,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (2)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A641,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (3)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A642,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (4)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A643,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (5)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A644,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (6)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A645,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (7)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A646,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (8)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A647,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (9)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A648,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (10)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A649,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (11)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A64A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (12)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A64B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (13)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A64C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (14)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A64D,
        can_create=lambda options: options.grasssanity.value
    ),

    # Road To Ikana Grotto Grass

    "Road To Ikana Grotto Grass (1)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A740,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (2)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A741,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (3)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A742,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (4)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A743,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (5)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A744,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (6)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A745,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (7)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A746,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (8)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A747,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (9)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A748,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (10)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A749,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (11)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A74A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (12)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A74B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (13)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A74C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road To Ikana Grotto Grass (14)": MMRLocationData(
        region="Road to Ikana",
        address=0x346942012A74D,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Graveyard Lower Region Grass

    "Ikana Graveyard Lower Grass (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124300,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Lower Grass (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124301,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Lower Grass (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124302,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Lower Grass (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124303,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Lower Grass (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124304,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Graveyard Upper Region Grass

    "Ikana Graveyard Upper Grass (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144320,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144321,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144322,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144323,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144324,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144325,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (7)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144326,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (8)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144327,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (9)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420144328,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Graveyard Bombable Grotto Grass

    "Ikana Graveyard Bombable Grotto Grass (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A940,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A941,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A942,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A943,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A944,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A945,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (7)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A946,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (8)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A947,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (9)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A948,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (10)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A949,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (11)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A94A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (12)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A94B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (13)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A94C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Bombable Grotto Grass (14)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x346942012A94D,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Canyon Grass

    "Ikana Canyon Grass (1)": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420121300,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grass (2)": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420121301,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grass (3)": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420121302,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grass (4)": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420121303,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Canyon Grotto Grass

    "Ikana Canyon Grotto Grass (1)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A540,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (2)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A541,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (3)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A542,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (4)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A543,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (5)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A544,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (6)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A545,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (7)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A546,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (8)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A547,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (9)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A548,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (10)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A549,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (11)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A54A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (12)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A54B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (13)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A54C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (14)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942012A54D,
        can_create=lambda options: options.grasssanity.value
    ),

    # Secret Shrine Grass

    "Secret Shrine Entrance Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Entrance Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Entrance Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126002,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Entrance Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126003,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Entrance Grass (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126004,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Entrance Grass (6)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126005,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Dinolfos Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126020,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Dinolfos Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126021,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Dinolfos Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126022,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Dinolfos Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126023,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126033,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126032,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126030,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126031,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126034,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126042,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126043,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126045,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126044,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126047,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (6)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126046,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (7)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126040,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (8)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126041,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126055,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126052,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126051,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126050,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126054,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (6)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126053,
        can_create=lambda options: options.grasssanity.value
    ),

    # Beneath the Well Grass

    "Beneath the Well Left Side Back Room Grass (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B51,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Left Side Back Room Grass (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B50,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B30,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B31,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B32,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B33,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Cow Grass (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B92,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Cow Grass (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B91,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Cow Grass (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B90,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (5)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B70,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Castle Grass

    "Ikana Castle Grass (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D0B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (4)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (5)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (6)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D05,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (7)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D06,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (8)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D07,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (9)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D08,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (10)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D09,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Castle Grass (11)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D0A,
        can_create=lambda options: options.grasssanity.value
    ),
    # Dungeon Grass
    # Woodfall Temple

    "Woodfall Temple Entrance Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B20,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Entrance Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B21,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Entrance Room Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B22,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Entrance Room Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B23,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Entrance Room Grass (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B24,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Main Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B10,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Main Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B11,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Main Room Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B12,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Deku Elevator Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B50,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Deku Elevator Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B51,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B60,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B61,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B62,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B63,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B64,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Dragonfly Chest Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Dragonfly Chest Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Dragonfly Chest Room Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (6)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (7)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (8)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (9)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BAA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (10)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (11)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (1)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (2)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (3)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (4)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (5)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (6)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F05,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (7)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F06,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (8)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F07,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (9)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F08,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (10)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F09,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (11)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F0A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (12)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F0B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (13)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F0C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (14)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F0D,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (15)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F0E,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (16)": MMRLocationData(
        region="Odolwa's Lair",
        address=0x3469420121F0F,
        can_create=lambda options: options.grasssanity.value
    ),

    # Southern Swamp Post Dungeon Grass Near Tourist Centre

    "Southern Swamp Post Dungeon Grass Near Tourist Centre (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100002,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100003,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100004,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100005,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100006,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100007,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100008,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100009,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942010000A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Tourist Centre (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942010000B,
        can_create=lambda options: options.grasssanity.value
    ),

    # Southern Swamp Post Dungeon Grass Near Witch Shop

    "Southern Swamp Post Dungeon Grass Near Witch Shop (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102002,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102003,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102004,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102005,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102006,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102007,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102008,
        can_create=lambda options: options.grasssanity.value
    ),

    # Southern Swamp Post Dungeon Grass Near Witch Shop

    "Southern Swamp Post Dungeon Grass Near Witch Shop (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103002,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (13)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103003,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (14)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103004,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (15)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103005,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (16)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103006,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (17)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103007,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Grass Near Witch Shop (18)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103008,
        can_create=lambda options: options.grasssanity.value
    ),

    # Southern Swamp Post Dungeon Gossip Grass

    "Southern Swamp Post Dungeon Gossip Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420120020,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Post Dungeon Gossip Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420120021,
        can_create=lambda options: options.grasssanity.value
    ),


        # Snowhead Temple Grass
    "Snowhead Temple Basement Grass (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122140,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122141,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122142,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122143,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122144,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122145,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122146,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (8)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122147,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (9)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122148,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (10)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122149,
        can_create=lambda options: options.grasssanity.value
    ),
        # Stone Tower Temple Grass

    "Stone Tower Temple Entrance Room Grass (1)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121600,
        can_create=lambda options: options.grasssanity.value
    ),

    "Stone Tower Temple Entrance Room Grass (2)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121601,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Entrance Room Grass (3)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121602,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (1)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121623,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (2)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121621,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (3)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121624,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (4)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121620,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (5)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121622,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (6)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121625,
        can_create=lambda options: options.grasssanity.value
    ),
      # Clock Town Pots
    "Trading Post Pot": MMRLocationData(
        region="Clock Town",
        address=0x3469420203400,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205403,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205402,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205404,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205401,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205400,
        can_create=lambda options: options.potsanity.value
    ),
    "Top of Clock Tower Pots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420201900,
        can_create=lambda options: options.potsanity.value
    ),
    "Top of Clock Tower Pots (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420201901,
        can_create=lambda options: options.potsanity.value
    ),
    "Top of Clock Tower Pots (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420201902,
        can_create=lambda options: options.potsanity.value
    ), 
    "Top of Clock Tower Pots (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420201903,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202901,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202900,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202902,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202903,
        can_create=lambda options: options.potsanity.value
    ),
    "Astral Observatory Pots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202911,
        can_create=lambda options: options.potsanity.value
    ),
    "Astral Observatory Pots (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202910,
        can_create=lambda options: options.potsanity.value
    ),
    "Astral Observatory Pots (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202912,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Termina Field Pots
    
    "Termina Field Eastern Pillar Pot": MMRLocationData(
        region="Termina Field",
        address=0x3469420202D00,
        can_create=lambda options: options.potsanity.value
    ),
    "Termina Field Deku Business Scrub Grotto Pot": MMRLocationData(
        region="Termina Field",
        address=0x3469420200790,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Southern Swamp Pots
    
    "Road to Southern Swamp Outside Archery Pots (1)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202040F1,
        can_create=lambda options: options.potsanity.value
    ),
    "Road to Southern Swamp Outside Archery Pots (2)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202040F0,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Beneath Witch Shop Pots (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420204522,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Beneath Witch Shop Pots (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420204521,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Beneath Witch Shop Pots (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420204520,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Swamp Spider House Pots
    
    "Swamp Spider House Main Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202710,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202711,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202712,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202713,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202714,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (6)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202715,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (7)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202716,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (8)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202717,
        can_create=lambda options: options.potsanity.value
    ),    
    "Swamp Spider House Tablet Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202730,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Tablet Room Pots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202731,
        can_create=lambda options: options.potsanity.value
    ),        

    "Swamp Spider House Giant Jar Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202740,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202741,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202742,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202743,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202744,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (6)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202745,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (7)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202746,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (8)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202747,
        can_create=lambda options: options.potsanity.value
    ),    
    "Swamp Spider House Gold Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202720,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202721,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202722,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202723,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202724,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (6)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202725,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Deku Palace Pots
    "Deku Palace Right Side Upper Pots (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420202B10,
        can_create=lambda options: options.potsanity.value
    ),
    "Deku Palace Right Side Upper Pots (2)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420202B11,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Butler Race Pots
    
    "Deku Butler Race Pots (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420205200,
        can_create=lambda options: options.potsanity.value
    ),
    "Deku Butler Race Pots (2)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420205201,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Woodfall Pots
    
    "Woodfall Owl Pots (1)": MMRLocationData(
        region="Woodfall",
        address=0x3469420204601,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Owl Pots (2)": MMRLocationData(
        region="Woodfall",
        address=0x3469420204600,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Owl Pots (3)": MMRLocationData(
        region="Woodfall",
        address=0x3469420204602,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Woodfall Temple Pots
    
    "Woodfall Temple Entrance Pot": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B20,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B10,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B11,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B12,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B13,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B14,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (6)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B15,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (7)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B17,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (8)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B18,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B51,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B50,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B53,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B52,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Gekko Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B83,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Gekko Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B82,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Gekko Pots (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B81,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Gekko Pots (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B80,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Left Side Bridge Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B30,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Left Side Bridge Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B31,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Pre Boss Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B01,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Pre Boss Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B00,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Post Dungeon Witch Pot (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420200020,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Post Dungeon Witch Pot (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420200021,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Post Dungeon Witch Pot (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420200022,
        can_create=lambda options: options.potsanity.value
    ),
    # Mountain Village Pots
    
    "Mountain Village Rooftop Pot": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205000,
        can_create=lambda options: options.potsanity.value
    ),
    "Mountain Village Pots (1)": MMRLocationData(
        region="Mountain Village",
        address=0x34694202050F0,
        can_create=lambda options: options.potsanity.value
    ),
    "Mountain Village Pots (2)": MMRLocationData(
        region="Mountain Village",
        address=0x34694202050F1,
        can_create=lambda options: options.potsanity.value
    ),
    "Mountain Smithy Pots Inside at Night (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420202CF0,
        can_create=lambda options: options.potsanity.value
    ),
    "Mountain Smithy Pots Inside at Night (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420202CF1,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Goron Racetrack Pots
    
    "Goron Racetrack Pots (1)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B14,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (2)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B15,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (3)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B17,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (4)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B16,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (5)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B12,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (6)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B10,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (7)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B13,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (8)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B0F,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (9)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B11,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (10)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B00,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (11)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B02,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (12)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B05,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (13)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B04,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (14)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B03,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (15)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B07,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (16)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B06,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (17)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B09,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (18)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B08,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (19)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B0A,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (20)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B01,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (21)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B0E,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (22)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B18,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (23)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B19,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (24)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B1A,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (25)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B1D,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (26)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B1B,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (27)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B1C,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (28)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B0D,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (29)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B0C,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (30)": MMRLocationData(
        region="Goron Racetrack",
        address=0x3469420206B0B,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Goron Shrine Pots
    
    "Goron Shrine Pots (1)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203204,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (2)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203203,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (3)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203207,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (4)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203202,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (5)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203200,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (6)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203205,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (7)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203201,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (8)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203206,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (9)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203210,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (10)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203211,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (11)": MMRLocationData(
        region="Goron Shrine",
        address=0x3469420203212,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Snowhead Temple Pots
    "Snowhead Temple Entrance Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202100,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Entrance Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202101,
        can_create=lambda options: options.potsanity.value
    ),

    "Snowhead Temple Blue Door Lava Bridge Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202123,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202125,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202124,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202126,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202122,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202120,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202121,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Pots Basement (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202146,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Pots Basement (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202147,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Scarecrow Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202140,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Scarecrow Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202141,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020215B,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020215C,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020215A,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202157,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202158,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202159,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202156,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (8)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202153,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (9)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202151,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (10)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202155,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (11)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202154,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (12)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202150,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (13)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202152,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Orange Door Push Block Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202131,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Orange Door Push Block Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202130,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Orange Door Push Block Ghost Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202132,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Orange Door Push Block Ghost Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202133,
        can_create=lambda options: options.potsanity.value
    ),         
    "Snowhead Temple Locked Grey Door Wolfos Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202112,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202113,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202110,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202114,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202111,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Goron Pound Puzzle Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202181,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Goron Pound Puzzle Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202180,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room 2nd Floor Bridge Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202144,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room 2nd Floor Bridge Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202145,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room 4th Floor Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202143,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room 4th Floor Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202142,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C0,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C1,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C2,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C3,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C4,
        can_create=lambda options: options.potsanity.value
    ),        
    "Goht Boss Room Pots (1)": MMRLocationData(
        region="Goht's Lair",
        address=0x346942020440C,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (2)": MMRLocationData(
        region="Goht's Lair",
        address=0x346942020440D,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (3)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204408,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (4)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204400,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (5)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204402,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (6)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204409,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (7)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204407,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (8)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204406,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (9)": MMRLocationData(
        region="Goht's Lair",
        address=0x346942020440A,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (10)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204401,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (11)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204403,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (12)": MMRLocationData(
        region="Goht's Lair",
        address=0x346942020440B,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (13)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204404,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (14)": MMRLocationData(
        region="Goht's Lair",
        address=0x3469420204405,
        can_create=lambda options: options.potsanity.value
    ),
    
    "Mountain Village Springtime Pots (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205AF0,
        can_create=lambda options: options.potsanity.value
    ),         
    "Mountain Village Springtime Pots (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205AF1   ,
        can_create=lambda options: options.potsanity.value
    ),   
    "Mountain Village Springtime Pots (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205A00,
        can_create=lambda options: options.potsanity.value
    ),   


    # Romani Ranch Pots
    
    "Romani Ranch Baby Cuccoos Pots (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202042F0,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Baby Cuccoos Pots (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202042F1,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204102,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204101,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204100,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204103,
        can_create=lambda options: options.potsanity.value
    ),
    # Great Bay Coast Pots
    
    "Great Bay Coast Behind Marine Lab Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203707,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Behind Marine Lab Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203709,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Behind Marine Lab Pots (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203708,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Behind Marine Lab Pots (4)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370E,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Rock Pools Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203704,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Rock Pools Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370B,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370D,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203706,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203705,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (4)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370C,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Upper Rock Wall Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203702,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Upper Rock Wall Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203701,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Upper Rock Wall Pots (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203700,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Beside Pirates Fortress Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203703,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Beside Pirates Fortress Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370A,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Ocean Spiderhouse Pots
    
    "Ocean Spiderhouse Bottom of Ramp Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202803,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Bottom of Ramp Pots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202800,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Bottom of Ramp Pots (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202801,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Bottom of Ramp Pots (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202802,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202813,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202814,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202810,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202811,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (5)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202812,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202857,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202851,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202856,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202855,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (5)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202850,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (6)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202854,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (7)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202852,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (8)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202853,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Coloured Skulls Room Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202831,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Coloured Skulls Room Pots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202830,
        can_create=lambda options: options.potsanity.value
    ),


    # Pinnacle Rock
    
    "Pinnacle Rock Pots (1)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202500,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (2)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202501,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (3)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202502,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (4)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202503,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (5)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202504,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (6)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202505,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (7)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202506,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (8)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202507,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (9)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202508,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (10)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202509,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (11)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x346942020250A,
        can_create=lambda options: options.potsanity.value
    ),
    
        # Pirates' Fortress Pots
    
    "Pirates Fortress Sewers Cage Room Pots (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202023B0,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Cage Room Pots (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202023B1,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers After Gate Hidden Ladder Pots (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202023A1,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers After Gate Hidden Ladder Pots (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202023A0,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Exit Pots (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420202391,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Exit Pots (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420202390,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Exit Pots (3)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420202392,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Underwater Chest Room Pots (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202360,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Underwater Chest Room Pots (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202361,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Underwater Chest Room Pots (3)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202362,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Green Guard Pots (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202380,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Green Guard Pots (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202381,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Green Guard Pots (3)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202382,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Upper Beehive Room Pots (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202331,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Upper Beehive Room Pots (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420202330,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Pink Guard Pots (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x34694202023D1,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Pink Guard Pots (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x34694202023D0,
        can_create=lambda options: options.potsanity.value
    ),

    # Zora Cape Pots


    "Zora Cape Like Like Pool Pots (1)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203800,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Like Like Pool Pots (2)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203801,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (1)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203802,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (2)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203803,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (3)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203804,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (4)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203805,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Jar Game Pots (1)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203811,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Jar Game Pots (2)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203812,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Jar Game Pots (3)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203813,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Jar Game Pots (4)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203814,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Jar Game Pots (5)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203815,
        can_create=lambda options: options.potsanity.value
    ),        

    # Great Bay Temple Pots
    
    "Great Bay Temple Above Blender Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204901,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Above Blender Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204900,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C3,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204910,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204911,
        can_create=lambda options: options.potsanity.value
    ),
    #Fairy Pot so no item
    # "Great Bay Temple Red Green Pipe Tunnel Room Pots (3)": MMRLocationData(
    #     region="Great Bay Temple",
    #     address=0x346942020491B,
    #     can_create=lambda options: options.potsanity.value
    # ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942020491A,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204913,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204915,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204916,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204917,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (9)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204914,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (10)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204912,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (11)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204918,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (12)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204919,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Before Gekko Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204945,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Before Gekko Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204940,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Before Gekko Room Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204946,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Before Gekko Room Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204941,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Before Gekko Room Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204943,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Before Gekko Room Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204944,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Before Gekko Room Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204942,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204963,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204962,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204961,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204960,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E3,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049EA,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E8,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E5,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E4,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E6,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (9)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E7,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (10)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (11)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049EB,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (12)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E9,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204972,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204970,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204976,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204971,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204977,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204974,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204975,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Wart Room Pots (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204973,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204996,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204997,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204990,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204991,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204994,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204995,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204993,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204992,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Seesaw Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049A2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Seesaw Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049A0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Seesaw Room Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049A1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B5,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B3,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B7,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B6,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B4,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (1)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F07,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (2)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F06,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (3)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F05,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (4)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F04,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (5)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F00,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (6)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F03,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (7)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F02,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (8)": MMRLocationData(
        region="Gyorg's Lair",
        address=0x3469420205F01,
        can_create=lambda options: options.potsanity.value
    ),

    # Ikana Road and Gravyard Pots
    
    "Road To Ikana Scarecrow Pillar Pot": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420205300,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C01,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C00,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C10,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C11,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C12,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Entrance Grave Pot": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C02,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Entryway Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C32,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Entryway Pots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C33,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C30,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C31,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C35,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C34,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203001,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203003,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203005,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203002,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203000,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203004,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (7)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203009,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (8)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203007,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (9)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203006,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (10)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203008,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Secret Shrine Pots
    
    "Secret Shrine Entrance Pots (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206001,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Entrance Pots (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206002,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Entrance Pots (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206000,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206015,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206014,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206013,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206012,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206010,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (6)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206011,
        can_create=lambda options: options.potsanity.value
    ),

    #Sakons Hideout
    "Sakons Hideout Pots (1)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420204F10,
        can_create=lambda options: options.potsanity.value
    ),
    "Sakons Hideout Pots (2)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420204F11,
        can_create=lambda options: options.potsanity.value
    ),          
    "Sakons Hideout Pots (3)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420204F12,
        can_create=lambda options: options.potsanity.value
    ),
    "Sakons Hideout Pots (4)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420204F13,
        can_create=lambda options: options.potsanity.value
    ),
    "Sakons Hideout Pots (5)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420204F14,
        can_create=lambda options: options.potsanity.value
    ),      

    
    # Ikana Castle
    "Ikana Castle Exterior Corner Pot": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D00,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Frozen Eyes Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D11,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Frozen Eyes Room Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D10,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D20,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D21,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D42,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D41,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D40,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (4)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D43,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Staircase Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D60,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Staircase Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D61,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Right Side Staircase Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D71,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Right Side Staircase Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D70,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205601,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205600,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205603,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (4)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205602,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (5)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205611,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (6)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205612,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (7)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205613,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (8)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205610,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Well Pots
    
    "Well Left Side Back Room Pots (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B52,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B50,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B54,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B51,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (5)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B53,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B69,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B68,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B67,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B66,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (5)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B65,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (6)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B64,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (7)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B63,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (8)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B62,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (9)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B61,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (10)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B60,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC2,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC3,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC1,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC0,
        can_create=lambda options: options.potsanity.value
    ),


    # Stone Tower Climb Pots
    "Stone Tower Climb Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205815,
        can_create=lambda options: options.potsanity.value    
     ),
    "Stone Tower Climb Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205816,
        can_create=lambda options: options.potsanity.value    
    ),  
    # Stone Tower Lower Scarecrow Pots
    "Stone Tower Lower Scarecrow Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205805,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205814,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205808,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (4)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205807,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (5)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205804,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (6)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205806,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (7)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205802,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (8)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205801,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (9)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205803,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (10)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205800,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (11)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205809,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (12)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580A,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205812,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205813,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205811,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (4)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580F,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (5)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205810,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (6)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580E,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (7)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580C,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (8)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580D,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (9)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580B,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020581A,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205817,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205818,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (4)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205819,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Stone Tower Temple Pots
    
    "Stone Tower Temple Entrance Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201601,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Entrance Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201600,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201645,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201642,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201644,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201643,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201646,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (6)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201641,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (7)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201640,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (8)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201647,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Near Locked Door Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201635,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Near Locked Door Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201636,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201633,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201634,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201632,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201630,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201631,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Mirror Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201671,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Mirror Room Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201670,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201693,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201690,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201692,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201691,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201680,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201681,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201682,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201686,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201683,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (6)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201687,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (7)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201685,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (8)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201684,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Inverted Stone Tower Temple Pots
    
    "Inverted Stone Tower Bean Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205903,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205904,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205900,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (4)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205901,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (5)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205902,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201832,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201833,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201835,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201834,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (5)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201831,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (6)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201830,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Gomess Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B3,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Gomess Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B0,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Gomess Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B1,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Gomess Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B2,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Lower Bridge Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201811,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Lower Bridge Room Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201810,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201822,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201820,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201821,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201823,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201840,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201843,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201844,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201841,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (5)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201842,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942020188A,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942020188B,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201889,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201888,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201883,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201881,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201885,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201887,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (5)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201884,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (6)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201886,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (7)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201880,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (8)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201882,
        can_create=lambda options: options.potsanity.value
    ),

    
    # Moon Trial Pots
    
    "Moon Goron Trial Pots (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F08,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (2)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F07,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (3)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F09,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (4)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0A,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (5)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F00,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (6)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F01,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (7)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F04,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (8)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F02,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (9)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F03,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (10)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0E,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (11)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0C,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (12)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0B,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (13)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0D,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (14)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F06,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (15)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F05,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420206602,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (2)": MMRLocationData(
        region="The Moon",
        address=0x3469420206603,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (3)": MMRLocationData(
        region="The Moon",
        address=0x3469420206601,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (4)": MMRLocationData(
        region="The Moon",
        address=0x3469420206600,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (5)": MMRLocationData(
        region="The Moon",
        address=0x3469420206606,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (6)": MMRLocationData(
        region="The Moon",
        address=0x3469420206604,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (7)": MMRLocationData(
        region="The Moon",
        address=0x3469420206605,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (8)": MMRLocationData(
        region="The Moon",
        address=0x3469420206607,
        can_create=lambda options: options.potsanity.value
    ),
    "Majora Lair Pots (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420200B00,
        can_create=lambda options: options.potsanity.value
    ),
    "Majora Lair Pots (2)": MMRLocationData(
        region="The Moon",
        address=0x3469420200B01,
        can_create=lambda options: options.potsanity.value
    ),

    # Hitspots

    # South Clock Town Targets Hitspot
    "South Clock Town Targets Hitspot (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156F02,
        can_create=lambda options: options.hitsanity.value
    ),
    "South Clock Town Targets Hitspot (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156F00,
        can_create=lambda options: options.hitsanity.value
    ),
    "South Clock Town Targets Hitspot (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156F01,
        can_create=lambda options: options.hitsanity.value
    ),

    # East Clock Town Targets And Basket Hitspots
    "East Clock Town Targets And Basket Hitspots (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C22,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C21,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C20,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C02,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C10,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C00,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (6)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C01,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (7)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C11,
        can_create=lambda options: options.hitsanity.value
    ),
    "East Clock Town Targets And Basket Hitspots (8)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156C12,
        can_create=lambda options: options.hitsanity.value
    ),

    # Sword School Gong
    "Sword School Gong": MMRLocationData(
        region="Clock Town",
        address=0x3469420155400,
        can_create=lambda options: options.hitsanity.value
    ),

    # Termina Field West Wall Hitspot
    "Termina Field West Wall Hitspot (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D11,
        can_create=lambda options: options.hitsanity.value
    ),
    "Termina Field West Wall Hitspot (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D10,
        can_create=lambda options: options.hitsanity.value
    ),
    "Termina Field West Wall Hitspot (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D12,
        can_create=lambda options: options.hitsanity.value
    ),

    # Termina Field Above West Clock Town Entry Hitspot
    "Termina Field Above West Clock Town Entry Hitspot (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D02,
        can_create=lambda options: options.hitsanity.value
    ),
    "Termina Field Above West Clock Town Entry Hitspot (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D00,
        can_create=lambda options: options.hitsanity.value
    ),
    "Termina Field Above West Clock Town Entry Hitspot (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D01,
        can_create=lambda options: options.hitsanity.value
    ),

    # Stock Pot Inn Mask Hitspot
    "Stock Pot Inn Mask Hitspot (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156102,
        can_create=lambda options: options.hitsanity.value
    ),
    "Stock Pot Inn Mask Hitspot (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156101,
        can_create=lambda options: options.hitsanity.value
    ),
    "Stock Pot Inn Mask Hitspot (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420156100,
        can_create=lambda options: options.hitsanity.value
    ),

    # Skull Kid Drawing Hitspot
    "Skull Kid Drawing Hitspot (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D22,
        can_create=lambda options: options.hitsanity.value
    ),
    "Skull Kid Drawing Hitspot (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D21,
        can_create=lambda options: options.hitsanity.value
    ),
    "Skull Kid Drawing Hitspot (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420152D20,
        can_create=lambda options: options.hitsanity.value
    ),

    # Romani Ranch Baby Cuccoos Hitspots
    "Romani Ranch Baby Cuccoos Hitspots (0)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420154202,
        can_create=lambda options: options.hitsanity.value
    ),
    "Romani Ranch Baby Cuccoos Hitspots (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420154201,
        can_create=lambda options: options.hitsanity.value
    ),
    "Romani Ranch Baby Cuccoos Hitspots (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420154211,
        can_create=lambda options: options.hitsanity.value
    ),
    "Romani Ranch Baby Cuccoos Hitspots (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420154212,
        can_create=lambda options: options.hitsanity.value
    ),
    "Romani Ranch Baby Cuccoos Hitspots (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420154210,
        can_create=lambda options: options.hitsanity.value
    ),
    "Romani Ranch Baby Cuccoos Hitspots (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420154200,
        can_create=lambda options: options.hitsanity.value
    ),

    # Swamp Spiderhouse Totem Eye Hitspots
    "Swamp Spiderhouse Totem Eye Hitspots (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152810,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152811,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152812,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152820,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152821,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152822,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (6)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152830,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (7)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152831,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (8)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152832,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (9)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152800,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (10)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152801,
        can_create=lambda options: options.hitsanity.value
    ),
    "Swamp Spiderhouse Totem Eye Hitspots (11)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420152802,
        can_create=lambda options: options.hitsanity.value
    ),

    # Ocean Spiderhouse Mask Hitspots
    "Ocean Spiderhouse Mask Hitspots (0)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152900,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152901,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152902,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152910,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152911,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (5)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152912,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (6)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152920,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (7)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152921,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ocean Spiderhouse Mask Hitspots (8)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420152922,
        can_create=lambda options: options.hitsanity.value
    ),

    # Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots
    "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (0)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420151410,
        can_create=lambda options: options.hitsanity.value
    ),
    "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420151402,
        can_create=lambda options: options.hitsanity.value
    ),
    "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420151412,
        can_create=lambda options: options.hitsanity.value
    ),
    "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (3)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420151411,
        can_create=lambda options: options.hitsanity.value
    ),
    "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (4)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420151400,
        can_create=lambda options: options.hitsanity.value
    ),
    "Pirates Fortress Interior Outdoor Pirate Flag Eye Hitspots (5)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420151401,
        can_create=lambda options: options.hitsanity.value
    ),

    # Pirates Fortress Interior Indoor Pirate Flag Eye Hitspot
    "Pirates Fortress Interior Indoor Pirate Flag Eye Hitspot (0)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420152600,
        can_create=lambda options: options.hitsanity.value
    ),
    "Pirates Fortress Interior Indoor Pirate Flag Eye Hitspot (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420152601,
        can_create=lambda options: options.hitsanity.value
    ),
    "Pirates Fortress Interior Indoor Pirate Flag Eye Hitspot (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420152602,
        can_create=lambda options: options.hitsanity.value
    ),

    # Ikana Graveyard Lantern Hitspots - 
    "Ikana Graveyard Lantern Hitspots (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154310,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154311,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154312,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154321,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154320,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154322,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154300,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (7)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154301,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (8)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154302,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (9)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154400,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (10)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154401,
        can_create=lambda options: options.hitsanity.value
    ),
    "Ikana Graveyard Lantern Hitspots (11)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420154402,
        can_create=lambda options: options.hitsanity.value
    ),            

    # Invisible Rupees

    # Termina Field Invisible Rupee Over Ramp Near Fountains
    "Termina Field Invisible Rupee Over Ramp Near Fountains": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D09,
        can_create=lambda options: options.invisisanity.value
    ),

    # Termina Field Fountain Rupees
    "Termina Field Fountain Rupees (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D06,
        can_create=lambda options: options.invisisanity.value
    ),
    "Termina Field Fountain Rupees (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D07,
        can_create=lambda options: options.invisisanity.value
    ),

    # Termina Field Invisible Rupee Over Water
    "Termina Field Invisible Rupee Over Water": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D0A,
        can_create=lambda options: options.invisisanity.value
    ),

    # Termina Field Invisible Rupee Over Stump
    "Termina Field Invisible Rupee Over Stump": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D05,
        can_create=lambda options: options.invisisanity.value
    ),

    # Termina Field Invisible Rupees In Long Grass
    # Duplicate removed
    "Termina Field Invisible Rupees In Long Grass (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D00,
        can_create=lambda options: options.invisisanity.value
    ),
    "Termina Field Invisible Rupees In Long Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D01,
        can_create=lambda options: options.invisisanity.value
    ),
    "Termina Field Invisible Rupees In Long Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D02,
        can_create=lambda options: options.invisisanity.value
    ),
    "Termina Field Invisible Rupees In Long Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D03,
        can_create=lambda options: options.invisisanity.value
    ),
    "Termina Field Invisible Rupees In Long Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D04,
        can_create=lambda options: options.invisisanity.value
    ),

    # Termina Field Invisible Rupee Over Northern Ramp
    "Termina Field Invisible Rupee Over Northern Ramp": MMRLocationData(
        region="Termina Field",
        address=0x3469420162D08,
        can_create=lambda options: options.invisisanity.value
    ),

    # Romani Ranch Invisible Fence Rupees
    "Romani Ranch Invisible Fence Rupees (0)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420163505,
        can_create=lambda options: options.invisisanity.value
    ),
    "Romani Ranch Invisible Fence Rupees (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420163504,
        can_create=lambda options: options.invisisanity.value
    ),
    "Romani Ranch Invisible Fence Rupees (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420163501,
        can_create=lambda options: options.invisisanity.value
    ),
    "Romani Ranch Invisible Fence Rupees (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420163500,
        can_create=lambda options: options.invisisanity.value
    ),
    "Romani Ranch Invisible Fence Rupees (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420163503,
        can_create=lambda options: options.invisisanity.value
    ),
    "Romani Ranch Invisible Fence Rupees (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420163502,
        can_create=lambda options: options.invisisanity.value
    ),

    # Swamp Spiderhouse Invisible Rupees Above Giant Jars
    "Swamp Spiderhouse Invisible Rupees Above Giant Jars (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420162744,
        can_create=lambda options: options.invisisanity.value
    ),
    "Swamp Spiderhouse Invisible Rupees Above Giant Jars (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420162743,
        can_create=lambda options: options.invisisanity.value
    ),
    "Swamp Spiderhouse Invisible Rupees Above Giant Jars (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420162742,
        can_create=lambda options: options.invisisanity.value
    ),
    "Swamp Spiderhouse Invisible Rupees Above Giant Jars (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420162741,
        can_create=lambda options: options.invisisanity.value
    ),
    "Swamp Spiderhouse Invisible Rupees Above Giant Jars (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420162740,
        can_create=lambda options: options.invisisanity.value
    ),

    # Freestanding Rupees

    # Songwall Rupees
    "Termina Field 6am Songwall (0)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0011,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 6am Songwall (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0022,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 6am Songwall (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0000,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 7am Songwall (0)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A00C0,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 7am Songwall (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A00D1,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 7am Songwall (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A00E2,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 8am Songwall (0)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0030,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 8am Songwall (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0041,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 8am Songwall (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0052,
        can_create=lambda options: options.rupeesanity.value
    ),
    # "Termina Field 9am Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A0052,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 9am Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A0052,
    #     can_create=lambda options: options.rupeesanity.value
    # ), 
    # "Termina Field 9am Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A0052,
    #     can_create=lambda options: options.rupeesanity.value
    # ),          
    "Termina Field 10am Songwall (0)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0060,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 10am Songwall (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0071,
        can_create=lambda options: options.rupeesanity.value
    ),  
    "Termina Field 10am Songwall (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0082,
        can_create=lambda options: options.rupeesanity.value
    ),
    # "Termina Field 11am Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A0052,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 11am Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A0052,
    #     can_create=lambda options: options.rupeesanity.value
    # ), 
    # "Termina Field 11am Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A0052,
    #     can_create=lambda options: options.rupeesanity.value
    # ),          
    # "Termina Field 12pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 1pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 1pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 1pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),        
    # "Termina Field 2pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 2pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 2pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 3pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 3pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 3pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 4pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 4pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 4pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 5pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 5pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 5pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ), 
    # "Termina Field 6pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 6pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 6pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 7pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 7pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 7pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A82,
    #     can_create=lambda options: options.rupeesanity.value
    # ), 
    "Termina Field 8pm Songwall (0)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A0090,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 8pm Songwall (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A00A1,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field 8pm Songwall (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694201A00B2,
        can_create=lambda options: options.rupeesanity.value
    ),
    # "Termina Field 9pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 9pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 9pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 10pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 10pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ), 
    # "Termina Field 10pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 11pm Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 11pm Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 11pm Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12am Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12am Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 12am Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 1am Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 1am Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 1am Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 2am Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 3am Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 3am Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 4am Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 4am Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 4am Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 5am Songwall (0)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201A90,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 5am Songwall (1)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AA1,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # "Termina Field 5am Songwall (2)": MMRLocationData(
    #     region="Clock Town",
    #     address=0x34694201AB2,
    #     can_create=lambda options: options.rupeesanity.value
    # ),
    # Laundry Pool Night 2 Rupees
    "Laundry Pool Night 2 Rupees (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420177000,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Laundry Pool Night 2 Rupees (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420177001,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Laundry Pool Night 2 Rupees (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420177002,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Termina Field Eastern Pillar Rupees
    "Termina Field Eastern Pillar Rupees": MMRLocationData(
        region="Termina Field",
        address=0x3469420172D00,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Termina Field Tree Rupees
    "Termina Field Tree Rupees (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420172DE1,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Tree Rupees (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420172DE2,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Observatory Secret Guay Rupee (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420172DC2,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Observatory Secret Guay Rupee (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420172DC3,
        can_create=lambda options: options.rupeesanity.value
    ),    
    # Termina Field Song Guay Rupees
    "Termina Field Song Guay Rupees (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF00,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF01,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF02,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF03,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF04,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF05,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF06,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF07,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF08,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF09,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF0A,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF0B,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF0C,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (13)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF0D,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (14)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF0E,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (15)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF0F,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (16)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF10,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (17)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF11,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (18)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF12,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Rupees (19)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF13,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Thieving Bird Rupee": MMRLocationData(
        region="Termina Field",
        address=0x3469420172DD3,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Termina Field Song Guay Goron/Epona Rupees
    "Termina Field Song Guay Goron/Epona Rupees (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF18,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Goron/Epona Rupees (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF1D,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Termina Field Song Guay Goron/Epona Rupees (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942017FF22,
        can_create=lambda options: options.rupeesanity.value
    ),


    # Deku PlayGround Day 1 Rupees
    "Deku PlayGround Day 1 Rupees (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E13,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 1 Rupees (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E10,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 1 Rupees (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E14,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 1 Rupees (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E12,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 1 Rupees (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E11,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 1 Rupees (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E15,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Deku PlayGround Day 2 Rupees
    "Deku PlayGround Day 2 Rupees (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E25,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 2 Rupees (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E21,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 2 Rupees (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E20,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 2 Rupees (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E23,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 2 Rupees (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E24,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 2 Rupees (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E22,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Deku PlayGround Day 3 Rupees
    "Deku PlayGround Day 3 Rupees (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E32,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 3 Rupees (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E31,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 3 Rupees (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E30,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 3 Rupees (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E33,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 3 Rupees (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E35,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku PlayGround Day 3 Rupees (5)": MMRLocationData(
        region="Clock Town",
        address=0x3469420171E34,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Southern Swamp Flower Rupees
    "Southern Swamp Flower Rupees (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420174500,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Southern Swamp Flower Rupees (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420174501,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Southern Swamp Witch Shop Rupee (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420170A00,
        can_create=lambda options: options.rupeesanity.value    
    ),

    # Deku Palace Right Side Rupees
    "Deku Palace Right Side Rupees (0)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172BF2,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172BF1,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (2)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172BF6,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (3)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172BF0,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (4)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172BF5,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (5)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172BF4,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (6)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172BF3,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (7)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B10,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (8)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B11,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (9)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B15,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (10)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B14,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (11)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B13,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Right Side Rupees (12)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B12,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Deku Palace Left Side Rupees
    "Deku Palace Left Side Rupees (0)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B24,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B25,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (2)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B26,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (3)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B21,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (4)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B20,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (5)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B22,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (6)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B2A,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (7)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B2B,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (8)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B27,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (9)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B28,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Palace Left Side Rupees (10)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420172B29,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Deku Butler Rupees
    "Deku Butler Rupees (0)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175225,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175224,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (2)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175221,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (3)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175220,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (4)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175222,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (5)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175223,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (6)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175227,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (7)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175226,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (8)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175230,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (9)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175231,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (10)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175232,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (11)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175233,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (12)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175234,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (13)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175235,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (14)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175240,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (15)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175241,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (16)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175242,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (17)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175244,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (18)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175245,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (19)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175243,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (20)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175289,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (21)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175288,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (22)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175287,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (23)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175286,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (24)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175285,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (25)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175282,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (26)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175281,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (27)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175280,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (28)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175283,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Deku Butler Rupees (29)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420175284,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Woodfall Stump Rupee
    "Woodfall Stump Rupee": MMRLocationData(
        region="Woodfall",
        address=0x3469420174600,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Romani Ranch Haystack Rupees
    "Romani Ranch Haystack Rupees (0)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420171001,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Romani Ranch Haystack Rupees (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420171000,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Woodfall Temple Pre Boss Rupees
    "Woodfall Temple Pre Boss Rupees (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420171B03,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Woodfall Temple Pre Boss Rupees (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420171B05,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Woodfall Temple Pre Boss Rupees (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420171B04,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Woodfall Temple Pre Boss Rupees (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420171B02,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Woodfall Temple Pre Boss Rupees (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420171B00,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Woodfall Temple Pre Boss Rupees (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420171B01,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Snowhead Temple Icicle Rupees
    "Snowhead Temple Icicle Rupees (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420172170,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Snowhead Temple Icicle Rupees (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420172172,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Snowhead Temple Icicle Rupees (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420172171,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Mountain Village Spring Boulder Under Smithy Rupee
    "Mountain Village Spring Boulder Under Smithy Rupee": MMRLocationData(
        region="Mountain Village",
        address=0x3469420175A00,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Twin Islands Spring Underwater Rupees
    "Twin Islands Spring Underwater Rupees (0)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420175E02,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Twin Islands Spring Underwater Rupees (1)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420175E03,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Twin Islands Spring Underwater Rupees (2)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420175E00,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Twin Islands Spring Underwater Rupees (3)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420175E01,
        can_create=lambda options: options.rupeesanity.value
    ),
    # Pirates' Fortress Sewers Rupees (Under Barrels)
    "Pirates' Fortress Sewers Rupees Under Barrel (0)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694201723B0,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates' Fortress Sewers Rupees Under Barrel (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694201723B1,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates' Fortress Sewers Rupees Under Barrel (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694201723B2,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates' Fortress Sewers Rupees Under Barrel (3)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694201723B3,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates' Fortress Sewers Rupees Under Barrel (4)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694201723B4,
        can_create=lambda options: options.rupeesanity.value
    ),    
    "Pirates Fortress' Sewers Exit Barrel Rupee (0)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420172390,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates Fortress' Sewers Exit Barrel Rupee (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420172391,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates Fortress' Sewers Exit Barrel Rupee (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420172392,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates Fortress' Interior Ledge Recovery Hearts (0)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420171400,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates Fortress' Interior Ledge Recovery Hearts (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420171401,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Pirates Fortress' Interior Ledge Recovery Hearts (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420171402,
        can_create=lambda options: options.rupeesanity.value
    ),           
    # Great Bay Temple Waterwheel Rupees
    "Great Bay Temple Waterwheel Rupees (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420174982,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Great Bay Temple Waterwheel Rupees (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420174984,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Great Bay Temple Waterwheel Rupees (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420174983,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Great Bay Temple Waterwheel Rupees (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420174980,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Great Bay Temple Waterwheel Rupees (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420174981,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Great Bay Temple Room Behind Waterfall Rupees (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694201749C1,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Great Bay Temple Room Behind Waterfall Rupees (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694201749C0,
        can_create=lambda options: options.rupeesanity.value
    ),
    # Great Bay Temple Before Gekko Room Underwater Rupees
    "Great Bay Temple Before Gekko Room Underwater Rupees (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420174941,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Great Bay Temple Before Gekko Room Underwater Rupees (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420174940,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Ikana Graveyard Day 2 Rupees
    "Ikana Graveyard Day 2 Rupees (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420170CF0,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Ikana Graveyard Day 2 Rupees (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420170CF5,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Ikana Graveyard Day 2 Rupees (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420170CF6,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Ikana Graveyard Day 2 Rupees (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420170CF1,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Ikana Graveyard Day 2 Rupees (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420170CF2,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Ikana Graveyard Day 2 Rupees (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420170CF3,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Ikana Graveyard Day 2 Rupees (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420170CF4,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Secret Shrine Rupees
    "Secret Shrine Rupees (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x346942017600A,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x346942017600B,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176004,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176002,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176009,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176000,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (6)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176001,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (7)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176010,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (8)": MMRLocationData(
        region="Secret Shrine",
        address=0x346942017600F,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (9)": MMRLocationData(
        region="Secret Shrine",
        address=0x346942017600E,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (10)": MMRLocationData(
        region="Secret Shrine",
        address=0x346942017600D,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (11)": MMRLocationData(
        region="Secret Shrine",
        address=0x346942017600C,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (12)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176008,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (13)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176007,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (14)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176006,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (15)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176005,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Secret Shrine Rupees (16)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420176003,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Stone Tower Bridge Room Rupees
    "Stone Tower Bridge Room Rupees (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171687,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Bridge Room Rupees (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171685,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Bridge Room Rupees (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171683,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Bridge Room Rupees (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171681,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Bridge Room Rupees (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171682,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Bridge Room Rupees (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171680,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Bridge Room Rupees (6)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171684,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Bridge Room Rupees (7)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171686,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Deku Updraft Rupees (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171690,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Deku Updraft Rupees (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171691,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Deku Updraft Rupees (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171692,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Deku Updraft Rupees (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171693,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Deku Updraft Rupees (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171694,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Deku Updraft Rupees (6)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171695,
        can_create=lambda options: options.rupeesanity.value
    ),                           
    # Stone Tower Eyegore Room Light Block Rupees
    "Stone Tower Eyegore Room Light Block Rupees (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171611,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Stone Tower Eyegore Room Light Block Rupees (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420171610,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Inverted Stone Tower Right Side Light Block Rupees
    "Inverted Stone Tower Right Side Light Block Rupees (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171832,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Right Side Light Block Rupees (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171831,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Inverted Stone Tower Dexihand Rupees
    "Inverted Stone Tower Dexihand Rupees (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171811,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Dexihand Rupees (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171810,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Dexihand Rupees (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171812,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Inverted Stone Tower Pre Boss Rupees
    "Inverted Stone Tower Pre Boss Rupees (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171881,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171880,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171882,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171886,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171883,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (5)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171889,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (6)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942017188A,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (7)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171888,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (8)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171887,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (9)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171885,
        can_create=lambda options: options.rupeesanity.value
    ),
    "Inverted Stone Tower Pre Boss Rupees (10)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420171884,
        can_create=lambda options: options.rupeesanity.value
    ),

    # Rocksanity

    # Termina Field 
    "Termina Field Boulder Over Gossip Grotto (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201B2D00,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Boulder Over Bio Baba Grotto (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201B2D01,
        can_create=lambda options: options.rocksanity.value
    ),        
    "Termina Field Kamaro Rock Circle (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D00,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Kamaro Rock Circle (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D01,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Kamaro Rock Circle (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D02,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Kamaro Rock Circle (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D03,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Kamaro Rock Circle (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D04,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Kamaro Rock Circle (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D05,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Kamaro Rock Circle (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D06,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field Kamaro Rock Circle (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420262D07,
        can_create=lambda options: options.rocksanity.value
    ),

    # Termina Field North West Rock Wall
    "Termina Field North West Rock Wall (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D07,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field North West Rock Wall (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D03,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field North West Rock Wall (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D01,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field North West Rock Wall (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D04,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field North West Rock Wall (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D0C,
        can_create=lambda options: options.rocksanity.value
    ),

    # Termina Field Rock Behind Coast Wall
    "Termina Field Rock Behind Coast Wall": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D00,
        can_create=lambda options: options.rocksanity.value
    ),
    # Termina Field Bio Baba Rock
    "Termina Field Bio Baba Rock": MMRLocationData(
        region="Termina Field",
        address=0x34694201807B0,
        can_create=lambda options: options.rocksanity.value
    ),    
    # South West Rock Wall
    "Termina Field South West Rock Wall (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D0B,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field South West Rock Wall (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D05,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field South West Rock Wall (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D06,
        can_create=lambda options: options.rocksanity.value
    ),
    "Termina Field South West Rock Wall (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420182D02,
        can_create=lambda options: options.rocksanity.value
    ),
    "Deku Palace Guarded Boulder (1)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201B2B10,
        can_create=lambda options: options.rocksanity.value
    ),
    "Deku Palace Guarded Boulder (2)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201B2B11,
        can_create=lambda options: options.rocksanity.value
    ),
    "Deku Palace Guarded Boulder (3)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201B2B12,
        can_create=lambda options: options.rocksanity.value
    ),
    # Swamp Spider Entry Rocks
    "Swamp Spider Entry Rocks (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420182701,
        can_create=lambda options: options.rocksanity.value
    ),
    "Swamp Spider Entry Rocks (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420182700,
        can_create=lambda options: options.rocksanity.value
    ),
    "Swamp Spider Monument Room Boulder": MMRLocationData(
        region="Swamp Spider House",
        address=0x34694201B2730,
        can_create=lambda options: options.rocksanity.value
    ),    

    # Swamp Spider Large Pots Rock
    "Swamp Spider Large Pots Rock": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420182740,
        can_create=lambda options: options.rocksanity.value
    ),
    # Twin islands 
    "Twin Isles Hot Spring Water Grotto Bomb Boulders (0)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201B07E0,
        can_create=lambda options: options.rocksanity.value
    ),
    "Twin Isles Hot Spring Water Grotto Bomb Boulders (1)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201B07E1,
        can_create=lambda options: options.rocksanity.value
    ),
    "Twin Isles Hot Spring Water Grotto Bomb Boulders (2)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201B07E2,
        can_create=lambda options: options.rocksanity.value
    ),
    "Twin Isles Hot Spring Water Grotto Bomb Boulders (3)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201B07E3,
        can_create=lambda options: options.rocksanity.value
    ),
    "Twin Isles Hot Spring Water Grotto Bomb Boulders (4)": MMRLocationData(
        region="Twin Islands",
        address=0x34694201B07E4,
        can_create=lambda options: options.rocksanity.value
    ),                
    # Goron Shrine Rocks
    "Goron Shrine Rocks (0)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183202,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183201,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (2)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183203,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (3)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183200,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (4)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183206,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (5)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183207,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (6)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183205,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (7)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183204,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (8)": MMRLocationData(
        region="Goron Village",
        address=0x346942018320D,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (9)": MMRLocationData(
        region="Goron Village",
        address=0x346942018320C,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (10)": MMRLocationData(
        region="Goron Village",
        address=0x346942018320E,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (11)": MMRLocationData(
        region="Goron Village",
        address=0x346942018320F,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (12)": MMRLocationData(
        region="Goron Village",
        address=0x346942018320A,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (13)": MMRLocationData(
        region="Goron Village",
        address=0x346942018320B,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (14)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183208,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Shrine Rocks (15)": MMRLocationData(
        region="Goron Village",
        address=0x3469420183209,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Village Lens Cave Bomb Boulder (1)": MMRLocationData(
        region="Goron Village",
        address=0x34694201B0750,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Village Lens Cave Bomb Boulder (2)": MMRLocationData(
        region="Goron Village",
        address=0x34694201B0751,
        can_create=lambda options: options.rocksanity.value
    ),
    "Goron Village Lens Cave Bomb Boulder (3)": MMRLocationData(
        region="Goron Village",
        address=0x34694201B0752,
        can_create=lambda options: options.rocksanity.value
    ),              

    # Mountain Village Spring Rocks
    "Mountain Village Boulders Under Stairs (0)": MMRLocationData(
        region="Mountain Village",
        address=0x34694201B5A00,
        can_create=lambda options: options.rocksanity.value
    ),
    "Mountain Village Boulders Under Stairs (1)": MMRLocationData(
        region="Mountain Village",
        address=0x34694201B5A01,
        can_create=lambda options: options.rocksanity.value
    ),  
    "Mountain Village Boulders Under Stairs (2)": MMRLocationData(
        region="Mountain Village",
        address=0x34694201B5A02,
        can_create=lambda options: options.rocksanity.value
    ),              
    "Mountain Village Spring Rock Triangle (0)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420185A02,
        can_create=lambda options: options.rocksanity.value
    ),
    "Mountain Village Spring Rock Triangle (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420185A03,
        can_create=lambda options: options.rocksanity.value
    ),
    "Mountain Village Spring Rock Triangle (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420185A04,
        can_create=lambda options: options.rocksanity.value
    ),
    "Mountain Village Spring Rock Triangle (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420185A05,
        can_create=lambda options: options.rocksanity.value
    ),
    "Mountain Village Spring Rock Triangle (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420185A06,
        can_create=lambda options: options.rocksanity.value
    ),

     # Mountain Village Spring Outside Goron Graveyard
    "Mountain Village Spring Outside Goron Graveyard Rocks (0)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420185A00,
        can_create=lambda options: options.rocksanity.value
    ),
    "Mountain Village Spring Outside Goron Graveyard Rocks (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420185A01,
        can_create=lambda options: options.rocksanity.value
    ),

    # Twin Isles Spring Above Grotto Rocks
    "Twin Isles Spring Above Grotto Rocks (0)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420185E00,
        can_create=lambda options: options.rocksanity.value
    ),
    "Twin Isles Spring Above Grotto Rocks (1)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420185E01,
        can_create=lambda options: options.rocksanity.value
    ),
    "Twin Isles Spring Above Grotto Rocks (2)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420185E02,
        can_create=lambda options: options.rocksanity.value
    ),


    # Great Bay Coast Scattered Beach Rocks
    "Great Bay Coast Scattered Beach Rocks (0)": MMRLocationData(
        region="Great Bay",
        address=0x3469420183727,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Scattered Beach Rocks (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420183728,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Scattered Beach Rocks (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420183729,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Scattered Beach Rocks (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420183726,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Scattered Beach Rocks (4)": MMRLocationData(
        region="Great Bay",
        address=0x346942018372A,
        can_create=lambda options: options.rocksanity.value
    ),

    # Great Bay Coast Rock Wall Rocks
    "Great Bay Coast Rock Wall Rocks (1)": MMRLocationData(
        region="Great Bay",
        address=0x346942018372D,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Rock Wall Rocks (2)": MMRLocationData(
        region="Great Bay",
        address=0x346942018372B,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Rock Wall Rocks (3)": MMRLocationData(
        region="Great Bay",
        address=0x346942018372C,
        can_create=lambda options: options.rocksanity.value
    ),
    # Great Bay Coast Underwater Rocks (Bombchus only)
    "Great Bay Coast Underwater Rocks (Bombchus only) Below Rock Pools (1)": MMRLocationData(
        region="Great Bay",
        address=0x346942018371C,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Underwater Rocks (Bombchus only) Next to Like-Like": MMRLocationData(
        region="Great Bay",
        address=0x346942018372E,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Underwater Rocks (Bombchus only) Below Rock Pools (2)": MMRLocationData(
        region="Great Bay",
        address=0x346942018371B,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Underwater Rocks (Bombchus only) Near Rock Wall": MMRLocationData(
        region="Great Bay",
        address=0x346942018371A,
        can_create=lambda options: options.rocksanity.value
    ),    
    # Rocks Underwater Easy to get
    "Great Bay Coast Beach Rocks Underwater (1)": MMRLocationData(
        region="Great Bay",
        address=0x346942018370A,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Beach Rocks Underwater (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420183724,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Beach Rocks Underwater (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420183723,
        can_create=lambda options: options.rocksanity.value
    ),
    "Great Bay Coast Beach Rocks Underwater (4)": MMRLocationData(
        region="Great Bay",
        address=0x346942018370B,
        can_create=lambda options: options.rocksanity.value
    ),

    # Zora Cape Beach Rocks
    "Zora Cape Beach Rocks (0)": MMRLocationData(
        region="Zora Cape",
        address=0x346942018380B,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (1)": MMRLocationData(
        region="Zora Cape",
        address=0x346942018380A,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (2)": MMRLocationData(
        region="Zora Cape",
        address=0x346942018380C,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (3)": MMRLocationData(
        region="Zora Cape",
        address=0x346942018380D,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (4)": MMRLocationData(
        region="Zora Cape",
        address=0x346942018380E,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (5)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183806,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (6)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183807,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (7)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183805,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (8)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183808,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Beach Rocks (9)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183809,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Boulder Over Grotto (0)": MMRLocationData(
        region="Zora Cape",
        address=0x34694201B3802,
        can_create=lambda options: options.rocksanity.value
    ),    

    # Zora Cape Island Rocks (Req Hook)
    "Zora Cape Island Rocks (0)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183801,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Island Rocks (1)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183803,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Island Rocks (2)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183802,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Island Rocks (3)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183804,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Island Rocks (4)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420183800,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Great Fairy Boulders (0)": MMRLocationData(
        region="Zora Cape",
        address=0x34694201B3800,
        can_create=lambda options: options.rocksanity.value
    ),
    "Zora Cape Great Fairy Boulders (1)": MMRLocationData(
        region="Zora Cape",
        address=0x34694201B3801,
        can_create=lambda options: options.rocksanity.value
    ),          

    # Road To Ikana Rocks
    "Road To Ikana Grotto Boulder": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5300,
        can_create=lambda options: options.rocksanity.value
    ),          
    "Road To Ikana Rock Circle (1)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265300,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Rock Circle (2)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265301,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Rock Circle (3)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265302,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Rock Circle (4)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265303,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Rock Circle (5)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265304,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Rock Circle (6)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265305,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Rock Circle (7)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265306,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Rock Circle (8)": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420265307,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Bomb Boulder (1)": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5301,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Bomb Boulder (2)": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5302,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Bomb Boulder (3)": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5303,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Bomb Boulder (4)": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5304,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Bomb Boulder (5)": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5305,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Bomb Boulder (6)": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5306,
        can_create=lambda options: options.rocksanity.value
    ),
    "Road To Ikana Bomb Boulder (7)": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201B5307,
        can_create=lambda options: options.rocksanity.value
    ),                        

    # Ikana Graveyard Rock Circle
    "Ikana Graveyard Rock Circle (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264310,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Rock Circle (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264311,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Rock Circle (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264312,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Rock Circle (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264313,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Rock Circle (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264314,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Rock Circle (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264315,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Rock Circle (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264316,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Rock Circle (7)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420264317,
        can_create=lambda options: options.rocksanity.value
    ),

    # Ikana Graveyard Captain Rockwall 
    "Ikana Graveyard Captain Rockwall (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420184310,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Captain Rockwall (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420184311,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Captain Rockwall (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420184312,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Captain Rockwall (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420184313,
        can_create=lambda options: options.rocksanity.value
    ),
    "Ikana Graveyard Captain Rockwall (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420184314,
        can_create=lambda options: options.rocksanity.value
    ),

    # Inverted Stone Lower Tower Rocks
    "Inverted Stone Tower Rocks (1)": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x3469420185900,
        can_create=lambda options: options.rocksanity.value
    ),
    "Inverted Stone Tower Rocks (2)": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x3469420185901,
        can_create=lambda options: options.rocksanity.value
    ),

    # Soil

    # Termina Field Stump Soil
    "Termina Field Stump Soil": MMRLocationData(
        region="Termina Field",
        address=0x3469420192DE3,
        can_create=lambda options: options.soilsanity.value
    ),

    # Termina Field Wall Soil
    "Termina Field Wall Soil (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420192D42,
        can_create=lambda options: options.soilsanity.value
    ),
    "Termina Field Wall Soil (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420192D40,
        can_create=lambda options: options.soilsanity.value
    ),
    "Termina Field Wall Soil (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420192D41,
        can_create=lambda options: options.soilsanity.value
    ),

    # Termina Field Eastern Soil
    "Termina Field Eastern Soil": MMRLocationData(
        region="Termina Field",
        address=0x3469420192DB3,
        can_create=lambda options: options.soilsanity.value
    ),

    # Termina Field Observatory Soil
    "Termina Field Observatory Soil (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420192D50,
        can_create=lambda options: options.soilsanity.value
    ),
    "Termina Field Observatory Soil (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420192D51,
        can_create=lambda options: options.soilsanity.value
    ),
    "Termina Field Observatory Soil (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420192D52,
        can_create=lambda options: options.soilsanity.value
    ),

    # Swamp Spider House Rock Soil
    "Swamp Spider House Rock Soil (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420192760,
        can_create=lambda options: options.soilsanity.value
    ),
    "Swamp Spider House Rock Soil (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420192762,
        can_create=lambda options: options.soilsanity.value
    ),
    "Swamp Spider House Rock Soil (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420192761,
        can_create=lambda options: options.soilsanity.value
    ),

    # Swamp Spider House Gold Room Soil
    "Swamp Spider House Gold Room Soil": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420192723,
        can_create=lambda options: options.soilsanity.value
    ),

    # Deku Palace Bean Seller Soil
    "Deku Palace Bean Seller Soil (0)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201907D0,
        can_create=lambda options: options.soilsanity.value
    ),
    "Deku Palace Bean Seller Soil (1)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201907D1,
        can_create=lambda options: options.soilsanity.value
    ),
    "Deku Palace Bean Seller Soil (2)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201907D2,
        can_create=lambda options: options.soilsanity.value
    ),

    # Deku Palace Exterior Soil
    "Deku Palace Exterior Soil (0)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420192B30,
        can_create=lambda options: options.soilsanity.value
    ),
    "Deku Palace Exterior Soil (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420192B32,
        can_create=lambda options: options.soilsanity.value
    ),
    "Deku Palace Exterior Soil (2)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420192B31,
        can_create=lambda options: options.soilsanity.value
    ),

    # Romani Ranch Day 1 Soil
    "Romani Ranch Day 1 Soil": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420193543,
        can_create=lambda options: options.soilsanity.value
    ),

    # Romani Ranch Day 2/3 Soil
    "Romani Ranch Day 2/3 Soil (0)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420193540,
        can_create=lambda options: options.soilsanity.value
    ),
    "Romani Ranch Day 2/3 Soil (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420193542,
        can_create=lambda options: options.soilsanity.value
    ),
    "Romani Ranch Day 2/3 Soil (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420193541,
        can_create=lambda options: options.soilsanity.value
    ),

    # Romani Ranch Doggy Racetrack Soil
    "Romani Ranch Doggy Racetrack Soil": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420194103,
        can_create=lambda options: options.soilsanity.value
    ),

    # Great Bay Coast Soil
    "Great Bay Coast Soil": MMRLocationData(
        region="Great Bay",
        address=0x3469420193793,
        can_create=lambda options: options.soilsanity.value
    ),

    # Secret Shrine Soil
    "Secret Shrine Soil (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420196000,
        can_create=lambda options: options.soilsanity.value
    ),
    "Secret Shrine Soil (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420196001,
        can_create=lambda options: options.soilsanity.value
    ),
    "Secret Shrine Soil (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420196002,
        can_create=lambda options: options.soilsanity.value
    ),

    # Stone Tower Inverted Soils
    "Stone Tower Inverted Soils (0)": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x3469420195903,
        can_create=lambda options: options.soilsanity.value
    ),
    "Stone Tower Inverted Soils (1)": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x3469420195933,
        can_create=lambda options: options.soilsanity.value
    ),

    # Snowballs

    # Path to Mountains Snowballs
    "Path to Mountains Snowballs (1)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C00,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (2)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C0C,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (3)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C07,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (4)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C01,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (5)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C09,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (6)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C02,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (7)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C08,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (8)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C04,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (9)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C05,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (10)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C06,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (11)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C03,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (12)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C0A,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (13)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C0E,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (14)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C0B,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Mountains Snowballs (15)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420211C0D,
        can_create=lambda options: options.snowsanity.value
    ),

    # Mountain Village Day 1 Snowballs
    "Mountain Village Day 1 Snowballs (0)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215000,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215001,
        can_create=lambda options: options.snowsanity.value
    ),    
    "Mountain Village Day 1 Snowballs (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215002,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215003,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215004,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (5)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215005,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (6)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215006,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (7)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215007,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (8)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215008,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (9)": MMRLocationData(
        region="Mountain Village",
        address=0x346942021500B,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (10)": MMRLocationData(
        region="Mountain Village",
        address=0x346942021500C,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (11)": MMRLocationData(
        region="Mountain Village",
        address=0x346942021500D,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (12)": MMRLocationData(
        region="Mountain Village",
        address=0x346942021500E,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Day 1 Snowballs (13)": MMRLocationData(
        region="Mountain Village",
        address=0x346942021500F,
        can_create=lambda options: options.snowsanity.value
    ),

    # Snowballs Outside Goron Graveyard
    "Snowballs Outside Goron Graveyard (0)": MMRLocationData(
        region="Mountain Village",
        address=0x346942021500A,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowballs Outside Goron Graveyard (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215009,
        can_create=lambda options: options.snowsanity.value
    ),

    # Twin Islands Day 1 Snowballs
    "Twin Islands Day 1 Snowballs (0)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D0D,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (1)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D0E,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (2)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D05,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (3)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D04,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (4)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D07,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (5)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D01,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (6)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D0B,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (7)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D06,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (8)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D08,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (9)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D09,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (10)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D02,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (11)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D0C,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (12)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D03,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (13)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D0A,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (14)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D0F,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Islands Day 1 Snowballs (15)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D00,
        can_create=lambda options: options.snowsanity.value
    ),

    # Twin Isles Snowballs Near Grotto
    "Twin Isles Snowballs Near Grotto (1)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D11,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Isles Snowballs Near Grotto (2)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D12,
        can_create=lambda options: options.snowsanity.value
    ),
    "Twin Isles Snowballs Near Grotto (3)": MMRLocationData(
        region="Twin Islands",
        address=0x3469420215D10,
        can_create=lambda options: options.snowsanity.value
    ),

    # Goron Village Snowballs
    "Goron Village Snowballs (0)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D00,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D0B,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (2)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D14,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (3)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D0D,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (4)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D10,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (5)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D0E,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (6)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D13,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (7)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D11,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (8)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D0C,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (9)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D03,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (10)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D0F,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (11)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D05,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (12)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D12,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (13)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D07,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (14)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D09,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (15)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D02,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (16)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D04,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (17)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D06,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (18)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D08,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (19)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D0A,
        can_create=lambda options: options.snowsanity.value
    ),
    "Goron Village Snowballs (20)": MMRLocationData(
        region="Goron Village",
        address=0x3469420214D01,
        can_create=lambda options: options.snowsanity.value
    ),


    # Path to Snowhead Snowballs
    "Path to Snowhead Snowballs (0)": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420215B06,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Snowhead Snowballs (1)": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420215B05,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Snowhead Snowballs (2)": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420215B04,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Snowhead Snowballs (3)": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420215B00,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Snowhead Snowballs (4)": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420215B01,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Snowhead Snowballs (5)": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420215B02,
        can_create=lambda options: options.snowsanity.value
    ),
    "Path to Snowhead Snowballs (6)": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420215B03,
        can_create=lambda options: options.snowsanity.value
    ),

    # Outside Snowhead Temple Snowballs
    "Outside Snowhead Temple Snowballs (0)": MMRLocationData(
        region="Snowhead",
        address=0x3469420215C01,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (1)": MMRLocationData(
        region="Snowhead",
        address=0x3469420215C03,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (2)": MMRLocationData(
        region="Snowhead",
        address=0x3469420215C00,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (3)": MMRLocationData(
        region="Snowhead",
        address=0x3469420215C02,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420215C04,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420215C06,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420215C07,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420215C08,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (8)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420215C09,
        can_create=lambda options: options.snowsanity.value
    ),
    "Outside Snowhead Temple Snowballs (9)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420215C05,
        can_create=lambda options: options.snowsanity.value
    ),

    # Snowhead Temple Lower Runway Room Snowballs
    "Snowhead Temple Lower Runway Room Snowballs (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212121,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Lower Runway Room Snowballs (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212120,
        can_create=lambda options: options.snowsanity.value
    ),    
    "Snowhead Temple Icicle Room Snowballs (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212172,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Icicle Room Snowballs (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212171,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Icicle Room Snowballs (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212175,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Icicle Room Snowballs (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212170,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Icicle Room Snowballs (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212174,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Icicle Room Snowballs (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212173,
        can_create=lambda options: options.snowsanity.value
    ),

    # Snowhead Temple Main Room 2nd Floor Snowballs
    "Snowhead Temple Main Room 2nd Floor Snowballs (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212145,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Main Room 2nd Floor Snowballs (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212141,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Main Room 2nd Floor Snowballs (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212140,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Main Room 2nd Floor Snowballs (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212142,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Main Room 2nd Floor Snowballs (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212143,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple Main Room 2nd Floor Snowballs (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212144,
        can_create=lambda options: options.snowsanity.value
    ),

    # Snowhead Temple 3rd Floor Bridge Snowballs
    "Snowhead Temple 3rd Floor Bridge Snowballs (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212147,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Bridge Snowballs (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212146,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Bridge Snowballs (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212148,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Bridge Snowballs (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420212149,
        can_create=lambda options: options.snowsanity.value
    ),

    # Snowhead Temple 3rd Floor Behind Locked Door Snowballs
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A0,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A3,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A2,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A4,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A1,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A7,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A5,
        can_create=lambda options: options.snowsanity.value
    ),
    "Snowhead Temple 3rd Floor Behind Locked Door Snowballs (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202121A6,
        can_create=lambda options: options.snowsanity.value
    ),

    # Mountain Village Spring Snowballs
    "Mountain Village Spring Snowballs (0)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215A03,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Spring Snowballs (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215A02,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Spring Snowballs (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215A01,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Spring Snowballs (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215A04,
        can_create=lambda options: options.snowsanity.value
    ),
    "Mountain Village Spring Snowballs (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420215A00,
        can_create=lambda options: options.snowsanity.value
    ),
    
    # Crates/ Barrels Woodsanity
    "Laundry Pool Crate (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420257000,
        can_create=lambda options: options.woodsanity.value
    ),    
    "East Clock Town Crates (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420256C00,
        can_create=lambda options: options.woodsanity.value
    ),
    "East Clock Town Crates (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420256C01,
        can_create=lambda options: options.woodsanity.value
    ),
    "Termina Field Business Scrub Grotto Crate (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420270790,
        can_create=lambda options: options.woodsanity.value
    ),
    "Gorman Racetrack Behind Fence Crate": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x3469420276A00,
        can_create=lambda options: options.woodsanity.value
    ),
    # Romani Ranch Crates
    "Romani Ranch Crate Next To Romani (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420273500,
        can_create=lambda options: options.woodsanity.value
    ), 
    "Romani Ranch Baby Cuccoo Crates (0)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420274200,
        can_create=lambda options: options.woodsanity.value
    ),
    "Romani Ranch Baby Cuccoo Crates (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420274201,
        can_create=lambda options: options.woodsanity.value
    ),
    "Romani Ranch Baby Cuccoo Crates (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420274202,
        can_create=lambda options: options.woodsanity.value
    ),
    # Swamp Spider House 
    "Swamp Spider House Monument Room Crates (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272730,
        can_create=lambda options: options.woodsanity.value
    ),
    "Swamp Spider House Monument Room Crates (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272731,
        can_create=lambda options: options.woodsanity.value
    ),                  
    "Swamp Spider House Monument Room Crates (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272732,
        can_create=lambda options: options.woodsanity.value
    ),                  
    "Swamp Spider House Monument Room Crates (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272733,
        can_create=lambda options: options.woodsanity.value
    ),                  
    "Swamp Spider House Monument Room Crates (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272734,
        can_create=lambda options: options.woodsanity.value
    ),                  
    "Swamp Spider House Monument Room Crates (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272735,
        can_create=lambda options: options.woodsanity.value
    ),                          
    "Swamp Spider House Gold Room Crates (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272720,
        can_create=lambda options: options.woodsanity.value
    ),
    "Swamp Spider House Gold Room Crates (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420272721,
        can_create=lambda options: options.woodsanity.value
    ),

    # Goron Village Keg Goron Crate
    "Goron Village Keg Goron Crate (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420274D10,
        can_create=lambda options: options.woodsanity.value
    ),
    "Goron Village Keg Goron Crate (Spring) (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420274810,
        can_create=lambda options: options.woodsanity.value
    ),
    "Ocean Spiderhouse Basement Crate (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420272850,
        can_create=lambda options: options.woodsanity.value
    ),
    # Pirates Fortress Entrance Wood Barrier
    "Pirates Fortress Entrance Bonk Board (0)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420223700,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates Fortress Entrance Bonk Board (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420223701,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates Fortress Entrance Bonk Board (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420223702,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates Fortress Entrance Bonk Board (3)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420223703,
        can_create=lambda options: options.woodsanity.value
    ),
    # Pirates Fortress Sewers Wooden Barriers
    "Pirates Fortress Sewers Bonk Board (0)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223C0,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates Fortress Sewers Bonk Board (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223C1,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates Fortress Sewers Bonk Board (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223C2,
        can_create=lambda options: options.woodsanity.value
    ),                      
    # Pirates' Fortress Sewers Barrels/Crates
    "Pirates' Fortress Sewers Barrel (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B0,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (2)": MMRLocationData(
        region="Pirates' Fortress Sewers", 
        address=0x34694202223B1,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (3)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B2,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (4)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B3,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (5)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B4,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (6)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B5,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (7)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B6,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (8)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B7,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (9)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B8,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (10)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223B9,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (11)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223BA,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (12)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223BB,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (13)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223BC,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (14)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223BD,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (15)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223BE,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Barrel (16)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x34694202223BF,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Exit Barrel (1)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420222390,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Exit Barrel (2)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420222391,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Exit Barrel (3)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420222392,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Exit Barrel (4)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420222393,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates' Fortress Sewers Exit Barrel (5)": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420222394,
        can_create=lambda options: options.woodsanity.value
    ),                                                                
    # Pirates Fortress Interior Crates
    "Pirates Fortress' Interior Crates (0)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420271400,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates Fortress' Interior Crates (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420271401,
        can_create=lambda options: options.woodsanity.value
    ),
    "Pirates Fortress' Interior Crates (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420271402,
        can_create=lambda options: options.woodsanity.value
    ), 
    "Pirates Fortress' Exterior Balcony Barrel (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420223B00,
        can_create=lambda options: options.woodsanity.value
    ),         
    "Pirates' Fortress Leader's Room Barrel (1)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420222330,
        can_create=lambda options: options.woodsanity.value        
    ),
    "Pirates' Fortress Leader's Room Barrel (2)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420222331,
        can_create=lambda options: options.woodsanity.value        
    ),
    "Pirates' Fortress Guarded Bridge Barrel (0)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x3469420221400,
        can_create=lambda options: options.woodsanity.value        
    ),
    "Pirates Fortress Interior Room Past Pink Guard Barrel (0)": MMRLocationData(
        region="Pirates' Fortress (Interior)",
        address=0x34694202223D0,
        can_create=lambda options: options.woodsanity.value        
    ),           
    #Dungeon Woodsanity
    #Snowhead Temple
    
    "Snowhead Temple Lava Bridge Room Crate (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272120,
        can_create=lambda options: options.woodsanity.value
    ),    
    "Snowhead Temple Elevator Room Crates (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272190,
        can_create=lambda options: options.woodsanity.value
    ),
    "Snowhead Temple Elevator Room Crates (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272191,
        can_create=lambda options: options.woodsanity.value
    ),
    "Snowhead Temple Elevator Room Crates (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272192,
        can_create=lambda options: options.woodsanity.value
    ),
    "Snowhead Temple Elevator Room Crates (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272193,
        can_create=lambda options: options.woodsanity.value
    ),
    "Snowhead Temple Elevator Room Crates (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272194,
        can_create=lambda options: options.woodsanity.value
    ),
    "Snowhead Temple Timed Switch Puzzle Room Crate (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272180,
        can_create=lambda options: options.woodsanity.value
    ),
    "Snowhead Temple Timed Switch Puzzle Room Crate (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420272181,
        can_create=lambda options: options.woodsanity.value
    ),        
    # Great Bay Temple Crates/Barrels
    "Great Bay Temple Entrance Barrels (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D0,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Entrance Barrels (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D1,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Entrance Barrels (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D2,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Entrance Barrels (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D3,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Entrance Barrels (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D4,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Entrance Barrels (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D5,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Entrance Barrels (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D6,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Entrance Barrels (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249D7,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall Barrels (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249C0,
        can_create=lambda options: options.woodsanity.value
    ),

    "Great Bay Temple Room Behind 1F Waterfall Barrels (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249C1,
        can_create=lambda options: options.woodsanity.value
    ),

    "Great Bay Temple Room Behind 1F Waterfall Barrels (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202249C2,
        can_create=lambda options: options.woodsanity.value
    ),    
    "Great Bay Temple 1F Red Valve Room Barrels (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420224920,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Barrels (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420224921,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Barrels (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420224922,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Barrels (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420224923,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Barrels (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420224924,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Crates (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420274920,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Crates (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420274921,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Crates (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420274922,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Crates (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420274923,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Red Valve Room Crates (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420274924,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254950,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254951,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254952,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254953,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254954,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254955,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254956,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254957,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254958,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (9)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420254959,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (10)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942025495A,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (11)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942025495B,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (12)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942025495C,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (13)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942025495D,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (14)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942025495E,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple 1F Frog Miniboss Crates (15)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942025495F,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Seesaw Room Crates (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202749A0,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Seesaw Room Crates (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202749A1,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Seesaw Room Crates (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202749A2,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Seesaw Room Crates (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202749A3,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Seesaw Room Crates (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202749A4,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Seesaw Room Crates (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202749A5,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Seesaw Room Crates (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202749A6,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Crates (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420224990,
        can_create=lambda options: options.woodsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Crates (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420224991,
        can_create=lambda options: options.woodsanity.value
    ),
    # Stone Tower Temple Crates
    "Stone Tower Temple Entrance Room Crates (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420251600,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Entrance Room Crates (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420251601,
        can_create=lambda options: options.woodsanity.value
    ),        
    "Stone Tower Temple Mirror Room Crates (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420271670,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Mirror Room Crates (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420271671,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Eyegore Room Crates (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420251610,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Eyegore Room Crates (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420251611,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Eyegore Room Crates (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420251612,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Behind Bombable Wall Crates (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420271620,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Behind Bombable Wall Crates (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420271621,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Behind Bombable Wall Crates (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420271622,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Behind Bombable Wall Crates (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420271623,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Behind Bombable Wall Crates (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420271624,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Behind Bombable Wall Crates (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420251620,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Behind Bombable Wall Crates (6)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420251621,
        can_create=lambda options: options.woodsanity.value
    ),         
    # Stone Tower Temple Inverted Crates
    "Stone Tower Temple Inverted Entry Crates (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251800,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Entry Crates (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251801,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Entry Crates (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251802,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Entry Crates (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251803,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Entry Crates (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251804,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Thin Hallway Crates (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251830,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Thin Hallway Crates (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251831,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Thin Hallway Crates (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251832,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Thin Hallway Crates (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251833,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Thin Hallway Crates (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251834,
        can_create=lambda options: options.woodsanity.value
    ),
    "Stone Tower Temple Inverted Thin Hallway Crates (5)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420251835,
        can_create=lambda options: options.woodsanity.value
    ),

    # Scarecrow Items
    "Clock Town Trading Post Scarecrow": MMRLocationData(
        region="Clock Town",
        address=0x3469420303400,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Astral Observatory Scarecrow": MMRLocationData(
        region="Clock Town",
        address=0x3469420302910,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Mountain Village Rooftop Scarecrow": MMRLocationData(
        region="Mountain Village",
        address=0x3469420305000,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Mountain Village Spring Rooftop Scarecrow": MMRLocationData(
        region="Mountain Village",
        address=0x3469420305A00,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Path to Snowhead Scarecrow": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420305B00,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Path to Snowhead Spring Scarecrow": MMRLocationData(
        region="Path to Snowhead",
        address=0x3469420305C00,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Twin Islands Scarecrow": MMRLocationData(
        region="Twin Islands",
        address=0x3469420305D00,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Twin Islands (Spring) Scarecrow": MMRLocationData(
        region="Twin Islands",
        address=0x3469420305E00,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Snowhead Temple Lower Scarecrow": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420302140,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Snowhead Temple Hidden Alcove Scarecrow": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420302141,
        can_create=lambda options: options.scarecrowsanity.value
    ),        
    "Great Bay Coast Rock Wall Scarecrow": MMRLocationData(
        region="Great Bay",
        address=0x3469420303700,
        can_create=lambda options: options.scarecrowsanity.value
    ),    
    "Zora Cape Beavers Scarecrow": MMRLocationData(
        region="Zora Cape",
        address=0x3469420303800,
        can_create=lambda options: options.scarecrowsanity.value
    ), 
    "Zora Cape Island Scarecrow": MMRLocationData(
        region="Zora Cape",
        address=0x3469420303801,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Zora Hall Pervert Scarecrow": MMRLocationData(
        region="Zora Hall",
        address=0x3469420303300,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Road to Ikana Scarecrow": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420305300,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Stone Tower Lower Scarecrow": MMRLocationData(
        region="Stone Tower",
        address=0x3469420305800,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Stone Tower Upper Scarecrow": MMRLocationData(
        region="Stone Tower",
        address=0x3469420305801,
        can_create=lambda options: options.scarecrowsanity.value
    ),

    # Icicles

    # Snowhead Temple
    "Snowhead Temple Entry Block Icicles (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232100,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Entry Block Icicles (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232105,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Entry Block Icicles (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232101,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Entry Block Icicles (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232106,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Entry Block Icicles (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232104,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Grey Door Icicles (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232103,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Grey Door Icicles (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232102,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Grey Door Ceiling Icicles (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232108,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Grey Door Ceiling Icicles (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232107,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Frozen Block Ceiling Icicle (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232110,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Frozen Block Ceiling Icicle (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232111,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Frozen Block Ceiling Icicle (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232112,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Frozen Block Ceiling Icicle (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232113,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Frozen Block Ceiling Icicle (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232114,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Icicle Room Ceiling Icicle (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232170,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Icicle Room Ceiling Icicle (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232171,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Icicle Room Ceiling Icicle (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232172,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Icicle Room Ceiling Icicle (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232173,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Icicle Room Ceiling Icicle (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232174,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 3F Behind Locked Door Icicles (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202321A0,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 3F Behind Locked Door Icicles (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202321A1,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 3F Behind Locked Door Icicles (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202321A2,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 3F Behind Locked Door Ceiling Icicles (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202321A3,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 3F Behind Locked Door Ceiling Icicles (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202321A4,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 3F Behind Locked Door Ceiling Icicles (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202321A5,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 3F Behind Locked Door Ceiling Icicles (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202321A6,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 4F Outside Wizzrobe Icicles (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232140,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple 4F Outside Wizzrobe Icicles (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232144,
        can_create=lambda options: options.iciclesanity.value
    ),
    # Snowhead Temple Outside Boss Icicles
    "Snowhead Temple Outside Boss Door Icicles (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232141,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Outside Boss Door Icicles (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232142,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Outside Boss Door Icicles (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232143,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Snowhead Temple Outside Boss Door Icicles (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420232145,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Great Bay Temple Outside Frog Miniboss Door Icicles (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420234940,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Great Bay Temple Outside Frog Miniboss Door Icicles (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420234941,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Great Bay Temple Outside Frog Miniboss Door Icicles (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420234942,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Great Bay Temple Outside Frog Miniboss Door Icicles (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420234943,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Great Bay Temple Outside Frog Miniboss Door Icicles (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420234944,
        can_create=lambda options: options.iciclesanity.value
    ),         
    "Bottom of the Well Icicle (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420234B11,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Bottom of the Well Icicle (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420234B10,
        can_create=lambda options: options.iciclesanity.value
    ),              
    "Goron Trial Icicles (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420233F00,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Goron Trial Icicles (2)": MMRLocationData(
        region="The Moon",
        address=0x3469420233F01,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Goron Trial Icicles (3)": MMRLocationData(
        region="The Moon",
        address=0x3469420233F02,
        can_create=lambda options: options.iciclesanity.value
    ),
    "Goron Trial Icicles (4)": MMRLocationData(
        region="The Moon",
        address=0x3469420233F03,
        can_create=lambda options: options.iciclesanity.value
    ),

    # Hivesanity

    # Termina Field
    "Termina Field Bombable Rock Grotto Hive (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420248000,
        can_create=lambda options: options.hivesanity.value
    ),
    "Termina Field Bio Baba Grotto Hive (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420248BB1,
        can_create=lambda options: options.hivesanity.value
    ),
    "Termina Field Bio Baba Grotto Hive (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420248BB2,
        can_create=lambda options: options.hivesanity.value
    ),   
    "Termina Field Cow Grotto Hive": MMRLocationData(
        region="Termina Field",
        address=0x346942024ADA0,
        can_create=lambda options: options.hivesanity.value
    ),   
    # Southern Swamp Hives
    "Southern Swamp Hive Near Frog (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420244500,
        can_create=lambda options: options.hivesanity.value
    ),
    # Swamp Spider House Hives
    "Swamp Spider House Giant Pot Room Hives (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242740,
        can_create=lambda options: options.hivesanity.value
    ),
    "Swamp Spider House Giant Pot Room Hives (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242741,
        can_create=lambda options: options.hivesanity.value
    ),
    "Swamp Spider House Giant Pot Room Hives (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242744,
        can_create=lambda options: options.hivesanity.value
    ),
    "Swamp Spider House Gold Room Hives (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242720,
        can_create=lambda options: options.hivesanity.value
    ),
    "Swamp Spider House Gold Room Hives (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242721,
        can_create=lambda options: options.hivesanity.value
    ),    
    "Swamp Spider House Gold Room Hives (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242722,
        can_create=lambda options: options.hivesanity.value
    ),
    "Swamp Spider Tree Room Hives (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242750,
        can_create=lambda options: options.hivesanity.value
    ),
    "Swamp Spider Tree Room Hives (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242751,
        can_create=lambda options: options.hivesanity.value
    ),
    "Swamp Spider Tree Room Hives (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420242753,
        can_create=lambda options: options.hivesanity.value
    ),            
    # Woodfall Temple Hives
    "Woodfall Temple Entrance Hive (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420241B20,
        can_create=lambda options: options.hivesanity.value
    ),
    "Woodfall Temple Push Block Hive (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420241B31,
        can_create=lambda options: options.hivesanity.value
    ),
    # Mountain Village Spring Hives   
    "Mountain Village Spring Tree Hive (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420245A00,
        can_create=lambda options: options.hivesanity.value
    ),
    "Great Bay Coast Cow Grotto Hive": MMRLocationData(
        region="Great Bay",
        address=0x346942024B7A0,
        can_create=lambda options: options.hivesanity.value
    ),
    #People complained so its removed now.

    # # Pirates Fortress Interior Guarded Hive From Barrel  
    # "Pirates Fortress Interior Leaders Hive From Lower Barrels": MMRLocationData(
    #     region="Pirates' Fortress (Interior)",
    #     address=0x3469420242330,
    #     can_create=lambda options: options.hivesanity.value
    # ),

    # Real Fairies including Gossips/Butterfly Fairies
    
    # Termina Field Gossip Fairies
    "Termina Field Southern Tree Gossip Fairy": MMRLocationData(
        region="Termina Field",
        address=0x34694201F2D30,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Near Thieving Bird Gossip Fairy": MMRLocationData(
        region="Termina Field",
        address=0x34694201F2D38,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Near Bombable Rock Grotto Gossip Fairy": MMRLocationData(
        region="Termina Field",
        address=0x34694201F2D39,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Gossip Grotto Gossip Fairy": MMRLocationData(
        region="Termina Field",
        address=0x34694201F0710,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Near Songwall Gossip Fairy": MMRLocationData(
        region="Termina Field",
        address=0x34694201F2D3A,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Eastern Corner Gossip Fairy": MMRLocationData(
        region="Termina Field",
        address=0x34694201F2D3B,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Observatory Gossip Fairy": MMRLocationData(
        region="Termina Field",
        address=0x34694201F2D31,
        can_create=lambda options: options.realfairysanity.value
    ), 

    # Road to Southern Swamp Gossip Fairy
    "Road to Southern Swamp Gossip Fairy": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694201F4030,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Southern Swamp Gossip Fairies
    "Southern Swamp Near Witch Gossip Fairy": MMRLocationData(
        region="Southern Swamp",
        address=0x34694201F4531,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Southern Swamp Near Witch Post Dungeon Gossip Fairy": MMRLocationData(
        region="Southern Swamp",
        address=0x34694201F0031,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Swamp Spider House Gossip Fairy": MMRLocationData(
        region="Swamp Spider House",
        address=0x34694201F2737,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Milk Road Gossip Fairy
    "Milk Road Gossip Fairy": MMRLocationData(
        region="Milk Road",
        address=0x34694201F223E,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Romani Ranch Gossip Fairies
    "Romani Ranch Entry Gossip Fairy": MMRLocationData(
        region="Romani Ranch",
        address=0x34694201F3534,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Romani Ranch Tree Gossip Fairy": MMRLocationData(
        region="Romani Ranch",
        address=0x34694201F353C,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Romani Ranch Near Barn Gossip Fairy": MMRLocationData(
        region="Romani Ranch",
        address=0x34694201F353D,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Romani Ranch Baby Cuccoos Gossip Fairy": MMRLocationData(
        region="Romani Ranch",
        address=0x34694201F4232,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Romani Ranch Doggy Racetrack Gossip Fairy": MMRLocationData(
        region="Romani Ranch",
        address=0x34694201F4133,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Path To Mountain Village Gossip Fairy
    "Path To Mountain Village Gossip Fairy": MMRLocationData(
        region="Path to Mountain Village",
        address=0x34694201F1C33,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Mountain Village Gossip Fairies
    "Mountain Village Spring Waterfall Gossip Fairy": MMRLocationData(
        region="Mountain Village",
        address=0x34694201F5A36,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Ramps To Goron Graveyard Gossip Fairy": MMRLocationData(
        region="Mountain Village",
        address=0x34694201F5A32,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Great Bay Gossip Fairy
    "Great Bay Coast Rock Wall Gossip Fairy": MMRLocationData(
        region="Great Bay",
        address=0x34694201F373F,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Zora Cape Gossip Fairy
    "Zora Cape Gossip Fairy": MMRLocationData(
        region="Zora Cape",
        address=0x34694201F3834,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Road To Ikana Gossip Fairy
    "Road To Ikana Gossip Fairy": MMRLocationData(
        region="Road to Ikana",
        address=0x34694201F5335,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Ikana Canyon Gossip Fairies
    "Ikana Canyon Near Octoroks Gossip Fairy": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x34694201F1336,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Ikana Canyon Across Ocean Deed Ravine Gossip Fairy": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x34694201F1335,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Ikana Canyon Near Ghost House Gossip Fairy": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x34694201F1337,
        can_create=lambda options: options.realfairysanity.value
    ),
    # Well Fairies 
    "Fairy Fountain Left Side Well (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB1,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Fairy Fountain Left Side Well (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB2,
        can_create=lambda options: options.realfairysanity.value
    ),   
    "Fairy Fountain Left Side Well (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB3,
        can_create=lambda options: options.realfairysanity.value
    ),   
    "Fairy Fountain Left Side Well (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB4,
        can_create=lambda options: options.realfairysanity.value
    ),   
    "Fairy Fountain Left Side Well (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB5,
        can_create=lambda options: options.realfairysanity.value
    ),   
    "Fairy Fountain Left Side Well (5)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB6,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Fairy Fountain Left Side Well (6)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB7,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Fairy Fountain Left Side Well (7)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694200F4BB8,
        can_create=lambda options: options.realfairysanity.value
    ),                                             
    # The Moon Gossip Fairies
    
    # Goron Trial Gossip Fairies
    "Goron Trial 1st Gazebo Gossip (0)": MMRLocationData(
        region="The Moon",
        address=0x34694201F3F0F,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Goron Trial 1st Gazebo Gossip (1)": MMRLocationData(
        region="The Moon",
        address=0x34694201F3F0E,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Goron Trial 2nd Gazebo Gossip (0)": MMRLocationData(
        region="The Moon",
        address=0x34694201F3F0C,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Goron Trial 2nd Gazebo Gossip (1)": MMRLocationData(
        region="The Moon",
        address=0x34694201F3F0D,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Goron Trial Near Heart Piece Gossip (1)": MMRLocationData(
        region="The Moon",
        address=0x34694201F3F0B,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Zora Trial Gossip Fairies
    "Zora Trial RRR Path Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F4714,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Zora Trial RRL Path Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F4713,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Zora Trial LRR Path Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F4712,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Zora Trial LRLL Path Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F4711,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Zora Trial LLL Path Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F4710,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Deku Trial Gossip Fairies
    "Deku Trial Front Left Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F2A06,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Deku Trial Back Left Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F2A08,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Deku Trial Front Right Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F2A07,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Deku Trial Back Right Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F2A09,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Deku Trial Furthest Back Gossip": MMRLocationData(
        region="The Moon",
        address=0x34694201F2A0A,
        can_create=lambda options: options.realfairysanity.value
    ),
    
    # Link Trial Gossip Fairies
    "Link Trial Gossip (1)": MMRLocationData(
        region="The Moon",
        address=0x34694201F6601,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Link Trial Gossip (2)": MMRLocationData(
        region="The Moon",
        address=0x34694201F6602,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Link Trial Gossip (3)": MMRLocationData(
        region="The Moon",
        address=0x34694201F6603,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Link Trial Gossip (4)": MMRLocationData(
        region="The Moon",
        address=0x34694201F6604,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Link Trial Gossip (5)": MMRLocationData(
        region="The Moon",
        address=0x34694201F6605,
        can_create=lambda options: options.realfairysanity.value
    ),
    #Butterfly Fairies
    #Termina Field Butterflies
    "Termina Field Near Peehat Grotto Butterfly Fairy (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420BF2D00,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Near Peehat Grotto Butterfly Fairy (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420BF2D01,
        can_create=lambda options: options.realfairysanity.value
    ),    
    "Termina Field Cow Grotto Butterfly Fairy (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420BFADA0,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Cow Grotto Butterfly Fairy (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420BFADA1,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Cow Grotto Butterfly Fairy (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420BFADA2,
        can_create=lambda options: options.realfairysanity.value
    ),                
    "Termina Field Bombable Rock Grotto Butterfly Fairy (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420BF8000,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Termina Field Bombable Rock Grotto Butterfly Fairy (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420BF8001,
        can_create=lambda options: options.realfairysanity.value
    ),    
    #Deku Palace Butterfly
    "Deku Palace Bean Seller Butterfly Fairy (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420BF8CC0,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Deku Palace Bean Seller Butterfly Fairy (2)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420BF8CC1,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Deku Palace Bean Seller Butterfly Fairy (3)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420BF8CC2,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Deku Palace Bean Seller Butterfly Fairy (4)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420BF8CC3,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A00,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A01,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A02,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A03,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (5)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A04,
        can_create=lambda options: options.realfairysanity.value
    ),                
    "Mountain Village Spring Day Butterfly (6)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A05,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (7)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A06,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (8)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A07,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Mountain Village Spring Day Butterfly (9)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420BF5A08,
        can_create=lambda options: options.realfairysanity.value
    ),                       
    #Great Bay Coast Butterflies
    "Great Bay Coast Outside Fisherman Hut Butterfly Fairy (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420BF3700,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Great Bay Coast Outside Fisherman Hut Butterfly Fairy (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420BF3701,
        can_create=lambda options: options.realfairysanity.value
    ),    
    "Great Bay Coast Cow Grotto Butterfly Fairy (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420BFB7A0,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Great Bay Coast Cow Grotto Butterfly Fairy (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420BFB7A1,
        can_create=lambda options: options.realfairysanity.value
    ), 
    "Great Bay Coast Cow Grotto Butterfly Fairy (3)": MMRLocationData(
        region="Great Bay",
        address=0x3469420BFB7A2,
        can_create=lambda options: options.realfairysanity.value
    ),           
    #Moon Butterflies
    "Moon Butterfly Fairy (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6700,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (2)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6701,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (3)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6702,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (4)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6703,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (5)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6704,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (6)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6705,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (7)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6706,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (8)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6707,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (9)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6708,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (10)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF6709,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (11)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF670A,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (12)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF670B,
        can_create=lambda options: options.realfairysanity.value
    ),
    "Moon Butterfly Fairy (13)": MMRLocationData(
        region="The Moon",
        address=0x3469420BF670C,
        can_create=lambda options: options.realfairysanity.value
    ),
    # Notebook Entries                
    "Notebook Meeting Bombers": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0000,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Anju": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0001,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Kafei": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0002,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Curiosity Shop Man": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0003,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Bomb Shop Lady": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0004,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Romani": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B0005,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Cremia": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B0006,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Mayor Dotour": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0007,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Madame Aroma": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0008,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Africa (Toto)": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0009,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Gorman": MMRLocationData(
        region="Clock Town",
        address=0x34694200B000A,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Postman": MMRLocationData(
        region="Clock Town",
        address=0x34694200B000B,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Rosa Sisters": MMRLocationData(
        region="Clock Town",
        address=0x34694200B000C,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Toilet Hand": MMRLocationData(
        region="Clock Town",
        address=0x34694200B000D,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Anju's Grandmother": MMRLocationData(
        region="Clock Town",
        address=0x34694200B000E,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Kamaro": MMRLocationData(
        region="Termina Field",
        address=0x34694200B000F,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Grog": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B0010,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Gorman Brothers": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694200B0011,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Shiro": MMRLocationData(
        region="Road to Ikana",
        address=0x34694200B0012,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Meeting Guru Guru": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0013,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Room Key": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0014,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Promised Midnight Meeting": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0015,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Promised To Meet Kafei": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0016,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Letter To Kafei": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0017,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Deposited Letter To Kafei": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0018,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Pendant of Memories": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0019,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Delivered Pendant of Memories": MMRLocationData(
        region="Clock Town",
        address=0x34694200B001A,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Escaped Sakons Hideout": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x34694200B001B,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Promised To Help With Aliens": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B001C,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Defended Against Aliens": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B001D,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Milk Bottle": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B001E,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Escorted Cremia": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B001F,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Romanis Mask": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B0020,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Keaton Mask": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0021,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Priority Mail": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0022,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Delivered Priority Mail": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0023,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Learned Secret Code": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0024,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Bombers NotebooK": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0025,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Mayor HP": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0026,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Rosa Sisters HP": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0027,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Toilet Hand HP": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0028,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Grandma Short Story HP": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0029,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Grandma Long Story HP": MMRLocationData(
        region="Clock Town",
        address=0x34694200B002A,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Postman HP": MMRLocationData(
        region="Clock Town",
        address=0x34694200B002B,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Kafeis Mask": MMRLocationData(
        region="Clock Town",
        address=0x34694200B002C,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received All Night Mask": MMRLocationData(
        region="Clock Town",
        address=0x34694200B002D,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Bunny Hood": MMRLocationData(
        region="Romani Ranch",
        address=0x34694200B002E,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Garos Mask": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694200B002F,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Circus Leaders Mask": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0030,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Postmans Hat": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0031,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Couples Mask": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0032,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Blast Mask": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0033,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Kamaros Mask": MMRLocationData(
        region="Termina Field",
        address=0x34694200B0034,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Stone Mask": MMRLocationData(
        region="Road to Ikana",
        address=0x34694200B0035,
        can_create=lambda options: options.notebooksanity.value
    ),
    "Notebook Event Received Bremen Mask": MMRLocationData(
        region="Clock Town",
        address=0x34694200B0036,
        can_create=lambda options: options.notebooksanity.value
    ),

    #Owlsanity 
    "Clock Town Owl Statue": MMRLocationData(
        region="Clock Town",
        address=0x3469420FF1504,
        can_create=lambda options: options.owlsanity.value
    ),
    "Milk Road Owl Statue": MMRLocationData(
        region="Milk Road",
        address=0x3469420FF1505,
        can_create=lambda options: options.owlsanity.value
    ),
    "Southern Swamp Owl Statue": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420FF1507,
        can_create=lambda options: options.owlsanity.value
    ),
    "Woodfall Owl Statue": MMRLocationData(
        region="Woodfall",
        address=0x3469420FF1506,
        can_create=lambda options: options.owlsanity.value
    ),
    "Mountain Village Owl Statue": MMRLocationData(
        region="Mountain Village",
        address=0x3469420FF1503,
        can_create=lambda options: options.owlsanity.value
    ),
    "Snowhead Owl Statue": MMRLocationData(
        region="Snowhead",
        address=0x3469420FF1502,
        can_create=lambda options: options.owlsanity.value
    ),
    "Great Bay Coast Owl Statue": MMRLocationData(
        region="Great Bay",
        address=0x3469420FF1500,
        can_create=lambda options: options.owlsanity.value
    ),
    "Zora Cape Owl Statue": MMRLocationData(
        region="Zora Cape",
        address=0x3469420FF1501,
        can_create=lambda options: options.owlsanity.value
    ),
    "Ikana Canyon Owl Statue": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420FF1508,
        can_create=lambda options: options.owlsanity.value
    ),
    "Stone Tower Owl Statue": MMRLocationData(
        region="Stone Tower",
        address=0x3469420FF1509,
        can_create=lambda options: options.owlsanity.value
    ),

    #Frogs
    "Laundry Pool Frog": MMRLocationData(
        region="Clock Town",
        address=0x3469420FF0004,
        can_create=lambda options: options.frogsanity.value
    ), 
    "Southern Swamp Frog": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420FF0003,
        can_create=lambda options: options.frogsanity.value
    ),
    "Woodfall Temple Miniboss Frog": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420FF0001,
        can_create=lambda options: options.frogsanity.value
    ),    
    "Great Bay Temple Miniboss Frog": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420FF0002,
        can_create=lambda options: options.frogsanity.value
    ),  
    # Treesanity Locations
    "North Clock Town Tree (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694202D6E00,
        can_create=lambda options: options.treesanity.value
    ),
    "North Clock Town Tree (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694202D6E01,
        can_create=lambda options: options.treesanity.value
    ),
    "West Clock Town Trading Post Bush (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694202C343F,
        can_create=lambda options: options.treesanity.value
    ),
    "West Clock Town Trading Post Bush (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694202C348C,
        can_create=lambda options: options.treesanity.value
    ),
    "West Clock Town Trading Post Bush (3)": MMRLocationData(
        region="Clock Town",
        address=0x34694202C34CA,
        can_create=lambda options: options.treesanity.value
    ),
    "West Clock Town Trading Post Bush (4)": MMRLocationData(
        region="Clock Town",
        address=0x34694202C34E8,
        can_create=lambda options: options.treesanity.value
    ),
    "Termina Field Tree Near Observatory (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694202C2DED,
        can_create=lambda options: options.treesanity.value
    ),
    "Termina Field Tree Near Observatory (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694202C2DAA,
        can_create=lambda options: options.treesanity.value
    ),            
    "Termina Field Tree Near Observatory (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694202C2DB3,
        can_create=lambda options: options.treesanity.value
    ),
    "Road to Southern Swamp Trees (1)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202D4000,
        can_create=lambda options: options.treesanity.value
    ),
    "Road to Southern Swamp Trees (2)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202D4001,
        can_create=lambda options: options.treesanity.value
    ),
    "Road to Southern Swamp Trees (3)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202D4002,
        can_create=lambda options: options.treesanity.value
    ),
    "Road to Southern Swamp Trees (4)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202D4003,
        can_create=lambda options: options.treesanity.value
    ),
    "Road to Southern Swamp Trees (5)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202D4004,
        can_create=lambda options: options.treesanity.value
    ),
    "Road to Southern Swamp Trees (6)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694202D4005,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Mountains Tree (1)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x34694202B1C00,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Mountains Tree (2)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x34694202B1C01,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Mountains Tree (3)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x34694202B1C02,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Mountains Tree (4)": MMRLocationData(
        region="Path to Mountain Village",
        address=0x34694202B1C03,
        can_create=lambda options: options.treesanity.value
    ),
    "Twin Islands Tree (1)": MMRLocationData(
        region="Twin Islands",
        address=0x34694202B5D00,
        can_create=lambda options: options.treesanity.value
    ),
    "Twin Islands Tree (2)": MMRLocationData(
        region="Twin Islands",
        address=0x34694202B5D01,
        can_create=lambda options: options.treesanity.value
    ),
    "Twin Islands Tree (3)": MMRLocationData(
        region="Twin Islands",
        address=0x34694202B5D02,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Snowhead Tree Near Ledge": MMRLocationData(
        region="Path to Snowhead",
        address=0x34694202B5B03,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Snowhead Tree (1)": MMRLocationData(
        region="Path to Snowhead",
        address=0x34694202B5B00,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Snowhead Tree (2)": MMRLocationData(
        region="Path to Snowhead",
        address=0x34694202B5B01,
        can_create=lambda options: options.treesanity.value
    ),
    "Path To Snowhead Tree (3)": MMRLocationData(
        region="Path to Snowhead",
        address=0x34694202B5B02,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (1)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B00,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (2)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B01,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (3)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B02,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (4)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B03,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (5)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B04,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (6)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B05,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (7)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B06,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (8)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B07,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (9)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B08,
        can_create=lambda options: options.treesanity.value
    ),
    "Goron Racetrack Trees (10)": MMRLocationData(
        region="Goron Racetrack",
        address=0x34694202D6B09,
        can_create=lambda options: options.treesanity.value
    ),
    "Twin Islands (Spring) Tree (1)": MMRLocationData(
        region="Twin Islands",
        address=0x34694202C5E94,
        can_create=lambda options: options.treesanity.value
    ),
    "Twin Islands (Spring) Tree (2)": MMRLocationData(
        region="Twin Islands",
        address=0x34694202C5E66,
        can_create=lambda options: options.treesanity.value
    ),
    "Twin Islands (Spring) Tree (3)": MMRLocationData(
        region="Twin Islands",
        address=0x34694202C5E0B,
        can_create=lambda options: options.treesanity.value
    ),
    "Romani Ranch Bush (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C35B9,
        can_create=lambda options: options.treesanity.value
    ),  
    "Romani Ranch Bush (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C3596,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Bush (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C3520,
        can_create=lambda options: options.treesanity.value
    ),
    "Romani Ranch Bush (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C3540,
        can_create=lambda options: options.treesanity.value
    ),
    "Romani Ranch Tree (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C356E,
        can_create=lambda options: options.treesanity.value
    ),   
    "Romani Ranch Tree (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C3554,
        can_create=lambda options: options.treesanity.value
    ),   
    "Romani Ranch Tree (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C356A,
        can_create=lambda options: options.treesanity.value
    ),    
    "Romani Ranch Tree (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C35E8,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Tree (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C3579,
        can_create=lambda options: options.treesanity.value
    ),
    "Romani Ranch Tree (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C353A,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Tree (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C351E,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Tree": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C426D,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Bush (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C42C2,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Bush (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C426A,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Bush (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C42DF,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Bush (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C42C1,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Bush (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C424A,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Bush (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C42AA,
        can_create=lambda options: options.treesanity.value
    ), 
    "Romani Ranch Baby Cucoo Bush (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202C427D,
        can_create=lambda options: options.treesanity.value
    ), 
    "Gorman Racetrack Tree Group 1 (1)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A01,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (2)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A06,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (3)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A14,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (4)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A41,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (5)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A77,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (6)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A99,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (7)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6AC7,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (8)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6ACF,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (9)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6AD3,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (10)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6AD7,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (11)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6AEF,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 1 (12)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A02,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (1)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A04,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (2)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A0A,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (3)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A13,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (4)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A1D,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (5)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A44,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (6)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A47,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (7)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A51,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (8)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A8F,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (9)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6AA8,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (10)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6ADA,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (11)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6ADC,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (12)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6AF2,
        can_create=lambda options: options.treesanity.value
    ),
    "Gorman Racetrack Tree Group 2 (13)": MMRLocationData(
        region="Inside Gorman Brothers Track",
        address=0x34694202C6A20,
        can_create=lambda options: options.treesanity.value
    ),
    "Great Bay Coast Nut Tree (1)": MMRLocationData(
        region="Great Bay",
        address=0x34694202A3701,
        can_create=lambda options: options.treesanity.value
    ),    
    "Great Bay Coast Nut Tree (2)": MMRLocationData(
        region="Great Bay",
        address=0x34694202A3702,
        can_create=lambda options: options.treesanity.value
    ),    
    "Great Bay Coast Nut Tree (3)": MMRLocationData(
        region="Great Bay",
        address=0x34694202A3703,
        can_create=lambda options: options.treesanity.value
    ),    
    "Great Bay Coast Fisherman Island Nut Tree (1)": MMRLocationData(
        region="Great Bay",
        address=0x34694202A3700,
        can_create=lambda options: options.treesanity.value
    ),   
    "Zora Cape Nut Tree Near Jars (1)": MMRLocationData(
        region="Zora Cape",
        address=0x34694202A3800,
        can_create=lambda options: options.treesanity.value
    ),   
    "Zora Cape Nut Tree Near Jars (2)": MMRLocationData(
        region="Zora Cape",
        address=0x34694202A3801,
        can_create=lambda options: options.treesanity.value
    ),   
    "Zora Cape Nut Tree On Islands (1)": MMRLocationData(
        region="Zora Cape",
        address=0x34694202A3802,
        can_create=lambda options: options.treesanity.value
    ),  
    "Zora Cape Nut Tree On Islands (2)": MMRLocationData(
        region="Zora Cape",
        address=0x34694202A3803,
        can_create=lambda options: options.treesanity.value
    ),  
    "Zora Cape Nut Tree On Islands (3)": MMRLocationData(
        region="Zora Cape",
        address=0x34694202A3804,
        can_create=lambda options: options.treesanity.value
    ),   
    "Zora Cape Nut Tree On Turtle Island (1)": MMRLocationData(
        region="Zora Cape",
        address=0x34694202A3805,
        can_create=lambda options: options.treesanity.value
    ),   
    "Zora Cape Nut Tree On Turtle Island (2)": MMRLocationData(
        region="Zora Cape",
        address=0x34694202A3806,
        can_create=lambda options: options.treesanity.value
    ), 
    "Beneath The Well Tree Near Cow": MMRLocationData(
        region="Beneath the Well",
        address=0x34694202C4BCB,
        can_create=lambda options: options.treesanity.value
    ), 
    "Beneath The Well Bush Near Cow (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694202C4B25,
        can_create=lambda options: options.treesanity.value
    ),
    "Beneath The Well Bush Near Cow (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694202C4B93,
        can_create=lambda options: options.treesanity.value
    ),

    # Flowersanity
   
    "Before Clock Town Flower (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A10,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A11,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (3)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A12,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (4)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A13,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (5)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A14,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (6)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A15,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (7)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A00,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (8)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A01,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (9)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A02,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (10)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A03,
        can_create=lambda options: options.flowersanity.value
    ),
    "Before Clock Town Flower (11)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1A04,
        can_create=lambda options: options.flowersanity.value
    ),
    "South Clock Town Business Scrub Flower": MMRLocationData(
        region="Clock Town",
        address=0x34694203F6F00,
        can_create=lambda options: options.flowersanity.value
    ),
    "East Clock Town Flower": MMRLocationData(
        region="Clock Town",
        address=0x34694203F6C00,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Flower (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F6E00,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Flower (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F6E01,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (1)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E00,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (2)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E01,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (3)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E02,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (4)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E03,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (5)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E04,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (6)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E05,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (7)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E06,
        can_create=lambda options: options.flowersanity.value
    ),
    "North Clock Town Deku Playground Flower (8)": MMRLocationData(
        region="Clock Town",
        address=0x34694203F1E07,
        can_create=lambda options: options.flowersanity.value
    ),
    "Termina Field Flower Near Observatory": MMRLocationData(
        region="Termina Field",
        address=0x34694203F2D03,
        can_create=lambda options: options.flowersanity.value
    ),
    "Termina Field Flower Near Skullkid Drawing": MMRLocationData(
        region="Termina Field",
        address=0x34694203F2D02,
        can_create=lambda options: options.flowersanity.value
    ),
    "Termina Field Flower Near Stump": MMRLocationData(
        region="Termina Field",
        address=0x34694203F2D01,
        can_create=lambda options: options.flowersanity.value
    ),
    "Termina Field Flower Near Giant Log": MMRLocationData(
        region="Termina Field",
        address=0x34694203F2D00,
        can_create=lambda options: options.flowersanity.value
    ),
    # Road To Swamp Flowers
    "Road to Southern Swamp Flowers (1)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4000,
        can_create=lambda options: options.flowersanity.value
    ),
    "Road to Southern Swamp Flowers (2)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4001,
        can_create=lambda options: options.flowersanity.value
    ),
    "Road to Southern Swamp Flowers (3)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4002,
        can_create=lambda options: options.flowersanity.value
    ),
    "Road to Southern Swamp Flowers (4)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4003,
        can_create=lambda options: options.flowersanity.value
    ),
    "Road to Southern Swamp Flowers (5)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4004,
        can_create=lambda options: options.flowersanity.value
    ),
    "Road to Southern Swamp Flowers (6)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4005,
        can_create=lambda options: options.flowersanity.value
    ),
    "Road to Southern Swamp Flowers (7)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4006,
        can_create=lambda options: options.flowersanity.value
    ),
    "Road to Southern Swamp Flowers (8)": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x34694203F4007,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Business Scrub Flower": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F4500,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Post Dungeon Business Scrub Flower": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F0000,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Woods of Mystery Flower Day 1/3 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F6430,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Woods of Mystery Flower Day 1/3 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F6431,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Woods of Mystery Flower Any Day (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F6440,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Woods of Mystery Flower Any Day (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F6450,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Woods of Mystery Flower Any Day (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F6451,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Woods of Mystery Flower Day 2 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F6470,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Woods of Mystery Flower Day 2 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F6471,
        can_create=lambda options: options.flowersanity.value
    ),
    #Deku Palace Flowers
    "Deku Palace Flower (1)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B10,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (2)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B11,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (3)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B12,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (4)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B13,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (5)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B14,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (6)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B15,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (7)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B20,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (8)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B21,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (9)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B22,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (10)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B23,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace Flower (11)": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B24,
        can_create=lambda options: options.flowersanity.value
    ),
    "Deku Palace To Swamp Flower": MMRLocationData(
        region="Deku Palace",
        address=0x34694203F2B00,
        can_create=lambda options: options.flowersanity.value
    ),
    # Swamp Spider Flowers
    "Swamp Spiderhouse Main Room Flowers (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x34694203F2710,
        can_create=lambda options: options.flowersanity.value
    ),
    "Swamp Spiderhouse Main Room Flowers (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x34694203F2711,
        can_create=lambda options: options.flowersanity.value
    ),
    "Swamp Spiderhouse Main Room Flower (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x34694203F2712,
        can_create=lambda options: options.flowersanity.value
    ),
    "Swamp Spiderhouse Giant Pot Room Flower (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x34694203F2740,
        can_create=lambda options: options.flowersanity.value
    ),
    # Requires Sonata 
    "Swamp Spiderhouse Giant Pot Room Flower (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x34694203F2741,
        can_create=lambda options: options.flowersanity.value
    ),
    #Heading to Woodfall
    "Southern Swamp Path To Woodfall Flower (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F4510,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Path To Woodfall Flower (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F4511,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Path To Woodfall Flower (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F4512,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Path To Woodfall Flower (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F4513,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Path To Woodfall Flower (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F4514,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Path To Woodfall Flower (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F4515,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (1)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4600,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (2)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4601,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (3)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4602,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (4)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4603,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (5)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4604,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (6)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4605,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (7)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4606,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (8)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4607,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Flower (9)": MMRLocationData(
        region="Woodfall",
        address=0x34694203F4608,
        can_create=lambda options: options.flowersanity.value
    ),
    # Woodfall Temple Flowers
    "Woodfall Temple Entrance Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B20,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Entrance Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B21,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Entrance Flower (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B22,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Entrance Flower (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B23,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Main Room Flower": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B10,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Elevator Room Flower": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B50,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Elevator Room Upper Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B51,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Elevator Room Upper Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B52,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Snapping Turtle Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B60,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Snapping Turtle Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B61,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Snapping Turtle Flower (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B62,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Gekko Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B80,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Gekko Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B81,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Gekko Flower (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B82,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Gekko Flower (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B83,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Gekko Flower (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B84,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Dinolfos Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B70,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Dinolfos Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B71,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple 2F Moving Platform Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1BA0,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple 2F Moving Platform Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1BA1,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple 2F Moving Platform Flower (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1BA2,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple 2F Moving Platform Flower (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1BA3,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Dragonfly Room Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B40,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Dragonfly Room Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B41,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Dragonfly Room Flower (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B42,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B00,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B01,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B02,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B03,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B04,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (6)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B05,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (7)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B06,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (8)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B07,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (9)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B08,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Pre Boss Room Flower (10)": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1B09,
        can_create=lambda options: options.flowersanity.value
    ),
    "Woodfall Temple Odolwa Golden Flower": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694203F1F00,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Post Dungeon Flower (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F0010,
        can_create=lambda options: options.flowersanity.value
    ),
    "Southern Swamp Post Dungeon Flower (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694203F0011,
        can_create=lambda options: options.flowersanity.value
    ),
    "Goron Village Business Scrub Flower": MMRLocationData(
        region="Goron Village",
        address=0x34694203F4D00,
        can_create=lambda options: options.flowersanity.value
    ),
    "Snowhead Temple Frozen Green Door Flower (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694203F2150,
        can_create=lambda options: options.flowersanity.value
    ),
    "Snowhead Temple Frozen Green Door Flower (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694203F2151,
        can_create=lambda options: options.flowersanity.value
    ),
    "Snowhead Temple Main Room Wall Chest Flower": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694203F2140,
        can_create=lambda options: options.flowersanity.value
    ),
    "Snowhead Temple Main Room Wall Chest Flower": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694203F2140,
        can_create=lambda options: options.flowersanity.value
    ),
    "Snowhead Temple Flower Outside Goht": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694203F2141,
        can_create=lambda options: options.flowersanity.value
    ),
    "Zora Cape Lower Wall Flower Near Beavers": MMRLocationData(
        region="Zora Cape",
        address=0x34694203F3800,
        can_create=lambda options: options.flowersanity.value
    ),
    "Zora Hall Business Scrub Flower": MMRLocationData(
        region="Zora Hall",
        address=0x34694203F4C20,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Canyon Business Scrub Flower (1)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x34694203F1340,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Canyon Business Scrub Flower (2)": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x34694203F1341,
        can_create=lambda options: options.flowersanity.value
    ),
    "Well Deku Flower (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694203F4B20,
        can_create=lambda options: options.flowersanity.value
    ),
    "Well Deku Flower (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694203F4B21,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Flower (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D20,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Flower (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D21,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Flower (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D22,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Flower (4)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D23,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Flower (5)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D24,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Flower (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D40,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Flower (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D41,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Flower (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D42,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Exterior Flower (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D00,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Exterior Flower (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D01,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Exterior Flower (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D02,
        can_create=lambda options: options.flowersanity.value
    ),
    "Ikana Castle Exterior Flower (4)": MMRLocationData(
        region="Ikana Castle",
        address=0x34694203F1D03,
        can_create=lambda options: options.flowersanity.value
    ),
    "Stone Tower Temple Deku Updraft Flower": MMRLocationData(
        region="Stone Tower Temple",
        address=0x34694203F1690,
        can_create=lambda options: options.flowersanity.value
    ),
    "Stone Tower Temple Inverted Eastern Air Gust Room Flower (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694203F1830,
        can_create=lambda options: options.flowersanity.value
    ),
    "Stone Tower Temple Inverted Eastern Air Gust Room Flower (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694203F1831,
        can_create=lambda options: options.flowersanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Flower (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694203F1820,
        can_create=lambda options: options.flowersanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Flower (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694203F1821,
        can_create=lambda options: options.flowersanity.value
    ),
    "Inverted Stone Tower Temple Lower Bridge Room Flower (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694203F1810,
        can_create=lambda options: options.flowersanity.value
    ),
    "Inverted Stone Tower Temple Lower Bridge Room Flower (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694203F1811,
        can_create=lambda options: options.flowersanity.value
    ),
    "Inverted Stone Tower Temple Lower Bridge Room Flower (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694203F1812,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (1)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A00,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (2)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A01,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (3)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A02,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (4)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A03,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (5)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A04,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (6)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A05,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (7)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A06,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (8)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A07,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (9)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A08,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (10)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A09,
        can_create=lambda options: options.flowersanity.value
    ),
    "The Moon Deku Trial Flower (11)": MMRLocationData(
        region="The Moon",
        address=0x34694203F2A0A,
        can_create=lambda options: options.flowersanity.value
    ),
    # "The Moon Majora Flower": MMRLocationData(
    #     region="The Moon",
    #     address=0x3469420,
    #     can_create=lambda options: options.flowersanity.value
    # ),
    
    # Signs
    "North Clock Town Cut the Sign": MMRLocationData(
        region="Clock Town",
        address=0x3469420310311,
        can_create=lambda options: options.signsanity.value
    ),
    "West Clock Town Sword School Night 3 Midnight Cut the Sign": MMRLocationData(
        region="Clock Town",
        address=0x3469420310310,
        can_create=lambda options: options.signsanity.value
    ),
    "East Clock Town Milk Bar Roof Cut the Sign": MMRLocationData(
        region="Clock Town",
        address=0x346942031033F,
        can_create=lambda options: options.signsanity.value
    ),
    "Termina Field Takkuri Cut the Sign": MMRLocationData(
        region="Termina Field",
        address=0x346942031033C,
        can_create=lambda options: options.signsanity.value
    ),
    "Road to Southern Swamp Entry Cut the Sign": MMRLocationData(
        region="Road to Southern Swamp",
        address=0x346942031030A,
        can_create=lambda options: options.signsanity.value
    ),
    "Southern Swamp Tourist Centre Cut the Sign": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420310307,
        can_create=lambda options: options.signsanity.value
    ),
    "Southern Swamp Witch's Hut Cut the Sign": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031030C,
        can_create=lambda options: options.signsanity.value
    ),
    "Southern Swamp Outside Woods of Mystery Cut the Sign": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031030B,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 1 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031033D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 1 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031133D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 1 (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031233D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 2 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031333D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 2 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031433D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 2 (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031533D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 3 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031633D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 3 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031733D,
        can_create=lambda options: options.signsanity.value
    ),
    "Woods of Mystery Cut the Sign Day 3 (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942031833D,
        can_create=lambda options: options.signsanity.value
    ),
    "Southern Swamp Log Cut the Sign": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420310309,
        can_create=lambda options: options.signsanity.value
    ),
    "Southern Swamp Outside Spider House": MMRLocationData(
        region="Southern Swamp (Deku Palace)",
        address=0x346942031030E,
        can_create=lambda options: options.signsanity.value
    ),
    "Swamp Spider House Behind Statue Cut the Sign": MMRLocationData(
        region="Swamp Spider House",
        address=0x346942031130C,
        can_create=lambda options: options.signsanity.value
    ),
    "Deku Palace Behind Entrance Guards Cut Left Sign": MMRLocationData(
        region="Deku Palace",
        address=0x3469420310338,
        can_create=lambda options: options.signsanity.value
    ),
    "Deku Palace Behind Entrance Guards Cut Right Sign": MMRLocationData(
        region="Deku Palace",
        address=0x3469420311338,
        can_create=lambda options: options.signsanity.value
    ),
    "Deku Palace Behind Entrance Guards Cut Sign Near King's Chamber": MMRLocationData(
        region="Deku Palace",
        address=0x346942031033A,
        can_create=lambda options: options.signsanity.value
    ),
    "Deku Palace Bean Daddy Grotto Cut the Sign": MMRLocationData(
        region="Deku Palace",
        address=0x346942031230C,
        can_create=lambda options: options.signsanity.value
    ),
    "Path to Mountain Village Cut the Sign": MMRLocationData(
        region="Path to Mountain Village",
        address=0x3469420310303,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Owl Statue Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420311314,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Owl Statue Spring Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420310317,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Bridge Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420310314,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Outside Smithy Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420310305,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Pond Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420310315,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Twin Island Entrance Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420310313,
        can_create=lambda options: options.signsanity.value
    ),
    "Twin Islands Outside Goron Racetrack Cut the Sign": MMRLocationData(
        region="Twin Islands",
        address=0x3469420310319,
        can_create=lambda options: options.signsanity.value
    ),
    "Goron Village Outside Lens Cave Cut the Sign": MMRLocationData(
        region="Goron Village",
        address=0x346942031031C,
        can_create=lambda options: options.signsanity.value
    ),
    "Goron Village Outside Keg Goron Cut the Sign": MMRLocationData(
        region="Goron Village",
        address=0x346942031031D,
        can_create=lambda options: options.signsanity.value
    ),
    "Goron Village Outside Goron Shrine": MMRLocationData(
        region="Goron Village",
        address=0x346942031031B,
        can_create=lambda options: options.signsanity.value
    ),
    "Path to Snowhead Cut the Sign": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942031031E,
        can_create=lambda options: options.signsanity.value
    ),
    "Path to Snowhead Upper Cut the Sign": MMRLocationData(
        region="Path to Snowhead",
        address=0x346942031031F,
        can_create=lambda options: options.signsanity.value
    ),
    "Outside Snowhead Temple Cut the Sign": MMRLocationData(
        region="Snowhead",
        address=0x3469420310320,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Spring Near Graveyard Pond Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420310318,
        can_create=lambda options: options.signsanity.value
    ),
    "Mountain Village Spring Path to Twin Islands Cut the Sign": MMRLocationData(
        region="Mountain Village",
        address=0x3469420310316,
        can_create=lambda options: options.signsanity.value
    ),
    "Twin Islands Spring Outside Goron Racetrack Cut the Sign": MMRLocationData(
        region="Twin Islands",
        address=0x346942031031A,
        can_create=lambda options: options.signsanity.value
    ),
    "Romani Ranch Epona Stable Cut the Sign": MMRLocationData(
        region="Romani Ranch",
        address=0x346942031033E,
        can_create=lambda options: options.signsanity.value
    ),
    "Romani Ranch Doggy Racetrack Cut the Sign": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420310302,
        can_create=lambda options: options.signsanity.value
    ),
    "Gorman Racetrack Fence Day 3 Cut the Sign": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x3469420310341,
        can_create=lambda options: options.signsanity.value
    ),
    "Great Bay Coast Entrance Cut the Sign": MMRLocationData(
        region="Great Bay",
        address=0x3469420310326,
        can_create=lambda options: options.signsanity.value
    ),
    "Great Bay Coast Outside Fisherman Hut Cut the Sign": MMRLocationData(
        region="Great Bay",
        address=0x3469420310321, 
        can_create=lambda options: options.signsanity.value
    ),
    "Great Bay Coast Beachfront Cut the Sign": MMRLocationData(
        region="Great Bay",
        address=0x3469420310327, 
        can_create=lambda options: options.signsanity.value
    ),
    "Great Bay Coast Entrance to Zora Cape Cut the Sign": MMRLocationData(
        region="Great Bay",
        address=0x3469420310325, 
        can_create=lambda options: options.signsanity.value
    ),
    "Great Bay Coast Marine Lab Cut the Sign": MMRLocationData(
        region="Great Bay",
        address=0x3469420310323, 
        can_create=lambda options: options.signsanity.value
    ),
    "Great Bay Coast Rock Pools Cut the Sign": MMRLocationData(
        region="Great Bay",
        address=0x3469420310322, 
        can_create=lambda options: options.signsanity.value
    ),
    "Great Bay Coast (Clear) Fisherman Boat Cut the Sign": MMRLocationData(
        region="Zora Cape",
        address=0x3469420310312, 
        can_create=lambda options: options.signsanity.value
    ),
    "Zora Cape Jar Game Cut the Sign": MMRLocationData(
        region="Zora Cape",
        address=0x346942031032B, 
        can_create=lambda options: options.signsanity.value
    ),
    "Zora Cape Waterfall Cut the Sign": MMRLocationData(
        region="Zora Cape",
        address=0x3469420310328,
        can_create=lambda options: options.signsanity.value
    ),
    "Zora Cape Turtle Cut the Sign": MMRLocationData(
        region="Zora Cape",
        address=0x346942031032A, 
        can_create=lambda options: options.signsanity.value
    ),
    "Ikana Canyon River Cut the Sign": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x346942031032E,
        can_create=lambda options: options.signsanity.value
    ),
    "Ikana Canyon Outside Sakon's Hideout Cut the Sign": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420310334,  
        can_create=lambda options: options.signsanity.value
    ),
    "Ikana Canyon Outside Secret Shrine Cut the Sign": MMRLocationData(
        region="Lower Ikana Canyon",
        address=0x3469420310333,  
        can_create=lambda options: options.signsanity.value
    ),
    "Ikana Canyon Outside Spring Cut the Sign": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420310330, 
        can_create=lambda options: options.signsanity.value
    ),
    "Ikana Canyon Outside Ikana Castle Cut the Sign": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420310332,
        can_create=lambda options: options.signsanity.value
    ),
    "Ikana Canyon Poe Hut Cut the Sign": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x3469420310331,
        can_create=lambda options: options.signsanity.value
    ),
    "Ikana Canyon Outside Well Cut the Sign": MMRLocationData(
        region="Upper Ikana Canyon",
        address=0x346942031032F,
        can_create=lambda options: options.signsanity.value
    ),

    # Websanity
    "Swamp Spider House Entrance Web": MMRLocationData(
        region="Southern Swamp",
        address=0x34694202E4510,
        can_create=lambda options: options.websanity.value
    ),
    "Swamp Spider House Entrance Web Cleared Swamp": MMRLocationData(
        region="Southern Swamp",
        address=0x34694202E0010,
        can_create=lambda options: options.websanity.value
    ),
    "Woodfall Temple Web Leading to Dark Room": MMRLocationData(
        region="Woodfall Temple",
        address=0x34694202E1B30,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Entrance Web (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2800,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Entrance Web (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2801,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Library Web": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2913,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web Above Door 1st Floor Door": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2910,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web Over 1st Floor Pot": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2915,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web 1st Floor Near Staircase": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2911,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web Basement Near Staircase": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2917,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web Basement Covering Crates": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2916,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web Basement Covering Hole": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2914,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web Basement Covering Door": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2912,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Web Boat Room Covering Crate": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2950,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Boat Room Ceiling Web": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2951,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Coloured Mask Ceiling Web (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2830,
        can_create=lambda options: options.websanity.value
    ),
    "Ocean Spider House Coloured Mask Ceiling Web (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202E2930,
        can_create=lambda options: options.websanity.value
    ),
    "Beneath the Well Left Side Web Near Fairy Fountain (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694202E4B50,
        can_create=lambda options: options.websanity.value
    ),
    "Beneath the Well Left Side Web Near Fairy Fountain (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x34694202E4B51,
        can_create=lambda options: options.websanity.value
    ),
    "Beneath the Well Right Side Web Near Milk Gibdo": MMRLocationData(
        region="Beneath the Well",
        address=0x34694202E4B70,
        can_create=lambda options: options.websanity.value
    ),
    
    #Oneoffs
    #Paintings
    "Ocean Spider House Behind Top Webbed Door Painting (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2820,
        can_create=lambda options: options.oneoffs.value
    ),
    "Ocean Spider House Behind Top Webbed Door Painting (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2821,
        can_create=lambda options: options.oneoffs.value
    ),
    "Ocean Spider House Behind Top Webbed Door Painting (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2822,
        can_create=lambda options: options.oneoffs.value
    ),
    "Ocean Spider House Behind Top Webbed Door Painting (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2823,
        can_create=lambda options: options.oneoffs.value
    ),
    "Ocean Spider House Coloured Mask Painting (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2830,
        can_create=lambda options: options.oneoffs.value
    ),
    "Ocean Spider House Coloured Mask Painting (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2831,
        can_create=lambda options: options.oneoffs.value
    ),
    "Ocean Spider House Coloured Mask Painting (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2832,
        can_create=lambda options: options.oneoffs.value
    ),
    "Ocean Spider House Coloured Mask Painting (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F2833,
        can_create=lambda options: options.oneoffs.value
    ),
    # Bombable Walls
    "Bombers Bombable Wall": MMRLocationData(
        region="Bomber's Hideout",
        address=0x34694202F290F,
        can_create=lambda options: options.oneoffs.value,
    ),
    "Snowhead Temple Bombable Wall": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202F211F,
        can_create=lambda options: options.oneoffs.value,
    ),
    "Ocean Spider House Entrance Wall": MMRLocationData(
        region="Ocean Spider House",
        address=0x34694202F280F,
        can_create=lambda options: options.oneoffs.value,
    ),
    "Stone Tower Temple Elegy Maze Bombable Wall": MMRLocationData(
        region="Stone Tower Temple",
        address=0x34694202F162F,
        can_create=lambda options: options.oneoffs.value,
    ),
    "Graveyard Day 2 Bombable Wall": MMRLocationData(
        region="Ikana Graveyard",
        address=0x34694202F0C3F,
        can_create=lambda options: options.oneoffs.value,
    ),
    "Link Trial Bombable Wall Iron Knuckle": MMRLocationData(
        region="The Moon",
        address=0x34694202F663F,
        can_create=lambda options: options.oneoffs.value,
    ),
    "Link Trial Bombable Wall Final Door": MMRLocationData(
        region="The Moon",
        address=0x34694202F664F,
        can_create=lambda options: options.oneoffs.value,
    ),
    "Goron Trial Chests": MMRLocationData(
        region="The Moon",
        address=0x3469420063F00,
        can_create=lambda options: options.oneoffs.value,
    ),

        # 100% Completion
    "Majora's Soul": MMRLocationData(
        region="Clock Town",
        address=0x34694200B012F,
        can_create=lambda options: options.completion_goal.value
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
