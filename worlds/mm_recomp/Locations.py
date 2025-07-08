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
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Curiosity Shop Red Rupee Trade": MMRLocationData(
        region="Clock Town",
        address=0x346942007C404,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Curiosity Shop Purple Rupee Trade": MMRLocationData(
        region="Clock Town",
        address=0x346942007C405,
        can_create=lambda options: options.shopsanity.value == 2
    ),
    "Curiosity Shop Gold Rupee Trade": MMRLocationData(
        region="Clock Town",
        address=0x346942007C407,
        can_create=lambda options: options.shopsanity.value == 2
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
    "Stock Pot Inn Upstairs Middle Room Chest": MMRLocationData(
        region="Clock Town",
        address=0x3469420066100
    ),
    "Stock Pot Inn Employees Only Room Night 3 Chest": MMRLocationData(
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
    "Termina Tall Grass Chest": MMRLocationData(
        region="Termina Field",
        address=0x3469420062D01
    ),
    "Termina Underwater Chest": MMRLocationData(
        region="Termina Field",
        address=0x3469420062D00
    ),
    "Termina Tall Grass Grotto Chest": MMRLocationData(
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
    "Termina Northern Midnight Dancer": MMRLocationData(
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
    "Termina Moon's Tear Scrub HP": MMRLocationData(
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
    "Southern Swamp Deku Scrub Purchase Beans": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420090135,
        can_create=lambda options: options.scrubsanity.value
    ),
    "Southern Swamp Deku Trade Freestanding HP": MMRLocationData(
        region="Southern Swamp",
        address=0x346942005451E
    ),
    "Southern Swamp Healthy Witch Request": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420000059
    ),
    "Southern Swamp Mystery Woods Day 2 Grotto Chest": MMRLocationData(
        region="Southern Swamp",
        address=0x346942006071C
    ),
    "Southern Swamp Tour Witch Gift": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420000043
    ),
    "Southern Swamp Tour Guide Winning Picture": MMRLocationData(
        region="Southern Swamp",
        address=0x34694200701C5
    ),
    "Southern Swamp Tour Guide Good Picture": MMRLocationData(
        region="Southern Swamp",
        address=0x3469420071C54
    ),
    "Southern Swamp Tour Guide Okay Picture": MMRLocationData(
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
    "Southern Swamp Near Swamp Spider House Grotto Chest": MMRLocationData(
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
    "Woodfall Near Owl Statue Chest": MMRLocationData(
        region="Woodfall",
        address=0x3469420064602
    ),
    "Woodfall After Great Fairy Cave Chest": MMRLocationData(
        region="Woodfall",
        address=0x3469420064601
    ),
    "Woodfall Near Swamp Entrance Chest": MMRLocationData(
        region="Woodfall",
        address=0x3469420064600
    ),
    "Woodfall Great Fairy Reward": MMRLocationData(
        region="Woodfall",
        address=0x3469420030001
    ),
    "Woodfall Temple Entrance Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B18
    ),
    "Woodfall Temple Moving Flower Platform Room Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B01
    ),
    "Woodfall Temple Gagwab Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1D
    ),
    "Woodfall Temple Dragonfly Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1C
    ),
    "Woodfall Temple Black Boe Room Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B19
    ),
    "Woodfall Temple Wooden Flower Switch Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B17
    ),
    "Woodfall Temple Dinolfos Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1B
    ),
    "Woodfall Temple Boss Key Chest": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420061B1E
    ),
    "Woodfall Temple Entrance Freestanding SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2B
    ),
    "Woodfall Temple Wooden Flower Deku Baba SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2E
    ),
    "Woodfall Temple Wooden Flower Pot SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B1C
    ),
    "Woodfall Temple Moving Flower Platform Room Beehive SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B1E
    ),
    "Woodfall Temple Wooden Flower Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B30
    ),
    "Woodfall Temple Push Block Skulltula SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B31
    ),
    "Woodfall Temple Push Block Bubble SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2F
    ),
    "Woodfall Temple Push Block Beehive SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B1D
    ),
    "Woodfall Temple Final Room Right Lower Platform SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2A
    ),
    "Woodfall Temple Final Room Right Upper Platform SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B32
    ),
    "Woodfall Temple Final Room Left Upper Platform SF": MMRLocationData(
        region="Woodfall Temple",
        address=0x3469420011B2C
    ),
    "Woodfall Temple Final Room Bubble SF": MMRLocationData(
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
    "Tour Witch Target Shooting": MMRLocationData(
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
    "Mountain Village Invisible Ladder Cave Healing Invisible Goron": MMRLocationData(
        region="Mountain Village",
        address=0x3469420000079
    ),
    "Mountain Village Feeding Freezing Goron": MMRLocationData(
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
    "Don Gero Mask Frog Song HP": MMRLocationData(
        region="Mountain Village",
        address=0x3469420070022
    ),
    "Twin Islands Spring Underwater Cave Chest": MMRLocationData(
        region="Twin Islands",
        address=0x3469420065E00
    ),
    "Twin Islands Spring Underwater Near Ramp Chest": MMRLocationData(
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
    "Goron Village Deku Scrub Purchase Bomb Bag": MMRLocationData(
        region="Goron Village",
        address=0x346942009011D,
        can_create=lambda options: options.scrubsanity.value
    ),
    "Goron Village Deku Trade": MMRLocationData(
        region="Goron Village",
        address=0x3469420000099
    ),
    "Goron Village Deku Trade Freestanding HP": MMRLocationData(
        region="Goron Village",
        address=0x3469420054D1E
    ),
    # "Goron Village Deku Trade Freestanding HP (Spring)": MMRLocationData(
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
    "Snowhead Temple Elevator Room Invisible Platform Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062113
    ),
    "Snowhead Temple 1st Wizzrobe Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211B
    ),
    "Snowhead Temple Initial Runway Under Platform Bubble SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942001212F
    ),
    "Snowhead Temple Initial Runway Tower Bubble SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420012130
    ),
    "Snowhead Temple Elevator Freestanding SF": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420012132
    ),
    "Snowhead Temple Grey Door Near Bombable Stairs Box SF": MMRLocationData(
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
    "Snowhead Temple Initial Runway Ice Blowers Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062101
    ),
    "Snowhead Temple Elevator Room Lower Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211D
    ),
    "Snowhead Temple Bottom Floor Switch Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062114
    ),
    "Snowhead Temple Green Door Ice Blowers Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062118
    ),
    "Snowhead Temple Orange Door Behind Block Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062103
    ),
    "Snowhead Temple Orange Door Upper Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062115
    ),
    "Snowhead Temple Light Blue Door Center Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211C
    ),
    "Snowhead Temple Light Blue Door Upper Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062119
    ),
    "Snowhead Temple Upstairs 2F Icicle Room Hidden Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062116
    ),
    "Snowhead Temple Upstairs 2F Icicle Room Snowball Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x3469420062104
    ),
    "Snowhead Temple 2nd Wizzrobe Chest": MMRLocationData(
        region="Snowhead Temple",
        address=0x346942006211E
    ),
    "Snowhead Temple Column Room 2F Hidden Chest": MMRLocationData(
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
    "Romani Ranch Bremen Mask March Baby Cuccos": MMRLocationData(
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
    "Romani Ranch Defended Against Aliens": MMRLocationData(
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
    "Great Bay Behind Fishermans Hut Grotto Chest": MMRLocationData(
        region="Great Bay",
        address=0x3469420060717
    ),
    "Great Bay Marine Research Lab Zora Egg Delivery Song": MMRLocationData(
        region="Great Bay",
        address=0x34694200000AC
    ),
    "Great Bay Marine Research Lab Feeding Fish": MMRLocationData(
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
    "Great Bay (Cleared) Fisherman Island Game HP": MMRLocationData(
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
    "Zora Cape Pot Game Silver Rupee": MMRLocationData(
        region="Zora Cape",
        address=0x3469420072806
    ),
    "Zora Cape Upper Chest": MMRLocationData(
        region="Zora Cape",
        address=0x3469420063801
    ),
    "Zora Cape Tree Chest": MMRLocationData(
        region="Zora Cape",
        address=0x3469420063802
    ),
    "Zora Cape Near Great Fairy Grotto Chest": MMRLocationData(
        region="Zora Cape",
        address=0x3469420060715
    ),
    "Beaver Bros. Race Bottle Reward": MMRLocationData(
        region="Zora Cape",
        address=0x346942009018D
    ),
    "Beaver Bros. Race HP": MMRLocationData(
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
    "Zora Hall Deku Scrub Purchase Green Potion": MMRLocationData(
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
    "Zora Hall Piano Zora Song": MMRLocationData(
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
    "Pirates' Fortress Sewers Push Block Maze Chest": MMRLocationData(
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
        region="Pirates' Fortress Sewers",
        address=0x3469420063B00
    ),
    "Pirates' Fortress Exterior Underwater Near Entrance Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420063B01
    ),
    "Pirates' Fortress Exterior Underwater Corner Near Fortress Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420063B02
    ),
    "Pirates' Fortress Near Egg Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420062300
    ),
    "Pirates' Fortress Pirates Surrounding Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420062303
    ),
    "Pirates' Fortress Hub Lower Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420061400
    ),
    "Pirates' Fortress Hub Upper Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
        address=0x3469420061401
    ),
    "Pirates' Fortress Leader's Room Chest": MMRLocationData(
        region="Pirates' Fortress Sewers",
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
    "Pinnacle Rock HP": MMRLocationData(
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
    "Ocean Spider House Dining Room Chandelier #3 Token ": MMRLocationData(
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
    "Great Bay Temple Pot At Bottom Of Blender SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491B
    ),
    "Great Bay Temple Waterwheel Room Skulltula SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420014932
    ),
    "Great Bay Temple Waterwheel Room Bubble Under Platform SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420014930
    ),
    "Great Bay Temple Blender Room Barrel SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491C
    ),
    "Great Bay Temple Red-Green Pipe First Room Pot SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491E
    ),
    "Great Bay Temple Froggy Entrance Room Pot SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491D
    ),
    "Great Bay Temple Seesaw Room Underwater Barrel SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942001491A
    ),
    "Great Bay Temple Four Torches Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064918
    ),
    "Great Bay Temple Behind Locked Door Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491B
    ),
    "Great Bay Temple Red-Green Pipe First Room Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491D
    ),
    "Great Bay Temple Bio-Baba Hall Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064919
    ),
    "Great Bay Temple Froggy Entrance Room Upper Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491C
    ),
    "Great Bay Temple Froggy Entrance Room Underwater Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064901
    ),
    "Great Bay Temple Froggy Entrance Room Caged Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x346942006491E
    ),
    "Great Bay Temple Room Behind Waterfall Ceiling Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064915
    ),
    "Great Bay Temple Green Pipe Freezable Waterwheel Upper Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064914
    ),
    "Great Bay Temple Green Pipe Freezable Waterwheel Lower Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064917
    ),
    "Great Bay Temple Seesaw Room Chest": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420064916
    ),
    "Great Bay Temple Before Boss Room Underneath Platform Bubble SF": MMRLocationData(
        region="Great Bay Temple",
        address=0x3469420014931
    ),
    "Great Bay Temple Before Boss Room Exit Tunnel Bubble SF": MMRLocationData(
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
    "Graveyard Sonata To Wake Sleeping Skeleton Chest": MMRLocationData(
        region="Ikana Graveyard",
        address=0x3469420064300
    ),
    "Secret Shrine Left Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066000
    ),
    "Secret Shrine Middle-Left Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066001
    ),
    "Secret Shrine Middle-Right Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066002
    ),
    "Secret Shrine Right Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x3469420066003
    ),
    "Secret Shrine Center Chest": MMRLocationData(
        region="Secret Shrine",
        address=0x346942006600A
    ),
    "Ikana Canyon Grotto Chest": MMRLocationData(
        region="Ikana Canyon",
        address=0x3469420060714
    ),
    "Ikana Canyon Deku Scrub Purchase Blue Potion": MMRLocationData(
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
    "Ikana Canyon Music Box Mummy": MMRLocationData(
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
    "Stone Tower Inverted Outside Left Chest": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x346942006591F
    ),
    "Stone Tower Inverted Outside Middle Chest": MMRLocationData(
        region="Stone Tower (Inverted)",
        address=0x346942006591E
    ),
    "Stone Tower Inverted Outside Right Chest": MMRLocationData(
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
    "Stone Tower Temple Inverted Eastern Air Gust Room Ice Eye Switch Chest": MMRLocationData(
        region="Stone Tower Temple (Inverted)",
        address=0x3469420061813
    ),
    "Stone Tower Temple Inverted Eastern Air Gust Room Hall Floor Switch Chest": MMRLocationData(
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
    address=0x127001,
    ),
"Laundry Pool Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x127002,
    ),
"Laundry Pool Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x127003,
    ),
    # North Clock Town Keaton Grass
"North Clock Town Keaton Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E00,
    ),
"North Clock Town Keaton Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E01,
    ),
"North Clock Town Grass (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E02,
    ),
"North Clock Town Keaton Grass (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E03,
    ),
"North Clock Town Keaton Grass (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E04,
    ),
"North Clock Town Keaton Grass (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E05,
    ),
"North Clock Town Keaton Grass (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E06,
    ),
"North Clock Town Keaton Grass (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E07,
    ),
"North Clock Town Keaton Grass (9)": MMRLocationData(
    region="Termina Field",
    address=0x3469420136E08,
    ),

# Termina Field 

"Termina Field Grass Group 0 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D0,
    ),
"Termina Field Grass Group 0 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D1,
    ),
"Termina Field Grass Group 0 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D2,
    ),
"Termina Field Grass Group 0 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D3,
    ),
"Termina Field Grass Group 0 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D4,
    ),
"Termina Field Grass Group 0 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D5,
    ),
"Termina Field Grass Group 0 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D6,
    ),
"Termina Field Grass Group 0 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D7,
    ),
"Termina Field Grass Group 0 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D8,
    ),
"Termina Field Grass Group 0 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002D9,
    ),
"Termina Field Grass Group 0 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002DA,
    ),
"Termina Field Grass Group 0 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201002DB,
    ),
"Termina Field Grass Group 1 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D0,
    ),
"Termina Field Grass Group 1 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D1,
    ),
"Termina Field Grass Group 1 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D2,
    ),
"Termina Field Grass Group 1 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D3,
    ),
"Termina Field Grass Group 1 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D4,
    ),
"Termina Field Grass Group 1 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D5,
    ),
"Termina Field Grass Group 1 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D6,
    ),
"Termina Field Grass Group 1 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D7,
    ),
"Termina Field Grass Group 1 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D8,
    ),
"Termina Field Grass Group 1 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012D9,
    ),
"Termina Field Grass Group 1 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012DA,
    ),
"Termina Field Grass Group 1 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201012DB,
    ),
"Termina Field Grass Group 2 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D0,
    ),
"Termina Field Grass Group 2 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D1,
    ),
"Termina Field Grass Group 2 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D2,
    ),
"Termina Field Grass Group 2 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D3,
    ),
"Termina Field Grass Group 2 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D4,
    ),
"Termina Field Grass Group 2 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D5,
    ),
"Termina Field Grass Group 2 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D6,
    ),
"Termina Field Grass Group 2 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D7,
    ),
"Termina Field Grass Group 2 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D8,
    ),
"Termina Field Grass Group 2 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022D9,
    ),
"Termina Field Grass Group 2 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022DA,
    ),
"Termina Field Grass Group 2 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201022DB,
    ),
"Termina Field Grass Group 3 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D0,
    ),
"Termina Field Grass Group 3 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D1,
    ),
"Termina Field Grass Group 3 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D2,
    ),
"Termina Field Grass Group 3 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D3,
    ),
"Termina Field Grass Group 3 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D4,
    ),
"Termina Field Grass Group 3 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D5,
    ),
"Termina Field Grass Group 3 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D6,
    ),
"Termina Field Grass Group 3 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D7,
    ),
"Termina Field Grass Group 3 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D8,
    ),
"Termina Field Grass Group 3 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032D9,
    ),
"Termina Field Grass Group 3 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032DA,
    ),
"Termina Field Grass Group 3 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201032DB,
    ),
"Termina Field Grass Group 4 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D0,
    ),
"Termina Field Grass Group 4 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D1,
    ),
"Termina Field Grass Group 4 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D2,
    ),
"Termina Field Grass Group 4 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D3,
    ),
"Termina Field Grass Group 4 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D4,
    ),
"Termina Field Grass Group 4 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D5,
    ),
"Termina Field Grass Group 4 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D6,
    ),
"Termina Field Grass Group 4 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D7,
    ),
"Termina Field Grass Group 4 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D8,
    ),
"Termina Field Grass Group 4 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042D9,
    ),
"Termina Field Grass Group 4 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042DA,
    ),
"Termina Field Grass Group 4 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201042DB,
    ),
"Termina Field Grass Group 5 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D0,
    ),
"Termina Field Grass Group 5 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D1,
    ),
"Termina Field Grass Group 5 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D2,
    ),
"Termina Field Grass Group 5 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D3,
    ),
"Termina Field Grass Group 5 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D4,
    ),
"Termina Field Grass Group 5 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D5,
    ),
"Termina Field Grass Group 5 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D6,
    ),
"Termina Field Grass Group 5 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D7,
    ),
"Termina Field Grass Group 5 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D8,
    ),
"Termina Field Grass Group 5 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052D9,
    ),
"Termina Field Grass Group 5 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052DA,
    ),
"Termina Field Grass Group 5 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201052DB,
    ),
"Termina Field Grass Group 6 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D0,
    ),
"Termina Field Grass Group 6 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D1,
    ),
"Termina Field Grass Group 6 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D2,
    ),
"Termina Field Grass Group 6 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D3,
    ),
"Termina Field Grass Group 6 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D4,
    ),
"Termina Field Grass Group 6 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D5,
    ),
"Termina Field Grass Group 6 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D6,
    ),
"Termina Field Grass Group 6 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D7,
    ),
"Termina Field Grass Group 6 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D8,
    ),
"Termina Field Grass Group 6 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062D9,
    ),
"Termina Field Grass Group 6 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062DA,
    ),
"Termina Field Grass Group 6 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201062DB,
    ),
"Termina Field Grass Group 7 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D0,
    ),
"Termina Field Grass Group 7 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D1,
    ),
"Termina Field Grass Group 7 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D2,
    ),
"Termina Field Grass Group 7 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D3,
    ),
"Termina Field Grass Group 7 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D4,
    ),
"Termina Field Grass Group 7 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D5,
    ),
"Termina Field Grass Group 7 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D6,
    ),
"Termina Field Grass Group 7 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D7,
    ),
"Termina Field Grass Group 7 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D8,
    ),
"Termina Field Grass Group 7 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072D9,
    ),
"Termina Field Grass Group 7 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072DA,
    ),
"Termina Field Grass Group 7 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201072DB,
    ),
"Termina Field Grass Group 8 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D0,
    ),
"Termina Field Grass Group 8 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D1,
    ),
"Termina Field Grass Group 8 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D2,
    ),
"Termina Field Grass Group 8 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D3,
    ),
"Termina Field Grass Group 8 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D4,
    ),
"Termina Field Grass Group 8 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D5,
    ),
"Termina Field Grass Group 8 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D6,
    ),
"Termina Field Grass Group 8 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D7,
    ),
"Termina Field Grass Group 8 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D8,
    ),
"Termina Field Grass Group 8 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082D9,
    ),
"Termina Field Grass Group 8 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082DA,
    ),
"Termina Field Grass Group 8 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201082DB,
    ),
"Termina Field Grass Group 9 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D0,
    ),
"Termina Field Grass Group 9 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D1,
    ),
"Termina Field Grass Group 9 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D2,
    ),
"Termina Field Grass Group 9 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D3,
    ),
"Termina Field Grass Group 9 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D4,
    ),
"Termina Field Grass Group 9 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D5,
    ),
"Termina Field Grass Group 9 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D6,
    ),
"Termina Field Grass Group 9 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D7,
    ),
"Termina Field Grass Group 9 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D8,
    ),
"Termina Field Grass Group 9 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092D9,
    ),
"Termina Field Grass Group 9 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092DA,
    ),
"Termina Field Grass Group 9 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201092DB,
    ),
"Termina Field Grass Group 10 (0)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D0,
    ),
"Termina Field Grass Group 10 (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D1,
    ),
"Termina Field Grass Group 10 (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D2,
    ),
"Termina Field Grass Group 10 (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D3,
    ),
"Termina Field Grass Group 10 (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D4,
   ),
"Termina Field Grass Group 10 (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D5,
    ),
"Termina Field Grass Group 10 (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D6,
    ),
"Termina Field Grass Group 10 (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D7,
    ),
"Termina Field Grass Group 10 (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D8,
    ),
"Termina Field Grass Group 10 (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2D9,
    ),
"Termina Field Grass Group 10 (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2DA,
    ),
"Termina Field Grass Group 10 (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942010A2DB,
    ),
"Termina Field Grass Group 11 (0)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D0,
    ),
"Termina Field Grass Group 11 (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D1,
    ),
"Termina Field Grass Group 11 (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D2,
    ),
"Termina Field Grass Group 11 (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D3,
    ),
"Termina Field Grass Group 11 (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D4,
    ),
"Termina Field Grass Group 11 (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D5,
    ),
"Termina Field Grass Group 11 (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D6,
    ),
"Termina Field Grass Group 11 (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D7,
    ),
"Termina Field Grass Group 11 (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D8,
    ),
"Termina Field Grass Group 11 (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2D9,
    ),
"Termina Field Grass Group 11 (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2DA,
    ),
"Termina Field Grass Group 11 (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942010B2DB,
    ),
"Termina Field Grass Group 12 (0)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D0,
    ),
"Termina Field Grass Group 12 (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D1,
    ),
"Termina Field Grass Group 12 (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D2,
    ),
"Termina Field Grass Group 12 (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D3,
    ),
"Termina Field Grass Group 12 (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D4,
    ),
"Termina Field Grass Group 12 (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D5,
    ),
"Termina Field Grass Group 12 (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D6,
    ),
"Termina Field Grass Group 12 (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D7,
    ),
"Termina Field Grass Group 12 (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D8,
    ),
"Termina Field Grass Group 12 (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2D9,
    ),
"Termina Field Grass Group 12 (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2DA,
    ),
"Termina Field Grass Group 12 (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942010C2DB,
    ),
"Termina Field Grass Group 13 (0)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D0,
    ),
"Termina Field Grass Group 13 (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D1,
    ),
"Termina Field Grass Group 13 (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D2,
    ),
"Termina Field Grass Group 13 (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D3,
    ),
"Termina Field Grass Group 13 (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D4,
    ),
"Termina Field Grass Group 13 (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D5,
    ),
"Termina Field Grass Group 13 (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D6,
    ),
"Termina Field Grass Group 13 (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D7,
    ),
"Termina Field Grass Group 13 (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D8,
    ),
"Termina Field Grass Group 13 (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2D9,
    ),
"Termina Field Grass Group 13 (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2DA,
    ),
"Termina Field Grass Group 13 (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942010D2DB,
    ),
"Termina Field Grass Group 14 (0)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D0,
    ),
"Termina Field Grass Group 14 (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D1,
    ),
"Termina Field Grass Group 14 (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D2,
    ),
"Termina Field Grass Group 14 (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D3,
    ),
"Termina Field Grass Group 14 (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D4,
    ),
"Termina Field Grass Group 14 (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D5,
    ),
"Termina Field Grass Group 14 (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D6,
    ),
"Termina Field Grass Group 14 (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D7,
    ),
"Termina Field Grass Group 14 (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D8,
    ),
"Termina Field Grass Group 14 (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2D9,
    ),
"Termina Field Grass Group 14 (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2DA,
    ),
"Termina Field Grass Group 14 (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942010E2DB,
    ),
"Termina Field Grass Group 15 (0)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D0,
    ),
"Termina Field Grass Group 15 (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D1,
    ),
"Termina Field Grass Group 15 (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D2,
    ),
"Termina Field Grass Group 15 (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D3,
    ),
"Termina Field Grass Group 15 (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D4,
    ),
"Termina Field Grass Group 15 (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D5,
    ),
"Termina Field Grass Group 15 (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D6,
    ),
"Termina Field Grass Group 15 (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D7,
    ),
"Termina Field Grass Group 15 (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D8,
    ),
"Termina Field Grass Group 15 (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2D9,
    ),
"Termina Field Grass Group 15 (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2DA,
    ),
"Termina Field Grass Group 15 (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942010F2DB,
    ),
"Termina Field Grass Group 16 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D0,
   ),
"Termina Field Grass Group 16 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D1,
    ),
"Termina Field Grass Group 16 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D2,
    ),
"Termina Field Grass Group 16 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D3,
    ),
"Termina Field Grass Group 16 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D4,
    ),
"Termina Field Grass Group 16 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D5,
    ),
"Termina Field Grass Group 16 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D6,
    ),
"Termina Field Grass Group 16 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D7,
    ),
"Termina Field Grass Group 16 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D8,
    ),
"Termina Field Grass Group 16 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102D9,
    ),
"Termina Field Grass Group 16 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102DA,
    ),
"Termina Field Grass Group 16 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201102DB,
    ),
"Termina Field Grass Group 17 (0)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D0,
    ),
"Termina Field Grass Group 17 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D1,
    ),
"Termina Field Grass Group 17 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D2,
    ),
"Termina Field Grass Group 17 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D3,
    ),
"Termina Field Grass Group 17 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D4,
    ),
"Termina Field Grass Group 17 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D5,
    ),
"Termina Field Grass Group 17 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D6, 
    ),
"Termina Field Grass Group 17 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D7,
    ),
"Termina Field Grass Group 17 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D8,
    ),
"Termina Field Grass Group 17 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D9,
    ),
"Termina Field Grass Group 17 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112DA,
    ),
"Termina Field Grass Group 17 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112DB,
    ),
"Termina Field Grass Group 18 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D0,
    ),
"Termina Field Grass Group 18 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D0,
    ),
"Termina Field Grass Group 18 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D1,
    ),
"Termina Field Grass Group 18 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D2,
    ),
"Termina Field Grass Group 18 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D3,
    ),
"Termina Field Grass Group 18 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D4,
    ),
"Termina Field Grass Group 18 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D5,
    ),
"Termina Field Grass Group 18 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D6,
    ),
"Termina Field Grass Group 18 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D7,
    ),
"Termina Field Grass Group 18 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D8,
    ),
"Termina Field Grass Group 18 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112D9,
    ),
"Termina Field Grass Group 18 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112DA,
    ),
"Termina Field Grass Group 18 (12)": MMRLocationData(
    region="Termina Field",
    address=0x34694201112DB,
    ),
# Termina Field Grass Grotto Grass

"Termina Field Grass Grotto Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B000,
    ),
"Termina Field Grass Grotto Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B001,
    ),
"Termina Field Grass Grotto Grass (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B002,
    ),
"Termina Field Grass Grotto Grass (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B003,
    ),
"Termina Field Grass Grotto Grass (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B004,
    ),
"Termina Field Grass Grotto Grass (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B005,
    ),
"Termina Field Grass Grotto Grass (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B006,
    ),
"Termina Field Grass Grotto Grass (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B007,
    ),
"Termina Field Grass Grotto Grass (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B008,
    ),
"Termina Field Grass Grotto Grass (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B009,
    ),
"Termina Field Grass Grotto Grass (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B00A,
    ),
"Termina Field Grass Grotto Grass (12)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B00B,
    ),
"Termina Field Grass Grotto Grass (13)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B00C,
    ),
"Termina Field Grass Grotto Grass (14)": MMRLocationData(
    region="Termina Field",
    address=0x346942012B00D,
    ),
# Termina Field Cow Grotto Grass

"Termina Field Cow Grotto Grass Group 1 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD0,
    ),
"Termina Field Cow Grotto Grass Group 1 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD1,
    ),
"Termina Field Cow Grotto Grass Group 1 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD2,
    ),
"Termina Field Cow Grotto Grass Group 1 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD3,
    ),
"Termina Field Cow Grotto Grass Group 1 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD4,
    ),
"Termina Field Cow Grotto Grass Group 1 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD5,
    ),
"Termina Field Cow Grotto Grass Group 1 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD6,
    ),
"Termina Field Cow Grotto Grass Group 1 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD7,
    ),
"Termina Field Cow Grotto Grass Group 1 (9)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD8,
    ),
"Termina Field Cow Grotto Grass Group 1 (10)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100AD9,
    ),
"Termina Field Cow Grotto Grass Group 1 (11)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100ADA,
    ),
"Termina Field Cow Grotto Grass Group 1 (12)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100ADB,
    ),
"Termina Field Cow Grotto Grass Group 2 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD0,
    ),
"Termina Field Cow Grotto Grass Group 2 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD1,
    ),
"Termina Field Cow Grotto Grass Group 2 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD2,
    ),
"Termina Field Cow Grotto Grass Group 2 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD3,
    ),
"Termina Field Cow Grotto Grass Group 2 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD4,
    ),
"Termina Field Cow Grotto Grass Group 2 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD5,
    ),
"Termina Field Cow Grotto Grass Group 2 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD6,
    ),
"Termina Field Cow Grotto Grass Group 2 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD7,
    ),
"Termina Field Cow Grotto Grass Group 2 (9)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD8,
    ),
"Termina Field Cow Grotto Grass Group 2 (10)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101AD9,
    ),
"Termina Field Cow Grotto Grass Group 2 (11)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101ADA,
    ),
"Termina Field Cow Grotto Grass Group 2 (12)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101ADB,
    ),
"Termina Field Cow Grotto Grass Group 3 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD0,
    ),
"Termina Field Cow Grotto Grass Group 3 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD1,
    ),
"Termina Field Cow Grotto Grass Group 3 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD2,
    ),
"Termina Field Cow Grotto Grass Group 3 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD3,
    ),
"Termina Field Cow Grotto Grass Group 3 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD4,
    ),
"Termina Field Cow Grotto Grass Group 3 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD5,
    ),
"Termina Field Cow Grotto Grass Group 3 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD6,
    ),
"Termina Field Cow Grotto Grass Group 3 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD7,
    ),
"Termina Field Cow Grotto Grass Group 3 (9)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD8,
    ),
"Termina Field Cow Grotto Grass Group 3 (10)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102AD9,
    ),
"Termina Field Cow Grotto Grass Group 3 (11)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102ADA,
    ),
"Termina Field Cow Grotto Grass Group 3 (12)": MMRLocationData(
    region="Termina Field",
    address=0x3469420102ADB,
    ),
"Termina Field Cow Grotto Grass Group 4 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD0,
    ),
"Termina Field Cow Grotto Grass Group 4 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD1,
    ),
"Termina Field Cow Grotto Grass Group 4 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD2,
    ),
"Termina Field Cow Grotto Grass Group 4 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD3,
    ),
"Termina Field Cow Grotto Grass Group 4 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD4,
    ),
"Termina Field Cow Grotto Grass Group 4 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD5,
    ),
"Termina Field Cow Grotto Grass Group 4 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD6,
    ),
"Termina Field Cow Grotto Grass Group 4 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD7,
    ),
"Termina Field Cow Grotto Grass Group 4 (9)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD8,
    ),
"Termina Field Cow Grotto Grass Group 4 (10)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103AD9,
    ),
"Termina Field Cow Grotto Grass Group 4 (11)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103ADA,
    ),
"Termina Field Cow Grotto Grass Group 4 (12)": MMRLocationData(
    region="Termina Field",
    address=0x3469420103ADB,
    ),
"Termina Field Cow Grotto Grass Group 5 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD0,
    ),
"Termina Field Cow Grotto Grass Group 5 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD1,
    ),
"Termina Field Cow Grotto Grass Group 5 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD2,
    ),
"Termina Field Cow Grotto Grass Group 5 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD3,
    ),
"Termina Field Cow Grotto Grass Group 5 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD4,
    ),
"Termina Field Cow Grotto Grass Group 5 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD5,
    ),
"Termina Field Cow Grotto Grass Group 5 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD6,
    ),
"Termina Field Cow Grotto Grass Group 5 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD7,
    ),
"Termina Field Cow Grotto Grass Group 5 (9)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD8,
    ),
"Termina Field Cow Grotto Grass Group 5 (10)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104AD9,
    ),
"Termina Field Cow Grotto Grass Group 5 (11)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104ADA,
    ),
"Termina Field Cow Grotto Grass Group 5 (12)": MMRLocationData(
    region="Termina Field",
    address=0x3469420104ADB,
    ),
"Termina Field Cow Grotto Grass Group 6 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD0,
    ),
"Termina Field Cow Grotto Grass Group 6 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD1,
    ),
"Termina Field Cow Grotto Grass Group 6 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD2,
    ),
"Termina Field Cow Grotto Grass Group 6 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD3,
    ),
"Termina Field Cow Grotto Grass Group 6 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD4,
    ),
"Termina Field Cow Grotto Grass Group 6 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD5,
    ),
"Termina Field Cow Grotto Grass Group 6 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD6,
    ),
"Termina Field Cow Grotto Grass Group 6 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD7,
    ),
"Termina Field Cow Grotto Grass Group 6 (9)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD8,
    ),
"Termina Field Cow Grotto Grass Group 6 (10)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105AD9,
    ),
"Termina Field Cow Grotto Grass Group 6 (11)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105ADA,
    ),
"Termina Field Cow Grotto Grass Group 6 (12)": MMRLocationData(
    region="Termina Field",
    address=0x3469420105ADB,
    ),
# Termina Field Peahat Grotto Grass

"Termina Field Peahat Grotto Grass Group 1 (1)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D0,
    ),
"Termina Field Peahat Grotto Grass Group 1 (2)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D1,
    ),
"Termina Field Peahat Grotto Grass Group 1 (3)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D2,
    ),
"Termina Field Peahat Grotto Grass Group 1 (4)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D3,
    ),
"Termina Field Peahat Grotto Grass Group 1 (5)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D4,
    ),
"Termina Field Peahat Grotto Grass Group 1 (6)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D5,
    ),
"Termina Field Peahat Grotto Grass Group 1 (7)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D6,
    ),
"Termina Field Peahat Grotto Grass Group 1 (8)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D7,
    ),
"Termina Field Peahat Grotto Grass Group 1 (9)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D8,
    ),
"Termina Field Peahat Grotto Grass Group 1 (10)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008D9,
    ),
"Termina Field Peahat Grotto Grass Group 1 (11)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008DA,
    ),
"Termina Field Peahat Grotto Grass Group 1 (12)": MMRLocationData(
    region="Termina Field",
    address=0x34694201008DB,
    ),
# Termina Field Bio Baba Grotto Grass

"Termina Field Bio Baba Grotto Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128B00,
    ),
"Termina Field Bio Baba Grotto Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128B01,
    ),
# Termina Field Eastern Gossip Grotto Grass

"Termina Field Eastern Gossip Grotto Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128200,
    ),
"Termina Field Eastern Gossip Grotto Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128201,
    ),
"Termina Field Eastern Gossip Grotto Grass (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128202,
    ),
"Termina Field Eastern Gossip Grotto Grass (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128203,
    ),
"Termina Field Eastern Gossip Grotto Grass (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128204,
    ),
# Termina Field Eastern Pillar Grotto Grass

    region="Termina Field",
"Termina Field Eastern Pillar Grotto Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB00,
    ),
"Termina Field Eastern Pillar Grotto Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB01,
    ),
"Termina Field Eastern Pillar Grotto Grass (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB02,
    ),
"Termina Field Eastern Pillar Grotto Grass (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB03,
    ),
"Termina Field Eastern Pillar Grotto Grass (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB04,
    ),
"Termina Field Eastern Pillar Grotto Grass (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB05,
    ),
"Termina Field Eastern Pillar Grotto Grass (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB06,
    ),
"Termina Field Eastern Pillar Grotto Grass (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB07,
    ),
"Termina Field Eastern Pillar Grotto Grass (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB08,
    ),
"Termina Field Eastern Pillar Grotto Grass (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB09,
    ),
"Termina Field Eastern Pillar Grotto Grass (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB0A,
    ),
"Termina Field Eastern Pillar Grotto Grass (12)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB0B,
    ),
"Termina Field Eastern Pillar Grotto Grass (13)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB0C,
    ),
"Termina Field Eastern Pillar Grotto Grass (14)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AB0D,
    ),
# Termina Field Bombable Rock Grass

"Termina Field Bombable Rock Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128000,
    ),
"Termina Field Bombable Rock Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128001,
    ),
"Termina Field Bombable Rock Grass (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128002,
    ),
"Termina Field Bombable Rock Grass (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128003,
    ),
"Termina Field Bombable Rock Grass (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420128004,
    ),
# Road to Southern Swamp
 
"Road to Southern Swamp Outside Archery Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420124000,
    ),
"Road to Southern Swamp Outside Archery Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420124001,
    ),
"Road to Southern Swamp Grass Group 0 (0)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100400,
    ),
"Road to Southern Swamp Grass Group 0 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100401,
    ),
"Road to Southern Swamp Grass Group 0 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100402,
    ),
"Road to Southern Swamp Grass Group 0 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100403,
    ),
"Road to Southern Swamp Grass Group 0 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100404,
    ),
"Road to Southern Swamp Grass Group 0 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100405,
    ),
"Road to Southern Swamp Grass Group 0 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100406,
    ),
"Road to Southern Swamp Grass Group 0 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100407,
    ),
"Road to Southern Swamp Grass Group 0 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420100408,
    ),
"Road to Southern Swamp Grass Group 1 (0)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101400,
    ),
"Road to Southern Swamp Grass Group 1 (1)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101401,
    ),
"Road to Southern Swamp Grass Group 1 (2)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101402,
    ),
"Road to Southern Swamp Grass Group 1 (3)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101403,
    ),
"Road to Southern Swamp Grass Group 1 (4)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101404,
    ),
"Road to Southern Swamp Grass Group 1 (5)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101405,
    ),
"Road to Southern Swamp Grass Group 1 (6)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101406,
    ),
"Road to Southern Swamp Grass Group 1 (7)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101407,
    ),
"Road to Southern Swamp Grass Group 1 (8)": MMRLocationData(
    region="Termina Field",
    address=0x3469420101408,
    ),
# Road To Southern Swamp Grotto
"Road to Southern Swamp Grotto Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF00,
    ),
"Road to Southern Swamp Grotto Grass (2)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF01,
    ),
"Road to Southern Swamp Grotto Grass (3)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF02,
    ),
"Road to Southern Swamp Grotto Grass (4)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF03,
    ),
"Road to Southern Swamp Grotto Grass (5)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF04,
    ),
"Road to Southern Swamp Grotto Grass (6)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF05,
    ),
"Road to Southern Swamp Grotto Grass (7)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF06,
    ),
"Road to Southern Swamp Grotto Grass (8)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF07,
    ),
"Road to Southern Swamp Grotto Grass (9)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF08,
    ),
"Road to Southern Swamp Grotto Grass (10)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF09,
    ),
"Road to Southern Swamp Grotto Grass (11)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF0A,
    ),
"Road to Southern Swamp Grotto Grass (12)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF0B,
    ),
"Road to Southern Swamp Grotto Grass (13)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF0C,
    ),
"Road to Southern Swamp Grotto Grass (14)": MMRLocationData(
    region="Termina Field",
    address=0x346942012AF0D,
    ),
# Southern Swamp

"Southern Swamp Grass (1)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420124500,
    ),
"Southern Swamp Grass (2)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420124501,
    ),
"Southern Swamp Grass Group 0 (0)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100450,
    ),
"Southern Swamp Grass Group 0 (1)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100451,
    ),
"Southern Swamp Grass Group 0 (2)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100452,
    ),
"Southern Swamp Grass Group 0 (3)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100453,
    ),
"Southern Swamp Grass Group 0 (4)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100454,
    ),
"Southern Swamp Grass Grass Group 0 (5)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100455,
    ),
"Southern Swamp Grass Grass Group 0 (6)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100456,
    ),
"Southern Swamp Grass Grass Group 0 (7)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100457,
    ),
"Southern Swamp Grass Grass Group 0 (8)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100458,
    ),
"Southern Swamp Grass Grass Group 0 (9)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420100459,
    ),
"Southern Swamp Grass Grass Group 0 (10)": MMRLocationData(
    region="Southern Swamp",
    address=0x346942010045A,
    ),
"Southern Swamp Grass Grass Group 0 (11)": MMRLocationData(
    region="Southern Swamp",
    address=0x346942010045B,
    ),

# Woods of Mystery

"Woods of Mystery Grass (0)": MMRLocationData(
    region="Southern Swamp",
    address=0x126410,
    ),
"Woods of Mystery Grass (1)": MMRLocationData(
    region="Southern Swamp",
    address=0x126412,
    ),
"Woods of Mystery Grass (2)": MMRLocationData(
    region="Southern Swamp",
    address=0x126411,
    ),
"Woods of Mystery Grass (3)": MMRLocationData(
    region="Southern Swamp",
    address=0x126400,
    ),
"Woods of Mystery Grass (4)": MMRLocationData(
    region="Southern Swamp",
    address=0x126401,
    ),
"Woods of Mystery Grass (5)": MMRLocationData(
    region="Southern Swamp",
    address=0x126431,
    ),
"Woods of Mystery Grass (6)": MMRLocationData(
    region="Southern Swamp",
    address=0x126430,
    ),
"Woods of Mystery Grass (7)": MMRLocationData(
    region="Southern Swamp",
    address=0x126442,
    ),
"Woods of Mystery Grass (8)": MMRLocationData(
    region="Southern Swamp",
    address=0x126440,
    ),
"Woods of Mystery Grass (9)": MMRLocationData(
    region="Southern Swamp",
    address=0x126441,
    ),
"Woods of Mystery Grass (10)": MMRLocationData(
    region="Southern Swamp",
    address=0x126443,
    ),
"Woods of Mystery Grass (11)": MMRLocationData(
    region="Southern Swamp",
    address=0x126450,
    ),
"Woods of Mystery Grass (12)": MMRLocationData(
    region="Southern Swamp",
    address=0x126451,
    ),
"Woods of Mystery Grass (13)": MMRLocationData(
    region="Southern Swamp",
    address=0x126482,
    ),
"Woods of Mystery Grass (14)": MMRLocationData(
    region="Southern Swamp",
    address=0x126484,
    ),
"Woods of Mystery Grass (15)": MMRLocationData(
    region="Southern Swamp",
    address=0x126481,
    ),
"Woods of Mystery Grass (16)": MMRLocationData(
    region="Southern Swamp",
    address=0x126480,
    ),
"Woods of Mystery Grass (17)": MMRLocationData(
    region="Southern Swamp",
    address=0x126483,
    ),
"Woods of Mystery Grass (18)": MMRLocationData(
    region="Southern Swamp",
    address=0x126471,
    ),
"Woods of Mystery Grass (19)": MMRLocationData(
    region="Southern Swamp",
    address=70,
    ),
"Woods of Mystery Grass (20)": MMRLocationData(
    region="Southern Swamp",
    address=,
    ),
"Woods of Mystery Day 2 Unique Grass": MMRLocationData(
    region="Southern Swamp",
    address=0x126420,
    ),
"Woods of Mystery Day 3 Unique Grass (0)": MMRLocationData(
    region="Southern Swamp",
    address=0x126460,
    ),
"Woods of Mystery Grass (1)": MMRLocationData(
    region="Southern Swamp",
    address=0x126461,
    ),
    
    # Woods of Mystery Day 2 Grotto grass missing?

   # Southern Swamp Grotto
"Southern Swamp Grotto Grass (1)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE00,
),
"Southern Swamp Grotto Grass (2)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE01,
),
"Southern Swamp Grotto Grass (3)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE02,
),
"Southern Swamp Grotto Grass (4)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE03,
),
"Southern Swamp Grotto Grass (5)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE04,
),
"Southern Swamp Grotto Grass (6)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE05,
),
"Southern Swamp Grotto Grass (7)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE06,
),
"Southern Swamp Grotto Grass (8)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE07,
),
"Southern Swamp Grotto Grass (9)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE08,
),
"Southern Swamp Grotto Grass (10)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE09,
),
"Southern Swamp Grotto Grass (11)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE0A,
),
"Southern Swamp Grotto Grass (12)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE0B,
),
"Southern Swamp Grotto Grass (13)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE0C,
),
"Southern Swamp Grotto Grass (14)": MMRLocationData(
    region="Southern Swamp (Deku Palace)",
    address=0x346942012AE0D,
),

#Deku Palace Bean Grotto Grass
"Deku Palace Bean Grotto Grass Group 0 (0)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C0,
),
"Deku Palace Bean Grotto Grass Group 0 (1)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C1,
),
"Deku Palace Bean Grotto Grass Group 0 (2)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C2,
),
"Deku Palace Bean Grotto Grass Group 0 (3)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C3,
),
"Deku Palace Bean Grotto Grass Group 0 (4)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C4,
),
"Deku Palace Bean Grotto Grass Group 0 (5)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C5,
),
"Deku Palace Bean Grotto Grass Group 0 (6)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C6,
),
"Deku Palace Bean Grotto Grass Group 0 (7)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C7,
),
"Deku Palace Bean Grotto Grass Group 0 (8)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C8,
),
"Deku Palace Bean Grotto Grass Group 0 (9)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008C9,
),
"Deku Palace Bean Grotto Grass Group 0 (10)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008CA,
),
"Deku Palace Bean Grotto Grass Group 0 (11)": MMRLocationData(
    region="Deku Palace",
    address=0x34694201008CB,
),

# Woodfall Grass
"Woodfall Grass (1)": MMRLocationData(
    region="Woodfall",
    address=0x3469420124600,
    # can_create=lamda options: options.grasssanity.value
),
"Woodfall Grass (2)": MMRLocationData(
    region="Woodfall",
    address=0x3469420124601,
    # can_create=lamda options: options.grasssanity.value
),
"Woodfall Grass (3)": MMRLocationData(
    region="Woodfall",
    address=0x3469420124602,
    # can_create=lamda options: options.grasssanity.value
),
"Woodfall Grass (4)": MMRLocationData(
    region="Woodfall",
    address=0x3469420124603,
    # can_create=lamda options: options.grasssanity.value
),
"Woodfall Grass (5)": MMRLocationData(
    region="Woodfall",
    address=0x3469420124604,
    # can_create=lamda options: options.grasssanity.value
),
"Woodfall Grass (6)": MMRLocationData(
    region="Woodfall",
    address=0x3469420124605,
   
# Southern Swamp After Dungeon Clear
"Southern Swamp Owl Post Dungeon Grass (1)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420120000,
),
"Southern Swamp Owl Post Dungeon Grass (2)": MMRLocationData(
    region="Southern Swamp",
    address=0x3469420120001,
),

# Milk Road Owl Grass
"Milk Road Owl Grass (1)": MMRLocationData(
    region="Milk Road",
    address=0x3469420122200,
    # can_create=lamda options: options.grasssanity.value
),
"Milk Road Owl Grass (2)": MMRLocationData(
    region="Milk Road",
    address=0x3469420122201,
    # can_create=lamda options: options.grasssanity.value
),
"Milk Road Owl Grass (3)": MMRLocationData(
    region="Milk Road",
    address=0x3469420122202,
    # can_create=lamda options: options.grasssanity.value
),
# Milk Road Keaton Grass
"Milk Road Keaton Grass (1)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132200,
),
"Milk Road Keaton Grass (2)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132201,
),
"Milk Road Keaton Grass (3)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132202,
),
"Milk Road Keaton Grass (4)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132203,
),
"Milk Road Keaton Grass (5)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132204,
),
"Milk Road Keaton Grass (6)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132205,
),
"Milk Road Keaton Grass (7)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132206,
),
"Milk Road Keaton Grass (8)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132207,
),
"Milk Road Keaton Grass (9)": MMRLocationData(
    region="Milk Road",
    address=0x3469420132208,
),
# Milk Road Gorman Racetrack Grass
"Milk Road Gorman Racetrack Grass Group 1 (1)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A0,
),
"Milk Road Gorman Racetrack Grass Group 1 (2)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A1,
),
"Milk Road Gorman Racetrack Grass Group 1 (3)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A2,
),
"Milk Road Gorman Racetrack Grass Group 1 (4)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A3,
),
"Milk Road Gorman Racetrack Grass Group 1 (5)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A4,
),
"Milk Road Gorman Racetrack Grass Group 1 (6)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A5,
),
"Milk Road Gorman Racetrack Grass Group 1 (7)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A6,
),
"Milk Road Gorman Racetrack Grass Group 1 (8)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A7,
),
"Milk Road Gorman Racetrack Grass Group 1 (9)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A8,
),
"Milk Road Gorman Racetrack Grass Group 1 (10)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006A9,
),
"Milk Road Gorman Racetrack Grass Group 1 (11)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006AA,
),
"Milk Road Gorman Racetrack Grass Group 1 (12)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201006AB,
),
"Milk Road Gorman Racetrack Grass Group 2 (1)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A0,
),
"Milk Road Gorman Racetrack Grass Group 2 (2)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A1,
),
"Milk Road Gorman Racetrack Grass Group 2 (3)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A2,
),
"Milk Road Gorman Racetrack Grass Group 2 (4)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A3,
),
"Milk Road Gorman Racetrack Grass Group 2 (5)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A4,
),
"Milk Road Gorman Racetrack Grass Group 2 (6)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A5,
),
"Milk Road Gorman Racetrack Grass Group 2 (7)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A6,
),
"Milk Road Gorman Racetrack Grass Group 2 (8)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A7,
),
"Milk Road Gorman Racetrack Grass Group 2 (9)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A8,
),
"Milk Road Gorman Racetrack Grass Group 2 (10)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016A9,
),
"Milk Road Gorman Racetrack Grass Group 2 (11)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016AA,
),
"Milk Road Gorman Racetrack Grass Group 2 (12)": MMRLocationData(
    region="Gorman Brothers Track",
    address=0x34694201016AB,
),
# Romani Ranch Grass
"Romani Ranch Grass Group 1 (1)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100350,
),
"Romani Ranch Grass Group 1 (2)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100351,
),
"Romani Ranch Grass Group 1 (3)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100352,
),
"Romani Ranch Grass Group 1 (4)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100353,
),
"Romani Ranch Grass Group 1 (5)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100354,
),
"Romani Ranch Grass Group 1 (6)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100355,
),
"Romani Ranch Grass Group 1 (7)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100356,
),
"Romani Ranch Grass Group 1 (8)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100357,
),
"Romani Ranch Grass Group 1 (9)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100358,
),
"Romani Ranch Grass Group 1 (10)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420100359,
),
"Romani Ranch Grass Group 1 (11)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010035A,
),
"Romani Ranch Grass Group 1 (12)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010035B,
),
"Romani Ranch Grass Group 2 (1)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101350,
),
"Romani Ranch Grass Group 2 (2)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101351,
),
"Romani Ranch Grass Group 2 (3)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101352,
),
"Romani Ranch Grass Group 2 (4)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101353,
),
"Romani Ranch Grass Group 2 (5)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101354,
),
"Romani Ranch Grass Group 2 (6)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101355,
),
"Romani Ranch Grass Group 2 (7)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101356,
),
"Romani Ranch Grass Group 2 (8)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101357,
),
"Romani Ranch Grass Group 2 (9)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101358,
),
"Romani Ranch Grass Group 2 (10)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420101359,
),
"Romani Ranch Grass Group 2 (11)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010135A,
),
"Romani Ranch Grass Group 2 (12)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010135B,
),
"Romani Ranch Grass Group 3 (1)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102350,
),
"Romani Ranch Grass Group 3 (2)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102351,
),
"Romani Ranch Grass Group 3 (3)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102352,
),
"Romani Ranch Grass Group 3 (4)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102353,
),
"Romani Ranch Grass Group 3 (5)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102354,
),
"Romani Ranch Grass Group 3 (6)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102355,
),
"Romani Ranch Grass Group 3 (7)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102356,
),
"Romani Ranch Grass Group 3 (8)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102357,
),
"Romani Ranch Grass Group 3 (9)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102358,
),
"Romani Ranch Grass Group 3 (10)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420102359,
),
"Romani Ranch Grass Group 3 (11)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010235A,
),
"Romani Ranch Grass Group 3 (12)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010235B,
),
"Romani Ranch Grass Group 4 (1)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103350,
),
"Romani Ranch Grass Group 4 (2)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103351,
),
"Romani Ranch Grass Group 4 (3)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103352,
),
"Romani Ranch Grass Group 4 (4)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103353,
),
"Romani Ranch Grass Group 4 (5)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103354,
),
"Romani Ranch Grass Group 4 (6)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103355,
),
"Romani Ranch Grass Group 4 (7)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103356,
),
"Romani Ranch Grass Group 4 (8)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103357,
),
"Romani Ranch Grass Group 4 (9)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103358,
),
"Romani Ranch Grass Group 4 (10)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420103359,
),
"Romani Ranch Grass Group 4 (11)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010335A,
),
"Romani Ranch Grass Group 4 (12)": MMRLocationData(
    region="Romani Ranch",
    address=0x346942010335B,
),
"Romani Ranch Grass Group 5 (1)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104350,
),
"Romani Ranch Grass Group 5 (2)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104351,
),
"Romani Ranch Grass Group 5 (3)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104352,
),
"Romani Ranch Grass Group 5 (4)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104353,
),
"Romani Ranch Grass Group 5 (5)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104354,
),
"Romani Ranch Grass Group 5 (6)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104355,
),
"Romani Ranch Grass Group 5 (7)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104356,
),
"Romani Ranch Grass Group 5 (8)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104357,
),
"Romani Ranch Grass Group 5 (9)": MMRLocationData(
    region="Romani Ranch",
    address=0x3469420104358,
),

# Twin Isles Grotto Grass

"Twin Isles Grotto Grass (1)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA00,
),
"Twin Isles Grotto Grass (2)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA01,
),
"Twin Isles Grotto Grass (3)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA02,
),
"Twin Isles Grotto Grass (4)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA03,
),
"Twin Isles Grotto Grass (5)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA04,
),
"Twin Isles Grotto Grass (6)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA05,
),
"Twin Isles Grotto Grass (7)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA06,
),
"Twin Isles Grotto Grass (8)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA07,
),
"Twin Isles Grotto Grass (9)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA08,
),
"Twin Isles Grotto Grass (10)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA09,
),
"Twin Isles Grotto Grass (11)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA0A,
),
"Twin Isles Grotto Grass (12)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA0B,
),
"Twin Isles Grotto Grass (13)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA0C,
),
"Twin Isles Grotto Grass (14)": MMRLocationData(
    region="Twin Islands",
    address=0x346942012AA0D,
),
# Goron Village Lens Cave Grass
"Goron Village Lens Cave Grass Group 1 (1)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100900,
),
"Goron Village Lens Cave Grass Group 1 (2)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100901,
),
"Goron Village Lens Cave Grass Group 1 (3)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100902,
),
"Goron Village Lens Cave Grass Group 1 (4)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100903,
),
"Goron Village Lens Cave Grass Group 1 (5)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100904,
),
"Goron Village Lens Cave Grass Group 1 (6)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100905,
),
"Goron Village Lens Cave Grass Group 1 (7)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100906,
),
"Goron Village Lens Cave Grass Group 1 (8)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100907,
),
"Goron Village Lens Cave Grass Group 1 (9)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100908,
),
"Goron Village Lens Cave Grass Group 1 (10)": MMRLocationData(
    region="Goron Village",
    address=0x3469420100909,
),
"Goron Village Lens Cave Grass Group 1 (11)": MMRLocationData(
    region="Goron Village",
    address=0x346942010090A,
),
"Goron Village Lens Cave Grass Group 1 (12)": MMRLocationData(
    region="Goron Village",
    address=0x346942010090B,
),
"Goron Village Lens Cave Grass Group 2 (1)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101900,
),
"Goron Village Lens Cave Grass Group 2 (2)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101901,
),
"Goron Village Lens Cave Grass Group 2 (3)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101902,
),
"Goron Village Lens Cave Grass Group 2 (4)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101903,
),
"Goron Village Lens Cave Grass Group 2 (5)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101904,
),
"Goron Village Lens Cave Grass Group 2 (6)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101905,
),
"Goron Village Lens Cave Grass Group 2 (7)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101906,
),
"Goron Village Lens Cave Grass Group 2 (8)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101907,
),
"Goron Village Lens Cave Grass Group 2 (9)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101908,
),
"Goron Village Lens Cave Grass Group 2 (10)": MMRLocationData(
    region="Goron Village",
    address=0x3469420101909,
),
"Goron Village Lens Cave Grass Group 2 (11)": MMRLocationData(
    region="Goron Village",
    address=0x346942010190A,
),
"Goron Village Lens Cave Grass Group 2 (12)": MMRLocationData(
    region="Goron Village",
    address=0x346942010190B,
),

# Path To Snowhead Grotto Grass

"Path To Snowhead Grotto Grass (1)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A400,
),
"Path To Snowhead Grotto Grass (2)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A401,
),
"Path To Snowhead Grotto Grass (3)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A402,
),
"Path To Snowhead Grotto Grass (4)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A403,
),
"Path To Snowhead Grotto Grass (5)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A404,
),
"Path To Snowhead Grotto Grass (6)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A405,
),
"Path To Snowhead Grotto Grass (7)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A406,
),
"Path To Snowhead Grotto Grass (8)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A407,
),
"Path To Snowhead Grotto Grass (9)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A408,
),
"Path To Snowhead Grotto Grass (10)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A409,
),
"Path To Snowhead Grotto Grass (11)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A40A,
),
"Path To Snowhead Grotto Grass (12)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A40B,
),
"Path To Snowhead Grotto Grass (13)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A40C,
),
"Path To Snowhead Grotto Grass (14)": MMRLocationData(
    region="Path to Snowhead",
    address=0x346942012A40D,
),

# Mountain Village Spring Grass

"Mountain Village Springtime Grass (1)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A00,
),
"Mountain Village Springtime Grass (2)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A01,
),
"Mountain Village Springtime Grass (3)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A02,
),
"Mountain Village Springtime Keaton Grass (1)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A00,
),
"Mountain Village Springtime Keaton Grass (2)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A01,
),
"Mountain Village Springtime Keaton Grass (3)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A02,
),
"Mountain Village Springtime Keaton Grass (4)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A03,
),
"Mountain Village Springtime Keaton Grass (5)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A04,
),
"Mountain Village Springtime Keaton Grass (6)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A05,
),
"Mountain Village Springtime Keaton Grass (7)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A06,
),
"Mountain Village Springtime Keaton Grass (8)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A07,
),
"Mountain Village Springtime Keaton Grass (9)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A08,
),
"Mountain Village Springtime Grass (4)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A03,
),
"Mountain Village Springtime Grass (5)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A04,
),
"Mountain Village Springtime Grass (6)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A05,
),
"Mountain Village Springtime Grass (7)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A06,
),
"Mountain Village Springtime Grass (8)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A07,
),
"Mountain Village Springtime Grass (9)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A08,
),
"Mountain Village Springtime Grass (10)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A09,
),
"Mountain Village Springtime Grass (11)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A0A,
),
"Mountain Village Springtime Grass (12)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A0B,
),
"Mountain Village Springtime Grass (13)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A0C,
),
"Mountain Village Springtime Grass (14)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A0D,
),
"Mountain Village Springtime Grass (15)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A0E,
),
"Mountain Village Springtime Grass (16)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A0F,
),
"Mountain Village Springtime Grass (17)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A10,
),
"Mountain Village Springtime Grass (18)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A11,
),
"Mountain Village Springtime Grass (19)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A12,
),
"Mountain Village Springtime Grass (20)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A13,
),
"Mountain Village Springtime Grass (21)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A14,
),
"Mountain Village Springtime Grass (22)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A15,
),
"Mountain Village Springtime Grass (23)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A16,
),
"Mountain Village Springtime Grass (24)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A17,
),
"Mountain Village Springtime Grass (25)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A18,
),
"Mountain Village Springtime Grass (26)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A19,
),
"Mountain Village Springtime Grass (27)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A1A,
),
"Mountain Village Springtime Grass (28)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A1B,
),
"Mountain Village Springtime Grass (29)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A1C,
),
"Mountain Village Springtime Grass (30)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420125A1D,
),

# Mountain Village Keaton Grass (These ID's aren't shared anywhere else, must be fine?)

"Mountain Village Keaton Grass (28)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A1B,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (29)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A1C,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (30)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A1D,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (31)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A1E,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (32)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A1F,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (33)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A20,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (34)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A21,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (35)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A22,
    # can_create=lamda options: options.grasssanity.value
),
"Mountain Village Keaton Grass (36)": MMRLocationData(
    region="Mountain Village",
    address=0x3469420135A23,
    # can_create=lamda options: options.grasssanity.value
),

# Mountain Village Spring Grotto Grass (also not shared anywhere, must also be okay? Testing req.)

"Mountain Village Spring Grotto Grass (1)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC00,
),
"Mountain Village Spring Grotto Grass (2)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC01,
),
"Mountain Village Spring Grotto Grass (3)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC02,
),
"Mountain Village Spring Grotto Grass (4)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC03,
),
"Mountain Village Spring Grotto Grass (5)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC04,
),
"Mountain Village Spring Grotto Grass (6)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC05,
),
"Mountain Village Spring Grotto Grass (7)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC06,
),
"Mountain Village Spring Grotto Grass (8)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC07,
),
"Mountain Village Spring Grotto Grass (9)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC08,
),
"Mountain Village Spring Grotto Grass (10)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC09,
),
"Mountain Village Spring Grotto Grass (11)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC0A,
),
"Mountain Village Spring Grotto Grass (12)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC0B,
),
"Mountain Village Spring Grotto Grass (13)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC0C,
),
"Mountain Village Spring Grotto Grass (14)": MMRLocationData(
    region="Mountain Village",
    address=0x346942012AC0D,
),

# Twin Isles Spring Grass

"Twin Islands Springtime Grass Group 1 (1)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E0,
),
"Twin Islands Springtime Grass Group 1 (2)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E1,
),
"Twin Islands Springtime Grass Group 1 (3)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E2,
),
"Twin Islands Springtime Grass Group 1 (4)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E3,
),
"Twin Islands Springtime Grass Group 1 (5)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E4,
),
"Twin Islands Springtime Grass Group 1 (6)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E5,
),
"Twin Islands Springtime Grass Group 1 (7)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E6,
),
"Twin Islands Springtime Grass Group 1 (8)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E7,
),
"Twin Islands Springtime Grass Group 1 (9)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E8,
),
"Twin Islands Springtime Grass Group 1 (10)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005E9,
),
"Twin Islands Springtime Grass Group 1 (11)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005EA,
),
"Twin Islands Springtime Grass Group 1 (12)": MMRLocationData(
    region="Twin Islands",
    address=0x34694201005EB,
),

# Great Bay Coast Grass

"Great Bay Coast Grass (1)": MMRLocationData(
    region="Great Bay",
    address=0x3469420123700,
),
"Great Bay Coast Grass (2)": MMRLocationData(
    region="Great Bay",
    address=0x3469420123701,
),
"Great Bay Coast Grass (3)": MMRLocationData(
    region="Great Bay",
    address=0x3469420123702,
),
"Great Bay Coast Grass (4)": MMRLocationData(
    region="Great Bay",
    address=0x3469420123703,
),
"Great Bay Coast Grass (5)": MMRLocationData(
    region="Great Bay",
    address=0x3469420123704,
),

# Great Bay Coast Cow Grotto Grass

"Great Bay Coast Cow Grotto Grass Group 1 (1)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B70,
),
"Great Bay Coast Cow Grotto Grass Group 1 (2)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B71,
),
"Great Bay Coast Cow Grotto Grass Group 1 (3)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B72,
),
"Great Bay Coast Cow Grotto Grass Group 1 (4)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B73,
),
"Great Bay Coast Cow Grotto Grass Group 1 (5)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B74,
),
"Great Bay Coast Cow Grotto Grass Group 1 (6)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B75,
),
"Great Bay Coast Cow Grotto Grass Group 1 (7)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B76,
),
"Great Bay Coast Cow Grotto Grass Group 1 (8)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B77,
),
"Great Bay Coast Cow Grotto Grass Group 1 (9)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B78,
),
"Great Bay Coast Cow Grotto Grass Group 1 (10)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B79,
),
"Great Bay Coast Cow Grotto Grass Group 1 (11)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B7A,
),
"Great Bay Coast Cow Grotto Grass Group 1 (12)": MMRLocationData(
    region="Great Bay",
    address=0x3469420100B7B,
),
"Great Bay Coast Cow Grotto Grass Group 2 (1)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B70,
),
"Great Bay Coast Cow Grotto Grass Group 2 (2)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B71,
),
"Great Bay Coast Cow Grotto Grass Group 2 (3)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B72,
),
"Great Bay Coast Cow Grotto Grass Group 2 (4)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B73,
),
"Great Bay Coast Cow Grotto Grass Group 2 (5)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B74,
),
"Great Bay Coast Cow Grotto Grass Group 2 (6)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B75,
),
"Great Bay Coast Cow Grotto Grass Group 2 (7)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B76,
),
"Great Bay Coast Cow Grotto Grass Group 2 (8)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B77,
),
"Great Bay Coast Cow Grotto Grass Group 2 (9)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B78,
),
"Great Bay Coast Cow Grotto Grass Group 2 (10)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B79,
),
"Great Bay Coast Cow Grotto Grass Group 2 (11)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B7A,
),
"Great Bay Coast Cow Grotto Grass Group 2 (12)": MMRLocationData(
    region="Great Bay",
    address=0x3469420101B7B,
),
"Great Bay Coast Cow Grotto Grass Group 3 (1)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B70,
),
"Great Bay Coast Cow Grotto Grass Group 3 (2)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B71,
),
"Great Bay Coast Cow Grotto Grass Group 3 (3)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B72,
),
"Great Bay Coast Cow Grotto Grass Group 3 (4)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B73,
),
"Great Bay Coast Cow Grotto Grass Group 3 (5)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B74,
),
"Great Bay Coast Cow Grotto Grass Group 3 (6)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B75,
),
"Great Bay Coast Cow Grotto Grass Group 3 (7)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B76,
),
"Great Bay Coast Cow Grotto Grass Group 3 (8)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B77,
),
"Great Bay Coast Cow Grotto Grass Group 3 (9)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B78,
),
"Great Bay Coast Cow Grotto Grass Group 3 (10)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B79,
),
"Great Bay Coast Cow Grotto Grass Group 3 (11)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B7A,
),
"Great Bay Coast Cow Grotto Grass Group 3 (12)": MMRLocationData(
    region="Great Bay",
    address=0x3469420102B7B,
),
"Great Bay Coast Cow Grotto Grass Group 4 (1)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B70,
),
"Great Bay Coast Cow Grotto Grass Group 4 (2)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B71,
),
"Great Bay Coast Cow Grotto Grass Group 4 (3)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B72,
),
"Great Bay Coast Cow Grotto Grass Group 4 (4)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B73,
),
"Great Bay Coast Cow Grotto Grass Group 4 (5)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B74,
),
"Great Bay Coast Cow Grotto Grass Group 4 (6)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B75,
),
"Great Bay Coast Cow Grotto Grass Group 4 (7)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B76,
),
"Great Bay Coast Cow Grotto Grass Group 4 (8)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B77,
),
"Great Bay Coast Cow Grotto Grass Group 4 (9)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B78,
),
"Great Bay Coast Cow Grotto Grass Group 4 (10)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B79,
),
"Great Bay Coast Cow Grotto Grass Group 4 (11)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B7A,
),
"Great Bay Coast Cow Grotto Grass Group 4 (12)": MMRLocationData(
    region="Great Bay",
    address=0x3469420103B7B,
),
"Great Bay Coast Cow Grotto Grass Group 5 (1)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B70,
),
"Great Bay Coast Cow Grotto Grass Group 5 (2)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B71,
),
"Great Bay Coast Cow Grotto Grass Group 5 (3)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B72,
),
"Great Bay Coast Cow Grotto Grass Group 5 (4)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B73,
),
"Great Bay Coast Cow Grotto Grass Group 5 (5)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B74,
),
"Great Bay Coast Cow Grotto Grass Group 5 (6)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B75,
),
"Great Bay Coast Cow Grotto Grass Group 5 (7)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B76,
),
"Great Bay Coast Cow Grotto Grass Group 5 (8)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B77,
),
"Great Bay Coast Cow Grotto Grass Group 5 (9)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B78,
),
"Great Bay Coast Cow Grotto Grass Group 5 (10)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B79,
),
"Great Bay Coast Cow Grotto Grass Group 5 (11)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B7A,
),
"Great Bay Coast Cow Grotto Grass Group 5 (12)": MMRLocationData(
    region="Great Bay",
    address=0x3469420104B7B,
),
"Great Bay Coast Cow Grotto Grass Group 6 (1)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B70,
),
"Great Bay Coast Cow Grotto Grass Group 6 (2)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B71,
),
"Great Bay Coast Cow Grotto Grass Group 6 (3)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B72,
),
"Great Bay Coast Cow Grotto Grass Group 6 (4)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B73,
),
"Great Bay Coast Cow Grotto Grass Group 6 (5)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B74,
),
"Great Bay Coast Cow Grotto Grass Group 6 (6)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B75,
),
"Great Bay Coast Cow Grotto Grass Group 6 (7)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B76,
),
"Great Bay Coast Cow Grotto Grass Group 6 (8)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B77,
),
"Great Bay Coast Cow Grotto Grass Group 6 (9)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B78,
),
"Great Bay Coast Cow Grotto Grass Group 6 (10)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B79,
),
"Great Bay Coast Cow Grotto Grass Group 6 (11)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B7A,
),
"Great Bay Coast Cow Grotto Grass Group 6 (12)": MMRLocationData(
    region="Great Bay",
    address=0x3469420105B7B,
),

# Zora Cape Grotto Grass

"Zora Cape Grotto Grass (0)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A601,
),
"Zora Cape Grotto Grass (1)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A602,
),
"Zora Cape Grotto Grass (2)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A603,
),
"Zora Cape Grotto Grass (3)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A604,
),
"Zora Cape Grotto Grass (4)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A605,
),
"Zora Cape Grotto Grass (5)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A606,
),
"Zora Cape Grotto Grass (6)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A607,
),
"Zora Cape Grotto Grass (7)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A608,
),
"Zora Cape Grotto Grass (8)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A609,
),
"Zora Cape Grotto Grass (9)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A60A,
),
"Zora Cape Grotto Grass (10)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A60B,
),
"Zora Cape Grotto Grass (11)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A60C,
),
"Zora Cape Grotto Grass (12)": MMRLocationData(
    region="Zora Cape",
    address=0x346942012A60D,
),

# Road To Ikana Grotto Grass

"Road To Ikana Grotto Grass (1)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A700,
),
"Road To Ikana Grotto Grass (2)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A701,
),
"Road To Ikana Grotto Grass (3)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A702,
),
"Road To Ikana Grotto Grass (4)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A703,
),
"Road To Ikana Grotto Grass (5)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A704,
),
"Road To Ikana Grotto Grass (6)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A705,
),
"Road To Ikana Grotto Grass (7)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A706,
),
"Road To Ikana Grotto Grass (8)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A707,
),
"Road To Ikana Grotto Grass (9)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A708,
),
"Road To Ikana Grotto Grass (10)": MMRLocationData(
    region="TRoad to Ikana",
    address=0x346942012A709,
),
"Road To Ikana Grotto Grass (11)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A70A,
),
"Road To Ikana Grotto Grass (12)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A70B,
),
"Road To Ikana Grotto Grass (13)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A70C,
),
"Road To Ikana Grotto Grass (14)": MMRLocationData(
    region="Road to Ikana",
    address=0x346942012A70D,
),

# Ikana Graveyard Lower Region Grass

"Ikana Graveyard Lower Grass (1)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124300,
),
"Ikana Graveyard Lower Grass (2)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124301,
),
"Ikana Graveyard Lower Grass (3)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124302,
),
"Ikana Graveyard Lower Grass (4)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124303,
),
"Ikana Graveyard Lower Grass (5)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124304,
),

# Ikana Graveyard Upper Region Grass

"Ikana Graveyard Upper Grass (1)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124300,
),
"Ikana Graveyard Upper Grass (2)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124301,
),
"Ikana Graveyard Upper Grass (3)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124302,
),
"Ikana Graveyard Upper Grass (4)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124303,
),
"Ikana Graveyard Upper Grass (5)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124304,
),
"Ikana Graveyard Upper Grass (6)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124305,
),
"Ikana Graveyard Upper Grass (7)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124306,
),
"Ikana Graveyard Upper Grass (8)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124307,
),
"Ikana Graveyard Upper Grass (9)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x3469420124308,
),

# Ikana Graveyard Bombable Grotto Grass

"Ikana Graveyard Bombable Grotto Grass (1)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A900,
),
"Ikana Graveyard Bombable Grotto Grass (2)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A901,
),
"Ikana Graveyard Bombable Grotto Grass (3)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A902,
),
"Ikana Graveyard Bombable Grotto Grass (4)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A903,
),
"Ikana Graveyard Bombable Grotto Grass (5)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A904,
),
"Ikana Graveyard Bombable Grotto Grass (6)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A905,
),
"Ikana Graveyard Bombable Grotto Grass (7)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A906,
),
"Ikana Graveyard Bombable Grotto Grass (8)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A907,
),
"Ikana Graveyard Bombable Grotto Grass (9)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A908,
),
"Ikana Graveyard Bombable Grotto Grass (10)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A909,
),
"Ikana Graveyard Bombable Grotto Grass (11)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A90A,
),
"Ikana Graveyard Bombable Grotto Grass (12)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A90B,
),
"Ikana Graveyard Bombable Grotto Grass (13)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A90C,
),
"Ikana Graveyard Bombable Grotto Grass (14)": MMRLocationData(
    region="Ikana Graveyard",
    address=0x346942012A90D,
),

# Ikana Canyon Grass

"Ikana Canyon Grass (1)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121300,
),
"Ikana Canyon Grass (2)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121301,
),
"Ikana Canyon Grass (3)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121302,
),
"Ikana Canyon Grass (4)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121303,
),

# Ikana Canyon Grotto Grass

"Ikana Canyon Grotto Grass (1)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A500,
),
"Ikana Canyon Grotto Grass (2)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A501,
),
"Ikana Canyon Grotto Grass (3)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A502,
),
"Ikana Canyon Grotto Grass (4)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A503,
),
"Ikana Canyon Grotto Grass (5)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A504,
),
"Ikana Canyon Grotto Grass (6)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A505,
),
"Ikana Canyon Grotto Grass (7)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A506,
),
"Ikana Canyon Grotto Grass (8)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A507,
),
"Ikana Canyon Grotto Grass (9)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A508,
),
"Ikana Canyon Grotto Grass (10)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A509,
),
"Ikana Canyon Grotto Grass (11)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A50A,
),
"Ikana Canyon Grotto Grass (12)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A50B,
),
"Ikana Canyon Grotto Grass (13)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A50C,
),
"Ikana Canyon Grotto Grass (14)": MMRLocationData(
    region="Ikana Canyon",
    address=0x346942012A50D,
),

# Secret Shrine Grass

"Secret Shrine Entrance Grass (1)": MMRLocationData(
    region="Secret Shrine",
    address=0x3469420126000,
),
"Secret Shrine Entrance Grass (2)": MMRLocationData(
    region="Secret Shrine",
    address=0x3469420126001,
),
"Secret Shrine Entrance Grass (3)": MMRLocationData(
    region="Secret Shrine",
    address=0x3469420126002,
),
"Secret Shrine Entrance Grass (4)": MMRLocationData(
    region="Secret Shrine",
    address=0x3469420126003,
),
"Secret Shrine Entrance Grass (5)": MMRLocationData(
    region="Secret Shrine",
    address=0x3469420126004,
),
"Secret Shrine Entrance Grass (6)": MMRLocationData(
    region="Secret Shrine",
    address=0x3469420126005,
),
"Secret Shrine Dinolfos Grass (0)": MMRLocationData(
    region="Secret Shrine",
    address=0x126020,
),
"Secret Shrine Dinolfos Grass (1)": MMRLocationData(
    region="Secret Shrine",
    address=0x126021,
),
"Secret Shrine Dinolfos Grass (2)": MMRLocationData(
    region="Secret Shrine",
    address=0x126022,
),
"Secret Shrine Dinolfos Grass (3)": MMRLocationData(
    region="Secret Shrine",
    address=0x126023,
),
"Secret Shrine Wizzrobe Grass (0)": MMRLocationData(
    region="Secret Shrine",
    address=0x126033,
),
"Secret Shrine Wizzrobe Grass (1)": MMRLocationData(
    region="Secret Shrine",
    address=0x126032,
),
"Secret Shrine Wizzrobe Grass (2)": MMRLocationData(
    region="Secret Shrine",
    address=0x126030,
),
"Secret Shrine Wizzrobe Grass (3)": MMRLocationData(
    region="Secret Shrine",
    address=0x126031,
),
"Secret Shrine Wizzrobe Grass (4)": MMRLocationData(
    region="Secret Shrine",
    address=0x126034,
),
"Secret Shrine Wart Grass (0)": MMRLocationData(
    region="Secret Shrine",
    address=0x126042,
),
"Secret Shrine Wart Grass (1)": MMRLocationData(
    region="Secret Shrine",
    address=0x126043,
),
"Secret Shrine Wart Grass (2)": MMRLocationData(
    region="Secret Shrine",
    address=0x126045,
),
"Secret Shrine Wart Grass (3)": MMRLocationData(
    region="Secret Shrine",
    address=0x126044,
),
"Secret Shrine Wart Grass (4)": MMRLocationData(
    region="Secret Shrine",
    address=0x126047,
),
"Secret Shrine Wart Grass (5)": MMRLocationData(
    region="Secret Shrine",
    address=0x126046,
),
"Secret Shrine Wart Grass (6)": MMRLocationData(
    region="Secret Shrine",
    address=0x126040,
),
"Secret Shrine Wart Grass (7)": MMRLocationData(
    region="Secret Shrine",
    address=0x126041,
),
"Secret Shrine Garo Master Grass (0)": MMRLocationData(
    region="Secret Shrine",
    address=0x126055,
),
"Secret Shrine Garo Master Grass (1)": MMRLocationData(
    region="Secret Shrine",
    address=0x126052,
),
"Secret Shrine Garo Master Grass (2)": MMRLocationData(
    region="Secret Shrine",
    address=0x126051,
),
"Secret Shrine Garo Master Grass (3)": MMRLocationData(
    region="Secret Shrine",
    address=0x126050,
),
"Secret Shrine Garo Master Grass (4)": MMRLocationData(
    region="Secret Shrine",
    address=0x126054,
),
"Secret Shrine Garo Master Grass (5)": MMRLocationData(
    region="Secret Shrine",
    address=0x126053,
),

# Beneath the Well Grass

"Beneath the Well Left Side Back Room Grass (0)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B51,
),
"Beneath the Well Left Side Back Room Grasss (1)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B50,
),
"Beneath the Well Right Side Before Big Poe and Cow Grass (0)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B30,
),
"Beneath the Well Right Side Before Big Poe and Cow Grass (1)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B31,
),
"Beneath the Well Right Side Before Big Poe and Cow Grass (2)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B32,
),
"Beneath the Well Right Side Before Big Poe and Cow Grass (3)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B33,
),
"Beneath the Well Right Side Cow Grass (0)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B92,
),
"Beneath the Well Right Side Cow Grass (1)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B91,
),
"Beneath the Well Right Side Cow Grass (2)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B90,
),
"Beneath the Well Right Side Back Room Grass (0)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B71,
),
"Beneath the Well Right Side Back Room Grass (1)": MMRLocationData(
    region="Termina Field",
    address=0x124B72,
),
"Beneath the Well Right Side Back Room Grass (2)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B74,
),
"Beneath the Well Right Side Back Room Grass (3)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B73,
),
"Beneath the Well Right Side Back Room Grass (4)": MMRLocationData(
    region="Beneath the Well",
    address=0x124B70,
),

# Ikana Castle Grass

"Ikana Castle Grass (1)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D00,
),
"Ikana Castle Grass (2)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D01,
),
"Ikana Castle Grass (3)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D02,
),
"Ikana Castle Grass (4)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D03,
),
"Ikana Castle Grass (5)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D04,
),
"Ikana Castle Grass (6)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D05,
),
"Ikana Castle Grass (7)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D06,
),
"Ikana Castle Grass (8)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D07,
),
"Ikana Castle Grass (9)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D08,
),
"Ikana Castle Grass (10)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D09,
),
"Ikana Castle Grass (11)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D0A,
),
"Ikana Castle Grass (12)": MMRLocationData(
    region="Ikana Castle",
    address=0x3469420121D0B,
),

# Ikana Canyon Post Dungeon

"Ikana Canyon Post Dungeon Grass (1)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121300,
),
"Ikana Canyon Post Dungeon Grass (2)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121301,
),
"Ikana Canyon Post Dungeon Grass (3)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121302,
),
"Ikana Canyon Post Dungeon Grass (4)": MMRLocationData(
    region="Ikana Canyon",
    address=0x3469420121303,
),

# Dungeon Grass
# Woodfall Temple

"Woodfall Temple Entrance Room Grass (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B24,
),
"Woodfall Temple Entrance Room Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B21,
),
"Woodfall Temple Entrance Room Grass (2)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B20,
),
"Woodfall Temple Entrance Room Grass (3)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B22,
),
"Woodfall Temple Entrance Room Grass (4)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B23,
),
"Woodfall Temple Main Room Grass (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B11,
),
"Woodfall Temple Main Room Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B10,
),
"Woodfall Temple Main Room Grass (2)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B12,
),
"Woodfall Temple Deku Elevator Room Grass (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B50
),
"Woodfall Temple Deku Elevator Room Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B51
),
"Woodfall Temple Snapping Turtle Grass (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B61,
),
"Woodfall Temple Snapping Turtle Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B64,
),
"Woodfall Temple Snapping Turtle Grass (2)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B63,
),
"Woodfall Temple Snapping Turtle Grass (3)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B62,
),
"Woodfall Temple Snapping Turtle Grass (4)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B60,
),
"Woodfall Temple Dragonfly Chest Room Grass (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B40,
),
"Woodfall Temple Dragonfly Chest Room Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B41,
),
"Woodfall Temple Dragonfly Chest Room Grass (2)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B42,
),
"Woodfall Temple 2F Moving Flower Platform Room (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA1,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA3,
),
"Woodfall Temple2F Moving Flower Platform Room Grass (2)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA5,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (3)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA4,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (4)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA9,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (5)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA7,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (6)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA0,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (7)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA2,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (8)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BAA,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (9)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA8,
),
"Woodfall Temple 2F Moving Flower Platform Room Grass (10)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121BA6,
),
"Woodfall Temple Odolwas Lair Grass (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B00,
),
"Woodfall Temple Odolwas Lair Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B04,
),
"Woodfall Temple Odolwas Lair Grass (2)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B02,
),
"Woodfall Temple Odolwas Lair Grass (3)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B01,
),
"Woodfall Temple Odolwas Lair Grass (4)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121B03,
),
"Woodfall Temple Odolwas Lair Grass (0)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F0E,
),
"Woodfall Temple Odolwas Lair Grass (1)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F0C,
),
"Woodfall Temple Odolwas Lair Grass (2)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F0B,
),
"Woodfall Temple Odolwas Lair Grass (3)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F09,
),
"Woodfall Temple Odolwas Lair Grass (4)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F07,
),
"Woodfall Temple Odolwas Lair Grass (5)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F05,
),
"Woodfall Temple Odolwas Lair Grass (6)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F03,
),
"Woodfall Temple Odolwas Lair Grass (7)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F01,
),
"Woodfall Temple Odolwas Lair Grass (8)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F00,
),
"Woodfall Temple Odolwas Lair Grass (9)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F02,
),
"Woodfall Temple Odolwas Lair Grass (10)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F04,
),
"Woodfall Temple Odolwas Lair Grass (11)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F06,
),
"Woodfall Temple Odolwas Lair Grass (12)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F08,
),
"Woodfall Temple Odolwas Lair Grass (13)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F0A,
),
"Woodfall Temple Odolwas Lair (14)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F0D,
),
"Woodfall Temple Odolwas Lair (15)": MMRLocationData(
    region="Woodfall Temple",
    address=0x121F0F,
),

    # Stone Tower Temple Grass

"Stone Tower Temple Entrance Room Grass (0)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121600,
),

"Stone Tower Temple Entrance Room Grass (1)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121601,
),
"Stone Tower Temple Entrance Room Grass (2)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121602,
),
"Stone Tower Temple Elegy Maze Grass (0)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121623,
),
"Stone Tower Temple Elegy Maze Grass (1)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121621,
),
"Stone Tower Temple Elegy Maze Grass (2)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121624,
),
"Stone Tower Temple Elegy Maze Grass (3)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121620,
),
"Stone Tower Temple Elegy Maze Grass (4)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121622,
),
"Stone Tower Temple Elegy Maze Grass (5)":MMRLocationData(
    region="Stone Tower Temple",
    address=0x121625,
),

}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
