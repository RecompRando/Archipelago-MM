from dataclasses import dataclass

from typing import Dict

from Options import Choice, Option, DefaultOnToggle, Toggle, Range, NamedRange, OptionList, StartInventoryPool, DeathLink, OptionGroup, PerGameCommonOptions


class LogicDifficulty(Choice):
    """Set the logic difficulty used when generating."""
    display_name = "Logic Difficulty"
    # ~ option_easy = 0
    option_normal = 1
    #option_obscure_glitchless = 2
    #option_glitched = 3
    option_no_logic = 4
    # ~ alias_baby = option_easy
    default = 1


class MajoraRemainsRequired(Range):
    """Set the amount of boss remains required to fight Majora."""
    display_name = "Majora Boss Remains Required"
    range_start = 0
    range_end = 4
    default = 4


class MoonRemainsRequired(Range):
    """Set the amount of boss remains required to reach the Moon after playing Oath to Order."""
    display_name = "Moon Boss Remains Required"
    range_start = 0
    range_end = 4
    default = 4


class CAMC(DefaultOnToggle):
    """Set whether chest appearance matches contents."""
    display_name = "CAMC"


class Swordless(Toggle):
    """Start the game without a sword, and shuffle an extra Progressive Sword into the pool."""
    display_name = "Swordless"


class Shieldless(Toggle):
    """Start the game without a shield, and shuffle an extra Progressive Shield into the pool."""
    display_name = "Shieldless"


class StartWithSoaring(DefaultOnToggle):
    """Start the game with Song of Soaring."""
    display_name = "Start With Soaring"


class StartingHeartQuarters(Range):
    """The number of heart quarters Link starts with.
    If less than 12, extra heart items will be shuffled into the pool to accommodate."""
    display_name = "Starting Hearts"
    range_start = 4
    range_end = 12
    default = 12


class StartingHeartsAreContainersOrPieces(Choice):
    """Choose whether Link's starting hearts are shuffled into the pool as Heart Containers (plus the remainder as Heart Pieces) or as all Heart Pieces."""
    display_name = "Starting Hearts are Containers or Pieces"
    option_containers = 0
    option_pieces = 1
    default = 0


class ShuffleRegionalMaps(Choice):
    """Choose whether to shuffle every regional map from Tingle."""
    display_name = "Shuffle Regional Maps"
    option_vanilla = 0
    option_starting = 1
    option_anywhere = 2
    default = 1


class ShuffleBossRemains(Choice):
    """Choose whether to shuffle the Boss Remains received after beating a boss at the end of a dungeon.
    
    vanilla: Boss Remains are placed in their vanilla locations.
    anything: Any item can be given by any of the Boss Remains, and Boss Remains can be found anywhere in any world.
    bosses: Boss Remains are shuffled amongst themselves as the rewards for defeating bosses."""
    display_name = "Shuffle Boss Remains"
    option_vanilla = 0
    option_anywhere = 1
    option_bosses = 2
    default = 0


class BossWarpsWithRemains(DefaultOnToggle):
    """Choose whether to retain the vanilla ability to warp the boss of dungeons by having their vanilla remains.
    Getting the remains check for a dungeon will open its warp regardless."""
    display_name = "Warp to Bosses Using Remains"


class ShuffleSpiderHouseReward(Choice):
    """Choose how Swamp Spider House and Ocean Spider House rewards are shuffled.
    
    disabled: Spider House rewards won't be shuffled into the pool.
    vanilla: Spider House rewards will be vanilla. Mask of Truth will be in Swamp and a wallet upgrade in Ocean.
    enabled: Spider House rewards will be shuffled. Any item can be shuffled at their locations."""
    display_name = "Shuffle Spider House Rewards"
    option_disabled = 0
    option_vanilla = 1
    option_enabled = 2


class RequiredSkullTokens(Range):
    """The number of Gold Skulltula Tokens needed to get the reward from their respective Spider House.
    All 30 Tokens from each Spider House are still shuffled into the item pool regardless of the selection.
    Valid amounts are within the range 0-30."""
    display_name = "Required Skulltula Tokens"
    range_start = 0
    range_end = 30
    default = 30


class Skullsanity(Choice):
    """Choose what items gold skulltulas can give.
    
    vanilla: Keep the Spider Houses in generation, but only place Skulltula tokens there.
    anything: Any item can be given by any Skulltula, and tokens can be found anywhere in any world.
    ignore: Remove the Spider Houses from generation entirely, lowering the hint percentage and removing them from the spoiler log."""
    display_name = "Skullsanity"
    option_vanilla = 0
    option_anything = 1
    option_ignore = 2
    default = 0


class Shopsanity(Choice):
    """Choose whether shops and their items are shuffled into the pool.
    This includes Trading Post, Bomb Shop, Goron Shop, and Zora Shop, along with the Gorman Ranch and Milk Bar purchases.
    
    vanilla: Shop items are not shuffled.
    enabled: Every item in shops are shuffled, with alternate shops sharing the same items.
    advanced: Every single item in shops are shuffled, including the alternate Night Trading Post and Spring Goron Shop."""
    display_name = "Shopsanity"
    option_vanilla = 0
    option_enabled = 1
    option_advanced = 2
    default = 0

class Scrubsanity(Toggle):
    """Choose whether to shuffle Business Scrub purchases."""
    display_name = "Shuffle Business Scrub Purchases"

class ShopPrices(Choice):
    """
    Choose whether prices for shop items are vanilla or random.
    This only apply to the main shops of the game. This has no effect if shopsanity is disabled.
    
    vanilla: Shop items have their normal prices.
    randomized: Shop items have their prices randomized. The maximum price can be configured in max_shop_prices.
    """
    display_name = "Shop Prices"
    option_vanilla = 0
    option_randomized = 1
    default = 0

class MaxShopPrices(NamedRange):
    """
    Choose the maximum price shop items can be. This only has an effect if shop_prices is set to random.
    """
    display_name = "Maximum Shop Prices"
    range_start = 0
    range_end = 500
    default = 300
    special_range_names = {
        "balanced": 300,
        "free": 0,
        "child": 99,
        "adult": 200,
        "giant": 500,
    }


class Cowsanity(Toggle):
    """Choose whether to shuffle Cows."""
    display_name = "Shuffle Cows"


class ShuffleGreatFairyRewards(Choice):
    """Choose how Great Fairy rewards are shuffled.
    
    disabled: Great Fairy rewards won't be shuffled into the pool.
    vanilla: Great Fairy rewards will be vanilla. For example, Magic will be behind Clock Town and Snowhead rewards.
    enabled: Great Fairy rewards will be shuffled. Any item can be shuffled at their locations."""
    display_name = "Shuffle Great Fairy Rewards"
    option_disabled = 0
    option_vanilla = 1
    option_enabled = 2
    default = 0


class RequiredStrayFairies(Range):
    """The number of Stray Fairies needed to get the reward from their respective Great Fairy (excluding North Clock Town's Great Fairy of Magic).
    All 15 Stray Fairies from each dungeon are still shuffled into the item pool regardless of the selection.
    Valid amounts are within the range 0-15."""
    display_name = "Required Stray Fairies"
    range_start = 0
    range_end = 15
    default = 15

class DungeonItems(Choice):
    """Base class for shuffle options for dungeon items (keys, maps, compasses)."""
    value: int
    option_vanilla = 1
    #option_dungeon = 2
    #option_any_dungeon = 3
    option_local = 4
    option_keysanity = 5
    default = 4

    @property
    def in_dungeon(self) -> bool:
        """
        Return whether the item should be shuffled into a dungeon.

        :return: Whether the item is shuffled into a dungeon.
        """
        return self.value in (2, 3)


class ShuffleStrayFairies(DungeonItems):
    """
    Choose how stray fairies will be shuffled in the pool.

    Vanilla: Stray fairies will be places where they can be found in vanilla.
    Local: Stray fairies will be placed anywhere in your own world.
    Fairysanity: Stray fairies will be placed in any world.
    """
    item_name_group = "Stray Fairies"
    display_name = "Shuffle Stray Fairies"
    option_fairysanity = 5
    default = 4

class ShuffleMapsAndCompasses(DungeonItems):
    """
    Choose how dungeon maps and compasses will be shuffled in the pool.

    Start With: Start the seed with dungeon maps and compasses.
    Vanilla: Dungeon maps and compasses will be placed where they can be found in vanilla.
    Local: Dungeon maps and compasses will be placed anywhere in your own world.
    Keysanity: Dungeon maps and compasses will be placed in any world.
    """
    item_name_group = "Maps and Compasses"
    display_name = "Shuffle Maps and Compasses"
    option_start_with = 0
    default = 4

class ShuffleSmallKeys(DungeonItems):
    """
    Choose how small keys will be shuffled in the pool.

    Start With: Start the seed with small keys.
    Vanilla: Small keys will be placed where they can be found in vanilla.
    Local: Small keys will be placed anywhere in your own world.
    Keysanity: Small keys will be placed in any world.
    """
    item_name_group = "Small Keys"
    display_name = "Shuffle Small Keys"
    option_start_with = 0
    default = 4

class ShuffleBossKeys(DungeonItems):
    """
    Choose how boss keys will be shuffled in the pool.

    Start With: Start the seed with boss keys.
    Vanilla: Boss keys will be placed where they can be found in vanilla.
    Local: Boss keys will be placed anywhere in your own world.
    Keysanity: Boss keys will be placed in any world.
    """
    item_name_group = "Boss Keys"
    display_name = "Shuffle Boss Keys"
    option_start_with = 0
    default = 4


class CuriosityShopTrades(Toggle):
    """Choose whether to shuffle the rupees given for trading bottled items at the Curiosity Shop."""
    display_name = "Curiosity Shop Trades"


class IntroChecks(Toggle):
    """Choose whether to shuffle the checks normally found before entering the Clock Tower.
    
    A way backwards through these areas has been added through the stone door at the bottom of the Clock Tower Interior."""
    display_name = "Enable Intro Checks"

class ShuffleMinigames(Choice):
    """Choose whether the minigames are shuffled or not. The minigames affected are:
    - Town and Swamp Shooting Galleries;
    - Honey & Darling;
    - Deku Playground;
    - Great Bay Fisherman Game.
    
    disabled: Listed minigames are not shuffled.
    single: Listed minigames only have one location. Where applicable, the easier locations (any day/lowest points requirements) are shuffled.
    everything: Listed minigames are fully shuffled."""
    display_name = "Shuffle Minigames"
    option_disabled = 0
    option_single = 1
    option_everything = 2
    default = 1

class ShuffleTreasureChestGame(Choice):
    """Choose which chests in the Treasure Chest minigame are shuffled.
    
    disabled: Chests are not shuffled.
    goron_only: Only the reward as Goron is shuffled.
    everything: Rewards for human, Deku, Goron, and Zora are shuffled."""
    display_name = "Treasure Chest Minigame Shuffle"
    option_disabled = 0
    option_goron_only = 1
    option_everything = 2
    default = 1

class ShuffleBeaverRace(Range):
    """
    Choose how many beaver race rewards are shuffled.
    
    Valid amounts are within the range 0-2.
    """
    display_name = "Shuffle Beaver Race"
    range_start = 0
    range_end = 2
    default = 0

class ShuffleLottery(Toggle):
    """Choose whether to shuffle lottery reward or not."""
    display_name = "Shuffle Lottery"

class ShufflePictureRewards(Choice):
    """
    Choose whether the rewards for the Tourist Center picture contest and the Lulu fan are shuffled or not.

    disabled: Picture rewards will be disabled.
    winning_only: Only the winning picture for the Tourist Center reward will be shuffled.
    all_pictures: All picture rewards will be shuffled.
    """
    display_name = "Shuffle Picture Rewards"
    option_disabled = 0
    option_winning_only = 1
    option_all_pictures = 2
    default = 1


class StartWithConsumables(DefaultOnToggle):
    """Choose whether to start with basic consumables (99 rupees, 10 deku sticks, 20 deku nuts)."""
    display_name = "Start With Consumables"


class InfiniteMagicBehavior(Choice):
    """
    Choose how infinite magic is handled.

    vanilla: Vanilla behavior. Infinite magic will end after a cycle reset.
    consume: Drinking Chateau Romani will give permanent infinite magic and will persist through cycle resets.
    upgrade: Adds a third Progressive Magic in the pool that gives permanent infinite magic. Drinking Chateau Romani
    before getting the third upgrade will still give infinite magic, but will end after a cycle reset.
    """
    display_name = "Permanent Chateau Romani"
    option_vanilla = 0
    option_consume = 1
    option_upgrade = 2


class StartWithInvertedTime(Toggle):
    """Choose whether time starts out inverted at Day 1, even after a reset."""
    display_name = "Reset With Inverted Time"


class ReceiveFilledWallets(DefaultOnToggle):
    """Choose whether you receive wallets pre-filled (not including the starting wallet)."""
    display_name = "Receive Filled Wallets"


class MagicIsATrap(Toggle):
    """Set whether to preserve the vanilla bug where you are able to use certain magic items and abilities without magic.
    Once you receive magic, those items and abilities will begin to reduce magic normally.
    
    (No logical implications)"""
    display_name = "Magic Is a Trap"


class DamageMultiplier(Choice):
    """Adjust the amount of damage taken."""
    display_name = "Damage Multiplier"
    option_half = 0
    option_normal = 1
    option_double = 2
    option_quad = 3
    option_ohko = 4
    default = 1

class DeathBehavior(Choice):
    """Change what happens when you die.
    
    vanilla: The normal death cutscene plays when you die.
    fast: The death cutscene is massively sped up.
    moon_crash: Triggers a moon crash and restarts the current cycle."""
    display_name = "Death Behavior"
    option_vanilla = 0
    option_fast = 1
    option_instant = 2
    option_moon_crash = 3
    default = 0


class LinkTunicColor(OptionList):
    """Choose a color for Link's tunic."""
    display_name = "Link Tunic Color"
    default = [30, 105, 27]


#mm_option_groups = [
#    OptionGroup("Goal Requirements", [
#        MajoraRemainsRequired,
#        MoonRemainsRequired,
#    ]),
#    OptionGroup("Starting Item Shuffle", [
#        Swordless,
#        Shieldless,
#        StartingHeartQuarters,
#        StartingHeartsAreContainersOrPieces,
#    ]),
#    OptionGroup("Dungeon Options", [
#        ShuffleBossRemains,
#        BossWarpsWithRemains,
#        ShuffleMapsAndCompasses,
#        ShuffleSmallKeys,
#        ShuffleBossKeys,
#        ShuffleStrayFairies,
#        RequiredStrayFairies,
#        ShuffleGreatFairyRewards,
#    ]),
#    OptionGroup("Shuffles" [
#        ShuffleRegionalMaps,
#        ShuffleMinigames,
#        ShuffleTreasureChestGame,
#        ShuffleLottery,
#        ShufflePictureRewards,
#        ShuffleBeaverRace,
#        IntroChecks,
#    ]),
#    OptionGroup("Sanities", [
#        Skullsanity,
#        RequiredSkullTokens,
#        ShuffleSpiderHouseReward,
#        Shopsanity,
#        ShopPrices,
#        MaxShopPrices,
#        Scrubsanity,
#        CuriosityShopTrades,
#        Cowsanity,
#    ]),
#    OptionGroup("Quality of Life", [
#        StartWithSoaring,
#        StartWithInvertedTime,
#        StartWithConsumables,
#        ReceiveFilledWallets,
#        InfiniteMagicBehavior,
#        CAMC,
#    ]),
#    OptionGroup("Other", [
#        MagicIsATrap,
#        DamageMultiplier,
#        DeathBehavior,
#        LinkTunicColor,
#    ]),
#]


@dataclass
class MMROptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    logic_difficulty: LogicDifficulty
    majora_remains_required: MajoraRemainsRequired
    moon_remains_required: MoonRemainsRequired
    camc: CAMC
    swordless: Swordless
    shieldless: Shieldless
    start_with_soaring: StartWithSoaring
    starting_hearts: StartingHeartQuarters
    starting_hearts_are_containers_or_pieces: StartingHeartsAreContainersOrPieces
    shuffle_regional_maps: ShuffleRegionalMaps
    shuffle_boss_remains: ShuffleBossRemains
    remains_allow_boss_warps: BossWarpsWithRemains
    shuffle_spiderhouse_reward: ShuffleSpiderHouseReward
    required_skull_tokens: RequiredSkullTokens
    skullsanity: Skullsanity
    shopsanity: Shopsanity
    scrubsanity: Scrubsanity
    shop_prices: ShopPrices
    max_shop_prices: MaxShopPrices
    cowsanity: Cowsanity
    shuffle_great_fairy_rewards: ShuffleGreatFairyRewards
    required_stray_fairies: RequiredStrayFairies
    shuffle_stray_fairies: ShuffleStrayFairies
    shuffle_maps_and_compasses: ShuffleMapsAndCompasses
    shuffle_small_keys: ShuffleSmallKeys
    shuffle_boss_keys: ShuffleBossKeys
    curiosity_shop_trades: CuriosityShopTrades
    intro_checks: IntroChecks
    shuffle_minigames: ShuffleMinigames
    shuffle_treasure_chest_game: ShuffleTreasureChestGame
    shuffle_beaver_races: ShuffleBeaverRace
    shuffle_lottery: ShuffleLottery
    shuffle_picture_rewards: ShufflePictureRewards
    start_with_consumables: StartWithConsumables
    infinite_magic_behavior: InfiniteMagicBehavior
    start_with_inverted_time: StartWithInvertedTime
    receive_filled_wallets: ReceiveFilledWallets
    magic_is_a_trap: MagicIsATrap
    damage_multiplier: DamageMultiplier
    death_behavior: DeathBehavior
    death_link: DeathLink
    link_tunic_color: LinkTunicColor
