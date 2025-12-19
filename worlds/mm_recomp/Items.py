from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class MMRItem(Item):
    game = "Majora's Mask Recompiled"


class MMRItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True


item_data_table: Dict[str, MMRItemData] = {
    "Stray Fairy (Clock Town)": MMRItemData(
        code=0x346942001007F,
        type=ItemClassification.progression,
        can_create=lambda options: options.fairysanity.value
    ),
    "Progressive Magic": MMRItemData(
        code=0x3469420020000,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_great_fairy_rewards.value,
        num_exist=2
    ),
    "Great Spin Attack": MMRItemData(
        code=0x3469420020001,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_great_fairy_rewards.value
    ),
    "Double Defense": MMRItemData(
        code=0x3469420020003,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_great_fairy_rewards.value
    ),
    "Bomber's Notebook": MMRItemData(
        code=0x3469420000050,
        type=ItemClassification.progression,
    ),
    "Moon's Tear": MMRItemData(
        code=0x3469420000096,
        type=ItemClassification.progression
    ),
    "Land Title Deed": MMRItemData(
        code=0x3469420000097,
        type=ItemClassification.progression
    ),
    "Swamp Title Deed": MMRItemData(
        code=0x3469420000098,
        type=ItemClassification.progression
    ),
    "Mountain Title Deed": MMRItemData(
        code=0x3469420000099,
        type=ItemClassification.progression
    ),
    "Ocean Title Deed": MMRItemData(
        code=0x346942000009A,
        type=ItemClassification.progression
    ),
    "Ocarina of Time": MMRItemData(
        code=0x346942000004C,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Heart Piece": MMRItemData(
        code=0x346942000000C,
        type=ItemClassification.useful,
        num_exist=36
        # ~ num_exist=52
    ),
    "Heart Container": MMRItemData(
        code=0x346942000000D,
        type=ItemClassification.useful,
        num_exist=8
        # ~ num_exist=4
    ),
    "Swamp Skulltula Token": MMRItemData(
        code=0x3469420000075,
        type=ItemClassification.progression,
        num_exist=30,
        can_create=lambda options: options.skullsanity.value == 1
    ),
    "Ocean Skulltula Token": MMRItemData(
        code=0x3469420000072,
        type=ItemClassification.progression,
        num_exist=30,
        can_create=lambda options: options.skullsanity.value == 1
    ),
    "Progressive Wallet": MMRItemData(
        code=0x3469420000008,
        type=ItemClassification.progression,
        num_exist=1
    ),
    "Sonata of Awakening": MMRItemData(
        code=0x3469420040061,
        type=ItemClassification.progression
    ),
    "Goron Lullaby": MMRItemData(
        code=0x3469420040062,
        type=ItemClassification.progression
    ),
    "New Wave Bossa Nova": MMRItemData(
        code=0x3469420040063,
        type=ItemClassification.progression
    ),
    "Elegy of Emptiness": MMRItemData(
        code=0x3469420040064,
        type=ItemClassification.progression
    ),
    "Oath to Order": MMRItemData(
        code=0x3469420040065,
        type=ItemClassification.progression
    ),
    "Song of Time": MMRItemData(
        code=0x3469420040067,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Song of Healing": MMRItemData(
        code=0x3469420040068,
        type=ItemClassification.progression
    ),
    "Epona's Song": MMRItemData(
        code=0x3469420040069,
        type=ItemClassification.progression
    ),
    "Song of Soaring": MMRItemData(
        code=0x346942004006A,
        type=ItemClassification.progression,
        can_create=lambda options: options.start_with_soaring.value == 0
    ),
    "Song of Storms": MMRItemData(
        code=0x346942004006B,
        type=ItemClassification.progression
    ),
    "Deku Mask": MMRItemData(
        code=0x3469420000078,
        type=ItemClassification.progression
    ),
    "Goron Mask": MMRItemData(
        code=0x3469420000079,
        type=ItemClassification.progression
    ),
    "Zora Mask": MMRItemData(
        code=0x346942000007A,
        type=ItemClassification.progression
    ),
    "Fierce Deity's Mask": MMRItemData(
        code=0x346942000007B,
        type=ItemClassification.progression
    ),
    "Captain's Hat": MMRItemData(
        code=0x346942000007C,
        type=ItemClassification.progression
    ),
    "Giant's Mask": MMRItemData(
        code=0x346942000007D,
        type=ItemClassification.progression
    ),
    "All-Night Mask": MMRItemData(
        code=0x346942000007E,
        type=ItemClassification.progression
    ),
    "Bunny Hood": MMRItemData(
        code=0x346942000007F,
        type=ItemClassification.progression
    ),
    "Keaton Mask": MMRItemData(
        code=0x3469420000080,
        type=ItemClassification.progression
    ),
    "Garo Mask": MMRItemData(
        code=0x3469420000081,
        type=ItemClassification.progression
    ),
    "Romani Mask": MMRItemData(
        code=0x3469420000082,
        type=ItemClassification.progression
    ),
    "Circus Leader's Mask": MMRItemData(
        code=0x3469420000083,
        type=ItemClassification.progression
    ),
    "Postman's Hat": MMRItemData(
        code=0x3469420000084,
        type=ItemClassification.progression
    ),
    "Couple's Mask": MMRItemData(
        code=0x3469420000085,
        type=ItemClassification.progression
    ),
    "Great Fairy Mask": MMRItemData(
        code=0x3469420000086,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_great_fairy_rewards.value
    ),
    "Gibdo Mask": MMRItemData(
        code=0x3469420000087,
        type=ItemClassification.progression
    ),
    "Don Gero Mask": MMRItemData(
        code=0x3469420000088,
        type=ItemClassification.progression
    ),
    "Kamaro Mask": MMRItemData(
        code=0x3469420000089,
        type=ItemClassification.progression
    ),
    "Mask of Truth": MMRItemData(
        code=0x346942000008A,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_spiderhouse_reward.value
    ),
    "Stone Mask": MMRItemData(
        code=0x346942000008B,
        type=ItemClassification.progression
    ),
    "Bremen Mask": MMRItemData(
        code=0x346942000008C,
        type=ItemClassification.progression
    ),
    "Blast Mask": MMRItemData(
        code=0x346942000008D,
        type=ItemClassification.progression
    ),
    "Mask of Scents": MMRItemData(
        code=0x346942000008E,
        type=ItemClassification.progression
    ),
    "Kafei's Mask": MMRItemData(
        code=0x346942000008F,
        type=ItemClassification.progression
    ),
    "Room Key": MMRItemData(
        code=0x34694200000A0,
        type=ItemClassification.progression
    ),
    "Letter to Kafei": MMRItemData(
        code=0x34694200000AA,
        type=ItemClassification.progression
    ),
    "Pendant of Memories": MMRItemData(
        code=0x34694200000AB,
        type=ItemClassification.progression
    ),
    "Priority Mail": MMRItemData(
        code=0x34694200000A1,
        type=ItemClassification.progression
    ),
    "Bottle": MMRItemData(
        code=0x346942000005A,
        type=ItemClassification.progression,
        num_exist=3
    ),
    "Bottle of Milk": MMRItemData(
        code=0x3469420000060,
        type=ItemClassification.progression
    ),
    "Bottle of Chateau Romani": MMRItemData(
        code=0x346942000006F,
        type=ItemClassification.progression
    ),
    "Progressive Sword": MMRItemData(
        code=0x3469420000037,
        type=ItemClassification.progression,
        num_exist=2
    ),
    "Great Fairy Sword": MMRItemData(
        code=0x346942000003B,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_great_fairy_rewards.value
    ),
    "Progressive Bow": MMRItemData(
        code=0x3469420000022,
        type=ItemClassification.progression,
        num_exist=3
    ),
    "Fire Arrow": MMRItemData(
        code=0x3469420000025,
        type=ItemClassification.progression
    ),
    "Ice Arrow": MMRItemData(
        code=0x3469420000026,
        type=ItemClassification.progression
    ),
    "Light Arrow": MMRItemData(
        code=0x3469420000027,
        type=ItemClassification.progression
    ),
    "Pictograph Box": MMRItemData(
        code=0x3469420000043,
        type=ItemClassification.progression
    ),
    "Lens of Truth": MMRItemData(
        code=0x3469420000042,
        type=ItemClassification.progression
    ),
    "Hookshot": MMRItemData(
        code=0x3469420000041,
        type=ItemClassification.progression
    ),
    "Progressive Shield": MMRItemData(
        code=0x3469420000032,
        type=ItemClassification.progression
    ),
    "Powder Keg": MMRItemData(
        code=0x3469420000034,
        type=ItemClassification.progression
    ),
    "Magic Bean": MMRItemData(
        code=0x3469420000035,
        type=ItemClassification.progression
    ),
    "Bottle of Red Potion": MMRItemData(
        code=0x3469420000059,
        type=ItemClassification.progression
    ),
    # ~ "Blue Potion": MMRItemData(
        # ~ code=0x346942000005D,
        # ~ type=ItemClassification.progression
    # ~ ),
    "Clock Town Map": MMRItemData(
        code=0x34694200000B4,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_regional_maps.value == 2
    ),
    "Woodfall Map": MMRItemData(
        code=0x34694200000B5,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_regional_maps.value == 2
    ),
    "Snowhead Map": MMRItemData(
        code=0x34694200000B6,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_regional_maps.value == 2
    ),
    "Romani Ranch Map": MMRItemData(
        code=0x34694200000B7,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_regional_maps.value == 2
    ),
    "Great Bay Map": MMRItemData(
        code=0x34694200000B8,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_regional_maps.value == 2
    ),
    "Stone Tower Map": MMRItemData(
        code=0x34694200000B9,
        type=ItemClassification.useful,
        can_create=lambda options: options.shuffle_regional_maps.value == 2
    ),
    "Stray Fairy (Woodfall)": MMRItemData(
        code=0x3469420010000,
        type=ItemClassification.progression,
        num_exist=15,
        can_create=lambda options: options.fairysanity.value
    ),
    "Stray Fairy (Snowhead)": MMRItemData(
        code=0x3469420010001,
        type=ItemClassification.progression,
        num_exist=15,
        can_create=lambda options: options.fairysanity.value
    ),
    "Stray Fairy (Great Bay)": MMRItemData(
        code=0x3469420010002,
        type=ItemClassification.progression,
        num_exist=15,
        can_create=lambda options: options.fairysanity.value
    ),
    "Stray Fairy (Stone Tower)": MMRItemData(
        code=0x3469420010003,
        type=ItemClassification.progression,
        num_exist=15,
        can_create=lambda options: options.fairysanity.value
    ),
    "Small Key (Woodfall)": MMRItemData(
        code=0x3469420090078,
        type=ItemClassification.progression,
        num_exist=1,
        can_create=lambda options: options.keysanity.value
    ),
    "Small Key (Snowhead)": MMRItemData(
        code=0x3469420090178,
        type=ItemClassification.progression,
        num_exist=3,
        can_create=lambda options: options.keysanity.value
    ),
    "Small Key (Great Bay)": MMRItemData(
        code=0x3469420090278,
        type=ItemClassification.progression,
        num_exist=1,
        can_create=lambda options: options.keysanity.value
    ),
    "Small Key (Stone Tower)": MMRItemData(
        code=0x3469420090378,
        type=ItemClassification.progression,
        num_exist=4,
        can_create=lambda options: options.keysanity.value
    ),
    "Dungeon Map (Woodfall)": MMRItemData(
        code=0x3469420090076,
        type=ItemClassification.useful
    ),
    "Dungeon Map (Snowhead)": MMRItemData(
        code=0x3469420090176,
        type=ItemClassification.useful
    ),
    "Dungeon Map (Great Bay)": MMRItemData(
        code=0x3469420090276,
        type=ItemClassification.useful
    ),
    "Dungeon Map (Stone Tower)": MMRItemData(
        code=0x3469420090376,
        type=ItemClassification.useful
    ),
    "Compass (Woodfall)": MMRItemData(
        code=0x3469420090075,
        type=ItemClassification.useful
    ),
    "Compass (Snowhead)": MMRItemData(
        code=0x3469420090175,
        type=ItemClassification.useful
    ),
    "Compass (Great Bay)": MMRItemData(
        code=0x3469420090275,
        type=ItemClassification.useful
    ),
    "Compass (Stone Tower)": MMRItemData(
        code=0x3469420090375,
        type=ItemClassification.useful
    ),
    "Boss Key (Woodfall)": MMRItemData(
        code=0x3469420090074,
        type=ItemClassification.progression,
        can_create=lambda options: options.bosskeysanity.value
    ),
    "Boss Key (Snowhead)": MMRItemData(
        code=0x3469420090174,
        type=ItemClassification.progression,
        can_create=lambda options: options.bosskeysanity.value
    ),
    "Boss Key (Great Bay)": MMRItemData(
        code=0x3469420090274,
        type=ItemClassification.progression,
        can_create=lambda options: options.bosskeysanity.value
    ),
    "Boss Key (Stone Tower)": MMRItemData(
        code=0x3469420090374,
        type=ItemClassification.progression,
        can_create=lambda options: options.bosskeysanity.value
    ),
    "Odolwa's Remains": MMRItemData(
        code=0x3469420000055,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_boss_remains.value == 1
    ),
    "Goht's Remains": MMRItemData(
        code=0x3469420000056,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_boss_remains.value == 1
    ),
    "Gyorg's Remains": MMRItemData(
        code=0x3469420000057,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_boss_remains.value == 1
    ),
    "Twinmold's Remains": MMRItemData(
        code=0x3469420000058,
        type=ItemClassification.progression,
        can_create=lambda options: options.shuffle_boss_remains.value == 1
    ),
    "Progressive Bomb Bag": MMRItemData(
        code=0x346942000001B,
        type=ItemClassification.progression,
        num_exist=3
    ),
    "Bundle of 10 Arrows": MMRItemData(
        code=0x346942000001E,
        type=ItemClassification.filler,
        num_exist=1
    ),
    "Bundle of 30 Arrows": MMRItemData(
        code=0x346942000001F,
        type=ItemClassification.filler,
        num_exist=1
    ),
    "Small Magic Jar": MMRItemData(
        code=0x346942000000E,
        type=ItemClassification.filler,
        num_exist=1
    ),
    "Large Magic Jar": MMRItemData(
        code=0x346942000000F,
        type=ItemClassification.filler,
        num_exist=1
    ),
    "Bomb Refill 10": MMRItemData(
        code=0x3469420000016,
        type=ItemClassification.filler,
        num_exist=1
    ),
    "Bomb Refill 30": MMRItemData(
        code=0x3469420000018,
        type=ItemClassification.filler,
        num_exist=1
    ),
    "Deku Nuts 10": MMRItemData(
        code=0x346942000002A,
        type=ItemClassification.filler,
        num_exist=1
    ),
    # "Deku Nuts Upgrade 30": MMRItemData(
    #     code=0x346942000009D,
    #     type=ItemClassification.filler,
    #     num_exist=1
    # ),
    # "Deku Nuts Upgrade 40": MMRItemData(
    #     code=0x346942000009E,
    #     type=ItemClassification.filler,
    #     num_exist=1
    # ),
    "Deku Stick": MMRItemData(
        code=0x3469420000019,
        type=ItemClassification.filler,
        num_exist=1
    ),    
    # "Deku Stick Upgrade 20": MMRItemData(
    #     code=0x346942000009B,
    #     type=ItemClassification.filler,
    #     num_exist=1
    # ),
    # "Deku Stick Upgrade 30": MMRItemData(
    #     code=0x346942000009C,
    #     type=ItemClassification.filler,
    #     num_exist=1
    # ),     
    "Recovery Heart": MMRItemData(
        code=0x346942000000A,
        type=ItemClassification.filler,
        num_exist=1
    ),                                    
    "Progressive Bombchu Bag": MMRItemData(
        code=0x3469420000054,
        type=ItemClassification.progression,
        num_exist=3
    ), 
    "Bombchu (1)": MMRItemData(
        code=0x3469420000036,
        type=ItemClassification.filler,
        num_exist=4,
        can_create=lambda options: False
    ),
    "Bombchu (5)": MMRItemData(
        code=0x346942000003A,
        type=ItemClassification.filler,
        num_exist=2,
        can_create=lambda options: False
    ),
    "Bombchu (10)": MMRItemData(
        code=0x346942000001A,
        type=ItemClassification.filler,
        num_exist=5,
        can_create=lambda options: False
    ),
    "Blue Rupee": MMRItemData(
        code=0x3469420000002,
        type=ItemClassification.filler,
        num_exist=6
        # ~ num_exist=6
    ),
    "Crimson Rupee": MMRItemData(
        code=0x3469420000003,
        type=ItemClassification.progression,
        num_exist=1
    ),
    "Red Rupee": MMRItemData(
        code=0x3469420000004,
        type=ItemClassification.filler,
        num_exist=29
        # ~ num_exist=29
    ),
    "Purple Rupee": MMRItemData(
        code=0x3469420000005,
        type=ItemClassification.filler,
        num_exist=11
    ),
    "Silver Rupee": MMRItemData(
        code=0x3469420000006,
        type=ItemClassification.filler,
        num_exist=7
    ),
    "Gold Rupee": MMRItemData(
        code=0x3469420000007,
        type=ItemClassification.filler,
        num_exist=3
    ),
    "Victory": MMRItemData(
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    # Owl Statues
    "Clock Town Owl Statue": MMRItemData(
        code=0x3469420FF1504,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Milk Road Owl Statue": MMRItemData(
        code=0x3469420FF1505,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Southern Swamp Owl Statue": MMRItemData(
        code=0x3469420FF1507,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Woodfall Owl Statue": MMRItemData(
        code=0x3469420FF1506,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Mountain Village Owl Statue": MMRItemData(
        code=0x3469420FF1503,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Snowhead Owl Statue": MMRItemData(
        code=0x3469420FF1502,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Great Bay Coast Owl Statue": MMRItemData(
        code=0x3469420FF1500,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Zora Cape Owl Statue": MMRItemData(
        code=0x3469420FF1501,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Ikana Canyon Owl Statue": MMRItemData(
        code=0x3469420FF1508,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    "Stone Tower Owl Statue": MMRItemData(
        code=0x3469420FF1509,
        type=ItemClassification.progression,
        can_create=lambda options: options.owlsanity.value
    ),
    # Frogs
    "Yellow Frog": MMRItemData(
        code=0x3469420FF0000,
        type=ItemClassification.progression,
        can_create=lambda options: options.frogsanity.value
    ),
    "White Frog": MMRItemData(
        code=0x3469420FF0004,
        type=ItemClassification.progression,
        can_create=lambda options: options.frogsanity.value
    ),
    "Cyan Frog": MMRItemData(
        code=0x3469420FF0003,
        type=ItemClassification.progression,
        can_create=lambda options: options.frogsanity.value
    ),
    "Blue Frog": MMRItemData(
        code=0x3469420FF0001,
        type=ItemClassification.progression,
        can_create=lambda options: options.frogsanity.value
    ),
    "Pink Frog": MMRItemData(
        code=0x3469420FF0002,
        type=ItemClassification.progression,
        can_create=lambda options: options.frogsanity.value
    ),
    # Scarecrows
    "Clock Town Trading Post Scarecrow": MMRItemData(
        code=0x3469420303400,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Astral Observatory Scarecrow": MMRItemData(
        code=0x3469420302910,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Mountain Village Rooftop Scarecrow": MMRItemData(
        code=0x3469420305000,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Mountain Village Spring Rooftop Scarecrow": MMRItemData(
        code=0x3469420305A00,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Path to Snowhead Scarecrow": MMRItemData(
        code=0x3469420305B00,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Path to Snowhead Spring Scarecrow": MMRItemData(
        code=0x3469420305C00,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Twin Islands Scarecrow": MMRItemData(
        code=0x3469420305D00,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Twin Islands Spring Scarecrow": MMRItemData(
        code=0x3469420305E00,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Snowhead Temple Lower Scarecrow": MMRItemData(
        code=0x3469420302140,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Snowhead Temple Hidden Alcove Scarecrow": MMRItemData(
        code=0x3469420302141,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),        
    "Great Bay Coast Rock Wall Scarecrow": MMRItemData(
        code=0x3469420303700,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),    
    "Zora Cape Beavers Scarecrow": MMRItemData(
        code=0x3469420303800,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ), 
    "Zora Cape Island Scarecrow": MMRItemData(
        code=0x3469420303801,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Zora Hall Pervert Scarecrow": MMRItemData(
        code=0x3469420303300,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ), 
    "Road to Ikana Scarecrow": MMRItemData(
        code=0x3469420305300,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Stone Tower Lower Scarecrow": MMRItemData(
        code=0x3469420305800,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    "Stone Tower Upper Scarecrow": MMRItemData(
        code=0x3469420305801,
        type=ItemClassification.progression,
        can_create=lambda options: options.scarecrowsanity.value
    ),
    # Souls
    # Boss Souls
    "Soul of Odolwa": MMRItemData(
        code=0x34694200B0129,
        type=ItemClassification.progression,
        can_create=lambda options: options.boss_souls.value
    ),
    "Soul of Goht": MMRItemData(
        code=0x34694200B01DD,
        type=ItemClassification.progression,
        can_create=lambda options: options.boss_souls.value
    ),
    "Soul of Gyorg": MMRItemData(
        code=0x34694200B012B,
        type=ItemClassification.progression,
        can_create=lambda options: options.boss_souls.value
    ),
    "Soul of Twinmold": MMRItemData(
        code=0x34694200B012A,
        type=ItemClassification.progression,
        can_create=lambda options: options.boss_souls.value
    ),
    "Soul of Majora": MMRItemData(
        code=0x34694200B012F,
        type=ItemClassification.progression,
        can_create=lambda options: options.boss_souls.value == 2 and not options.completion_goal.value
    ),
    # Misc. Souls
    "Soul of Cows": MMRItemData(
        code=0x34694200A00F3,
        type=ItemClassification.progression,
        can_create=lambda options: options.misc_souls.value
    ),
    "Soul of Keaton": MMRItemData(
        code=0x34694200A028C,
        type=ItemClassification.progression,
        can_create=lambda options: options.misc_souls.value
    ),
    "Soul of Gold Skulltulas": MMRItemData(
        code=0x34694200A0050,
        type=ItemClassification.progression,
        can_create=lambda options: options.misc_souls.value
    ),
    "Soul of Butterflies": MMRItemData(
        code=0x34694200A0015,
        type=ItemClassification.progression,
        can_create=lambda options: options.misc_souls.value
    ),
    # NPC Souls
    "Soul of Anju": MMRItemData(
        code=0x34694200C0202,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Anju's Grandmother": MMRItemData(
        code=0x34694200C0243,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Anju's Mother": MMRItemData(
        code=0x34694200C0253,
        type=ItemClassification.filler,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Kafei": MMRItemData(
        code=0x34694200C0159,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Toilet Hand": MMRItemData(
        code=0x34694200C027D,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Guru-Guru": MMRItemData(
        code=0x34694200C0248,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Honey and Darling": MMRItemData(
        code=0x34694200C00B5,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Treasure Game Lady": MMRItemData(
        code=0x34694200C01C1,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Toto & Gorman": MMRItemData(
        code=0x34694200C0234,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Barten": MMRItemData(
        code=0x34694200C0263,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Madame Aroma": MMRItemData(
        code=0x34694200C0262,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Receptionist": MMRItemData(
        code=0x34694200C0290,
        type=ItemClassification.filler,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Council": MMRItemData(
        code=0x34694200C026F,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Guards": MMRItemData(
        code=0x34694200C01C7,
        type=ItemClassification.filler,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Bomber Kids": MMRItemData(
        code=0x34694200C027E,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Tingle": MMRItemData(
        code=0x34694200C0176,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Bomb Granny": MMRItemData(
        code=0x34694200C0236,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Sakon": MMRItemData(
        code=0x34694200C0237,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Deku Playground Employee": MMRItemData(
        code=0x34694200C01C9,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Great Fairies": MMRItemData(
        code=0x34694200C0130,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Archery Man": MMRItemData(
        code=0x34694200C011D,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Postman": MMRItemData(
        code=0x34694200C01D5,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    # "Soul of Bomb Shop Owner": MMRItemData(
    #     code=0x34694200C0016,
    #     type=ItemClassification.progression,
    #     can_create=lambda options: options.npc_souls.value
    # ),
    "Soul of Shop Owners": MMRItemData(
        code=0x34694200C002A,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    # "Soul of Trading Post Night Worker": MMRItemData(
    #     code=0x34694200C0018,
    #     type=ItemClassification.progression,
    #     can_create=lambda options: options.npc_souls.value
    # ),
    "Soul of Scarecrow": MMRItemData(
        code=0x34694200C00CA,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Curiosity Shop Man": MMRItemData(
        code=0x34694200C01C4,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Happy Mask Salesman": MMRItemData(
        code=0x34694200C01B5,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Skull Kid": MMRItemData(
        code=0x34694200C0191,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Kamaro": MMRItemData(
        code=0x34694200C027A,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    # "Soul of Shooting Gallery Man": MMRItemData(
    #     code=0x34694200C001E,
    #     type=ItemClassification.progression,
    #     can_create=lambda options: options.npc_souls.value
    # ),
    "Soul of Jugglers": MMRItemData(
        code=0x34694200C0244,
        type=ItemClassification.filler,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Carpenters": MMRItemData(
        code=0x34694200C009C,
        type=ItemClassification.filler,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Spider Man": MMRItemData(
        code=0x34694200C00D4,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Business Scrubs": MMRItemData(
        code=0x34694200C0274,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Astral Observatory Man": MMRItemData(
        code=0x34694200C0124,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Keg Selling Goron": MMRItemData(
        code=0x34694200C0242,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Inn Goron": MMRItemData(
        code=0x34694200C0276,
        type=ItemClassification.filler,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Swordsman": MMRItemData(
        code=0x34694200C01EF,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Banker": MMRItemData(
        code=0x34694200C0177,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Rosa Sisters": MMRItemData(
        code=0x34694200C027B,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Lottery": MMRItemData(
        code=0x34694200C0239,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Romani & Cremia": MMRItemData(
        code=0x34694200C021F,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Grog": MMRItemData(
        code=0x34694200C00A6,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Doggy Race Lady & Dogs": MMRItemData(
        code=0x34694200C0117,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Gorman Brothers": MMRItemData(
        code=0x34694200C0067,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Swamp Tourist Guide": MMRItemData(
        code=0x34694200C01C5,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Kotake": MMRItemData(
        code=0x34694200C0188,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Koume": MMRItemData(
        code=0x34694200C0187,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Deku Palace Entry Guards": MMRItemData(
        code=0x34694200C01A0,
        type=ItemClassification.useful,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Deku Palace Searching Guards": MMRItemData(
        code=0x34694200C017A,
        type=ItemClassification.useful,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Monkey": MMRItemData(
        code=0x34694200C019E,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Bean Daddy": MMRItemData(
        code=0x34694200C00A5,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Goron Elder": MMRItemData(
        code=0x34694200C0213,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Gatekeeper & Medigoron": MMRItemData(
        code=0x34694200C0138,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Hungry Goron": MMRItemData(
        code=0x34694200C023A,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Mountain Smithy": MMRItemData(
        code=0x34694200C01FF,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Fisherman": MMRItemData(
        code=0x34694200C01C2,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Marine Lab Researcher": MMRItemData(
        code=0x34694200C00AE,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Coast Zora": MMRItemData(
        code=0x34694200C0260,
        type=ItemClassification.useful,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Pot Game & Hall Zora": MMRItemData(
        code=0x34694200C0228,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Lulu": MMRItemData(
        code=0x34694200C0252,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Shiro": MMRItemData(
        code=0x34694200C024A,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Stalchildren": MMRItemData(
        code=0x34694200C00ED,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Dampe": MMRItemData(
        code=0x34694200C01CA,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Composer Poe": MMRItemData(
        code=0x34694200C0247,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Pamela's Father": MMRItemData(
        code=0x34694200C0250,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Gibdos": MMRItemData(
        code=0x34694200C01DA,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Spirit House Owner": MMRItemData(
        code=0x34694200C01DE,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    "Soul of Moon Kids": MMRItemData(
        code=0x34694200C00BF,
        type=ItemClassification.progression,
        can_create=lambda options: options.npc_souls.value
    ),
    # Utility Souls
    "Soul of Postboxes": MMRItemData(
        code=0x34694200D01F2,
        type=ItemClassification.progression,
        can_create=lambda options: options.utility_souls.value
    ),
    # Absurd Souls
    "Soul of Songwall": MMRItemData(
        code=0x34694200F01D6,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Trees & Bushes": MMRItemData(
        code=0x34694200F0041,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Grass": MMRItemData(
        code=0x34694200F010B,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Grottos": MMRItemData(
        code=0x34694200F0055,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Deku Flowers": MMRItemData(
        code=0x34694200F0183,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Barrels": MMRItemData(
        code=0x34694200F022D,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Gorman Ranch Bulldozer": MMRItemData(
        code=0x34694200F0287,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Pots": MMRItemData(
        code=0x34694200F0082,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Rocks": MMRItemData(
        code=0x34694200F00B0,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    "Soul of Signs": MMRItemData(
        code=0x34694200F00A8,
        type=ItemClassification.progression,
        can_create=lambda options: options.absurd_souls.value
    ),
    # Enemy Souls
    "Soul of Guays": MMRItemData(
        code=0x34694200E00F1,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Takkuri": MMRItemData(
        code=0x34694200E0291,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Wolfos": MMRItemData(
        code=0x34694200E00EC,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Chu Jelly": MMRItemData(
        code=0x34694200E014A,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Deku Baba": MMRItemData(
        code=0x34694200E0033,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Real Bombchu": MMRItemData(
        code=0x34694200E016F,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Eenos": MMRItemData(
        code=0x34694200E01E6,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Tektite": MMRItemData(
        code=0x34694200E0012,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Peehats": MMRItemData(
        code=0x34694200E0014,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Dodongos": MMRItemData(
        code=0x34694200E000B,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Dragonflies": MMRItemData(
        code=0x34694200E0109,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Gekko": MMRItemData(
        code=0x34694200E0007,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Boes": MMRItemData(
        code=0x34694200E0164,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Hanging Skulltulas": MMRItemData(
        code=0x34694200E0024,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Dinolfos": MMRItemData(
        code=0x34694200E0019,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Snappers": MMRItemData(
        code=0x34694200E01BA,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Carnivorous Lilypad": MMRItemData(
        code=0x34694200E013A,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Freezard": MMRItemData(
        code=0x34694200E008F,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Wizrobe": MMRItemData(
        code=0x34694200E015D,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Pirate Guards": MMRItemData(
        code=0x34694200E021E,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Coloured Pirates": MMRItemData(
        code=0x34694200E021D,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Giant Bonefish": MMRItemData(
        code=0x34694200E014B,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Wart": MMRItemData(
        code=0x34694200E012C,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Ocotoroks": MMRItemData(
        code=0x34694200E0008,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Jellied Gekko": MMRItemData(
        code=0x34694200E0065,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Iron Knuckle": MMRItemData(
        code=0x34694200E0084,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Bad Bats": MMRItemData(
        code=0x34694200E015B,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Keese": MMRItemData(
        code=0x34694200E000C,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Leevers": MMRItemData(
        code=0x34694200E0216,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Garo": MMRItemData(
        code=0x34694200E0113,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Garo Master": MMRItemData(
        code=0x34694200E0182,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Armos": MMRItemData(
        code=0x34694200E0032,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Death Armos": MMRItemData(
        code=0x34694200E002D,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Eyegore": MMRItemData(
        code=0x34694200E0184,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Redead": MMRItemData(
        code=0x34694200E004C,
        type=ItemClassification.filler,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Igos": MMRItemData(
        code=0x34694200E0115,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),
    "Soul of Gomess": MMRItemData(
        code=0x34694200E0043,
        type=ItemClassification.progression,
        can_create=lambda options: options.enemy_souls.value
    ),


}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
code_to_item_table = {data.code: name for name, data in item_data_table.items() if data.code is not None}
