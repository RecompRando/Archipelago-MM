from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld

from .Constants import *


class BKLocation(Location):
    game = "Banjo-Kazooie"


class BKLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, BKLocationData] = {
    LOC_TRANSFORMATION_TERMITE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None,
        locked_item=ITEM_TRANSFORMATION_TERMITE
    ),
    LOC_TRANSFORMATION_CROCODILE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=None,
        locked_item=ITEM_TRANSFORMATION_CROCODILE
    ),
    LOC_TRANSFORMATION_WALRUS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_TRANSFORMATION_WALRUS
    ),
    LOC_TRANSFORMATION_PUMPKIN: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=None,
        locked_item=ITEM_TRANSFORMATION_PUMPKIN
    ),
    LOC_TRANSFORMATION_BEE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_TRANSFORMATION_BEE
    ),
    LOC_BLUBBER_GOLD_TTC_POOP_DECK: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=None,
        locked_item=ITEM_BLUBBER_GOLD
    ),
    LOC_BLUBBER_GOLD_TTC_HOLD_UNDERWATER: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=None,
        locked_item=ITEM_BLUBBER_GOLD
    ),
    LOC_RED_PRESENT_FP_TREE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_RED_PRESENT
    ),
    LOC_GREEN_PRESENT_FP_NEAR_RAMP: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_GREEN_PRESENT
    ),
    LOC_BLUE_PRESENT_FP_GIANT_SNOWMAN_NOSE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_BLUE_PRESENT
    ),
    LOC_WORM_SUMMER_CCW_ENTRY_PATH: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_SNAPPER_NEAR_BULL: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_LEDGE_NEAR_MUMBO: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_OUTSIDE_MUMBO: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_IN_DRIED_LAKE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_LEDGE_ABOVE_BRAMBLES: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_NEAR_CABIN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_ZUBBAS_NEST: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_SUMMER_CCW_NEAR_NABNUTS_HOME: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_ENTRY_LEAF_PILE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_RAMP_NEAR_LAKE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_NEAR_STILT_BOOTS: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_INSIDE_MUMBO_HUT: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_LEAF_PILE_NEAR_BRAMBLES: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_LEAF_PILE_NEAR_FLOWER: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_LEDGE_ABOVE_BRAMBLES: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_ATOP_BEEHIVE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_INSIDE_BEEHIVE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_BELOW_CABIN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_INSIDE_NABNUTS_HOUSE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_BEHIND_EYRIE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_WORM_AUTUMN_CCW_TREETOP_PAST_NEST: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_WORM
    ),
    LOC_ACORN_AUTUMN_CCW_BEHIND_UPPER_WINDOW: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_ACORN
    ),
    LOC_ACORN_AUTUMN_CCW_EDGE_OF_CIRCULAR_GAP_PATH: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_ACORN
    ),
    LOC_ACORN_AUTUMN_CCW_MIDDLE_OF_CIRCULAR_GAP_PATH: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_ACORN
    ),
    LOC_ACORN_AUTUMN_CCW_LEDGE_BELOW_CIRCULAR_GAP_PATH: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_ACORN
    ),
    LOC_ACORN_AUTUMN_CCW_LOWER_SLOPED_PATH: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_ACORN
    ),
    LOC_ACORN_AUTUMN_CCW_INSIDE_NABNUTS_HOUSE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_ACORN
    ),
    LOC_JINJO_MM_BLUE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None,
        locked_item=ITEM_JINJO_MM_BLUE
    ),
    LOC_JINJO_MM_GREEN: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None,
        locked_item=ITEM_JINJO_MM_GREEN
    ),
    LOC_JINJO_MM_ORANGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None,
        locked_item=ITEM_JINJO_MM_ORANGE
    ),
    LOC_JINJO_MM_PURPLE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None,
        locked_item=ITEM_JINJO_MM_PURPLE
    ),
    LOC_JINJO_MM_YELLOW: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None,
        locked_item=ITEM_JINJO_MM_YELLOW
    ),
    LOC_JINJO_TTC_BLUE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=None,
        locked_item=ITEM_JINJO_TTC_BLUE
    ),
    LOC_JINJO_TTC_GREEN: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=None,
        locked_item=ITEM_JINJO_TTC_GREEN
    ),
    LOC_JINJO_TTC_ORANGE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=None,
        locked_item=ITEM_JINJO_TTC_ORANGE
    ),
    LOC_JINJO_TTC_PURPLE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=None,
        locked_item=ITEM_JINJO_TTC_PURPLE
    ),
    LOC_JINJO_TTC_YELLOW: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=None,
        locked_item=ITEM_JINJO_TTC_YELLOW
    ),
    LOC_JINJO_CC_BLUE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=None,
        locked_item=ITEM_JINJO_CC_BLUE
    ),
    LOC_JINJO_CC_GREEN: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=None,
        locked_item=ITEM_JINJO_CC_GREEN
    ),
    LOC_JINJO_CC_ORANGE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=None,
        locked_item=ITEM_JINJO_CC_ORANGE
    ),
    LOC_JINJO_CC_PURPLE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=None,
        locked_item=ITEM_JINJO_CC_PURPLE
    ),
    LOC_JINJO_CC_YELLOW: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=None,
        locked_item=ITEM_JINJO_CC_YELLOW
    ),
    LOC_JINJO_BGS_BLUE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=None,
        locked_item=ITEM_JINJO_BGS_BLUE
    ),
    LOC_JINJO_BGS_GREEN: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=None,
        locked_item=ITEM_JINJO_BGS_GREEN
    ),
    LOC_JINJO_BGS_ORANGE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=None,
        locked_item=ITEM_JINJO_BGS_ORANGE
    ),
    LOC_JINJO_BGS_PURPLE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=None,
        locked_item=ITEM_JINJO_BGS_PURPLE
    ),
    LOC_JINJO_BGS_YELLOW: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=None,
        locked_item=ITEM_JINJO_BGS_YELLOW
    ),
    LOC_JINJO_FP_BLUE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_JINJO_FP_BLUE
    ),
    LOC_JINJO_FP_GREEN: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_JINJO_FP_GREEN
    ),
    LOC_JINJO_FP_ORANGE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_JINJO_FP_ORANGE
    ),
    LOC_JINJO_FP_PURPLE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_JINJO_FP_PURPLE
    ),
    LOC_JINJO_FP_YELLOW: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_JINJO_FP_YELLOW
    ),
    LOC_JINJO_GV_BLUE: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=None,
        locked_item=ITEM_JINJO_GV_BLUE
    ),
    LOC_JINJO_GV_GREEN: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=None,
        locked_item=ITEM_JINJO_GV_GREEN
    ),
    LOC_JINJO_GV_ORANGE: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=None,
        locked_item=ITEM_JINJO_GV_ORANGE
    ),
    LOC_JINJO_GV_PURPLE: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=None,
        locked_item=ITEM_JINJO_GV_PURPLE
    ),
    LOC_JINJO_GV_YELLOW: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=None,
        locked_item=ITEM_JINJO_GV_YELLOW
    ),
    LOC_JINJO_MMM_BLUE: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=None,
        locked_item=ITEM_JINJO_MMM_BLUE
    ),
    LOC_JINJO_MMM_GREEN: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=None,
        locked_item=ITEM_JINJO_MMM_GREEN
    ),
    LOC_JINJO_MMM_ORANGE: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=None,
        locked_item=ITEM_JINJO_MMM_ORANGE
    ),
    LOC_JINJO_MMM_PURPLE: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=None,
        locked_item=ITEM_JINJO_MMM_PURPLE
    ),
    LOC_JINJO_MMM_YELLOW: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=None,
        locked_item=ITEM_JINJO_MMM_YELLOW
    ),
    LOC_JINJO_RBB_BLUE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=None,
        locked_item=ITEM_JINJO_RBB_BLUE
    ),
    LOC_JINJO_RBB_GREEN: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=None,
        locked_item=ITEM_JINJO_RBB_GREEN
    ),
    LOC_JINJO_RBB_ORANGE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=None,
        locked_item=ITEM_JINJO_RBB_ORANGE
    ),
    LOC_JINJO_RBB_PURPLE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=None,
        locked_item=ITEM_JINJO_RBB_PURPLE
    ),
    LOC_JINJO_RBB_YELLOW: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=None,
        locked_item=ITEM_JINJO_RBB_YELLOW
    ),
    LOC_JINJO_CCW_BLUE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_JINJO_CCW_BLUE
    ),
    LOC_JINJO_CCW_GREEN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_JINJO_CCW_GREEN
    ),
    LOC_JINJO_CCW_ORANGE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_JINJO_CCW_ORANGE
    ),
    LOC_JINJO_CCW_PURPLE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_JINJO_CCW_PURPLE
    ),
    LOC_JINJO_CCW_YELLOW: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_JINJO_CCW_YELLOW
    ),
    LOC_JIGGY_GL_ENTRYWAY: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_LOBBY,
        address=0x00000033
    ),
    LOC_JIGGY_GL_ATOP_MUMBOS_MOUNTAIN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_LOBBY,
        address=0x00000034
    ),
    LOC_JIGGY_GL_TTC_CANNON: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,
        address=0x00000036
    ),
    LOC_JIGGY_GL_EYE_SWITCHES: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,
        address=0x00000035
    ),
    LOC_JIGGY_GL_WITCHS_HAT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,
        address=0x00000037
    ),
    LOC_JIGGY_GL_ABOVE_FP: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,
        address=0x00000038
    ),
    LOC_JIGGY_GL_SARCOPHAGUS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,
        address=0x0000003A
    ),
    LOC_JIGGY_GL_GRUNTYS_EYE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,
        address=0x00000039
    ),
    LOC_JIGGY_GL_WATER_SWITCH: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR,
        address=0x0000003B
    ),
    LOC_JIGGY_GL_BEE_TREE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR,
        address=0x0000003C
    ),
    LOC_JIGGY_MM_CONGA_ORANGE_THROW: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000008
    ),
    LOC_JIGGY_MM_CHIMPY_ORANGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000009
    ),
    LOC_JIGGY_MM_CONGA_ATTACK: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0000000A
    ),
    LOC_JIGGY_MM_STONEHENGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000006
    ),
    LOC_JIGGY_MM_HILLSIDE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000007
    ),
    LOC_JIGGY_MM_MUMBOS_HUT: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000003
    ),
    LOC_JIGGY_MM_TOTEM_POLE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000004
    ),
    LOC_JIGGY_MM_HUT: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000005
    ),
    LOC_JIGGY_MM_MOUNTAINTOP: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000002
    ),
    LOC_JIGGY_MM_JINJO: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000001
    ),
    LOC_JIGGY_TTC_NIPPER: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000012
    ),
    LOC_JIGGY_TTC_BLUBBER: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000014
    ),
    LOC_JIGGY_TTC_SANDCASTLE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000010
    ),
    LOC_JIGGY_TTC_SHOCK_SPRING: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000D
    ),
    LOC_JIGGY_TTC_X_MARK: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000011
    ),
    LOC_JIGGY_TTC_POOL: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000F
    ),
    LOC_JIGGY_TTC_CLIFFSIDE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000E
    ),
    LOC_JIGGY_TTC_LOCKUP: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000013
    ),
    LOC_JIGGY_TTC_LIGHTHOUSE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000C
    ),
    LOC_JIGGY_TTC_JINJO: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000B
    ),
    LOC_JIGGY_CC_CLANKER_RAISE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000017
    ),
    LOC_JIGGY_CC_CLANKER_TAIL: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000018
    ),
    LOC_JIGGY_CC_CLANKER_BOLT: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000019
    ),
    LOC_JIGGY_CC_CLANKER_GOLD_TEETH: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001B
    ),
    LOC_JIGGY_CC_CLANKER_BLOWHOLE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001D
    ),
    LOC_JIGGY_CC_WONDERWING: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001E
    ),
    LOC_JIGGY_CC_STOMACH_RINGS: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001C
    ),
    LOC_JIGGY_CC_SNIPPET: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000016
    ),
    LOC_JIGGY_CC_UNDERWATER_TUNNEL: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001A
    ),
    LOC_JIGGY_CC_JINJO: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000015
    ),
    LOC_JIGGY_BGS_EGG: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000021
    ),
    LOC_JIGGY_BGS_CENTER_RACE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000020
    ),
    LOC_JIGGY_BGS_FLIBBET: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000024
    ),
    LOC_JIGGY_BGS_TANKTUP: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000026
    ),
    LOC_JIGGY_BGS_TIPTUP: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000027
    ),
    LOC_JIGGY_BGS_HUT: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000023
    ),
    LOC_JIGGY_BGS_MUMBOS_HUT_RACE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000025
    ),
    LOC_JIGGY_BGS_CROCTUS: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000022
    ),
    LOC_JIGGY_BGS_MR_VILE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000028
    ),
    LOC_JIGGY_BGS_JINJO: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0000001F
    ),
    LOC_JIGGY_FP_SIR_SLUSH: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000031
    ),
    LOC_JIGGY_FP_SNOWMAN_PIPE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002B
    ),
    LOC_JIGGY_FP_TOBOGGAN: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002A
    ),
    LOC_JIGGY_FP_SNOWMAN_BUTTONS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002D
    ),
    LOC_JIGGY_FP_CHRISTMAS_TREE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002F
    ),
    LOC_JIGGY_FP_WOZZA: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000032
    ),
    LOC_JIGGY_FP_PRESENTS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002E
    ),
    LOC_JIGGY_FP_BOGGY_RACE_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000030
    ),
    LOC_JIGGY_FP_BOGGY_RACE_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002C
    ),
    LOC_JIGGY_FP_JINJO: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000029
    ),
    LOC_JIGGY_GV_JINXY: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0000003F
    ),
    LOC_JIGGY_GV_GRABBA: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0000003E
    ),
    LOC_JIGGY_GV_FLIP_PANELS: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000040
    ),
    LOC_JIGGY_GV_WATER_PYRAMID: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000042
    ),
    LOC_JIGGY_GV_ANCIENT_ONES: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000046
    ),
    LOC_JIGGY_GV_RUBEE: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000043
    ),
    LOC_JIGGY_GV_SANDYBUTT: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000041
    ),
    LOC_JIGGY_GV_GOBI: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000044
    ),
    LOC_JIGGY_GV_TRUNKER: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000045
    ),
    LOC_JIGGY_GV_JINJO: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0000003D
    ),
    LOC_JIGGY_MMM_NAPPER: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005D
    ),
    LOC_JIGGY_MMM_CELLAR: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005E
    ),
    LOC_JIGGY_MMM_TUMBLAR: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000062
    ),
    LOC_JIGGY_MMM_WELL: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005C
    ),
    LOC_JIGGY_MMM_FLOWERPOT: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000063
    ),
    LOC_JIGGY_MMM_CLOCK_TOWER: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005F
    ),
    LOC_JIGGY_MMM_MOTZAND: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000060
    ),
    LOC_JIGGY_MMM_LOGGO: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000064
    ),
    LOC_JIGGY_MMM_STORM_DRAIN: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000061
    ),
    LOC_JIGGY_MMM_JINJO: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005B
    ),
    LOC_JIGGY_RBB_SMOKESTACK: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000055
    ),
    LOC_JIGGY_RBB_WHISTLE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000054
    ),
    LOC_JIGGY_RBB_WAREHOUSE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000052
    ),
    LOC_JIGGY_RBB_METAL_CAGE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000059
    ),
    LOC_JIGGY_RBB_CAPTAINS_ROOM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000058
    ),
    LOC_JIGGY_RBB_BOSS_BOOM_BOX: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000056
    ),
    LOC_JIGGY_RBB_SNORKEL: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000053
    ),
    LOC_JIGGY_RBB_ENGINE_ROOM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0000005A
    ),
    LOC_JIGGY_RBB_PROPELLER: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000057
    ),
    LOC_JIGGY_RBB_JINJO: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000051
    ),
    "GLTF Secret Prize": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_882_NOTE_DOOR,
        address=0x05000000
    ),
    LOC_JIGGY_CCW_TREETOP_ROOM: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000050
    ),
    LOC_JIGGY_CCW_TREETOP_SNAREBEAR: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004F
    ),
    LOC_JIGGY_CCW_ZUBBA: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004C
    ),
    LOC_JIGGY_CCW_LEAVES: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004E
    ),
    LOC_JIGGY_CCW_CABIN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000048
    ),
    LOC_JIGGY_CCW_GNAWTY: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004B
    ),
    LOC_JIGGY_CCW_PLANT: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004D
    ),
    LOC_JIGGY_CCW_NABNUTS: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004A
    ),
    LOC_JIGGY_CCW_EYRIE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000049
    ),
    LOC_JIGGY_CCW_JINJO: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000047
    ),
    LOC_EMPTY_HONEYCOMB_SM_LOG: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x02000013
    ),
    LOC_EMPTY_HONEYCOMB_SM_WATERFALL: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x02000014
    ),
    LOC_EMPTY_HONEYCOMB_SM_TREE: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x02000016
    ),
    LOC_EMPTY_HONEYCOMB_SM_UNDERWATER: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x02000015
    ),
    LOC_EMPTY_HONEYCOMB_SM_ROCKS: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x02000018
    ),
    LOC_EMPTY_HONEYCOMB_SM_COLLIWOBBLE: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x02000017
    ),
    LOC_EMPTY_HONEYCOMB_MM_HILLSIDE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x02000001
    ),
    LOC_EMPTY_HONEYCOMB_MM_TOTEM: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x02000002
    ),
    LOC_EMPTY_HONEYCOMB_TTC_UNDERWATER: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x02000003
    ),
    LOC_EMPTY_HONEYCOMB_TTC_CRATE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x02000004
    ),
    LOC_EMPTY_HONEYCOMB_CC_PIPE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x02000005
    ),
    LOC_EMPTY_HONEYCOMB_CC_GRATE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x02000006
    ),
    LOC_EMPTY_HONEYCOMB_BGS_TIPTUP_STAND: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x02000008
    ),
    LOC_EMPTY_HONEYCOMB_BGS_INSIDE_MUMBOS_HUT: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x02000007
    ),
    LOC_EMPTY_HONEYCOMB_FP_SIR_SLUSH: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0200000A
    ),
    LOC_EMPTY_HONEYCOMB_FP_WOZZA: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x02000009
    ),
    LOC_EMPTY_HONEYCOMB_GV_CACTUS: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0200000B
    ),
    LOC_EMPTY_HONEYCOMB_GV_GOBI: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0200000C
    ),
    LOC_EMPTY_HONEYCOMB_MMM_CHURCH_RAFTER: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x02000011
    ),
    LOC_EMPTY_HONEYCOMB_MMM_FLOORBOARD: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x02000012
    ),
    LOC_EMPTY_HONEYCOMB_RBB_ENGINE_ROOM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x02000010
    ),
    LOC_EMPTY_HONEYCOMB_RBB_WAREHOUSE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0200000F
    ),
    LOC_EMPTY_HONEYCOMB_CCW_WINTER_NABNUTS: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0200000E
    ),
    LOC_EMPTY_HONEYCOMB_CCW_WINTER_GNAWTY: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0200000D
    ),
    LOC_MUMBO_TOKEN_GL_RED_CAULDRON: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,
        address=0x03000051
    ),
    LOC_MUMBO_TOKEN_GL_DRAIN_PIPE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,
        address=0x03000053
    ),
    LOC_MUMBO_TOKEN_GL_CCW_PODIUM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,
        address=0x03000052
    ),
    LOC_MUMBO_TOKEN_GL_ABOVE_CC_ENTRANCE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,
        address=0x03000054
    ),
    LOC_MUMBO_TOKEN_GL_BEHIND_SARCOPHAGUS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,
        address=0x03000055
    ),
    LOC_MUMBO_TOKEN_GL_ABOVE_FP_ENTRANCE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,
        address=0x03000056
    ),
    LOC_MUMBO_TOKEN_GL_BEHIND_MUMBO: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR,
        address=0x03000057
    ),
    LOC_MUMBO_TOKEN_GL_BELOW_RBB_ENTRANCE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR,
        address=0x03000059
    ),
    LOC_MUMBO_TOKEN_GL_BY_MMM_PODIUM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR,
        address=0x0300005A
    ),
    LOC_MUMBO_TOKEN_GL_NEAR_CCW_PODIUM_SWITCH: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR,
        address=0x03000058
    ),
    LOC_MUMBO_TOKEN_MM_BEHIND_PINK_JINJO: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000004
    ),
    LOC_MUMBO_TOKEN_MM_CHIMPY: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000001
    ),
    LOC_MUMBO_TOKEN_MM_STONEHENGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000002
    ),
    LOC_MUMBO_TOKEN_MM_MUMBOS_HUT: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000003
    ),
    LOC_MUMBO_TOKEN_MM_TERMITE_MOUND: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000005
    ),
    LOC_MUMBO_TOKEN_TTC_NIPPER: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0300000F
    ),
    LOC_MUMBO_TOKEN_TTC_MAST: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x03000009
    ),
    LOC_MUMBO_TOKEN_TTC_HOLD: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x03000006
    ),
    LOC_MUMBO_TOKEN_TTC_SHOCK_SPRING: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0300000E
    ),
    LOC_MUMBO_TOKEN_TTC_X_MARK: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0300000C
    ),
    LOC_MUMBO_TOKEN_TTC_LOCKUP_LEFT: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x03000007
    ),
    LOC_MUMBO_TOKEN_TTC_LOCKUP_RIGHT: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x03000008
    ),
    LOC_MUMBO_TOKEN_TTC_POOL: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0300000D
    ),
    LOC_MUMBO_TOKEN_TTC_CRATE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0300000B
    ),
    LOC_MUMBO_TOKEN_TTC_LIGHTHOUSE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0300000A
    ),
    LOC_MUMBO_TOKEN_CC_ENTRANCE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x03000011
    ),
    LOC_MUMBO_TOKEN_CC_CLANKER_TAIL: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x03000010
    ),
    LOC_MUMBO_TOKEN_CC_CLANKER_GOLD_TEETH: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x03000014
    ),
    LOC_MUMBO_TOKEN_CC_GRATE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x03000013
    ),
    LOC_MUMBO_TOKEN_CC_UNDERWATER_TUNNEL: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x03000012
    ),
    LOC_MUMBO_TOKEN_BGS_BEHIND_YELLOW_JINJO: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x03000018
    ),
    LOC_MUMBO_TOKEN_BGS_ATOP_CATTAIL: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x03000017
    ),
    LOC_MUMBO_TOKEN_BGS_CENTRAL_PLATFORM: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0300001B
    ),
    LOC_MUMBO_TOKEN_BGS_INSIDE_TANKTUP: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0300001C
    ),
    LOC_MUMBO_TOKEN_BGS_INSIDE_HUT: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x03000019
    ),
    LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBOS_HUT: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0300001A
    ),
    LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBO: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0300001E
    ),
    LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_LEFT: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x03000015
    ),
    LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_RIGHT: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x03000016
    ),
    LOC_MUMBO_TOKEN_BGS_INSIDE_MR_VILE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0300001D
    ),
    LOC_MUMBO_TOKEN_FP_INSIDE_IGLOO: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000028
    ),
    LOC_MUMBO_TOKEN_FP_BEHIND_PRESENTS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000021
    ),
    LOC_MUMBO_TOKEN_FP_ABOVE_HOUSE_FLIGHT_PAD: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000022
    ),
    LOC_MUMBO_TOKEN_FP_SIR_SLUSH_WOZZA: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000024
    ),
    LOC_MUMBO_TOKEN_FP_SIR_SLUSH_ISLAND: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000023
    ),
    LOC_MUMBO_TOKEN_FP_TOBOGGAN: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000026
    ),
    LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_LEFT: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0300001F
    ),
    LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_RIGHT: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000020
    ),
    LOC_MUMBO_TOKEN_FP_UNDER_CHRISTMAS_TREE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000025
    ),
    LOC_MUMBO_TOKEN_FP_UNDERWATER: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x03000027
    ),
    LOC_MUMBO_TOKEN_GV_BEHIND_JINXY: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0300002A
    ),
    LOC_MUMBO_TOKEN_GV_ABOVE_JINXYS_NOSE: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x03000029
    ),
    LOC_MUMBO_TOKEN_GV_INSIDE_JINXY: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x03000032
    ),
    LOC_MUMBO_TOKEN_GV_OUTSIDE_WATER_PYRAMID_FRONT: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0300002D
    ),
    LOC_MUMBO_TOKEN_GV_FLIP_PANEL_PYRAMID: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0300002E
    ),
    LOC_MUMBO_TOKEN_GV_MOAT: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0300002B
    ),
    LOC_MUMBO_TOKEN_GV_RUBEE: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x03000031
    ),
    LOC_MUMBO_TOKEN_GV_ATOP_CENTRAL_PYRAMID: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0300002C
    ),
    LOC_MUMBO_TOKEN_GV_CENTRAL_PYRAMID_POT: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0300002F
    ),
    LOC_MUMBO_TOKEN_GV_INSIDE_WATER_PYRAMID: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x03000030
    ),
    LOC_MUMBO_TOKEN_MMM_FIREPLACE: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0300003E
    ),
    LOC_MUMBO_TOKEN_MMM_CELLAR: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0300003D
    ),
    LOC_MUMBO_TOKEN_MMM_LOGGO: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000074
    ),
    LOC_MUMBO_TOKEN_MMM_SINK: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000041
    ),
    LOC_MUMBO_TOKEN_MMM_MAZE: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000037
    ),
    LOC_MUMBO_TOKEN_MMM_MAZE_HIDDEN_AREA: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000036
    ),
    LOC_MUMBO_TOKEN_MMM_SHACK_ROOF: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0300003C
    ),
    LOC_MUMBO_TOKEN_MMM_WELL: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0300003F
    ),
    LOC_MUMBO_TOKEN_MMM_BEHIND_GRAVE: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000038
    ),
    LOC_MUMBO_TOKEN_MMM_CLOCK_TOWER: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000035
    ),
    LOC_MUMBO_TOKEN_MMM_CHURCH_CHAIR: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0300003B
    ),
    LOC_MUMBO_TOKEN_MMM_CHURCH_RAFTER: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0300003A
    ),
    LOC_MUMBO_TOKEN_MMM_NEAR_SHACK: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000034
    ),
    LOC_MUMBO_TOKEN_MMM_BEDROOM: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000040
    ),
    LOC_MUMBO_TOKEN_MMM_FOUNTAIN: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000039
    ),
    LOC_MUMBO_TOKEN_MMM_NEAR_FOUNTAIN: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x03000033
    ),
    LOC_MUMBO_TOKEN_RBB_TOLL_BRIDGE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000045
    ),
    LOC_MUMBO_TOKEN_RBB_LIFEBOAT: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000044
    ),
    LOC_MUMBO_TOKEN_RBB_BEHIND_WITCH_SWITCH_TOWER: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000047
    ),
    LOC_MUMBO_TOKEN_RBB_BARRACKS: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0300004A
    ),
    LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_ENTRY: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0300004F
    ),
    LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_LEFT: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0300004D
    ),
    LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_RIGHT: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0300004E
    ),
    LOC_MUMBO_TOKEN_RBB_PERISCOPE_STOREROOM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000050
    ),
    LOC_MUMBO_TOKEN_RBB_NAVIGATION_ROOM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0300004B
    ),
    LOC_MUMBO_TOKEN_RBB_OVEN: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0300004C
    ),
    LOC_MUMBO_TOKEN_RBB_SMOKESTACK: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000042
    ),
    LOC_MUMBO_TOKEN_RBB_TOXIC_WASTE_DRUM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000046
    ),
    LOC_MUMBO_TOKEN_RBB_SHIP_BOW: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000043
    ),
    LOC_MUMBO_TOKEN_RBB_LEFT_SHIPPING_CRATE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000048
    ),
    LOC_MUMBO_TOKEN_RBB_MIDDLE_SHIPPING_CRATE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x03000049
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_ENTRANCE_SNAREBEAR: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000060
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_GARDEN_SNAREBEAR: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300005F
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_TREETOP_ABOVE_MUMBOS_HUT: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300005C
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_BEEHIVE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000061
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_CABIN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300005B
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_NABNUTS_DRESSER: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000062
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_NEAR_EYRIES_NEST: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300005D
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_THORNS: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300005E
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_ENTRANCE_SNAREBEAR: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000065
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_GNAWTY: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000067
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_GARDEN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000064
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_MUMBOS_HUT: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000069
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_TREETOP_ABOVE_MUMBOS_HUT: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000066
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_LEAVES: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000068
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_AFTER_NABNUTS_HOUSE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000063
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_ENTRANCE_SNAREBEAR: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300006B
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_ABOVE_MUMBOS_HUT: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300006E
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_LEAVES: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300006A
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_CABIN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300006D
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_SNAREBEAR: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300006C
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_GARDEN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0300006F
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_SIR_SLUSH: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000073
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_BEEHIVE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000071
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_NEAR_NABNUTS_HOUSE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000072
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_BEHIND_LAKE_PLATFORM: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x03000070
    ),
    LOC_MOLEHILL_MM_AFTER_CHIMPYS_STUMP: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x04000006
    ),
    LOC_MOLEHILL_MM_STONEHENGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x04000010
    ),
    LOC_MOLEHILL_MM_HUTS: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x04000002
    ),
    LOC_MOLEHILL_TTC_MAST: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x04000009
    ),
    LOC_MOLEHILL_TTC_NEAR_SANDCASTLE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0400000D
    ),
    LOC_MOLEHILL_CC_NEAR_SPINNING_BLADES: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x04000012
    ),
    LOC_MOLEHILL_BGS_BEHIND_WORLD_ENTRY: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0400000E
    ),
    LOC_MOLEHILL_FP_NEXT_TO_STACK_OF_PRESENTS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x04000001
    ),
    LOC_MOLEHILL_GV_NEAR_KAZOOIE_PYRAMID: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x04000011
    ),
    LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_1: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x0400000A
    ),
    LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_2: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x04000007
    ),
    LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_3: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x04000008
    ),
    LOC_MOLEHILL_SM_NEAR_MOUNTAIN_BRIDGE: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x0400000F
    ),
    LOC_MOLEHILL_SM_NEAR_RIVER: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x04000005
    ),
    LOC_MOLEHILL_SM_ROCKS: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x04000000
    ),
    LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_1: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x04000004
    ),
    LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_2: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x0400000C
    ),
    LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_3: BKLocationData(
        region=RGN_SPIRAL_MOUNTAIN,
        address=0x0400000B
    ),
    # ~ "BLUEEGGS Cheato": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5BE
    # ~ ),
    # ~ "REDFEATHERS Cheato": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5BF
    # ~ ),
    # ~ "GOLDFEATHERS Cheato": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C0
    # ~ ),
    # ~ "Ice Key": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C1
    # ~ ),
    # ~ "Pink Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C2
    # ~ ),
    # ~ "Blue Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C3
    # ~ ),
    # ~ "Cyan Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C4
    # ~ ),
    # ~ "Green Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C5
    # ~ ),
    # ~ "Red Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C6
    # ~ ),
    # ~ "Yellow Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C7
    # ~ ),
# Mumbo's Mountain Notes
    LOC_NOTE_MM_BRIDGE_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010218DD
    ),
    LOC_NOTE_MM_BRIDGE_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021791
    ),
    LOC_NOTE_MM_BRIDGE_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102165A
    ),
    LOC_NOTE_MM_BRIDGE_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021537
    ),
    LOC_NOTE_MM_BRIDGE_5: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102141F
    ),
    LOC_NOTE_MM_BRIDGE_6: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021317
    ),
    LOC_NOTE_MM_BRIDGE_7: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021226
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010202F1
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010202BB
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020281
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020216
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_5: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102018E
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_6: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102010A
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_7: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020098
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_8: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010200CC
    ),
    LOC_NOTE_MM_SLOPE_TO_TICKERS_9: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020176
    ),
    LOC_NOTE_MM_SLOPE_TO_STONEHENGE_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FAF7
    ),
    LOC_NOTE_MM_SLOPE_TO_STONEHENGE_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FA8E
    ),
    LOC_NOTE_MM_SLOPE_TO_STONEHENGE_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FA16
    ),
    LOC_NOTE_MM_SLOPE_TO_STONEHENGE_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F9AB
    ),
    LOC_NOTE_MM_STONEHENGE_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F46F
    ),
    LOC_NOTE_MM_STONEHENGE_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F2DF
    ),
    LOC_NOTE_MM_STONEHENGE_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F145
    ),
    LOC_NOTE_MM_STONEHENGE_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F041
    ),
    LOC_NOTE_MM_STONEHENGE_5: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102EF58
    ),
    LOC_NOTE_MM_STONEHENGE_6: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102EF42
    ),
    LOC_NOTE_MM_STONEHENGE_7: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102EF46
    ),
    LOC_NOTE_MM_STONEHENGE_8: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102EFF6
    ),
    LOC_NOTE_MM_STONEHENGE_9: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F0C1
    ),
    LOC_NOTE_MM_STONEHENGE_10: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F236
    ),
    LOC_NOTE_MM_STONEHENGE_11: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F39E
    ),
    LOC_NOTE_MM_STONEHENGE_12: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F515
    ),
    LOC_NOTE_MM_STONEHENGE_13: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F68B
    ),
    LOC_NOTE_MM_STONEHENGE_14: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F777
    ),
    LOC_NOTE_MM_CONGA_UPPER_RIGHT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FB90
    ),
    LOC_NOTE_MM_CONGA_UPPER_RIGHT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FADF
    ),
    LOC_NOTE_MM_CONGA_UPPER_RIGHT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FAF0
    ),
    LOC_NOTE_MM_CONGA_UPPER_LEFT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F808
    ),
    LOC_NOTE_MM_CONGA_UPPER_LEFT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F75B
    ),
    LOC_NOTE_MM_CONGA_UPPER_LEFT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F765
    ),
    LOC_NOTE_MM_CONGA_MIDDLE_RIGHT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FDBB
    ),
    LOC_NOTE_MM_CONGA_MIDDLE_RIGHT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FD10
    ),
    LOC_NOTE_MM_CONGA_MIDDLE_RIGHT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FD11
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_LEFT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F5CD
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_LEFT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F5E1
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_LEFT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F693
    ),
    LOC_NOTE_MM_CONGA_MIDDLE_LEFT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F38B
    ),
    LOC_NOTE_MM_CONGA_MIDDLE_LEFT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F37D
    ),
    LOC_NOTE_MM_CONGA_MIDDLE_LEFT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F435
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_RIGHT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FBAA
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_RIGHT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FBFA
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_RIGHT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FC5A
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F9BF
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102F9CA
    ),
    LOC_NOTE_MM_CONGA_BOTTOM_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102FA70
    ),
    LOC_NOTE_MM_MUMBO_TOP_RIGHT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021D2D
    ),
    LOC_NOTE_MM_MUMBO_TOP_RIGHT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021E20
    ),
    LOC_NOTE_MM_MUMBO_TOP_RIGHT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021E1A
    ),
    LOC_NOTE_MM_MUMBO_MIDDLE_RIGHT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021BBB
    ),
    LOC_NOTE_MM_MUMBO_MIDDLE_RIGHT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021C6D
    ),
    LOC_NOTE_MM_MUMBO_MIDDLE_RIGHT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021C22
    ),
    LOC_NOTE_MM_MUMBO_MIDDLE_LEFT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010214FE
    ),
    LOC_NOTE_MM_MUMBO_MIDDLE_LEFT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102150B
    ),
    LOC_NOTE_MM_MUMBO_MIDDLE_LEFT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102159C
    ),
    LOC_NOTE_MM_MUMBO_LOWER_LEFT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102177B
    ),
    LOC_NOTE_MM_MUMBO_LOWER_LEFT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021835
    ),
    LOC_NOTE_MM_MUMBO_LOWER_LEFT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010217F4
    ),
    LOC_NOTE_MM_MUMBO_BOTTOM_MIDDLE_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021B3C
    ),
    LOC_NOTE_MM_MUMBO_BOTTOM_MIDDLE_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021BF5
    ),
    LOC_NOTE_MM_MUMBO_BOTTOM_MIDDLE_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021B12
    ),
    LOC_NOTE_MM_MUMBO_BOTTOM_RIGHT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01022186
    ),
    LOC_NOTE_MM_MUMBO_BOTTOM_RIGHT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01022094
    ),
    LOC_NOTE_MM_MUMBO_BOTTOM_RIGHT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102209A
    ),
    LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010E0083
    ),
    LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010EFF4D
    ),
    LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010EFE4D
    ),
    LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010EFE46
    ),
    LOC_NOTE_MM_TOTEM_POLE_HUT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010211FA
    ),
    LOC_NOTE_MM_TOTEM_POLE_HUT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010215C3
    ),
    LOC_NOTE_MM_TOTEM_POLE_HUT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010219FA
    ),
    LOC_NOTE_MM_TOTEM_POLE_HUT_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01021799
    ),
    LOC_NOTE_MM_TOTEM_POLE_HUT_5: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020F57
    ),
    LOC_NOTE_MM_TOTEM_POLE_HUT_6: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020D88
    ),
    LOC_NOTE_MM_DESTROY_HUT_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020069
    ),
    LOC_NOTE_MM_DESTROY_HUT_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102006A
    ),
    LOC_NOTE_MM_DESTROY_HUT_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102006B
    ),
    LOC_NOTE_MM_DESTROY_HUT_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102006C
    ),
    LOC_NOTE_MM_DESTROY_HUT_5: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0102006D
    ),
    LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010208F5
    ),
    LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020923
    ),
    LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020952
    ),
    LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020CB1
    ),
    LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020D28
    ),
    LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x01020D9D
    ),
    LOC_NOTE_MM_TERMITE_MOUND_LANDING_1: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010C0374
    ),
    LOC_NOTE_MM_TERMITE_MOUND_LANDING_2: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010C0316
    ),
    LOC_NOTE_MM_TERMITE_MOUND_LANDING_3: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010C02AA
    ),
    LOC_NOTE_MM_TERMITE_MOUND_LANDING_4: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010C029A
    ),
    LOC_NOTE_MM_TERMITE_MOUND_LANDING_5: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010C02FA
    ),
    LOC_NOTE_MM_TERMITE_MOUND_LANDING_6: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x010C0362
    ),
    LOC_NOTE_TTC_ARRIVAL_PLATFORM_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010719EA
    ),
    LOC_NOTE_TTC_ARRIVAL_PLATFORM_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071C0D
    ),
    LOC_NOTE_TTC_ARRIVAL_PLATFORM_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071E29
    ),
    LOC_NOTE_TTC_ARRIVAL_PLATFORM_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071C0A
    ),
    LOC_NOTE_TTC_BLUBBERS_FORWARD_NETTING_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070156
    ),
    LOC_NOTE_TTC_BLUBBERS_FORWARD_NETTING_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010702D8
    ),
    LOC_NOTE_TTC_BLUBBERS_FORWARD_NETTING_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107047C
    ),
    LOC_NOTE_TTC_TOP_SANDCASTLE_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071CC5
    ),
    LOC_NOTE_TTC_TOP_SANDCASTLE_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071CBE
    ),
    LOC_NOTE_TTC_TOP_SANDCASTLE_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071D71
    ),
    LOC_NOTE_TTC_TOP_SANDCASTLE_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071E14
    ),
    LOC_NOTE_TTC_TOP_SANDCASTLE_5: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071E2A
    ),
    LOC_NOTE_TTC_INSIDE_SANDCASTLE_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010A010A
    ),
    LOC_NOTE_TTC_INSIDE_SANDCASTLE_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010A0065
    ),
    LOC_NOTE_TTC_INSIDE_SANDCASTLE_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010A053B
    ),
    LOC_NOTE_TTC_INSIDE_SANDCASTLE_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010A0496
    ),
    LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0106FB6F
    ),
    LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0106FF9A
    ),
    LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01060367
    ),
    LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010604A3
    ),
    LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_5: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010602BD
    ),
    LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_6: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0106FF54
    ),
    LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EF90
    ),
    LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EDD8
    ),
    LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EC2A
    ),
    LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EA70
    ),
    LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EBE6
    ),
    LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EBB0
    ),
    LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EB78
    ),
    LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EB42
    ),
    LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EB41
    ),
    LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EB28
    ),
    LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EB10
    ),
    LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107EAF5
    ),
    LOC_NOTE_TTC_RAISED_POOL_CRAB_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107F2BD
    ),
    LOC_NOTE_TTC_RAISED_POOL_CRAB_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107F3A0
    ),
    LOC_NOTE_TTC_RAISED_POOL_CRAB_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107F3ED
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_CHEST_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010707ED
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_CHEST_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010708EE
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_CHEST_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010709F2
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_NIPPER_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070EFD
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_NIPPER_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070F48
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_NIPPER_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070F98
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_BLUBBERS_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010713D9
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_BLUBBERS_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071495
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_BLUBBERS_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071552
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_SANDCASTLE_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071B66
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_SANDCASTLE_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071C38
    ),
    LOC_NOTE_TTC_HIGH_BRIDGE_SANDCASTLE_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071D0A
    ),
    LOC_NOTE_TTC_SHOCK_SPRING_PILLAR_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071695
    ),
    LOC_NOTE_TTC_SHOCK_SPRING_PILLAR_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071712
    ),
    LOC_NOTE_TTC_SHOCK_SPRING_PILLAR_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107178F
    ),
    LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071CC6
    ),
    LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071F07
    ),
    LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107213E
    ),
    LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010720A2
    ),
    LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_5: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071DB9
    ),
    LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_6: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071BCB
    ),
    LOC_NOTE_TTC_TREE_STERN_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071264
    ),
    LOC_NOTE_TTC_TREE_STERN_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010712D2
    ),
    LOC_NOTE_TTC_TREE_STERN_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010711F7
    ),
    LOC_NOTE_TTC_TREE_STERN_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071176
    ),
    LOC_NOTE_TTC_TREE_BOW_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070929
    ),
    LOC_NOTE_TTC_TREE_BOW_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070945
    ),
    LOC_NOTE_TTC_TREE_BOW_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070859
    ),
    LOC_NOTE_TTC_TREE_BOW_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070852
    ),
    LOC_NOTE_TTC_BLUBBERS_BOW_NETTING_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070618
    ),
    LOC_NOTE_TTC_BLUBBERS_BOW_NETTING_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010707A2
    ),
    LOC_NOTE_TTC_BLUBBERS_BOW_NETTING_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070935
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070D41
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070D1C
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070D04
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070D02
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_5: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070D05
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01050174
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010500B5
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01050038
    ),
    LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0105FFB7
    ),
    LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0105FA71
    ),
    LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0105F9EF
    ),
    LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0105F970
    ),
    LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0105F8E9
    ),
    LOC_NOTE_TTC_TREASURE_CHEST_SSS_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070CC7
    ),
    LOC_NOTE_TTC_TREASURE_CHEST_SSS_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070CF9
    ),
    LOC_NOTE_TTC_TREASURE_CHEST_SSS_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070C74
    ),
    LOC_NOTE_TTC_TREASURE_CHEST_SSS_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070C17
    ),
    LOC_NOTE_TTC_TREASURE_CHEST_SSS_5: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070BE7
    ),
    LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107FB5D
    ),
    LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107FA87
    ),
    LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107F9AD
    ),
    LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107F894
    ),
    LOC_NOTE_TTC_CAVE_TO_LIGHTHOUSE_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070828
    ),
    LOC_NOTE_TTC_PATH_TO_LIGHTHOUSE_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070CA5
    ),
    LOC_NOTE_TTC_PATH_TO_LIGHTHOUSE_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070BD3
    ),
    LOC_NOTE_TTC_PATH_TO_LIGHTHOUSE_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01070BA4
    ),
    LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_1: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071625
    ),
    LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_2: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0107155A
    ),
    LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_3: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x01071693
    ),
    LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_4: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010717FF
    ),
    LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_5: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x010717C5
    ),
    LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BF1CA
    ),
    LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BF090
    ),
    LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BF19E
    ),
    LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BF02D
    ),
    LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BFDE3
    ),
    LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BFB60
    ),
    LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BFBD0
    ),
    LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010BF89A
    ),
    LOC_NOTE_CC_PIPE_TO_CLANKER_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0105
    ),
    LOC_NOTE_CC_PIPE_TO_CLANKER_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B01B4
    ),
    LOC_NOTE_CC_PIPE_TO_CLANKER_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B03D5
    ),
    LOC_NOTE_CC_PIPE_TO_CLANKER_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B05E3
    ),
    LOC_NOTE_CC_PIPE_TO_CLANKER_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0740
    ),
    LOC_NOTE_CC_PIPE_TO_CLANKER_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0915
    ),
    LOC_NOTE_CC_RIGHT_FLOOR_PIPE_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1E02
    ),
    LOC_NOTE_CC_RIGHT_FLOOR_PIPE_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B203C
    ),
    LOC_NOTE_CC_RIGHT_FLOOR_PIPE_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B225A
    ),
    LOC_NOTE_CC_RIGHT_FLOOR_PIPE_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B240B
    ),
    LOC_NOTE_CC_RIGHT_FLOOR_PIPE_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B25C1
    ),
    LOC_NOTE_CC_RIGHT_FLOOR_PIPE_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B271B
    ),
    LOC_NOTE_CC_RIGHT_FLOOR_PIPE_7: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B286D
    ),
    LOC_NOTE_CC_GLOWING_ROOM_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B42C5
    ),
    LOC_NOTE_CC_GLOWING_ROOM_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B45A7
    ),
    LOC_NOTE_CC_GLOWING_ROOM_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B47DB
    ),
    LOC_NOTE_CC_GLOWING_ROOM_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B48DE
    ),
    LOC_NOTE_CC_GLOWING_ROOM_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B4350
    ),
    LOC_NOTE_CC_GLOWING_ROOM_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B4069
    ),
    LOC_NOTE_CC_GLOWING_ROOM_7: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B3E39
    ),
    LOC_NOTE_CC_GLOWING_ROOM_8: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B3D0D
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0E1D
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1023
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0E18
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B093B
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B045C
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0251
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_7: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0457
    ),
    LOC_NOTE_CC_AROUND_ANCHOR_8: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B0940
    ),
    LOC_NOTE_CC_ALONG_SPINE_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1D13
    ),
    LOC_NOTE_CC_ALONG_SPINE_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1E5B
    ),
    LOC_NOTE_CC_ALONG_SPINE_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1F91
    ),
    LOC_NOTE_CC_ALONG_SPINE_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B20C9
    ),
    LOC_NOTE_CC_ALONG_SPINE_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2525
    ),
    LOC_NOTE_CC_ALONG_SPINE_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2621
    ),
    LOC_NOTE_CC_ALONG_SPINE_7: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2715
    ),
    LOC_NOTE_CC_ALONG_SPINE_8: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2820
    ),
    LOC_NOTE_CC_ALONG_SPINE_9: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2933
    ),
    LOC_NOTE_CC_ALONG_SPINE_10: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2A6F
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B37B3
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B3854
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B3905
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B389B
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B382E
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B3562
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_7: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B337E
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_8: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B318D
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_9: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2F4D
    ),
    LOC_NOTE_CC_RAISED_PIPE_BEHIND_10: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2D2A
    ),
    LOC_NOTE_CC_PLATFORM_BLOWHOLE_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1E22
    ),
    LOC_NOTE_CC_PLATFORM_BLOWHOLE_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1DB7
    ),
    LOC_NOTE_CC_PLATFORM_BLOWHOLE_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1BC9
    ),
    LOC_NOTE_CC_PLATFORM_BLOWHOLE_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B19D7
    ),
    LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0122F5C5
    ),
    LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0122F600
    ),
    LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0122F700
    ),
    LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0122F864
    ),
    LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0122FA97
    ),
    LOC_NOTE_CC_TUNNEL_PORTSIDE_GILLS_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01220E76
    ),
    LOC_NOTE_CC_TUNNEL_PORTSIDE_GILLS_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01220CD5
    ),
    LOC_NOTE_CC_TUNNEL_PORTSIDE_GILLS_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01220A0D
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01221820
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01221BA2
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01221EAF
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0122205D
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01221F6C
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01221BF9
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_7: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0122188C
    ),
    LOC_NOTE_CC_INSIDE_MOUTH_8: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01221640
    ),
    LOC_NOTE_CC_BLOWHOLE_SAWBLADE_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x012104A1
    ),
    LOC_NOTE_CC_BLOWHOLE_SAWBLADE_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01210249
    ),
    LOC_NOTE_CC_BLOWHOLE_SAWBLADE_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0121FFF1
    ),
    LOC_NOTE_CC_BLOWHOLE_SAWBLADE_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0121FD99
    ),
    LOC_NOTE_CC_BLOWHOLE_SAWBLADE_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0121FB41
    ),
    LOC_NOTE_CC_BLOWHOLE_SAWBLADE_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0121F8E9
    ),
    LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B26C7
    ),
    LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B284D
    ),
    LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B296F
    ),
    LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B2A91
    ),
    LOC_NOTE_CC_RIGHT_ANGLED_DUCT_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B3842
    ),
    LOC_NOTE_CC_RIGHT_ANGLED_DUCT_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B3818
    ),
    LOC_NOTE_CC_RIGHT_ANGLED_DUCT_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B37FF
    ),
    LOC_NOTE_CC_RIGHT_ANGLED_DUCT_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B37DE
    ),
    LOC_NOTE_CC_RIGHT_ANGLED_DUCT_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B37B4
    ),
    LOC_NOTE_CC_LEFT_CUBBIES_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B1DAA
    ),
    LOC_NOTE_CC_LEFT_CUBBIES_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x010B13A5
    ),
    LOC_NOTE_CC_AFT_SAWBLADE_1: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x012304AB
    ),
    LOC_NOTE_CC_AFT_SAWBLADE_2: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01230276
    ),
    LOC_NOTE_CC_AFT_SAWBLADE_3: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x01230037
    ),
    LOC_NOTE_CC_AFT_SAWBLADE_4: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0123FDF8
    ),
    LOC_NOTE_CC_AFT_SAWBLADE_5: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0123FBB4
    ),
    LOC_NOTE_CC_AFT_SAWBLADE_6: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0123F8D5
    ),
    LOC_NOTE_BGS_BRIDGE_ENTRYWAY_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0BFD
    ),
    LOC_NOTE_BGS_BRIDGE_ENTRYWAY_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0B3C
    ),
    LOC_NOTE_BGS_BRIDGE_ENTRYWAY_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0A74
    ),
    LOC_NOTE_BGS_BRIDGE_ENTRYWAY_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0972
    ),
    LOC_NOTE_BGS_BRIDGE_ENTRYWAY_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0877
    ),
    LOC_NOTE_BGS_LOG_JIGGY_SWITCH_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0479
    ),
    LOC_NOTE_BGS_LOG_JIGGY_SWITCH_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D03AB
    ),
    LOC_NOTE_BGS_LOG_JIGGY_SWITCH_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D02DB
    ),
    LOC_NOTE_BGS_LOG_STUMPS_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFA82
    ),
    LOC_NOTE_BGS_LOG_STUMPS_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DF972
    ),
    LOC_NOTE_BGS_LOG_STUMPS_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DF866
    ),
    LOC_NOTE_BGS_LOG_TURTLE_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D09C5
    ),
    LOC_NOTE_BGS_LOG_TURTLE_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0AF9
    ),
    LOC_NOTE_BGS_LOG_TURTLE_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0C31
    ),
    LOC_NOTE_BGS_TANKTUPS_FLIPPERS_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D1581
    ),
    LOC_NOTE_BGS_TANKTUPS_FLIPPERS_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D1B5A
    ),
    LOC_NOTE_BGS_TANKTUPS_FLIPPERS_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D1B4B
    ),
    LOC_NOTE_BGS_TANKTUPS_FLIPPERS_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D1568
    ),
    LOC_NOTE_BGS_LOG_HUT_PILLARS_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D03BF
    ),
    LOC_NOTE_BGS_LOG_HUT_PILLARS_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D03DC
    ),
    LOC_NOTE_BGS_LOG_HUT_PILLARS_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D03F7
    ),
    LOC_NOTE_BGS_LOG_CROCODILE_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DF94E
    ),
    LOC_NOTE_BGS_LOG_CROCODILE_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DF80B
    ),
    LOC_NOTE_BGS_LOG_CROCODILE_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DF6C7
    ),
    LOC_NOTE_BGS_CROCODILES_SNOUT_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DF092
    ),
    LOC_NOTE_BGS_CROCODILES_SNOUT_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DEF66
    ),
    LOC_NOTE_BGS_CROCODILES_SNOUT_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DEE9E
    ),
    LOC_NOTE_BGS_CROCODILES_SNOUT_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DEE01
    ),
    LOC_NOTE_BGS_CROCODILES_SNOUT_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DED8A
    ),
    LOC_NOTE_BGS_BEHIND_GIANT_EGG_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DF93A
    ),
    LOC_NOTE_BGS_BEHIND_GIANT_EGG_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFBB7
    ),
    LOC_NOTE_BGS_BEHIND_GIANT_EGG_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFE35
    ),
    LOC_NOTE_BGS_BEHIND_GIANT_EGG_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFF73
    ),
    LOC_NOTE_BGS_BEHIND_GIANT_EGG_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D00A7
    ),
    LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFB93
    ),
    LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFB59
    ),
    LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFCDE
    ),
    LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DFEA5
    ),
    LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0049
    ),
    LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0425
    ),
    LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0615
    ),
    LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0765
    ),
    LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0A47
    ),
    LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0ED7
    ),
    LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D103C
    ),
    LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0FF5
    ),
    LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0E32
    ),
    LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0CD1
    ),
    LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_6: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0D4C
    ),
    LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_7: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0F2E
    ),
    LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0C88
    ),
    LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0AF5
    ),
    LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D09DF
    ),
    LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0727
    ),
    LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0111FCFE
    ),
    LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0111FC02
    ),
    LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0111FB29
    ),
    LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x01110301
    ),
    LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x011103FE
    ),
    LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_6: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x011104D9
    ),
    LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D006C
    ),
    LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D006D
    ),
    LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0069
    ),
    LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D006A
    ),
    LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D006B
    ),
    LOC_NOTE_BGS_CATTAIL_BLUE_JINJO_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD277
    ),
    LOC_NOTE_BGS_CATTAIL_BLUE_JINJO_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD2DB
    ),
    LOC_NOTE_BGS_CATTAIL_BLUE_JINJO_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD33F
    ),
    LOC_NOTE_BGS_BEHIND_BLUE_JINJO_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD1DC
    ),
    LOC_NOTE_BGS_BEHIND_BLUE_JINJO_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DCF92
    ),
    LOC_NOTE_BGS_BEHIND_BLUE_JINJO_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DCD27
    ),
    LOC_NOTE_BGS_BEHIND_BLUE_JINJO_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DCA51
    ),
    LOC_NOTE_BGS_BEHIND_BLUE_JINJO_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DC77B
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DDDC7
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DE598
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DE1AA
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DE1BD
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD9DC
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_6: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD7E8
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_7: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD9D7
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_8: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD214
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_9: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD20F
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_10: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD020
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_11: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DD018
    ),
    LOC_NOTE_BGS_WADING_BOOTS_MAZE_12: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010DDA0B
    ),
    LOC_NOTE_BGS_CROCODILE_RIGHT_NOSTRIL_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0110F980
    ),
    LOC_NOTE_BGS_CROCODILE_RIGHT_NOSTRIL_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0110F9C3
    ),
    LOC_NOTE_BGS_CROCODILE_RIGHT_NOSTRIL_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0110FA33
    ),
    LOC_NOTE_BGS_CROCODILE_LEFT_NOSTRIL_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0110F8A4
    ),
    LOC_NOTE_BGS_CROCODILE_LEFT_NOSTRIL_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0110F80F
    ),
    LOC_NOTE_BGS_CROCODILE_LEFT_NOSTRIL_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0110F74F
    ),
    LOC_NOTE_BGS_UNDER_HUT_PILLAR_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D01F9
    ),
    LOC_NOTE_BGS_UNDER_HUT_PILLAR_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D02D7
    ),
    LOC_NOTE_BGS_UNDER_HUT_PILLAR_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D01F6
    ),
    LOC_NOTE_BGS_UNDER_HUT_PILLAR_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D011E
    ),
    LOC_NOTE_BGS_BEHIND_HUT_PILLARS_1: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0AE3
    ),
    LOC_NOTE_BGS_BEHIND_HUT_PILLARS_2: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0C2E
    ),
    LOC_NOTE_BGS_BEHIND_HUT_PILLARS_3: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0D77
    ),
    LOC_NOTE_BGS_BEHIND_HUT_PILLARS_4: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0DAE
    ),
    LOC_NOTE_BGS_BEHIND_HUT_PILLARS_5: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x010D0DE2
    ),
    LOC_NOTE_FP_UPPER_BOGGY_RAMP_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01272B34
    ),
    LOC_NOTE_FP_UPPER_BOGGY_RAMP_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127280F
    ),
    LOC_NOTE_FP_UPPER_BOGGY_RAMP_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127248D
    ),
    LOC_NOTE_FP_UPPER_BOGGY_RAMP_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012720D4
    ),
    LOC_NOTE_FP_UPPER_BOGGY_RAMP_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271CF4
    ),
    LOC_NOTE_FP_LOWER_BOGGY_RAMP_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271966
    ),
    LOC_NOTE_FP_LOWER_BOGGY_RAMP_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271578
    ),
    LOC_NOTE_FP_LOWER_BOGGY_RAMP_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271134
    ),
    LOC_NOTE_FP_LOWER_BOGGY_RAMP_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270D17
    ),
    LOC_NOTE_FP_BEHIND_TREE_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270C30
    ),
    LOC_NOTE_FP_BEHIND_TREE_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270D1E
    ),
    LOC_NOTE_FP_BEHIND_TREE_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270A2F
    ),
    LOC_NOTE_FP_BEHIND_TREE_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270544
    ),
    LOC_NOTE_FP_BEHIND_TREE_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127010C
    ),
    LOC_NOTE_FP_STACK_PRESENTS_PURPLE_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127EFAE
    ),
    LOC_NOTE_FP_STACK_PRESENTS_PURPLE_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127EED2
    ),
    LOC_NOTE_FP_STACK_PRESENTS_PURPLE_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127EDF8
    ),
    LOC_NOTE_FP_STACK_PRESENTS_PURPLE_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127ED1B
    ),
    LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127EB8A
    ),
    LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127EC9C
    ),
    LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127EABA
    ),
    LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127E9A8
    ),
    LOC_NOTE_FP_HOUSE_MUMBOS_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127124C
    ),
    LOC_NOTE_FP_HOUSE_MUMBOS_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012711FF
    ),
    LOC_NOTE_FP_HOUSE_MUMBOS_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012711C0
    ),
    LOC_NOTE_FP_HOUSE_BETWEEN_SLUSHES_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271E33
    ),
    LOC_NOTE_FP_HOUSE_BETWEEN_SLUSHES_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271F07
    ),
    LOC_NOTE_FP_HOUSE_BETWEEN_SLUSHES_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271FF9
    ),
    LOC_NOTE_FP_BEEHIVE_PLATFORM_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01272329
    ),
    LOC_NOTE_FP_BEEHIVE_PLATFORM_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012724F2
    ),
    LOC_NOTE_FP_BEEHIVE_PLATFORM_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012725F6
    ),
    LOC_NOTE_FP_BEEHIVE_PLATFORM_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01272521
    ),
    LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127036F
    ),
    LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012705FD
    ),
    LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012702A3
    ),
    LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127000D
    ),
    LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270077
    ),
    LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127FAD2
    ),
    LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127FA70
    ),
    LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127F770
    ),
    LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127F556
    ),
    LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127F848
    ),
    LOC_NOTE_FP_INSIDE_TREE_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0153FF41
    ),
    LOC_NOTE_FP_INSIDE_TREE_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0153FE19
    ),
    LOC_NOTE_FP_INSIDE_TREE_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0153FE1C
    ),
    LOC_NOTE_FP_INSIDE_TREE_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0153FF3E
    ),
    LOC_NOTE_FP_INSIDE_TREE_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01530137
    ),
    LOC_NOTE_FP_INSIDE_TREE_6: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0153037B
    ),
    LOC_NOTE_FP_INSIDE_TREE_7: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01530571
    ),
    LOC_NOTE_FP_INSIDE_TREE_8: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01530691
    ),
    LOC_NOTE_FP_INSIDE_TREE_9: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0153068D
    ),
    LOC_NOTE_FP_INSIDE_TREE_10: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01530575
    ),
    LOC_NOTE_FP_INSIDE_TREE_11: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01530376
    ),
    LOC_NOTE_FP_INSIDE_TREE_12: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01530132
    ),
    LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127E546
    ),
    LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127E4F4
    ),
    LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127E368
    ),
    LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127E109
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127E920
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127ECDC
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127F328
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127F59A
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127F6CF
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_6: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127FC28
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_7: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127FE0E
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_8: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127FAB4
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_9: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127FAC3
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_10: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127000F
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_11: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127042F
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_12: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012707C0
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_13: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270AFE
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_14: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270B91
    ),
    LOC_NOTE_FP_UP_SNOWMANS_SCARF_15: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270E9C
    ),
    LOC_NOTE_FP_SCARF_AROUND_NECK_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012710E4
    ),
    LOC_NOTE_FP_SCARF_AROUND_NECK_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01270F98
    ),
    LOC_NOTE_FP_SCARF_AROUND_NECK_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271584
    ),
    LOC_NOTE_FP_SCARF_AROUND_NECK_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271700
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01272397
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012724CC
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012721F5
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271CBC
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271886
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_6: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271708
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_7: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012719E1
    ),
    LOC_NOTE_FP_TOP_SNOWMANS_HAT_8: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271F28
    ),
    LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0148FF9A
    ),
    LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0148FEA7
    ),
    LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0148017A
    ),
    LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01480377
    ),
    LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01480463
    ),
    LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_6: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01480195
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127134D
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271157
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_3: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271119
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_4: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127117F
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_5: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0127144B
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_6: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x012716DF
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_7: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271A5E
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_8: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271CA8
    ),
    LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_9: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x01271BE6
    ),
    LOC_NOTE_GV_SLOPE_ENTRYWAY_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011222F7
    ),
    LOC_NOTE_GV_SLOPE_ENTRYWAY_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01122157
    ),
    LOC_NOTE_GV_SLOPE_ENTRYWAY_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121F98
    ),
    LOC_NOTE_GV_SLOPE_ENTRYWAY_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121DAC
    ),
    LOC_NOTE_GV_SLOPE_ENTRYWAY_5: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121BB1
    ),
    LOC_NOTE_GV_JINXYS_RIGHT_PAW_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011214C4
    ),
    LOC_NOTE_GV_JINXYS_RIGHT_PAW_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011214B7
    ),
    LOC_NOTE_GV_JINXYS_RIGHT_PAW_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121345
    ),
    LOC_NOTE_GV_JINXYS_LEFT_PAW_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120FF3
    ),
    LOC_NOTE_GV_JINXYS_LEFT_PAW_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120FE7
    ),
    LOC_NOTE_GV_JINXYS_LEFT_PAW_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120E5A
    ),
    LOC_NOTE_GV_MAGIC_CARPET_RIDE_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112F414
    ),
    LOC_NOTE_GV_MAGIC_CARPET_RIDE_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112F377
    ),
    LOC_NOTE_GV_MAGIC_CARPET_RIDE_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112F2EC
    ),
    LOC_NOTE_GV_MAGIC_CARPET_RIDE_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112F261
    ),
    LOC_NOTE_GV_MAGIC_CARPET_RIDE_5: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112F1DD
    ),
    LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120FAB
    ),
    LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120F4C
    ),
    LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011213C8
    ),
    LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121428
    ),
    LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121577
    ),
    LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121A86
    ),
    LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121590
    ),
    LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121081
    ),
    LOC_NOTE_GV_NEXT_FLIP_PUZZLE_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121740
    ),
    LOC_NOTE_GV_NEXT_FLIP_PUZZLE_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121999
    ),
    LOC_NOTE_GV_FLIP_PUZZLE_FRONT_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121E58
    ),
    LOC_NOTE_GV_FLIP_PUZZLE_FRONT_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121D0A
    ),
    LOC_NOTE_GV_FLIP_PUZZLE_FRONT_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121BBF
    ),
    LOC_NOTE_GV_FLIP_PUZZLE_FRONT_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121A75
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120D2E
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120825
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112030D
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FF80
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_5: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FBF2
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_6: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FBDF
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_7: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FBE3
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_8: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FF62
    ),
    LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_9: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011202DF
    ),
    LOC_NOTE_GV_TURBO_TRAINERS_PLATFORM_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120395
    ),
    LOC_NOTE_GV_TURBO_TRAINERS_PLATFORM_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120014
    ),
    LOC_NOTE_GV_WATER_PYRAMID_RACE_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FBC2
    ),
    LOC_NOTE_GV_WATER_PYRAMID_RACE_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011205B3
    ),
    LOC_NOTE_GV_WATER_PYRAMID_RACE_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FDB5
    ),
    LOC_NOTE_GV_WATER_PYRAMID_RACE_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FBA1
    ),
    LOC_NOTE_GV_BEHIND_JINXY_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011206B7
    ),
    LOC_NOTE_GV_BEHIND_JINXY_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120B1A
    ),
    LOC_NOTE_GV_BEHIND_JINXY_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120F3E
    ),
    LOC_NOTE_GV_BEHIND_JINXY_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121390
    ),
    LOC_NOTE_GV_BEHIND_JINXY_5: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011217D0
    ),
    LOC_NOTE_GV_BEHIND_JINXY_6: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011217DE
    ),
    LOC_NOTE_GV_BEHIND_JINXY_7: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011217F2
    ),
    LOC_NOTE_GV_BEHIND_JINXY_8: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01121802
    ),
    LOC_NOTE_GV_FLOOR_INSIDE_JINXY_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011A058C
    ),
    LOC_NOTE_GV_FLOOR_INSIDE_JINXY_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011AEFC0
    ),
    LOC_NOTE_GV_FLOOR_INSIDE_JINXY_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011AF5F7
    ),
    LOC_NOTE_GV_FLOOR_INSIDE_JINXY_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011A0BCA
    ),
    LOC_NOTE_GV_CARPETS_INSIDE_JINXY_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011A05EF
    ),
    LOC_NOTE_GV_CARPETS_INSIDE_JINXY_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011A03BC
    ),
    LOC_NOTE_GV_CARPETS_INSIDE_JINXY_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011A015B
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112E5B4
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112E76B
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112E932
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112EAE4
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_5: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112EC98
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_6: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112EC45
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_7: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112EBF4
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_8: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112EB91
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_9: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112EA00
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_10: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112E870
    ),
    LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_11: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112E6D0
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_ENTRYWAY_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0114165E
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_ENTRYWAY_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0114124C
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_ENTRYWAY_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0114111F
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0114F95C
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0114F61C
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0114F192
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0114F089
    ),
    LOC_NOTE_GV_INSIDE_WATER_PYRAMID_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011502DD
    ),
    LOC_NOTE_GV_INSIDE_WATER_PYRAMID_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0115FD02
    ),
    LOC_NOTE_GV_INSIDE_WATER_PYRAMID_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0115FD13
    ),
    LOC_NOTE_GV_INSIDE_WATER_PYRAMID_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x011502DB
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FCB3
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112FF42
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120416
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120AC2
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_5: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01120884
    ),
    LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_6: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0112046C
    ),
    LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01130013
    ),
    LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01130397
    ),
    LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01130014
    ),
    LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0113FC8F
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_1: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x01160538
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_2: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0116049F
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_3: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0116FFBF
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_4: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0116FE82
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_5: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0116FAA1
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_6: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0116FA6C
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_7: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0116FCEF
    ),
    LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_8: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0116FE1B
    ),
    LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0AB6
    ),
    LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0BE5
    ),
    LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0DF9
    ),
    LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0E2D
    ),
    LOC_NOTE_MMM_HEDGE_MAZE_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BFEE0
    ),
    LOC_NOTE_MMM_HEDGE_MAZE_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0195
    ),
    LOC_NOTE_MMM_HEDGE_MAZE_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF975
    ),
    LOC_NOTE_MMM_HEDGE_MAZE_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF826
    ),
    LOC_NOTE_MMM_HEDGE_MAZE_5: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF335
    ),
    LOC_NOTE_MMM_HEDGE_MAZE_6: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF299
    ),
    LOC_NOTE_MMM_FOUL_FOUNTAIN_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B16C0
    ),
    LOC_NOTE_MMM_FOUL_FOUNTAIN_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B1AE2
    ),
    LOC_NOTE_MMM_FOUL_FOUNTAIN_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B1EF7
    ),
    LOC_NOTE_MMM_FOUL_FOUNTAIN_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B1AD4
    ),
    LOC_NOTE_MMM_ALCOVE_GRAVEYARD_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF254
    ),
    LOC_NOTE_MMM_ALCOVE_GRAVEYARD_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF1A4
    ),
    LOC_NOTE_MMM_ALCOVE_GRAVEYARD_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF0F5
    ),
    LOC_NOTE_MMM_GUTTER_DRAIN_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BFC2F
    ),
    LOC_NOTE_MMM_GUTTER_DRAIN_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B07DF
    ),
    LOC_NOTE_MMM_GUTTER_DRAIN_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B1311
    ),
    LOC_NOTE_MMM_GUTTER_DRAIN_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0764
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012605F1
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012603FF
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0126020A
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0126FCDB
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_5: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0126FA3A
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_6: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0126FC49
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_7: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0126FE3C
    ),
    LOC_NOTE_MMM_DINING_ROOM_CHAIR_8: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0126002F
    ),
    LOC_NOTE_MMM_UPPER_GUTTERS_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0AB3
    ),
    LOC_NOTE_MMM_UPPER_GUTTERS_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B12DE
    ),
    LOC_NOTE_MMM_UPPER_GUTTERS_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0B96
    ),
    LOC_NOTE_MMM_UPPER_GUTTERS_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0363
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0129FDBD
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0129FDF3
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0129FE3E
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0129FE89
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_5: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0129002F
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_6: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x01290113
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_7: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0129015E
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_8: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012901A9
    ),
    LOC_NOTE_MMM_PAINTING_ROOM_9: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012901A2
    ),
    LOC_NOTE_MMM_BEDROOM_DRESSER_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012D038B
    ),
    LOC_NOTE_MMM_BEDROOM_DRESSER_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012D0363
    ),
    LOC_NOTE_MMM_BEDROOM_DRESSER_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012D02C3
    ),
    LOC_NOTE_MMM_BEDROOM_DRESSER_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012D02E4
    ),
    LOC_NOTE_MMM_WINE_RACK_BASEMENT_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011D04AF
    ),
    LOC_NOTE_MMM_WINE_RACK_BASEMENT_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011D05A9
    ),
    LOC_NOTE_MMM_WINE_RACK_BASEMENT_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011D06A4
    ),
    LOC_NOTE_MMM_WINE_RACK_BASEMENT_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011D079E
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF04A
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BEAC4
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BEC52
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BEDE3
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_5: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BEC51
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_6: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BEABD
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_7: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BE92A
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_8: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BE797
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_9: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BEF73
    ),
    LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_10: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF0E0
    ),
    LOC_NOTE_MMM_ATOP_CLOCK_TOWER_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF433
    ),
    LOC_NOTE_MMM_ATOP_CLOCK_TOWER_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF6EC
    ),
    LOC_NOTE_MMM_ATOP_CLOCK_TOWER_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF9A1
    ),
    LOC_NOTE_MMM_ATOP_CLOCK_TOWER_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF6EB
    ),
    LOC_NOTE_MMM_ON_TUMBLARS_SHACK_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF897
    ),
    LOC_NOTE_MMM_ON_TUMBLARS_SHACK_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BF98F
    ),
    LOC_NOTE_MMM_ON_TUMBLARS_SHACK_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BFA8B
    ),
    LOC_NOTE_MMM_ON_TUMBLARS_SHACK_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011BFB85
    ),
    LOC_NOTE_MMM_CHURCH_PEW_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011C124C
    ),
    LOC_NOTE_MMM_CHURCH_PEW_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011C0C3B
    ),
    LOC_NOTE_MMM_CHURCH_PEW_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011CFF8D
    ),
    LOC_NOTE_MMM_CHURCH_PEW_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011C05A0
    ),
    LOC_NOTE_MMM_CHURCH_ORGAN_PEDALS_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011CFA77
    ),
    LOC_NOTE_MMM_CHURCH_ORGAN_PEDALS_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011CF9B3
    ),
    LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011C0131
    ),
    LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011C0045
    ),
    LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011CFC2D
    ),
    LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011CF8ED
    ),
    LOC_NOTE_MMM_LEDGES_AROUND_WELL_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0DDE
    ),
    LOC_NOTE_MMM_LEDGES_AROUND_WELL_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0D49
    ),
    LOC_NOTE_MMM_LEDGES_AROUND_WELL_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B01C3
    ),
    LOC_NOTE_MMM_LEDGES_AROUND_WELL_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x011B0258
    ),
    LOC_NOTE_MMM_INSIDE_WELL_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0125035F
    ),
    LOC_NOTE_MMM_INSIDE_WELL_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0125FF36
    ),
    LOC_NOTE_MMM_INSIDE_WELL_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0125FDE1
    ),
    LOC_NOTE_MMM_INSIDE_WELL_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0125FFAA
    ),
    LOC_NOTE_MMM_INSIDE_WELL_5: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0125FBBC
    ),
    LOC_NOTE_MMM_INSIDE_WELL_6: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0125FF86
    ),
    LOC_NOTE_MMM_INSIDE_WELL_7: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012501FC
    ),
    LOC_NOTE_MMM_INSIDE_MUMBOS_SKULL_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x01300089
    ),
    LOC_NOTE_MMM_INSIDE_MUMBOS_SKULL_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0130FE3E
    ),
    LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0124056C
    ),
    LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0124FFE7
    ),
    LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0124FA6E
    ),
    LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0124FFF4
    ),
    LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_1: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012FFF8E
    ),
    LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_2: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012FFE5C
    ),
    LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_3: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012FFECA
    ),
    LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_4: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012F0074
    ),
    LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_5: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x012F01A4
    ),
    LOC_NOTE_RBB_GANGPLANK_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310AE7
    ),
    LOC_NOTE_RBB_GANGPLANK_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013109FD
    ),
    LOC_NOTE_RBB_GANGPLANK_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310917
    ),
    LOC_NOTE_RBB_GANGPLANK_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131082D
    ),
    LOC_NOTE_RBB_GANGPLANK_5: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310745
    ),
    LOC_NOTE_RBB_RAMP_AFT_DECK_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131FFF9
    ),
    LOC_NOTE_RBB_RAMP_AFT_DECK_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131FF24
    ),
    LOC_NOTE_RBB_RAMP_AFT_DECK_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131FE50
    ),
    LOC_NOTE_RBB_RAMP_AFT_DECK_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131FD7C
    ),
    LOC_NOTE_RBB_AFT_DECK_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01312085
    ),
    LOC_NOTE_RBB_AFT_DECK_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131203B
    ),
    LOC_NOTE_RBB_AFT_DECK_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01311DE2
    ),
    LOC_NOTE_RBB_AFT_DECK_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01311B8A
    ),
    LOC_NOTE_RBB_AFT_DECK_5: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01311869
    ),
    LOC_NOTE_RBB_AFT_DECK_6: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131162B
    ),
    LOC_NOTE_RBB_FAN_SWITCH_ROOM_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134EDAA
    ),
    LOC_NOTE_RBB_FAN_SWITCH_ROOM_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134EEF4
    ),
    LOC_NOTE_RBB_FAN_SWITCH_ROOM_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134EDA9
    ),
    LOC_NOTE_RBB_FAN_SWITCH_ROOM_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134EC59
    ),
    LOC_NOTE_RBB_KITCHEN_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013CFB86
    ),
    LOC_NOTE_RBB_KITCHEN_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013CFFA4
    ),
    LOC_NOTE_RBB_KITCHEN_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013C050C
    ),
    LOC_NOTE_RBB_KITCHEN_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013C01F5
    ),
    LOC_NOTE_RBB_KITCHEN_5: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013CFFAA
    ),
    LOC_NOTE_RBB_STOREROOM_SHELF_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013B0384
    ),
    LOC_NOTE_RBB_STOREROOM_SHELF_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013B0401
    ),
    LOC_NOTE_RBB_STOREROOM_SHELF_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013B047E
    ),
    LOC_NOTE_RBB_STOREROOM_SHELF_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013B04FA
    ),
    LOC_NOTE_RBB_STOREROOM_SHELF_5: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013B0578
    ),
    LOC_NOTE_RBB_NEXT_TO_WHISTLES_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131F831
    ),
    LOC_NOTE_RBB_NEXT_TO_WHISTLES_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131F381
    ),
    LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013100FA
    ),
    LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310226
    ),
    LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310352
    ),
    LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131047E
    ),
    LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131086D
    ),
    LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310741
    ),
    LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310615
    ),
    LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013104E9
    ),
    LOC_NOTE_RBB_BUNK_ROOM_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0139FF1E
    ),
    LOC_NOTE_RBB_BUNK_ROOM_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0139FD01
    ),
    LOC_NOTE_RBB_BUNK_ROOM_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0139013E
    ),
    LOC_NOTE_RBB_BUNK_ROOM_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01390326
    ),
    LOC_NOTE_RBB_NAVIGATION_ROOM_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013DFE48
    ),
    LOC_NOTE_RBB_NAVIGATION_ROOM_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013DFD90
    ),
    LOC_NOTE_RBB_NAVIGATION_ROOM_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013DFCD9
    ),
    LOC_NOTE_RBB_NAVIGATION_ROOM_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013DFC23
    ),
    LOC_NOTE_RBB_CAPTAINS_BEDROOM_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013FFAC9
    ),
    LOC_NOTE_RBB_CAPTAINS_BEDROOM_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013FFB9D
    ),
    LOC_NOTE_RBB_CAPTAINS_BEDROOM_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013FFC70
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134083E
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01340906
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01340775
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013406AE
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_LEFT_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134FAF5
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_LEFT_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134FA2D
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_LEFT_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134FBBD
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_LEFT_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134FC87
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_CENTER_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134FB59
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_CENTER_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134F9C9
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_CENTER_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134F839
    ),
    LOC_NOTE_RBB_ENGINE_ROOM_CENTER_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0134F9CA
    ),
    LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01312279
    ),
    LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01312661
    ),
    LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01312D69
    ),
    LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01312981
    ),
    LOC_NOTE_RBB_TNT_CRANE_CATWALK_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310578
    ),
    LOC_NOTE_RBB_TNT_CRANE_CATWALK_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131044C
    ),
    LOC_NOTE_RBB_TNT_CRANE_CATWALK_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01310320
    ),
    LOC_NOTE_RBB_FLOODED_WAREHOUSE_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01350AE7
    ),
    LOC_NOTE_RBB_FLOODED_WAREHOUSE_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01350BC2
    ),
    LOC_NOTE_RBB_FLOODED_WAREHOUSE_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01350A8C
    ),
    LOC_NOTE_RBB_FLOODED_WAREHOUSE_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013509B0
    ),
    LOC_NOTE_RBB_AROUND_SNACKERS_POOL_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131ED6A
    ),
    LOC_NOTE_RBB_AROUND_SNACKERS_POOL_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131EAE3
    ),
    LOC_NOTE_RBB_AROUND_SNACKERS_POOL_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131E88F
    ),
    LOC_NOTE_RBB_AROUND_SNACKERS_POOL_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131E71A
    ),
    LOC_NOTE_RBB_AROUND_SNACKERS_POOL_5: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131E5A5
    ),
    LOC_NOTE_RBB_TOXIC_WASTE_BARREL_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131D47D
    ),
    LOC_NOTE_RBB_TOXIC_WASTE_BARREL_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131D4EC
    ),
    LOC_NOTE_RBB_TOXIC_WASTE_BARREL_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131D0FE
    ),
    LOC_NOTE_RBB_TOXIC_WASTE_CRANE_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131DF95
    ),
    LOC_NOTE_RBB_TOXIC_WASTE_CRANE_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131E0C0
    ),
    LOC_NOTE_RBB_TOXIC_WASTE_CRANE_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0131E1EC
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01370251
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0137FCBE
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0137FC96
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013700B9
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_5: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01370154
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_6: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0137FEF7
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_7: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0137FD21
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_1_8: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013701D6
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_3_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013804A6
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_3_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01380537
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_3_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x013805B8
    ),
    LOC_NOTE_RBB_WAREHOUSE_CRATE_3_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x01380527
    ),
    LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_1: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x018B115F
    ),
    LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_2: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x018B1548
    ),
    LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_3: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x018B1160
    ),
    LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_4: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x018B0D78
    ),
    LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014009A1
    ),
    LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01400C41
    ),
    LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01400EED
    ),
    LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01401005
    ),
    LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0143EED9
    ),
    LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0143EB4E
    ),
    LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0143E766
    ),
    LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0143EAE6
    ),
    LOC_NOTE_CCW_SPRING_BRIDGE_GOBIS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014304FB
    ),
    LOC_NOTE_CCW_SPRING_BRIDGE_GOBIS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014304FC
    ),
    LOC_NOTE_CCW_SPRING_BRIDGE_GOBIS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014304FD
    ),
    LOC_NOTE_CCW_SPRING_BRIDGE_FLOODED_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014319F4
    ),
    LOC_NOTE_CCW_SPRING_BRIDGE_FLOODED_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01431B72
    ),
    LOC_NOTE_CCW_SPRING_BRIDGE_FLOODED_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01431CE2
    ),
    LOC_NOTE_CCW_SPRING_HIGH_WALL_MUMBOS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01430384
    ),
    LOC_NOTE_CCW_SPRING_HIGH_WALL_MUMBOS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01430385
    ),
    LOC_NOTE_CCW_SPRING_HIGH_WALL_MUMBOS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01430399
    ),
    LOC_NOTE_CCW_SPRING_LOW_WALL_MUMBOS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0143E9EE
    ),
    LOC_NOTE_CCW_SPRING_LOW_WALL_MUMBOS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0143E897
    ),
    LOC_NOTE_CCW_SPRING_LOW_WALL_MUMBOS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0143E732
    ),
    LOC_NOTE_CCW_SUMMER_LEAVES_ENTRYWAY_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01440CAC
    ),
    LOC_NOTE_CCW_SUMMER_LEAVES_ENTRYWAY_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01440EC3
    ),
    LOC_NOTE_CCW_SUMMER_GNAWTYS_ENTRYWAY_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01440641
    ),
    LOC_NOTE_CCW_SUMMER_GNAWTYS_ENTRYWAY_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01440457
    ),
    LOC_NOTE_CCW_SUMMER_BRIDGE_ZUBBAS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01440226
    ),
    LOC_NOTE_CCW_SUMMER_BRIDGE_ZUBBAS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01440168
    ),
    LOC_NOTE_CCW_SUMMER_BRIDGE_ZUBBAS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014400C8
    ),
    LOC_NOTE_CCW_SUMMER_TREEHOUSE_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01442328
    ),
    LOC_NOTE_CCW_SUMMER_TREEHOUSE_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0144229B
    ),
    LOC_NOTE_CCW_SUMMER_TREEHOUSE_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01442189
    ),
    LOC_NOTE_CCW_SUMMER_TREEHOUSE_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01442102
    ),
    LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01442403
    ),
    LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014422A5
    ),
    LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014422A6
    ),
    LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014425C5
    ),
    LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_5: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0144281D
    ),
    LOC_NOTE_CCW_AUTUMN_SNAREBEAR_MUMBOS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014505A1
    ),
    LOC_NOTE_CCW_AUTUMN_SNAREBEAR_MUMBOS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014505F1
    ),
    LOC_NOTE_CCW_AUTUMN_SNAREBEAR_MUMBOS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450641
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014509CE
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450E42
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01451156
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014512C0
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_5: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01451157
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_6: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450E43
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_7: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014509C4
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_8: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450384
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_9: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FD45
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_10: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145F95C
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_11: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145F5B0
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_12: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145F46D
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_13: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145F669
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_14: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145F8C6
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_15: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FD3F
    ),
    LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_16: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450546
    ),
    LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014CFEAD
    ),
    LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014C0178
    ),
    LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014C0465
    ),
    LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014C019D
    ),
    LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145E81E
    ),
    LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145E61A
    ),
    LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145E468
    ),
    LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145E2D1
    ),
    LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_5: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145EA3D
    ),
    LOC_NOTE_CCW_AUTUMN_SNAREBEAR_GOBIS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FE2A
    ),
    LOC_NOTE_CCW_AUTUMN_SNAREBEAR_GOBIS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FDDA
    ),
    LOC_NOTE_CCW_AUTUMN_SNAREBEAR_GOBIS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FD8A
    ),
    LOC_NOTE_CCW_AUTUMN_GNAWTYS_SHELF_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014508E3
    ),
    LOC_NOTE_CCW_AUTUMN_GNAWTYS_SHELF_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145093A
    ),
    LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x015C0001
    ),
    LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x015CF9DA
    ),
    LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x015C00FA
    ),
    LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x015C063E
    ),
    LOC_NOTE_CCW_AUTUMN_NABNUTS_SHELF_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01600289
    ),
    LOC_NOTE_CCW_AUTUMN_NABNUTS_SHELF_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x016001F3
    ),
    LOC_NOTE_CCW_AUTUMN_NABNUTS_SHELF_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01600158
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450292
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FF0E
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FC86
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FC8C
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_5: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145FEFD
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_6: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450282
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_7: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0145050A
    ),
    LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_8: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01450503
    ),
    LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0146F7E6
    ),
    LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0146F3E7
    ),
    LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0146FDCD
    ),
    LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0146FB4B
    ),
    LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01462579
    ),
    LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0146278E
    ),
    LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x014629A4
    ),
    LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01462BBD
    ),
    LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0146187F
    ),
    LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0146187C
    ),
    LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01461C02
    ),
    LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01461C01
    ),
    LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_1: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01460425
    ),
    LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_2: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01460409
    ),
    LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_3: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01460528
    ),
    LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_4: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x01460890
    ),
    LOC_DEFEAT_GRUNTILDA: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR_FIGHT,
        locked_item=ITEM_VICTORY
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}