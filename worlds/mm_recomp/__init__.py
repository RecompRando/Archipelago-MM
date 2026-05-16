from typing import List
from typing import Dict
from typing import TextIO, ClassVar

from BaseClasses import Region, Tutorial, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import MMRItem, item_data_table, item_table, code_to_item_table
from .Locations import MMRLocation, location_data_table, location_table, code_to_location_table, locked_locations
from .Options import MMROptions
from .Regions import region_data_table, get_exit
from .Rules import *
from .NormalRules import *
from .Constants import default_shop_prices

class MMRWebWorld(WebWorld):
    # ~ theme = "partyTime"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Majora's Mask Recompiled in Archipelago.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["LittleCube", "ThatHypedPerson", "PixelShake92", "Muervo_"]
    )
    
    tutorials = [setup_en]


class MMRWorld(World):
    """A Zelda game we're not completely burnt out on."""

    game = "Majora's Mask Recompiled"
    data_version = 1
    web = MMRWebWorld()
    options_dataclass = MMROptions
    options = MMROptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    prices_ints: List[int]
    prices: str

    #item_name_groups: ClassVar[dict[str, set[str]]] = item_name_groups

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #
    #    self.dungeon_local_item_names: set[str] = set()
    #    self.dungeon_specific_item_names: set[str] = set()

    def generate_early(self):

        #for dungeon_item in ["shuffle_small_keys", "shuffle_boss_keys", "shuffle_maps_and_compasses", "shuffle_stray_fairies"]:
        #    option = getattr(self.options, dungeon_item)
        #    if option == "local":
        #        self.options.local_items.value |= self.item_name_groups[option.item_name_group]
        #    elif option.in_dungeon:
        #        self.dungeon_local_item_names |= self.item_name_groups[option.item_name_group]
        #        if option == "dungeon":
        #            self.dungeon_specific_item_names |= self.item_name_groups[option.item_name_group]
        #        else:
        #            self.options.local_items.value |= self.dungeon_local_item_names

        if self.options.shuffle_stray_fairies.value == 4:
            self.options.local_items.value.add("Stray Fairy (Clock Town)")
            self.options.local_items.value.add("Stray Fairy (Woodfall)")
            self.options.local_items.value.add("Stray Fairy (Snowhead)")
            self.options.local_items.value.add("Stray Fairy (Great Bay)")
            self.options.local_items.value.add("Stray Fairy (Stone Tower)")

        if self.options.shuffle_maps_and_compasses.value == 4:
            self.options.local_items.value.add("Dungeon Map (Woodfall)")
            self.options.local_items.value.add("Dungeon Map (Snowhead)")
            self.options.local_items.value.add("Dungeon Map (Great Bay)")
            self.options.local_items.value.add("Dungeon Map (Stone Tower)")
            self.options.local_items.value.add("Compass (Woodfall)")
            self.options.local_items.value.add("Compass (Snowhead)")
            self.options.local_items.value.add("Compass (Great Bay)")
            self.options.local_items.value.add("Compass (Stone Tower)")

        if self.options.shuffle_small_keys.value == 4:
            self.options.local_items.value.add("Small Key (Woodfall)")
            self.options.local_items.value.add("Small Key (Snowhead)")
            self.options.local_items.value.add("Small Key (Great Bay)")
            self.options.local_items.value.add("Small Key (Stone Tower)")

        if self.options.shuffle_boss_keys.value == 4:
            self.options.local_items.value.add("Boss Key (Woodfall)")
            self.options.local_items.value.add("Boss Key (Snowhead)")
            self.options.local_items.value.add("Boss Key (Great Bay)")
            self.options.local_items.value.add("Boss Key (Stone Tower)")

        # Create shop prices.
        self.prices_ints = []
        self.prices = ""

        if self.options.shopsanity.value != 0:
            price_max = 0

            if self.options.shop_prices.value == 2:
                price_max = 99
            elif self.options.shop_prices.value == 3:
                price_max = 200
            elif self.options.shop_prices.value == 4:
                price_max = 500

            # There are 34 (+2 fake) shop locations that need prices
            for i in range(0, 36):
                if self.options.shop_prices.value == 0:
                    price = default_shop_prices[i]
                else:
                    price = self.random.randint(0, price_max)
                self.prices_ints.append(price)
                self.prices += str(price) + " "

            self.prices = self.prices[:-1]

    def create_item(self, name: str) -> MMRItem:
        if (name == "Stray Fairy (Clock Town)" or
            name == "Stray Fairy (Woodfall)" or
            name == "Stray Fairy (Snowhead)" or
            name == "Stray Fairy (Great Bay)" or
            name == "Stray Fairy (Stone Tower)") and self.options.shuffle_great_fairy_rewards == 0:
            return MMRItem(name, ItemClassification.filler, item_data_table[name].code, self.player)
        elif (name == "Swamp Skulltula Token" or
              name == "Ocean Skulltula Token") and self.options.shuffle_spiderhouse_reward == 0:
            return MMRItem(name, ItemClassification.filler, item_data_table[name].code, self.player)
        else:
            return MMRItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def place(self, location, item):
        player = self.player
        mw = self.multiworld

        mw.get_location(location, player).place_locked_item(self.create_item(item))

    def create_items(self) -> None:
        mw = self.multiworld

        item_pool: List[MMRItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            item_pool_count[name] = 0
            if item.code and item.can_create(self.options):
                while item_pool_count[name] < item.num_exist:
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1

        mw.itempool += item_pool

        mw.push_precollected(self.create_item("Ocarina of Time"))
        mw.push_precollected(self.create_item("Song of Time"))

        if self.options.swordless.value:
            mw.itempool.append(self.create_item("Progressive Sword"))

        if self.options.shieldless.value:
            mw.itempool.append(self.create_item("Progressive Shield"))

        if self.options.start_with_soaring.value:
            mw.push_precollected(self.create_item("Song of Soaring"))
            self.create_and_add_filler_items()

        if self.options.shuffle_spiderhouse_reward.value != 1:
            mw.itempool.append(self.create_item("Progressive Wallet"))

        if self.options.shuffle_regional_maps.value == 1:
            mw.push_precollected(self.create_item("Clock Town Map"))
            mw.push_precollected(self.create_item("Woodfall Map"))
            mw.push_precollected(self.create_item("Snowhead Map"))
            mw.push_precollected(self.create_item("Romani Ranch Map"))
            mw.push_precollected(self.create_item("Great Bay Map"))
            mw.push_precollected(self.create_item("Stone Tower Map"))
            self.create_and_add_filler_items(6)

        if self.options.shuffle_maps_and_compasses.value == 0:
            mw.push_precollected(self.create_item("Dungeon Map (Woodfall)"))
            mw.push_precollected(self.create_item("Compass (Woodfall)"))
            mw.push_precollected(self.create_item("Dungeon Map (Snowhead)"))
            mw.push_precollected(self.create_item("Compass (Snowhead)"))
            mw.push_precollected(self.create_item("Dungeon Map (Great Bay)"))
            mw.push_precollected(self.create_item("Compass (Great Bay)"))
            mw.push_precollected(self.create_item("Dungeon Map (Stone Tower)"))
            mw.push_precollected(self.create_item("Compass (Stone Tower)"))

        if self.options.shuffle_small_keys.value == 0:
            mw.push_precollected(self.create_item("Small Key (Woodfall)"))
            mw.push_precollected(self.create_item("Small Key (Snowhead)"))
            mw.push_precollected(self.create_item("Small Key (Snowhead)"))
            mw.push_precollected(self.create_item("Small Key (Snowhead)"))
            mw.push_precollected(self.create_item("Small Key (Great Bay)"))
            mw.push_precollected(self.create_item("Small Key (Stone Tower)"))
            mw.push_precollected(self.create_item("Small Key (Stone Tower)"))
            mw.push_precollected(self.create_item("Small Key (Stone Tower)"))
            mw.push_precollected(self.create_item("Small Key (Stone Tower)"))

        if self.options.shuffle_boss_keys == 0:
            mw.push_precollected(self.create_item("Boss Key (Woodfall)"))
            mw.push_precollected(self.create_item("Boss Key (Snowhead)"))
            mw.push_precollected(self.create_item("Boss Key (Great Bay)"))
            mw.push_precollected(self.create_item("Boss Key (Stone Tower)"))

        if self.options.curiostity_shop_trades.value:
            mw.itempool.append(self.create_item("Blue Rupee"))
            mw.itempool.append(self.create_item("Red Rupee"))
            mw.itempool.append(self.create_item("Purple Rupee"))
            mw.itempool.append(self.create_item("Gold Rupee"))

        if self.options.scrubsanity.value != 0:
            self.create_and_add_filler_items(4)

        if self.options.shopsanity.value != 0:
            self.create_and_add_filler_items(27)

        if self.options.shopsanity.value == 2:
            self.create_and_add_filler_items(11)

        if self.options.cowsanity.value != 0:
            self.create_and_add_filler_items(8)

        if self.options.intro_checks.value:
            self.create_and_add_filler_items(1)

        if self.options.shuffle_great_fairy_rewards.value != 0:
            self.create_and_add_filler_items(6)

        if self.options.shuffle_spiderhouse_reward.value != 0:
            self.create_and_add_filler_items(2)
        
        if self.options.shuffle_minigames.value == 1:
            self.create_and_add_filler_items(5)
        elif self.options.shuffle_minigames.value == 2:
            self.create_and_add_filler_items(9)

        if self.options.shuffle_treasure_chest_game.value == 1:
            self.create_and_add_filler_items(1)
        elif self.options.shuffle_treasure_chest_game.value == 2:
            self.create_and_add_filler_items(4)

        if self.options.shuffle_maps_and_compasses.value == 0:
            self.create_and_add_filler_items(8)

        if self.options.shuffle_small_keys.value == 0:
            self.create_and_add_filler_items(9)

        if self.options.shuffle_boss_keys == 0:
            self.create_and_add_filler_items(4)

        shp = self.options.starting_hearts.value
        if self.options.starting_hearts_are_containers_or_pieces.value == 0:
            for i in range(0, int((12 - shp)/4)):
                mw.itempool.append(self.create_item("Heart Container"))
            for i in range(0, (12 - shp) % 4):
                mw.itempool.append(self.create_item("Heart Piece"))
        else:
            for i in range(0, 12 - shp):
                mw.itempool.append(self.create_item("Heart Piece"))

    def create_regions(self) -> None:
        player = self.player
        mw = self.multiworld
        
        available_dungeon_locations = [
            "Woodfall Temple Dinolfos Chest",
            "Snowhead Temple Lower Wizzrobe Chest",
            "Great Bay Temple Behind Locked Door Chest",
            "Stone Tower Temple Garo Master Chest",
            "Stone Tower Temple Inverted Eyegore Chest"
        ]
        available_wft_locations = ["Woodfall Temple Dinolfos Chest"]
        available_sht_locations = ["Snowhead Temple Lower Wizzrobe Chest"]
        available_gbt_locations = ["Great Bay Temple Behind Locked Door Chest"]
        available_stt_locations = ["Stone Tower Temple Garo Master Chest", "Stone Tower Temple Inverted Eyegore Chest"]
        item_name_groups_to_shuffle = []

        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, player, mw)
            mw.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = mw.get_region(region_name, player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.options)
            }, MMRLocation)
            region.add_exits(region_data.connecting_regions)

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.options):
                continue

            self.place(location_name, location_data_table[location_name].locked_item)

        if self.options.shuffle_regional_maps.value == 0:
            self.place("Tingle Clock Town Map Purchase", "Clock Town Map")
            self.place("Tingle Woodfall Map Purchase", "Woodfall Map")
            self.place("Tingle Snowhead Map Purchase", "Snowhead Map")
            self.place("Tingle Romani Ranch Map Purchase", "Romani Ranch Map")
            self.place("Tingle Great Bay Map Purchase", "Great Bay Map")
            self.place("Tingle Stone Tower Map Purchase", "Stone Tower Map")

        if self.options.shuffle_boss_remains.value == 0:
            self.place("Woodfall Temple Odolwa's Remains", "Odolwa's Remains")
            self.place("Snowhead Temple Goht's Remains", "Goht's Remains")
            self.place("Great Bay Temple Gyorg's Remains", "Gyorg's Remains")
            self.place("Stone Tower Temple Inverted Twinmold's Remains", "Twinmold's Remains")
        
        if self.options.shuffle_boss_remains.value == 2:
            remains_list = ["Odolwa's Remains", "Goht's Remains", "Gyorg's Remains", "Twinmold's Remains"]
            
            self.place("Woodfall Temple Odolwa's Remains", remains_list.pop(self.random.randint(0, 3)))
            self.place("Snowhead Temple Goht's Remains", remains_list.pop(self.random.randint(0, 2)))
            self.place("Great Bay Temple Gyorg's Remains", remains_list.pop(self.random.randint(0, 1)))
            self.place("Stone Tower Temple Inverted Twinmold's Remains", remains_list[0])

        if self.options.shuffle_spiderhouse_reward.value == 1:
            self.place("Swamp Spider House Reward", "Mask of Truth")
            self.place("Ocean Spider House Reward", "Progressive Wallet")

        if self.options.skullsanity.value == 0:
            for i in range(0, 31):
                if i != 3:
                    self.place(code_to_location_table[0x3469420062700 | i], "Swamp Skulltula Token")
                if i != 0:
                    self.place(code_to_location_table[0x3469420062800 | i], "Ocean Skulltula Token")

        if self.options.shuffle_great_fairy_rewards.value == 1: #vanilla
            self.place("North Clock Town Great Fairy Reward", "Progressive Magic")
            self.place("North Clock Town Great Fairy Reward (Has Transformation Mask)", "Great Fairy Mask")
            self.place("Woodfall Great Fairy Reward", "Great Spin Attack")
            self.place("Snowhead Great Fairy Reward", "Progressive Magic")
            self.place("Great Bay Great Fairy Reward", "Double Defense")
            self.place("Stone Tower Great Fairy Reward", "Great Fairy Sword")

        if self.options.shuffle_maps_and_compasses.value == "vanilla":
            self.place("Woodfall Temple Turtle Chest", "Dungeon Map (Woodfall)")
            self.place("Woodfall Temple Dragonfly Chest", "Compass (Woodfall)")
            self.place("Snowhead Temple Elevator Room Lower Chest", "Dungeon Map (Snowhead)")
            self.place("Snowhead Temple Frozen Block Chest", "Compass (Snowhead)")
            self.place("Great Bay Temple Before Red Valve Room Chest", "Dungeon Map (Great Bay)")
            self.place("Great Bay Temple Caged Chest Room Upper Chest", "Compass (Great Bay)")
            self.place("Stone Tower Temple Armos Room Back Chest", "Dungeon Map (Stone Tower)")
            self.place("Stone Tower Temple Eastern Water Room Sun Block Chest", "Compass (Stone Tower)")
#        elif self.options.shuffle_maps_and_compasses.value == "dungeon":
#            available_wft_locations.append("Woodfall Temple Turtle Chest")
#            available_wft_locations.append("Woodfall Temple Dragonfly Chest")
#            available_sht_locations.append("Snowhead Temple Elevator Room Lower Chest")
#            available_sht_locations.append("Snowhead Temple Frozen Block Chest")
#            available_gbt_locations.append("Great Bay Temple Before Red Valve Room Chest")
#            available_gbt_locations.append("Great Bay Temple Caged Chest Room Upper Chest")
#            available_stt_locations.append("Stone Tower Temple Armos Room Back Chest")
#            available_stt_locations.append("Stone Tower Temple Eastern Water Room Sun Block Chest")
#
#            available_wft_locations.append("Dungeon Map (Woodfall)")
#            available_wft_locations.append("Compass (Woodfall)")
#            available_sht_locations.append("Dungeon Map (Snowhead)")
#            available_sht_locations.append("Compass (Snowhead)")
#            available_gbt_locations.append("Dungeon Map (Great Bay)")
#            available_gbt_locations.append("Compass (Great Bay)")
#            available_stt_locations.append("Dungeon Map (Stone Tower)")
#            available_stt_locations.append("Compass (Stone Tower)")
#        elif self.options.shuffle_maps_and_compasses.value == "any_dungeon":
#            available_dungeon_locations.append("Woodfall Temple Turtle Chest")
#            available_dungeon_locations.append("Woodfall Temple Dragonfly Chest")
#            available_dungeon_locations.append("Snowhead Temple Elevator Room Lower Chest")
#            available_dungeon_locations.append("Snowhead Temple Frozen Block Chest")
#            available_dungeon_locations.append("Great Bay Temple Before Red Valve Room Chest")
#            available_dungeon_locations.append("Great Bay Temple Caged Chest Room Upper Chest")
#            available_dungeon_locations.append("Stone Tower Temple Armos Room Back Chest")
#            available_dungeon_locations.append("Stone Tower Temple Eastern Water Room Sun Block Chest")
#
#            item_name_groups_to_shuffle.append("Dungeon Map (Woodfall)")
#            item_name_groups_to_shuffle.append("Compass (Woodfall)")
#            item_name_groups_to_shuffle.append("Dungeon Map (Snowhead)")
#            item_name_groups_to_shuffle.append("Compass (Snowhead)")
#            item_name_groups_to_shuffle.append("Dungeon Map (Great Bay)")
#            item_name_groups_to_shuffle.append("Compass (Great Bay)")
#            item_name_groups_to_shuffle.append("Dungeon Map (Stone Tower)")
#            item_name_groups_to_shuffle.append("Compass (Stone Tower)")

        if self.options.shuffle_small_keys.value == 1:
            self.place("Woodfall Temple Ledge Chest", "Small Key (Woodfall)")

            self.place("Snowhead Temple Behind Stacked Block Chest", "Small Key (Snowhead)")
            self.place("Snowhead Temple Icicle Room Snowball Chest", "Small Key (Snowhead)")
            self.place("Snowhead Temple Bridge Room Freezard Chest", "Small Key (Snowhead)")

            self.place("Great Bay Temple Caged Chest Room Underwater Chest", "Small Key (Great Bay)")

            self.place("Stone Tower Temple Armos Room Lava Chest", "Small Key (Stone Tower)")
            self.place("Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest", "Small Key (Stone Tower)")
            self.place("Stone Tower Temple Inverted Eastern Air Gust Room Switch Chest", "Small Key (Stone Tower)")
            self.place("Stone Tower Temple Inverted Death Armos Maze Chest", "Small Key (Stone Tower)")
#        elif self.options.shuffle_small_keys.value == "dungeon":
#            available_wft_locations.append("Woodfall Temple Ledge Chest")
#            available_sht_locations.append("Snowhead Temple Behind Stacked Block Chest")
#            available_sht_locations.append("Snowhead Temple Icicle Room Snowball Chest")
#            available_sht_locations.append("Snowhead Temple Bridge Room Freezard Chest")
#            available_gbt_locations.append("Great Bay Temple Caged Chest Room Underwater Chest")
#            available_stt_locations.append("Stone Tower Temple Armos Room Lava Chest")
#            available_stt_locations.append("Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest")
#            available_stt_locations.append("Stone Tower Temple Inverted Eastern Air Gust Room Switch Chest")
#            available_stt_locations.append("Stone Tower Temple Inverted Death Armos Maze Chest")
#
#            available_wft_locations.append("Small Key (Woodfall)")
#            available_sht_locations.append("Small Key (Snowhead)")
#            available_sht_locations.append("Small Key (Snowhead)")
#            available_sht_locations.append("Small Key (Snowhead)")
#            available_gbt_locations.append("Small Key (Great Bay)")
#            available_sst_locations.append("Small Key (Stone Tower)")
#            available_sst_locations.append("Small Key (Stone Tower)")
#            available_sst_locations.append("Small Key (Stone Tower)")
#            available_sst_locations.append("Small Key (Stone Tower)")
#        elif self.options.shuffle_small_keys.value == "any_dungeon":
#            available_dungeon_locations.append("Woodfall Temple Ledge Chest")
#            available_dungeon_locations.append("Snowhead Temple Behind Stacked Block Chest")
#            available_dungeon_locations.append("Snowhead Temple Icicle Room Snowball Chest")
#            available_dungeon_locations.append("Snowhead Temple Bridge Room Freezard Chest")
#            available_dungeon_locations.append("Great Bay Temple Caged Chest Room Underwater Chest")
#            available_dungeon_locations.append("Stone Tower Temple Armos Room Lava Chest")
#            available_dungeon_locations.append("Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest")
#            available_dungeon_locations.append("Stone Tower Temple Inverted Eastern Air Gust Room Switch Chest")
#            available_dungeon_locations.append("Stone Tower Temple Inverted Death Armos Maze Chest")
#
#            item_name_groups_to_shuffle.append("Small Key (Woodfall)")
#            item_name_groups_to_shuffle.append("Small Key (Snowhead)")
#            item_name_groups_to_shuffle.append("Small Key (Snowhead)")
#            item_name_groups_to_shuffle.append("Small Key (Snowhead)")
#            item_name_groups_to_shuffle.append("Small Key (Great Bay)")
#            item_name_groups_to_shuffle.append("Small Key (Stone Tower)")
#            item_name_groups_to_shuffle.append("Small Key (Stone Tower)")
#            item_name_groups_to_shuffle.append("Small Key (Stone Tower)")
#            item_name_groups_to_shuffle.append("Small Key (Stone Tower)")
        
        if self.options.shuffle_boss_keys.value == "vanilla":
            self.place("Woodfall Temple Gekko Chest", "Boss Key (Woodfall)")
            self.place("Snowhead Temple Upper Wizzrobe Chest", "Boss Key (Snowhead)")
            self.place("Great Bay Temple Mad Jellied Gekko Chest", "Boss Key (Great Bay)")
            self.place("Stone Tower Temple Inverted Gomess Chest", "Boss Key (Stone Tower)")
#        elif self.options.shuffle_boss_keys.value == "dungeon":
#            available_wft_locations.append("Woodfall Temple Gekko Chest")
#            available_sht_locations.append("Snowhead Temple Upper Wizzrobe Chest")
#            available_gbt_locations.append("Great Bay Temple Mad Jellied Gekko Chest")
#            available_stt_locations.append("Stone Tower Temple Inverted Gomess Chest")
#
#            available_wft_locations.append("Boss Key (Woodfall)")
#            available_sht_locations.append("Boss Key (Snowhead)")
#            available_gbt_locations.append("Boss Key (Great Bay)")
#            available_stt_locations.append("Boss Key (Stone Tower)")
#        elif self.options.shuffle_boss_keys.value == "any_dungeon":
#            available_dungeon_locations.append("Woodfall Temple Gekko Chest")
#            available_dungeon_locations.append("Snowhead Temple Upper Wizzrobe Chest")
#            available_dungeon_locations.append("Great Bay Temple Mad Jellied Gekko Chest")
#            available_dungeon_locations.append("Stone Tower Temple Inverted Gomess Chest")
#
#            item_name_groups_to_shuffle.append("Boss Key (Woodfall)")
#            item_name_groups_to_shuffle.append("Boss Key (Snowhead)")
#            item_name_groups_to_shuffle.append("Boss Key (Great Bay)")
#            item_name_groups_to_shuffle.append("Boss Key (Stone Tower)")

        if self.options.shuffle_stray_fairies.value == "vanilla":
            self.place("Laundry Pool Stray Fairy (Clock Town)", "Stray Fairy (Clock Town)")

            self.place("Woodfall Temple Entrance Chest SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Switch Chest SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Dark Room Chest SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Entrance Freestanding SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Deku Baba SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Pot SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Platform Hive SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Main Room Bubble SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Skulltula SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Bridge Room Bubble SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Bridge Room Hive SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Pre-Boss Lower Right Bubble SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Pre-Boss Upper Right Bubble SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Pre-Boss Upper Left Bubble SF", "Stray Fairy (Woodfall)")
            self.place("Woodfall Temple Pre-Boss Pillar Bubble SF", "Stray Fairy (Woodfall)")

            self.place("Snowhead Temple Basement Switch Chest SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Elevator Room Invisible Platform Chest SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Stacked Block Upper Chest SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Freezard Torch Room Chest SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Frozen Block Upper Chest SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Icicle Room Hidden Chest SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Main Room Wall Chest SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Bridge Room Pillar Bubble SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Bridge Room Under Platform Bubble SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Elevator Freestanding SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Bombable Stairs Crate SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Timed Switch Room Bubble SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Snowmen Bubble SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Dinolfos Room First SF", "Stray Fairy (Snowhead)")
            self.place("Snowhead Temple Dinolfos Room Second SF", "Stray Fairy (Snowhead)")

            self.place("Great Bay Temple Entrance Torches Chest SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Bio-Baba Hall Chest SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Freezable Waterwheel Upper Chest SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Freezable Waterwheel Lower Chest SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Seesaw Room Chest SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Room Behind Waterfall Ceiling Chest SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Waterwheel Room Skulltula SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Waterwheel Room Bubble SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Blender Pot SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Blender Room Barrel SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Before Red Valve Room Pot SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Caged Chest Room Pot SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Seesaw Room Underwater Barrel SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Pre-Boss Room Platform Bubble SF", "Stray Fairy (Great Bay)")
            self.place("Great Bay Temple Pre-Boss Room Tunnel Bubble SF", "Stray Fairy (Great Bay)")

            self.place("Stone Tower Temple Entrance Room Eye Switch Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Armos Room Upper Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Eyegore Room Switch Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Mirror Room Sun Face Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Mirror Room Sun Block Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Air Gust Room Side Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Air Gust Room Goron Switch Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Eyegore Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Eastern Water Room Underwater Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Inverted Entrance Room Sun Face Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Inverted Eastern Air Gust Room Frozen Switch Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Inverted Wizzrobe Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple Entrance Room Lower Chest", "Stray Fairy (Stone Tower)")
            self.place("Stone Tower Temple After Garo Upside Down Chest", "Stray Fairy (Stone Tower)")
#        else:
#            available_dungeon_locations.append("Woodfall Temple Entrance Chest SF")
#            available_dungeon_locations.append("Woodfall Temple Switch Chest SF")
#            available_dungeon_locations.append("Woodfall Temple Dark Room Chest SF")
#            available_dungeon_locations.append("Woodfall Temple Entrance Freestanding SF")
#            available_dungeon_locations.append("Woodfall Temple Deku Baba SF")
#            available_dungeon_locations.append("Woodfall Temple Pot SF")
#            available_dungeon_locations.append("Woodfall Temple Platform Hive SF")
#            available_dungeon_locations.append("Woodfall Temple Main Room Bubble SF")
#            available_dungeon_locations.append("Woodfall Temple Skulltula SF")
#            available_dungeon_locations.append("Woodfall Temple Bridge Room Bubble SF")
#            available_dungeon_locations.append("Woodfall Temple Bridge Room Hive SF")
#            available_dungeon_locations.append("Woodfall Temple Pre-Boss Lower Right Bubble SF")
#            available_dungeon_locations.append("Woodfall Temple Pre-Boss Upper Right Bubble SF")
#            available_dungeon_locations.append("Woodfall Temple Pre-Boss Upper Left Bubble SF")
#            available_dungeon_locations.append("Woodfall Temple Pre-Boss Pillar Bubble SF")
#
#            available_dungeon_locations.append("Snowhead Temple Basement Switch Chest SF")
#            available_dungeon_locations.append("Snowhead Temple Elevator Room Invisible Platform Chest SF")
#            available_dungeon_locations.append("Snowhead Temple Stacked Block Upper Chest SF")
#            available_dungeon_locations.append("Snowhead Temple Freezard Torch Room Chest SF")
#            available_dungeon_locations.append("Snowhead Temple Frozen Block Upper Chest SF")
#            available_dungeon_locations.append("Snowhead Temple Icicle Room Hidden Chest SF")
#            available_dungeon_locations.append("Snowhead Temple Main Room Wall Chest SF")
#            available_dungeon_locations.append("Snowhead Temple Bridge Room Pillar Bubble SF")
#            available_dungeon_locations.append("Snowhead Temple Bridge Room Under Platform Bubble SF")
#            available_dungeon_locations.append("Snowhead Temple Elevator Freestanding SF")
#            available_dungeon_locations.append("Snowhead Temple Bombable Stairs Crate SF")
#            available_dungeon_locations.append("Snowhead Temple Timed Switch Room Bubble SF")
#            available_dungeon_locations.append("Snowhead Temple Snowmen Bubble SF")
#            available_dungeon_locations.append("Snowhead Temple Dinolfos Room First SF")
#            available_dungeon_locations.append("Snowhead Temple Dinolfos Room Second SF")
#
#            available_dungeon_locations.append("Great Bay Temple Entrance Torches Chest SF")
#            available_dungeon_locations.append("Great Bay Temple Bio-Baba Hall Chest SF")
#            available_dungeon_locations.append("Great Bay Temple Freezable Waterwheel Upper Chest SF")
#            available_dungeon_locations.append("Great Bay Temple Freezable Waterwheel Lower Chest SF")
#            available_dungeon_locations.append("Great Bay Temple Seesaw Room Chest SF")
#            available_dungeon_locations.append("Great Bay Temple Room Behind Waterfall Ceiling Chest SF")
#            available_dungeon_locations.append("Great Bay Temple Waterwheel Room Skulltula SF")
#            available_dungeon_locations.append("Great Bay Temple Waterwheel Room Bubble SF")
#            available_dungeon_locations.append("Great Bay Temple Blender Pot SF")
#            available_dungeon_locations.append("Great Bay Temple Blender Room Barrel SF")
#            available_dungeon_locations.append("Great Bay Temple Before Red Valve Room Pot SF")
#            available_dungeon_locations.append("Great Bay Temple Caged Chest Room Pot SF")
#            available_dungeon_locations.append("Great Bay Temple Seesaw Room Underwater Barrel SF")
#            available_dungeon_locations.append("Great Bay Temple Pre-Boss Room Platform Bubble SF")
#            available_dungeon_locations.append("Great Bay Temple Pre-Boss Room Tunnel Bubble SF")
#
#            available_dungeon_locations.append("Stone Tower Temple Entrance Room Eye Switch Chest")
#            available_dungeon_locations.append("Stone Tower Temple Armos Room Upper Chest")
#            available_dungeon_locations.append("Stone Tower Temple Eyegore Room Switch Chest")
#            available_dungeon_locations.append("Stone Tower Temple Mirror Room Sun Face Chest")
#            available_dungeon_locations.append("Stone Tower Temple Mirror Room Sun Block Chest")
#            available_dungeon_locations.append("Stone Tower Temple Air Gust Room Side Chest")
#            available_dungeon_locations.append("Stone Tower Temple Air Gust Room Goron Switch Chest")
#            available_dungeon_locations.append("Stone Tower Temple Eyegore Chest")
#            available_dungeon_locations.append("Stone Tower Temple Eastern Water Room Underwater Chest")
#            available_dungeon_locations.append("Stone Tower Temple Inverted Entrance Room Sun Face Chest")
#            available_dungeon_locations.append("Stone Tower Temple Inverted Eastern Air Gust Room Frozen Switch Chest")
#            available_dungeon_locations.append("Stone Tower Temple Inverted Wizzrobe Chest")
#            available_dungeon_locations.append("Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest")
#            available_dungeon_locations.append("Stone Tower Temple Entrance Room Lower Chest")
#            available_dungeon_locations.append("Stone Tower Temple After Garo Upside Down Chest")
#            for i in range(1, 15, 1):
#                item_name_groups_to_shuffle.append("Stray Fairy (Woodfall)")
#            for i in range(1, 15, 1):
#                item_name_groups_to_shuffle.append("Stray Fairy (Snowhead)")
#            for i in range(1, 15, 1):
#                item_name_groups_to_shuffle.append("Stray Fairy (Great Bay)")
#            for i in range(1, 15, 1):
#                item_name_groups_to_shuffle.append("Stray Fairy (Stone Tower)")

        sword_location = mw.get_location("Link's Inventory (Kokiri Sword)", player)
        if self.options.swordless.value:
            sword_location.item_rule = lambda item: item.name != "Progressive Sword"
        else:
            sword_location.place_locked_item(self.create_item("Progressive Sword"))

        shield_location = mw.get_location("Link's Inventory (Hero's Shield)", player)
        if self.options.shieldless.value:
            shield_location.item_rule = lambda item: item.name != "Progressive Shield"
        else:
            shield_location.place_locked_item(self.create_item("Progressive Shield"))

        shp = self.options.starting_hearts.value
        if self.options.starting_hearts_are_containers_or_pieces.value == 0:
            containers = int(shp/4) - 1
            for i in range(0, containers):
                self.place(code_to_location_table[0x34694200D0000 | i], "Heart Container")

            hearts_left = shp % 4
            for i in range(0, hearts_left):
                self.place(code_to_location_table[0x34694200D0000 | (containers + i)], "Heart Piece")

            if (shp % 4) != 0:
                for i in range(containers + hearts_left, containers + 4):
                    mw.get_location(code_to_location_table[0x34694200D0000 | i], player).item_rule = lambda item: item.name != "Heart Piece" and item.name != "Heart Container"
        else:
            for i in range(0, shp - 4):
                self.place(code_to_location_table[0x34694200D0000 | i], "Heart Piece")

            for i in range(shp - 4, 8):
                mw.get_location(code_to_location_table[0x34694200D0000 | i], player).item_rule = lambda item: item.name != "Heart Piece" and item.name != "Heart Container"

        # TODO: check options to see what player starts with
        # ~ mw.get_location("Top of Clock Tower (Ocarina of Time)", player).place_locked_item(self.create_item(self.get_filler_item_name()))
        # ~ mw.get_location("Top of Clock Tower (Song of Time)", player).place_locked_item(self.create_item(self.get_filler_item_name()))

    def create_and_add_filler_items(self, count: int = 1):
        for i in range(count):
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))

    def get_filler_item_name(self) -> str:
        filler_items = ["Blue Rupee", "Red Rupee", "Purple Rupee", "Silver Rupee", "Gold Rupee"]
        return self.random.choice(filler_items)
        # filler_weights = (50, 25, 10, 5, 1)
        # return self.random.choices(filler_items, weights=filler_weights)[0]

    def set_rules(self) -> None:
        player = self.player
        mw = self.multiworld
        options = self.options
        prices = self.prices_ints

        # Completion condition.
        mw.completion_condition[player] = lambda state: state.has("Victory", player)

        if (self.options.logic_difficulty.value == 4):
            return

        # ~ if (self.options.logic_difficulty.value == 0):
            # ~ region_rules = get_baby_region_rules(player, options)
            # ~ location_rules = get_baby_location_rules(player, options)
        if (self.options.logic_difficulty.value == 1):
            region_rules = get_region_rules(player, options)
            location_rules = get_location_rules(player, options, prices)

        for entrance_name, rule in region_rules.items():
            entrance = mw.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        for location in mw.get_locations(player):
            name = location.name

            if name not in location_rules:
                print(f"Location '{name}' does not have any logic")
            
            if self.options.skullsanity.value == 2 and (name == "Swamp Spider House Reward" or name == "Ocean Spider House Reward"):
                continue
            if name in location_rules and location_data_table[name].can_create(self.options):
                location.access_rule = location_rules[name]

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        if self.options.shopsanity.value:
            spoiler_handle.write("\nShop Prices:\n")
            for location, shop_id in shop_location_to_id.items():
                spoiler_handle.write(f"\n{location}: {self.prices_ints[shop_id]} Rupees")

    def fill_slot_data(self):
        shp = self.options.starting_hearts.value
        starting_containers = int(shp/4) - 1
        starting_pieces = shp % 4
        shuffled_containers = int((12 - shp)/4)
        shuffled_pieces = (12 - shp) % 4
        return {
            "skullsanity": self.options.skullsanity.value,
            "shuffle_stray_fairies": self.options.shuffle_stray_fairies.value,
            "shopsanity": self.options.shopsanity.value,                                                                
            "scrubsanity": self.options.scrubsanity.value,
            "shop_prices": self.prices,
            "shop_prices_ints": self.prices_ints,
            "cowsanity": self.options.cowsanity.value,
            "shuffle_maps_and_compasses": self.options.shuffle_maps_and_compasses.value,
            "shuffle_small_keys": self.options.shuffle_small_keys.value,
            "shuffle_boss_keys": self.options.shuffle_boss_keys.value,
            "intro_checks": self.options.intro_checks.value,
            "curiostity_shop_trades": self.options.curiostity_shop_trades.value,
            "damage_multiplier": self.options.damage_multiplier.value,
            "death_behavior": self.options.death_behavior.value,
            "death_link": self.options.death_link.value,
            "camc": self.options.camc.value,
            "starting_heart_locations": 8 if self.options.starting_hearts_are_containers_or_pieces.value == 1 else starting_containers + starting_pieces + shuffled_containers + shuffled_pieces,
            "majora_remains_required": self.options.majora_remains_required.value,
            "moon_remains_required": self.options.moon_remains_required.value,
            "required_skull_tokens": self.options.required_skull_tokens.value,
            "required_stray_fairies": self.options.required_stray_fairies.value,
            "start_with_consumables": self.options.start_with_consumables.value,
            "permanent_chateau_romani": self.options.permanent_chateau_romani.value,
            "start_with_inverted_time": self.options.start_with_inverted_time.value,
            "receive_filled_wallets": self.options.receive_filled_wallets.value,
            "remains_allow_boss_warps": self.options.remains_allow_boss_warps.value,
            "magic_is_a_trap": self.options.magic_is_a_trap.value,
            "shuffle_regional_maps": self.options.shuffle_regional_maps.value,
            "shuffle_spiderhouse_reward": self.options.shuffle_spiderhouse_reward.value,
            "shuffle_great_fairy_rewards": self.options.shuffle_great_fairy_rewards.value,
            "shuffle_minigames": self.options.shuffle_minigames.value,
            "shuffle_treasure_chest_game": self.options.shuffle_treasure_chest_game.value,
            "link_tunic_color": ((self.options.link_tunic_color.value[0] & 0xFF) << 16) | ((self.options.link_tunic_color.value[1] & 0xFF) << 8) | (self.options.link_tunic_color.value[2] & 0xFF),
            "random_seed": self.random.getrandbits(32),
            "logic_difficulty": self.options.logic_difficulty.value
        }
