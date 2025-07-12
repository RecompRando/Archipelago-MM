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
    "Termina Peahat Grotto Chest": MMRLocationData(
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
        region="Woodfall Temple",
        address=0x3469420051F00
    ),
    "Woodfall Temple Odolwa's Remains": MMRLocationData(
        region="Woodfall Temple",
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
    # "Goron Village Freestanding HP (Spring)": MMRLocationData(
    #     region="Goron Village",
    #     address=0x346942005481E,
    #     can_create=lambda options: options.shopsanity.value == 2
    # ),
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
        region="Snowhead Temple",
        address=0x3469420054400
    ),
    "Snowhead Temple Goht's Remains": MMRLocationData(
        region="Snowhead Temple",
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
        address=0x3469420062304
    ),
    "Pirates' Fortress Sewers Underwater Upper Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420062306
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
    "Ocean Spider House Libary Painting #1 Token": MMRLocationData(
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
    "Great Bay Temple Caged Chest Room Pot SF": MMRLocationData(
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
    "Great Bay Temple Caged Chest Room Upper Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491C
    ),
    "Great Bay Temple Caged Chest Room Underwater Chest": MMRLocationData(
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
        region="Great Bay Temple",
        address=0x3469420055F00
    ),
    "Great Bay Temple Gyorg's Remains": MMRLocationData(
        region="Great Bay Temple",
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
        region="Ikana Canyon",
        address=0x3469420060714
    ),
    "Ikana Canyon Scrub Purchase": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942009015D,
        can_create=lambda options: options.scrubsanity.value
    ),
    "Ikana Canyon Zora Scrub Trade": MMRLocationData(
        region="Ikana Canyon",
        address=0x3469420001307
    ),
    "Ikana Canyon Zora Trade Freestanding HP": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942005131E
    ),
    "Ikana Canyon Healing Pamela's Father": MMRLocationData(
        region="Ikana Canyon",
        address=0x3469420000087
    ),
    "Ikana Canyon Spirit House": MMRLocationData(
        region="Ikana Canyon",
        address=0x34694200701DE
    ),
    "Stone Tower Great Fairy Reward": MMRLocationData(
        region="Ikana Canyon",
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
        region="Stone Tower Temple (Inverted)",
        address=0x3469420053600
    ),
    "Stone Tower Temple Inverted Twinmold's Remains": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
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
    
    # Grass/Pots/Hitspots/Hidden Rupees 'wonder items' past this point

    # Laundry Pool Grass

    "Laundry Pool Grass (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420127001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Laundry Pool Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420127002,
        can_create=lambda options: options.grasssanity.value
    ),
    "Laundry Pool Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420127003,
        can_create=lambda options: options.grasssanity.value
    ),
    # North Clock Town Keaton Grass
    "North Clock Town Keaton Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E00,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E01,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E02,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E03,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E04,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E05,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E06,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E07,
        can_create=lambda options: options.grasssanity.value
    ),
    "North Clock Town Keaton Grass (9)": MMRLocationData(
        region="Termina Field",
        address=0x3469420136E08,
        can_create=lambda options: options.grasssanity.value
    ),

    # Termina Field 

    "Termina Field Grass Group 0 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 0 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201002DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 1 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201012DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 2 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201022DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 3 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201032DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 4 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201042DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 5 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201052DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 6 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201062DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 7 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201072DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 8 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201082DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 9 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201092DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 10 (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010A2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 11 (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010B2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 12 (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010C2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 13 (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010D2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 14 (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010E2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (0)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 15 (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942010F2DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 16 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201102DB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (0)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201112DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Grass Group 17 (11)": MMRLocationData(
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
    # Termina Field Peahat Grotto Grass

    "Termina Field Peahat Grotto Grass Group 1 (1)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (2)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (3)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (4)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (5)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (6)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (7)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (8)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (9)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (10)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008D9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (11)": MMRLocationData(
        region="Termina Field",
        address=0x34694201008DA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Termina Field Peahat Grotto Grass Group 1 (12)": MMRLocationData(
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
        region="Termina Field",
        address=0x3469420124000,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Outside Archery Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420124001,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100400,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100401,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100402,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100403,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100404,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100405,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100406,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100407,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 0 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420100408,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (0)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101400,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101401,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (2)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101402,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (3)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101403,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (4)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101404,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (5)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101405,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (6)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101406,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (7)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101407,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grass Group 1 (8)": MMRLocationData(
        region="Termina Field",
        address=0x3469420101408,
        can_create=lambda options: options.grasssanity.value
    ),
    # Road To Southern Swamp Grotto
    "Road to Southern Swamp Grotto Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (2)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (3)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (4)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (5)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (6)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (7)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (8)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (9)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (10)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (11)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (12)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (13)": MMRLocationData(
        region="Termina Field",
        address=0x346942012AF4C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Road to Southern Swamp Grotto Grass (14)": MMRLocationData(
        region="Termina Field",
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
    "Southern Swamp Grass Group 0 (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100452,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100453,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100454,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100455,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100456,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100457,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100458,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420100459,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942010045A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 0 (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942010045B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102452,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102453,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102454,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102455,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102456,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102457,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 1 (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420102458,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942010450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103452,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103453,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103454,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103455,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103456,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420103457,
        can_create=lambda options: options.grasssanity.value
    ),
    "Southern Swamp Grass Group 2 (8)": MMRLocationData(
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

    "Woods of Mystery Grass (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126410,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126412,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126411,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126400,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126401,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126431,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126430,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126442,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126440,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126441,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126443,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126450,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126451,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (13)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126482,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (14)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126484,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (15)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126481,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (16)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126480,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (17)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126483,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (18)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126471,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Grass (19)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126470,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Unique Grass": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126420,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 3 Unique Grass (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126460,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 3 Unique Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420126461,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD48,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD49,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD4D,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (3)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD4B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (4)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD44,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (5)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (6)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD45,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (7)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD47,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (8)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD43,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (9)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (10)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD4A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (11)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (12)": MMRLocationData(
        region="Southern Swamp",
        address=0x346942012AD46,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woods of Mystery Day 2 Grotto Grass (13)": MMRLocationData(
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
    "Deku Palace Bean Grotto Grass Group 0 (0)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (1)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (2)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (3)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (4)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (5)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (6)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (7)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (8)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (9)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008C9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (10)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008CA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Deku Palace Bean Grotto Grass Group 0 (11)": MMRLocationData(
        region="Deku Palace",
        address=0x34694201008CB,
        can_create=lambda options: options.grasssanity.value
    ),

    # Woodfall Grass
    "Woodfall Grass (1)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124600,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Woodfall Grass (2)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124601,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Woodfall Grass (3)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124602,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Woodfall Grass (4)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124603,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Woodfall Grass (5)": MMRLocationData(
        region="Woodfall",
        address=0x3469420124604,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
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
        # can_create=lamda options: options.grasssanity.value
    ),
    "Milk Road Owl Grass (2)": MMRLocationData(
        region="Milk Road",
        address=0x3469420122201,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Milk Road Owl Grass (3)": MMRLocationData(
        region="Milk Road",
        address=0x3469420122202,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
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
        region="Gorman Brothers Track",
        address=0x34694201006A0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (2)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (3)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (4)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (5)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (6)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (7)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (8)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (9)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (10)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006A9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (11)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006AA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 1 (12)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201006AB,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (1)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (2)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (3)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (4)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (5)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (6)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (7)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (8)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (9)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (10)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016A9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (11)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016AA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Milk Road Gorman Racetrack Grass Group 2 (12)": MMRLocationData(
        region="Gorman Brothers Track",
        address=0x34694201016AB,
        can_create=lambda options: options.grasssanity.value
    ),
    # Romani Ranch Grass
    "Romani Ranch Grass Group 1 (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420100359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010035A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 1 (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010035B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420101359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010135A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 2 (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010135B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420102359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010235A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 3 (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010235B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (9)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103358,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (10)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420103359,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (11)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010335A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 4 (12)": MMRLocationData(
        region="Romani Ranch",
        address=0x346942010335B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104350,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104351,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104352,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (4)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104353,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (5)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104354,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (6)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104355,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (7)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104356,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (8)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420104357,
        can_create=lambda options: options.grasssanity.value
    ),
    "Romani Ranch Grass Group 5 (9)": MMRLocationData(
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
    "Goron Village Lens Cave Grass Group 1 (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100900,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (2)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100901,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (3)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100902,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (4)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100903,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (5)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100904,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (6)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100905,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (7)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100906,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (8)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100907,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (9)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100908,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (10)": MMRLocationData(
        region="Goron Village",
        address=0x3469420100909,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (11)": MMRLocationData(
        region="Goron Village",
        address=0x346942010090A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 1 (12)": MMRLocationData(
        region="Goron Village",
        address=0x346942010090B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101900,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (2)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101901,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (3)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101902,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (4)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101903,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (5)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101904,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (6)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101905,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (7)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101906,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (8)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101907,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (9)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101908,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (10)": MMRLocationData(
        region="Goron Village",
        address=0x3469420101909,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (11)": MMRLocationData(
        region="Goron Village",
        address=0x346942010190A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Goron Village Lens Cave Grass Group 2 (12)": MMRLocationData(
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
    "Mountain Village Springtime Keaton Grass (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (3)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (5)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (6)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A05,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (7)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A06,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (8)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A07,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Keaton Grass (9)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A08,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (4)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (5)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (6)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A05,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (7)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A06,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (8)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A07,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (9)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A08,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (10)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A09,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (11)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A0A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (12)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A0B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (13)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A0C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (14)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A0D,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (15)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A0E,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (16)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A0F,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (17)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A10,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (18)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A11,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (19)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A12,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (20)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A13,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (21)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A14,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (22)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A15,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (23)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A16,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (24)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A17,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (25)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A18,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (26)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A19,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (27)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A1A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (28)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A1B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (29)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A1C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Mountain Village Springtime Grass (30)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420125A1D,
        can_create=lambda options: options.grasssanity.value
    ),

    # Mountain Village Keaton Grass (These ID's aren't shared anywhere else, must be fine?)

    "Mountain Village Keaton Grass (28)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A1B,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (29)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A1C,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (30)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A1D,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (31)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A1E,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (32)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A1F,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (33)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A20,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (34)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A21,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (35)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A22,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),
    "Mountain Village Keaton Grass (36)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420135A23,
        can_create=lambda options: options.grasssanity.value
        # can_create=lamda options: options.grasssanity.value
    ),

    # Mountain Village Spring Grotto Grass (also not shared anywhere, must also be okay? Testing req.)

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
    # Great Bay Coast Grass

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

    "Zora Cape Grotto Grass (0)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A641,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (1)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A642,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (2)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A643,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (3)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A644,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (4)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A645,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (5)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A646,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (6)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A647,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (7)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A648,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (8)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A649,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (9)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A64A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (10)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A64B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (11)": MMRLocationData(
        region="Zora Cape",
        address=0x346942012A64C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Zora Cape Grotto Grass (12)": MMRLocationData(
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
        address=0x3469420124310,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124311,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124312,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124313,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124314,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124315,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (7)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124316,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (8)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124317,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Graveyard Upper Grass (9)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420124318,
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
        region="Ikana Canyon",
        address=0x3469420121300,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grass (2)": MMRLocationData(
        region="Ikana Canyon",
        address=0x3469420121301,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grass (3)": MMRLocationData(
        region="Ikana Canyon",
        address=0x3469420121302,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grass (4)": MMRLocationData(
        region="Ikana Canyon",
        address=0x3469420121303,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Canyon Grotto Grass

    "Ikana Canyon Grotto Grass (1)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A540,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (2)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A541,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (3)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A542,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (4)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A543,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (5)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A544,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (6)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A545,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (7)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A546,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (8)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A547,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (9)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A548,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (10)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A549,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (11)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A54A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (12)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A54B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (13)": MMRLocationData(
        region="Ikana Canyon",
        address=0x346942012A54C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Ikana Canyon Grotto Grass (14)": MMRLocationData(
        region="Ikana Canyon",
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
    "Secret Shrine Dinolfos Grass (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126020,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Dinolfos Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126021,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Dinolfos Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126022,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Dinolfos Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126023,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126033,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126032,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126030,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126031,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wizzrobe Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126034,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126042,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126043,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126045,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126044,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126047,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126046,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (6)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126040,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Wart Grass (7)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126041,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126055,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126052,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126051,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126050,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126054,
        can_create=lambda options: options.grasssanity.value
    ),
    "Secret Shrine Garo Master Grass (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420126053,
        can_create=lambda options: options.grasssanity.value
    ),

    # Beneath the Well Grass

    "Beneath the Well Left Side Back Room Grass (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B51,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Left Side Back Room Grasss (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B50,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B30,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B31,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B32,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Before Big Poe and Cow Grass (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B33,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Cow Grass (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B92,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Cow Grass (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B91,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Cow Grass (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B90,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B71,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (1)": MMRLocationData(
        region="Termina Field",
        address=0x3469420124B72,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B74,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B73,
        can_create=lambda options: options.grasssanity.value
    ),
    "Beneath the Well Right Side Back Room Grass (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420124B70,
        can_create=lambda options: options.grasssanity.value
    ),

    # Ikana Castle Grass

    "Ikana Castle Grass (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D00,
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
    "Ikana Castle Grass (12)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420121D0B,
        can_create=lambda options: options.grasssanity.value
    ),

    # Dungeon Grass
    # Woodfall Temple

    "Woodfall Temple Entrance Room Grass (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B24,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Entrance Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B21,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Entrance Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B20,
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
    "Woodfall Temple Main Room Grass (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B11,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Main Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B10,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Main Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B12,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Deku Elevator Room Grass (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B50,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Deku Elevator Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B51,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B61,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B64,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B63,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B62,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Snapping Turtle Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B60,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Dragonfly Chest Room Grass (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B40,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Dragonfly Chest Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B41,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Dragonfly Chest Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B42,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA1,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA3,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple2F Moving Flower Platform Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA5,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA4,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA9,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA7,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (6)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA0,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (7)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA2,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (8)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BAA,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (9)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA8,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple 2F Moving Flower Platform Room Grass (10)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121BA6,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Pre Boss Room Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121B03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F0E,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F0C,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F0B,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F09,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F07,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F05,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (6)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F03,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (7)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F01,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (8)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F00,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (9)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F02,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (10)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F04,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (11)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F06,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (12)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F08,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair Grass (13)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F0A,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair (14)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F0D,
        can_create=lambda options: options.grasssanity.value
    ),
    "Woodfall Temple Odolwas Lair (15)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420121F0F,
        can_create=lambda options: options.grasssanity.value
    ),
        # Snowhead Temple Grass
    "Snowhead Temple Basement Grass (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122149,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122147,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122148,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122142,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122145,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122146,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122141,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122144,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (8)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122143,
        can_create=lambda options: options.grasssanity.value
    ),
    "Snowhead Temple Basement Grass (9)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420122140,
        can_create=lambda options: options.grasssanity.value
    ),
        # Stone Tower Temple Grass

    "Stone Tower Temple Entrance Room Grass (0)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121600,
        can_create=lambda options: options.grasssanity.value
    ),

    "Stone Tower Temple Entrance Room Grass (1)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121601,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Entrance Room Grass (2)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121602,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (0)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121623,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (1)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121621,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (2)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121624,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (3)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121620,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (4)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121622,
        can_create=lambda options: options.grasssanity.value
    ),
    "Stone Tower Temple Elegy Maze Grass (5)":MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420121625,
        can_create=lambda options: options.grasssanity.value
    ),
      # Clock Town Pots
    "Sword School Night 3 Midnight Pots (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205403,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205402,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205404,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205401,
        can_create=lambda options: options.potsanity.value
    ),
    "Sword School Night 3 Midnight Pots (4)": MMRLocationData(
        region="Clock Town",
        address=0x3469420205400,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202901,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202900,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (2)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202902,
        can_create=lambda options: options.potsanity.value
    ),
    "Bombers Hideout Pots (3)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202903,
        can_create=lambda options: options.potsanity.value
    ),
    "Astral Observatory Pots (0)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202911,
        can_create=lambda options: options.potsanity.value
    ),
    "Astral Observatory Pots (1)": MMRLocationData(
        region="Clock Town",
        address=0x3469420202910,
        can_create=lambda options: options.potsanity.value
    ),
    "Astral Observatory Pots (2)": MMRLocationData(
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
    
    "Road To Southern Swamp Outside Archery Pots (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694202040F1,
        can_create=lambda options: options.potsanity.value
    ),
    "Road To Southern Swamp Outside Archery Pots (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x34694202040F0,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Beneath Witch Shop Pots (0)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420204522,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Beneath Witch Shop Pots (1)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420204521,
        can_create=lambda options: options.potsanity.value
    ),
    "Southern Swamp Beneath Witch Shop Pots (2)": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420204520,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Swamp Spider House Pots
    
    "Swamp Spider House Main Room Pots (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202712,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202713,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202714,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202711,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202710,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202715,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (6)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202716,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Main Room Pots (6)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202717,
        can_create=lambda options: options.potsanity.value
    ),    
    "Swamp Spider House Tablet Room Pots (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202730,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Tablet Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202731,
        can_create=lambda options: options.potsanity.value
    ),        

    "Swamp Spider House Giant Jar Room Pots (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202740,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202741,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202742,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202743,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202744,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202745,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (6)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202746,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Giant Jar Room Pots (7)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202747,
        can_create=lambda options: options.potsanity.value
    ),    
    "Swamp Spider House Gold Room Pots (0)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202722,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (1)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202725,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (2)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202723,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (3)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202721,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (4)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202720,
        can_create=lambda options: options.potsanity.value
    ),
    "Swamp Spider House Gold Room Pots (5)": MMRLocationData(
        region="Swamp Spider House",
        address=0x3469420202724,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Deku Palace Pots
    "Deku Palace Right Side Upper Pots (0)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420202B10,
        can_create=lambda options: options.potsanity.value
    ),
    "Deku Palace Right Side Upper Pots (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420202B11,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Butler Race Pots
    
    "Deku Butler Race Pots (0)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420205200,
        can_create=lambda options: options.potsanity.value
    ),
    "Deku Butler Race Pots (1)": MMRLocationData(
        region="Deku Palace",
        address=0x3469420205201,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Woodfall Pots
    
    "Woodfall Owl Pots (0)": MMRLocationData(
        region="Woodfall",
        address=0x3469420204601,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Owl Pots (1)": MMRLocationData(
        region="Woodfall",
        address=0x3469420204600,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Owl Pots (2)": MMRLocationData(
        region="Woodfall",
        address=0x3469420204602,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Woodfall Temple Pots
    
    "Woodfall Temple Entrance Pot": MMRLocationData(
        region="Woodfall",
        address=0x3469420201B20,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B15,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B18,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B16,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B17,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (4)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B12,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (5)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B10,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (6)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B11,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (7)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B14,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Main Room Pots (8)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B13,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B51,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B50,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B53,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Deku Elevator Pots (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B52,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Frog Boss Pots (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B83,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Frog Boss Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B82,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Frog Boss Pots (2)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B81,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Frog Boss Pots (3)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B80,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Left Side Bridge Pots (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B30,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Left Side Bridge Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B31,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Pre Boss Pots (0)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B01,
        can_create=lambda options: options.potsanity.value
    ),
    "Woodfall Temple Pre Boss Pots (1)": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420201B00,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Mountain Village Pots
    
    "Mountain Village Pots (0)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205000,
        can_create=lambda options: options.potsanity.value
    ),
    "Mountain Village Pots (1)": MMRLocationData(
        region="Mountain Village",
        address=0x34694202050F1,
        can_create=lambda options: options.potsanity.value
    ),
    "Mountain Village Pots (2)": MMRLocationData(
        region="Mountain Village",
        address=0x34694202050F0,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Goron Racetrack Pots
    
    "Goron Racetrack Pots (0)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B14,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B15,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (2)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B17,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (3)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B16,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (4)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B12,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (5)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B10,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (6)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B13,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (7)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B0F,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (8)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B11,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (9)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B00,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (10)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B02,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (11)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B05,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (12)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B04,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (13)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B03,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (14)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B07,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (15)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B06,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (16)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B09,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (17)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B08,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (18)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B0A,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (19)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B01,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (20)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B0E,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (21)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B18,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (22)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B19,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (23)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B1A,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (24)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B1D,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (25)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B1B,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (26)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B1C,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (27)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B0D,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (28)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B0C,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Racetrack Pots (29)": MMRLocationData(
        region="Goron Village",
        address=0x3469420206B0B,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Goron Shrine Pots
    
    "Goron Shrine Pots (0)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203204,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (1)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203203,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (2)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203207,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (3)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203202,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (4)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203200,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (5)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203205,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (6)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203201,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (7)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203206,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (8)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203210,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (9)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203211,
        can_create=lambda options: options.potsanity.value
    ),
    "Goron Shrine Pots (10)": MMRLocationData(
        region="Goron Village",
        address=0x3469420203212,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Snowhead Temple Pots
    "Snowhead Temple Entrance Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202100,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Entrance Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202101,
        can_create=lambda options: options.potsanity.value
    ),

    "Snowhead Temple Blue Door Lava Bridge Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202123,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202125,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202124,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202126,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202122,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202120,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Blue Door Lava Bridge Pots (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202121,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Pots Basement (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202146,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Pots Basement (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202147,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Scarecrow Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202140,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Scarecrow Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202141,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020215B,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020215C,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020215A,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202157,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202158,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202159,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202156,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202153,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (8)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202151,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (9)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202155,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (10)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202154,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (11)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202150,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Frozen Green Door Pots (12)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202152,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Orange Door Push Block Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202131,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Orange Door Push Block Pots (1)": MMRLocationData(
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
    "Snowhead Temple Locked Grey Door Wolfos Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202112,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202113,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202110,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202114,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Locked Grey Door Wolfos Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202111,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Goron Pound Puzzle Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202181,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Goron Pound Puzzle Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202180,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Pots 2nd Floor Bridge (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202144,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room Pots 2nd Floor Bridge (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202145,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room 4th Floor Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202143,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple Main Room 4th Floor Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420202142,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C2,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C4,
        can_create=lambda options: options.potsanity.value
    ),
    "Snowhead Temple 4th Floor Wizzrobe Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x34694202021C3,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (0)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020440C,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (1)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020440D,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (2)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204408,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (3)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204400,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (4)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204402,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (5)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204409,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (6)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204407,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (7)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204406,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (8)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020440A,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (9)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204401,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (10)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204403,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (11)": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942020440B,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (12)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204404,
        can_create=lambda options: options.potsanity.value
    ),
    "Goht Boss Room Pots (13)": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420204405,
        can_create=lambda options: options.potsanity.value
    ),
    
    "Mountain Village Springtime Pots (0)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205AF0,
        can_create=lambda options: options.potsanity.value
    ),         
    "Mountain Village Springtime Pots (1)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205AF1   ,
        can_create=lambda options: options.potsanity.value
    ),   
    "Mountain Village Springtime Pots (2)": MMRLocationData(
        region="Mountain Village",
        address=0x3469420205A00,
        can_create=lambda options: options.potsanity.value
    ),   


    # Romani Ranch Pots
    
    "Romani Ranch Baby Chickens Pots (0)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202042F0,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Baby Chickens Pots (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x34694202042F1,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (0)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204102,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (1)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204101,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (2)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204100,
        can_create=lambda options: options.potsanity.value
    ),
    "Romani Ranch Doggy Racetrack Pots (3)": MMRLocationData(
        region="Romani Ranch",
        address=0x3469420204103,
        can_create=lambda options: options.potsanity.value
    ),
    # Great Bay Coast Pots
    
    "Great Bay Coast Behind Marine Lab Pots (0)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203707,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Behind Marine Lab Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203709,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Behind Marine Lab Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203708,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Behind Marine Lab Pots (3)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370E,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Rock Pools Pots (0)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203704,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Rock Pools Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370B,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (0)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370D,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203706,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203705,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Lower Rock Wall Pots (3)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370C,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Upper Rock Wall Pots (0)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203702,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Upper Rock Wall Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203701,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Upper Rock Wall Pots (2)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203700,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Beside Pirates Fortress Pots (0)": MMRLocationData(
        region="Great Bay",
        address=0x3469420203703,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Coast Beside Pirates Fortress Pots (1)": MMRLocationData(
        region="Great Bay",
        address=0x346942020370A,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Ocean Spiderhouse Pots
    
    "Ocean Spiderhouse Bottom Of Ramp Pots (0)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202803,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Bottom Of Ramp Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202800,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Bottom Of Ramp Pots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202801,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Bottom Of Ramp Pots (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202802,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (0)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202813,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202814,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202810,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202811,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Main Room Lower Pots (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202812,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (0)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202857,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202851,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (2)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202856,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (3)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202855,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (4)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202850,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (5)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202854,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (6)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202852,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Crate Room Pots (7)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202853,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Coloured Skulls Room Pots (0)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202831,
        can_create=lambda options: options.potsanity.value
    ),
    "Ocean Spiderhouse Coloured Skulls Room Pots (1)": MMRLocationData(
        region="Ocean Spider House",
        address=0x3469420202830,
        can_create=lambda options: options.potsanity.value
    ),

    # Pirates' Fortress Pots
    
    "Pirates Fortress Sewers Cage Room Pots (0)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x34694202023B0,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Cage Room Pots (1)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x34694202023B1,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers After Gate Hidden Ladder Pots (0)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x34694202023A1,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers After Gate Hidden Ladder Pots (1)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x34694202023A0,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Exit Pots (0)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202391,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Exit Pots (1)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202390,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Sewers Exit Pots (2)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202392,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Underwater Chest Room Pots (0)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202360,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Underwater Chest Room Pots (1)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202361,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Underwater Chest Room Pots (2)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202362,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Green Guard Pots (0)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420000E80,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Green Guard Pots (1)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202382,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Green Guard Pots (2)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202380,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Upper Beehive Room Pots (0)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202331,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Upper Beehive Room Pots (1)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x3469420202330,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Pink Guard Pots (0)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x34694202023D1,
        can_create=lambda options: options.potsanity.value
    ),
    "Pirates Fortress Interior Room Past Pink Guard Pots (1)": MMRLocationData(
        region="Pirates' Fortress",
        address=0x34694202023D0,
        can_create=lambda options: options.potsanity.value
    ),

    # Pinnacle Rock
    
    "Pinnacle Rock Pots (0)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202505,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (1)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202504,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (2)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202503,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (3)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202502,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (4)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202500,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (5)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x346942020250A,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (6)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202509,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (7)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202508,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (8)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202501,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (9)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202507,
        can_create=lambda options: options.potsanity.value
    ),
    "Pinnacle Rock Pots (10)": MMRLocationData(
        region="Pinnacle Rock",
        address=0x3469420202506,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Zora Cape Pots
    
    "Zora Cape Like Like Pool Pots (0)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203800,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Like Like Pool Pots (1)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203801,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (0)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203803,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (1)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203802,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (2)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203805,
        can_create=lambda options: options.potsanity.value
    ),
    "Zora Cape Owl Pots (3)": MMRLocationData(
        region="Zora Cape",
        address=0x3469420203804,
        can_create=lambda options: options.potsanity.value
    ),

    # Great Bay Temple Pots
    
    "Great Bay Temple Above Whirlpool Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204901,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Above Whirlpool Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204900,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C3,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Room Behind 1F Waterfall (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049C1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204910,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204911,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942020491B,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942020491A,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204913,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204915,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204916,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204917,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204914,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (9)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204912,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (10)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204918,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Green Pipe Tunnel Room Pots (11)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204919,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204945,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204940,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204946,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204941,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204943,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204944,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204942,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Caged Chest Room Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204947,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204963,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204962,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204961,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Red Valve Underwater Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204960,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E3,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049EA,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E8,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E5,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E4,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E6,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (8)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E7,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (9)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (10)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049EB,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Behind Locked Door Pots (11)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049E9,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204972,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204970,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204976,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204971,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204977,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204974,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204975,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Floating Eye Miniboss Room Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204973,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204996,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204997,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204990,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204991,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204994,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204995,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204993,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Green Pipe Frozen Waterwheel Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420204992,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Seesaw Room Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049A2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Seesaw Room Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049A0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Seesaw Room Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049A1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B5,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B3,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B1,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B7,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B6,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B0,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B4,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Pots Underneath Boss Door Platform (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x34694202049B2,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (0)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F07,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (1)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F06,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (2)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F05,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (3)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F04,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (4)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F00,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (5)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F03,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (6)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F02,
        can_create=lambda options: options.potsanity.value
    ),
    "Great Bay Temple Gyorg Pots (7)": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420205F01,
        can_create=lambda options: options.potsanity.value
    ),

    # Ikana Graveyard Pots
    
    "Road To Ikana Scarecrow Pillar Pot": MMRLocationData(
        region="Road to Ikana",
        address=0x3469420205300,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C01,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C00,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C10,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C11,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 1 Grave Pots (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C12,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Entrance Grave Pot": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C02,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Entryway Pots (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C32,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Entryway Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C33,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C30,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C31,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C35,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 2 Invisible Path Pots (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420200C34,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (0)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203001,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (1)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203003,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (2)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203005,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (3)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203002,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (4)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203000,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (5)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203004,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (6)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203009,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (7)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203007,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (8)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203006,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Graveyard Day 3 Pots (9)": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420203008,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Secret Shrine Pots
    
    "Secret Shrine Entrance Pots (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206001,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Entrance Pots (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206002,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Entrance Pots (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206000,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (0)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206015,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (1)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206014,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (2)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206013,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (3)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206012,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (4)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206010,
        can_create=lambda options: options.potsanity.value
    ),
    "Secret Shrine Underwater Pots (5)": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420206011,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Ikana Castle
    
    "Ikana Castle Frozen Eyes Room Pots (0)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D11,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Frozen Eyes Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D10,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Pots (0)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D20,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Falling Ceiling Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D21,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (0)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D42,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D41,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D40,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Broken Floor Room Pots (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D43,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Staircase Pots (0)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D60,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Left Side Staircase Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D61,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Right Side Staircase Pots (0)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D71,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Right Side Staircase Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420201D70,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (0)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205601,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (1)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205600,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (2)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205603,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (3)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205602,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (4)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205611,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (5)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205612,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (6)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205613,
        can_create=lambda options: options.potsanity.value
    ),
    "Ikana Castle Throne Room Pots (7)": MMRLocationData(
        region="Ikana Castle",
        address=0x3469420205610,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Well Pots
    
    "Well Left Side Back Room Pots (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B52,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B50,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B54,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B51,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Left Side Back Room Pots (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B53,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B69,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B68,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B67,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B66,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (4)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B65,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (5)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B64,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (6)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B63,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (7)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B62,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (8)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B61,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Right Side Before Chest Room Pots (9)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204B60,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (0)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC2,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (1)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC3,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (2)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC1,
        can_create=lambda options: options.potsanity.value
    ),
    "Well Big Poe Pots (3)": MMRLocationData(
        region="Beneath the Well",
        address=0x3469420204BC0,
        can_create=lambda options: options.potsanity.value
    ),

    # Stone Tower Pots
    
    "Stone Tower Lower Scarecrow Pots (0)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205805,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205814,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205808,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205807,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (4)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205804,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (5)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205806,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (6)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205802,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (7)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205801,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (8)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205803,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (9)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205800,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (10)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205809,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Lower Scarecrow Pots (11)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580A,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (0)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205812,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205813,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205811,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580F,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (4)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205810,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (5)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580E,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (6)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580C,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (7)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580D,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Upper Scarecrow Pots (8)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020580B,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (0)": MMRLocationData(
        region="Stone Tower",
        address=0x346942020581A,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205817,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205818,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Owl Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205819,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Stone Tower Temple Pots
    
    "Stone Tower Temple Entrance Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201601,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Entrance Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201600,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201645,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201642,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201644,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201643,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201646,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201641,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (6)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201640,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Basement Armos Pots (7)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201647,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Near Locked Door Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201635,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Near Locked Door Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201636,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201633,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201634,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201632,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201630,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Right Side Underwater Pots (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201631,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Mirror Room Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201671,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Mirror Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201670,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201693,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201690,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201692,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Deku Updraft Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201691,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201680,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (1)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201681,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (2)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201682,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (3)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201686,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (4)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201683,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (5)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201687,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (6)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201685,
        can_create=lambda options: options.potsanity.value
    ),
    "Stone Tower Temple Lower Spike Roller Pots (7)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201684,
        can_create=lambda options: options.potsanity.value
    ),
    
    # Inverted Stone Tower Temple Pots
    
    "Inverted Stone Tower Bean Pots (0)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205903,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (1)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205904,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (2)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205900,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (3)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205901,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Bean Pots (4)": MMRLocationData(
        region="Stone Tower",
        address=0x3469420205902,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (0)": MMRLocationData(
        region="Stone Tower Temple",
        address=0x3469420201832,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201833,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201835,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201834,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201831,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Updraft Pots (5)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201830,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Miniboss Pots (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B3,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Miniboss Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B0,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Miniboss Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B1,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Miniboss Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x34694202018B2,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Lower Bridge Room Pots (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201811,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Lower Bridge Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201810,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201822,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201820,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201821,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Small Poe Room Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201823,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201840,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201843,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201844,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201841,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Wizzrobe Room Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201842,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942020188A,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x346942020188B,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201889,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (Flying) (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201888,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (0)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201883,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (1)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201881,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (2)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201885,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (3)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201887,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (4)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201884,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (5)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201886,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (6)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201880,
        can_create=lambda options: options.potsanity.value
    ),
    "Inverted Stone Tower Temple Pre Boss Pots (7)": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420201882,
        can_create=lambda options: options.potsanity.value
    ),

    
    # Moon Trial Pots
    
    "Moon Goron Trial Pots (0)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F08,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F07,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (2)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F09,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (3)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0A,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (4)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F00,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (5)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F01,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (6)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F04,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (7)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F02,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (8)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F03,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (9)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0E,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (10)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0C,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (11)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0B,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (12)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F0D,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (13)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F06,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Goron Trial Pots (14)": MMRLocationData(
        region="The Moon",
        address=0x3469420203F05,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (0)": MMRLocationData(
        region="The Moon",
        address=0x3469420206602,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420206603,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (2)": MMRLocationData(
        region="The Moon",
        address=0x3469420206601,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (3)": MMRLocationData(
        region="The Moon",
        address=0x3469420206600,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (4)": MMRLocationData(
        region="The Moon",
        address=0x3469420206606,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (5)": MMRLocationData(
        region="The Moon",
        address=0x3469420206604,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (6)": MMRLocationData(
        region="The Moon",
        address=0x3469420206605,
        can_create=lambda options: options.potsanity.value
    ),
    "Moon Link Trial Pots (7)": MMRLocationData(
        region="The Moon",
        address=0x3469420206607,
        can_create=lambda options: options.potsanity.value
    ),
    "Majora Arena Pots (0)": MMRLocationData(
        region="The Moon",
        address=0x3469420200B00,
        can_create=lambda options: options.potsanity.value
    ),
    "Majora Arena Pots (1)": MMRLocationData(
        region="The Moon",
        address=0x3469420200B01,
        can_create=lambda options: options.potsanity.value
    ),

}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
