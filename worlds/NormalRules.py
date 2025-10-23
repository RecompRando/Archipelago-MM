from .Constants import *

def rgn_connection_string(rgn1, rgn2):
    return str(rgn1) + " -> " + str(rgn2)

def has_tokens_for_termite(state, player):
    return state.has(ITEM_MUMBO_TOKEN, player, 5)

def has_tokens_for_crocodile(state, player):
    return state.has(ITEM_MUMBO_TOKEN, player, 10)

def has_tokens_for_walrus(state, player):
    return state.has(ITEM_MUMBO_TOKEN, player, 15)

def has_tokens_for_pumpkin(state, player):
    return state.has(ITEM_MUMBO_TOKEN, player, 20)

def has_tokens_for_bee(state, player):
    return state.has(ITEM_MUMBO_TOKEN, player, 25)

def can_smash_mm_huts(state, player):
    return (
        state.has(ITEM_BEAK_BUSTER, player) and
        (
            state.has(ITEM_JUMP, player) or
            state.has(ITEM_FLAP_FLIP, player)    #required to get on top of the huts
        )
    )

def can_traverse_bgs(state, player):
    return (
        state.has(ITEM_JUMP, player) or
        state.has(ITEM_FEATHERY_FLAP, player) or  # required to access most of the level
        state.has(ITEM_FLAP_FLIP, player)
    )

def can_break_mmm_gates(state, player):
    return (
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        state.has(ITEM_BEAK_BARGE, player)
    )

def can_reach_eyrie(state, player):
    return (
        state.has(ITEM_TALON_TROT, player) and
        state.has(ITEM_JUMP, player) and
        state.has(ITEM_FEATHERY_FLAP, player) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    )

def get_region_rules(player, options):
    return {
        rgn_connection_string(RGN_SPIRAL_MOUNTAIN, RGN_GRUNTILDAS_LAIR_LOBBY):
            lambda state: True,
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_LOBBY, RGN_MUMBOS_MOUNTAIN):
            lambda state:
            (
                state.has(ITEM_JIGGY, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_LOBBY, RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 50) and 
                state.has(ITEM_TALON_TROT, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR, RGN_TREASURE_TROVE_COVE):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 15) and  # 1+2+5+7
                state.has(ITEM_TALON_TROT, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR, RGN_CLANKERS_CAVERN):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 15) and 
                state.has(ITEM_FLAP_FLIP, player) # 1+2+5+7
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 180) and
                state.has(ITEM_TALON_TROT, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR, RGN_BUBBLEGLOOP_SWAMP):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 23) and
                state.has(ITEM_TALON_TROT, player)  # 1+2+5+7+8
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 260) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR, RGN_FREEZEEZY_PEAK):
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_JIGGY, player, 32)  # 1+2+5+7+8+9
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR, RGN_GOBIS_VALLEY):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 32) and  # 1+2+5+7+8+9
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 350)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR, RGN_MAD_MONSTER_MANSION):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 54)  # 1+2+5+7+8+9+10+12
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 450)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR, RGN_MAD_MONSTER_MANSION):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 54)  # 1+2+5+7+8+9+10+12
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR, RGN_RUSTY_BUCKET_BAY):
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JIGGY, player, 54)  # 1+2+5+7+8+9+10+12
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_NOTE, player, 640)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR, RGN_CLICK_CLOCK_WOOD):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 69) and  # 1+2+5+7+8+9+10+12+15
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_765_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 765) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_765_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_FURNACE_FUN):
            lambda state: True,
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_FURNACE_FUN, RGN_GRUNTILDAS_LAIR_810_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 810) and
                state.has(ITEM_JIGGY, player, 94)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_810_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_882_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 882)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_882_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_FIGHT):
            lambda state: True,
    }

def get_location_rules(player, options):
    return {
        # Blubbers Gold
        LOC_BLUBBER_GOLD_TTC_POOP_DECK:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_BLUBBER_GOLD_TTC_HOLD_UNDERWATER:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        # Presents
        LOC_RED_PRESENT_FP_TREE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_FLAP_FLIP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_GREEN_PRESENT_FP_NEAR_RAMP:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_BLUE_PRESENT_FP_GIANT_SNOWMAN_NOSE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player) or
                (
                    state.has(ITEM_FLIGHT, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        # Worms
        LOC_WORM_SUMMER_CCW_ENTRY_PATH:
            lambda state: True,
        LOC_WORM_SUMMER_CCW_SNAPPER_NEAR_BULL:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_WORM_SUMMER_CCW_LEDGE_NEAR_MUMBO:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_WORM_SUMMER_CCW_OUTSIDE_MUMBO:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_SUMMER_CCW_IN_DRIED_LAKE:
            lambda state: True,
        LOC_WORM_SUMMER_CCW_LEDGE_ABOVE_BRAMBLES:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_SUMMER_CCW_NEAR_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_SUMMER_CCW_NEAR_NABNUTS_HOME:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        # NOTE! The worms for Autumn will not spawn without feeding Eyrie in Summer (5 worms needed). ALSO! if you suck and die the worms respawn but Eyrie state is saved so you can get more worms than normally possible.
        LOC_WORM_AUTUMN_CCW_ENTRY_LEAF_PILE:
            lambda state:
            lambda state:
            (
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_RAMP_NEAR_LAKE:
            lambda state:
            (
                can_reach_eyrie(state, player) and 
                state.has(ITEM_WORM, player, 5)  # Requires 5 worms fed to Eyrie
            ),
        LOC_WORM_AUTUMN_CCW_NEAR_STILT_BOOTS:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_INSIDE_MUMBO_HUT:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_WORM_AUTUMN_CCW_LEAF_PILE_NEAR_BRAMBLES:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_LEAF_PILE_NEAR_FLOWER:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_LEDGE_ABOVE_BRAMBLES:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_ATOP_BEEHIVE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_INSIDE_BEEHIVE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_WORM_AUTUMN_CCW_BELOW_CABIN:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_AUTUMN_CCW_INSIDE_NABNUTS_HOUSE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_AUTUMN_CCW_BEHIND_EYRIE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_AUTUMN_CCW_TREETOP_PAST_NEST:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_WORM, player, 5) and  # Requires 5 worms fed to Eyrie
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        # Acorns
        LOC_ACORN_AUTUMN_CCW_BEHIND_UPPER_WINDOW:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_RAT_A_TAT_RAP, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_ACORN_AUTUMN_CCW_EDGE_OF_CIRCULAR_GAP_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_MIDDLE_OF_CIRCULAR_GAP_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_LEDGE_BELOW_CIRCULAR_GAP_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_LOWER_SLOPED_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_INSIDE_NABNUTS_HOUSE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_TRANSFORMATION_TERMITE:
            lambda state:
            (
                has_tokens_for_termite(state, player)
            ),
        LOC_TRANSFORMATION_CROCODILE:
            lambda state:
            (
                has_tokens_for_crocodile(state, player) and
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_TRANSFORMATION_WALRUS:
            lambda state:
            (
                has_tokens_for_walrus(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_TRANSFORMATION_PUMPKIN:
            lambda state:
            (
                has_tokens_for_pumpkin(state, player) and
                can_break_mmm_gates(state, player)
            ),
        LOC_TRANSFORMATION_BEE:
            lambda state:
            (
                has_tokens_for_bee(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_1:
            lambda state: True,
        LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_2:
            lambda state: True,
        LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_3:
            lambda state: True,
        LOC_MOLEHILL_SM_ROCKS:
            lambda state: True,
        LOC_MOLEHILL_SM_NEAR_MOUNTAIN_BRIDGE:
            lambda state: True,
        LOC_MOLEHILL_SM_NEAR_RIVER:
            lambda state: True,
        LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_1:
            lambda state: True,
        LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_2:
            lambda state: True,
        LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_3:
            lambda state: True,
        LOC_EMPTY_HONEYCOMB_SM_LOG:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player)
                    )
                )
            ),
        LOC_EMPTY_HONEYCOMB_SM_WATERFALL:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_SM_TREE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_SM_UNDERWATER:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_EMPTY_HONEYCOMB_SM_ROCKS:
            lambda state:
            (
                state.has(ITEM_BEAK_BARGE, player)
            ),
        LOC_EMPTY_HONEYCOMB_SM_COLLIWOBBLE:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_JIGGY_GL_ENTRYWAY:
            lambda state: True,
        LOC_JIGGY_GL_ATOP_MUMBOS_MOUNTAIN:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_JIGGY_GL_TTC_CANNON:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_JIGGY_GL_EYE_SWITCHES:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_GL_ABOVE_FP:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_GL_SARCOPHAGUS:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) or
                (
                    state.has(ITEM_FLAP_FLIP, player) and   #Requires somewhat specific timing
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JIGGY_GL_GRUNTYS_EYE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_FEATHERY_FLAP, player)
                    ) or
                    (
                        state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                        state.has(ITEM_BEAK_BUSTER, player) and
                        state.has(ITEM_TURBO_TALON_TROT, player) and
                        state.has(ITEM_FLIGHT, player)
                    )
                ) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player) or
                    state.has(ITEM_WONDERWING, player) or
                    (
                        state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                        state.has(ITEM_BEAK_BUSTER, player) and
                        state.has(ITEM_TURBO_TALON_TROT, player) and
                        state.has(ITEM_FLIGHT, player) and
                        state.has(ITEM_BEAK_BOMB, player)
                    )
                )
            ),
        LOC_JIGGY_GL_WATER_SWITCH:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_GL_BEE_TREE:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_BEE, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or  # required to access Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_MUMBO_TOKEN_GL_RED_CAULDRON:
            lambda state: True,
        LOC_MUMBO_TOKEN_GL_DRAIN_PIPE:
            lambda state: True,
        LOC_MUMBO_TOKEN_GL_CCW_PODIUM:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_GL_ABOVE_CC_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_MUMBO_TOKEN_GL_BEHIND_SARCOPHAGUS:
            lambda state: True,
        LOC_MUMBO_TOKEN_GL_ABOVE_FP_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_GL_BEHIND_MUMBO:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player)  #TODO: figure out semantics regarding levels
            ),
        LOC_MUMBO_TOKEN_GL_BELOW_RBB_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_GL_BY_MMM_PODIUM:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_GL_NEAR_CCW_PODIUM_SWITCH:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MOLEHILL_MM_AFTER_CHIMPYS_STUMP:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MOLEHILL_MM_STONEHENGE:
            lambda state: True,
        LOC_MOLEHILL_MM_HUTS:
            lambda state: True,
        LOC_JIGGY_MM_CONGA_ORANGE_THROW:
            lambda state: True,
        LOC_JIGGY_MM_CHIMPY_ORANGE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_JUMP, player) and    #can reach orange with good timing
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JIGGY_MM_CONGA_ATTACK:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MM_STONEHENGE:
            lambda state: True, #you can just mash shorthop, it's not hard:P
        LOC_JIGGY_MM_HILLSIDE:
            lambda state: True,
        LOC_JIGGY_MM_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_JIGGY_MM_TOTEM_POLE:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get on the platform
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_JIGGY_MM_HUT:
            lambda state:
            (
                can_smash_mm_huts(state, player)
            ),
        LOC_JIGGY_MM_MOUNTAINTOP:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_JIGGY_MM_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_MM_BLUE, player) and
                state.has(ITEM_JINJO_MM_GREEN, player) and
                state.has(ITEM_JINJO_MM_ORANGE, player) and
                state.has(ITEM_JINJO_MM_PURPLE, player) and
                state.has(ITEM_JINJO_MM_YELLOW, player)
            ),
        LOC_JINJO_MM_BLUE:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_JINJO_MM_GREEN:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JINJO_MM_ORANGE:
            lambda state: True,
        LOC_JINJO_MM_PURPLE:
            lambda state:
            (
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JINJO_MM_YELLOW:
            lambda state: True,
        LOC_EMPTY_HONEYCOMB_MM_HILLSIDE:
            lambda state: True,
        LOC_EMPTY_HONEYCOMB_MM_TOTEM:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_BEAK_BUSTER, player) and
                        (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or # required to get on the platform
                            state.has(ITEM_FEATHERY_FLAP, player)
                        )
                    )
                 )
            ),
        LOC_MUMBO_TOKEN_MM_BEHIND_PINK_JINJO:
            lambda state: True,
        LOC_MUMBO_TOKEN_MM_CHIMPY:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_MM_STONEHENGE:
            lambda state: True,
        LOC_MUMBO_TOKEN_MM_MUMBOS_HUT:
            lambda state: True,
        LOC_MUMBO_TOKEN_MM_TERMITE_MOUND:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player) or
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MOLEHILL_TTC_MAST:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MOLEHILL_TTC_NEAR_SANDCASTLE:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_TTC_NIPPER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) #can actually hurt him with Wonderwing as well
                )
                and
                (
                    state.has(ITEM_JUMP, player) or    #required to get the Jiggy
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_JIGGY_TTC_BLUBBER:
            lambda state: True,
            # ~ (
                # ~ state.has(ITEM_BLUBBER_GOLD, player, 2)
            # ~ ),
        LOC_JIGGY_TTC_SANDCASTLE:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_JUMP, player) or    #required to get the Jiggy
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_JIGGY_TTC_SHOCK_SPRING:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_TTC_X_MARK:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach all Xs
                    (
                        state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        )
                    )
                )
            ),
        LOC_JIGGY_TTC_POOL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_TTC_CLIFFSIDE:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to get the Jiggy, some of which require falling
                state.has(ITEM_BEAK_BUSTER, player) or      #onto the platform
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_JIGGY_TTC_LOCKUP:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_TTC_LIGHTHOUSE:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_TTC_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_TTC_BLUE, player) and
                state.has(ITEM_JINJO_TTC_GREEN, player) and
                state.has(ITEM_JINJO_TTC_ORANGE, player) and
                state.has(ITEM_JINJO_TTC_PURPLE, player) and
                state.has(ITEM_JINJO_TTC_YELLOW, player)
            ),
        LOC_JINJO_TTC_BLUE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JINJO_TTC_GREEN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_JINJO_TTC_ORANGE:
            lambda state: True,
        LOC_JINJO_TTC_PURPLE:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_JUMP, player) or
                (
                    state.has(ITEM_FLIGHT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP,player) and
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_FEATHERY_FLAP, player)
                    )
                )

            ),
        LOC_JINJO_TTC_YELLOW:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_TTC_UNDERWATER:
            lambda state:
            (
             state.has(ITEM_SWIM, player)
            ),
        LOC_EMPTY_HONEYCOMB_TTC_CRATE:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_NIPPER:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_MAST:
            lambda state:
            (
             state.has(ITEM_CLIMB, player) or
             state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_TTC_HOLD:
            lambda state:
            (
             state.has(ITEM_BEAK_BUSTER, player) and
             state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_TTC_SHOCK_SPRING:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_TTC_X_MARK:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_LOCKUP_LEFT:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_LOCKUP_RIGHT:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_POOL:
            lambda state:
            (
             state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_TTC_CRATE:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_LIGHTHOUSE:
            lambda state:
            (
             state.has(ITEM_FLIGHT, player)
            ),
        LOC_MOLEHILL_CC_NEAR_SPINNING_BLADES:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_JIGGY_CC_CLANKER_RAISE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)    #required to access most of the level
            ),
        LOC_JIGGY_CC_CLANKER_TAIL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open the gate and/or get the Jiggy
                    (
                        state.has(ITEM_EGGS, player) and
                        (
                            state.has(ITEM_FLAP_FLIP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        )
                    )
                )
            ),
        LOC_JIGGY_CC_CLANKER_BOLT:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                (
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get the Jiggy
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_JIGGY_CC_CLANKER_GOLD_TEETH:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_CC_CLANKER_BLOWHOLE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)    #required to access most of the level
            ),
        LOC_JIGGY_CC_WONDERWING:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_JIGGY_CC_STOMACH_RINGS:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                state.has(ITEM_FLAP_FLIP, player) and    #required to jump through all the rings
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_JIGGY_CC_SNIPPET:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                (
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get the Jiggy
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
                and
                (
                    state.has(ITEM_CLAW_SWIPE, player) or
                    state.has(ITEM_ROLL, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or    #required to defeat the Snippets
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player) or
                    state.has(ITEM_WONDERWING, player)
                )
            ),
        LOC_JIGGY_CC_UNDERWATER_TUNNEL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)    #required to access most of the level
            ),
        LOC_JIGGY_CC_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_CC_BLUE, player) and
                state.has(ITEM_JINJO_CC_GREEN, player) and
                state.has(ITEM_JINJO_CC_ORANGE, player) and
                state.has(ITEM_JINJO_CC_PURPLE, player) and
                state.has(ITEM_JINJO_CC_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_CC_PIPE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_EMPTY_HONEYCOMB_CC_GRATE:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_CC_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player)
                        )
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CC_CLANKER_TAIL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_CC_CLANKER_GOLD_TEETH:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_CC_GRATE:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_MUMBO_TOKEN_CC_UNDERWATER_TUNNEL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MOLEHILL_BGS_BEHIND_WORLD_ENTRY:
            lambda state: True,
        LOC_JIGGY_BGS_EGG:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_RAT_A_TAT_RAP, player) and
                state.has(ITEM_BEAK_BARGE, player)
            ),
        LOC_JIGGY_BGS_CENTER_RACE:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_JIGGY_BGS_FLIBBET:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or    #required to access most of the level
                    state.has(ITEM_TALON_TROT, player) or    #can fall from bridge without taking damage
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_ROLL, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player) or
                    state.has(ITEM_WONDERWING, player)
                )
            ),
        LOC_JIGGY_BGS_TANKTUP:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_TIPTUP:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_HUT:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level/get on the huts
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_MUMBOS_HUT_RACE:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_JIGGY_BGS_CROCTUS:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_TALON_TROT, player) and    #required to reach all Croctus locations
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_MR_VILE:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_JIGGY_BGS_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_BGS_BLUE, player) and
                state.has(ITEM_JINJO_BGS_GREEN, player) and
                state.has(ITEM_JINJO_BGS_ORANGE, player) and
                state.has(ITEM_JINJO_BGS_PURPLE, player) and
                state.has(ITEM_JINJO_BGS_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_BGS_TIPTUP_STAND:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_EMPTY_HONEYCOMB_BGS_INSIDE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    )
                )
            ),
        LOC_MUMBO_TOKEN_BGS_BEHIND_YELLOW_JINJO:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_ATOP_CATTAIL:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or  # required to access most of the level
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_MUMBO_TOKEN_BGS_CENTRAL_PLATFORM:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_INSIDE_TANKTUP:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_BGS_INSIDE_HUT:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or  # required to access most of the level/get on the huts
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBO:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_LEFT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_RIGHT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_INSIDE_MR_VILE:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MOLEHILL_FP_NEXT_TO_STACK_OF_PRESENTS:
            lambda state: True,
        LOC_JIGGY_FP_SIR_SLUSH:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_JIGGY_FP_SNOWMAN_PIPE:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or    #required to reach the snowman's scarf
                (
                    state.has(ITEM_TALON_TROT, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_JIGGY_FP_TOBOGGAN:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or    #required to reach the snowman's scarf
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_FP_SNOWMAN_BUTTONS:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_JIGGY_FP_CHRISTMAS_TREE:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to the Jiggy at the top of the tree
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_JIGGY_FP_WOZZA:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_JIGGY_FP_PRESENTS:
            lambda state:
            (
                state.has(ITEM_RED_PRESENT, player) and
                state.has(ITEM_BLUE_PRESENT, player) and
                state.has(ITEM_GREEN_PRESENT, player)
            ),
        LOC_JIGGY_FP_BOGGY_RACE_1:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_JIGGY_FP_BOGGY_RACE_2:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull (Race 1 must be completed)
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player) and
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_JIGGY_FP_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_FP_BLUE, player) and
                state.has(ITEM_JINJO_FP_GREEN, player) and
                state.has(ITEM_JINJO_FP_ORANGE, player) and
                state.has(ITEM_JINJO_FP_PURPLE, player) and
                state.has(ITEM_JINJO_FP_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_FP_SIR_SLUSH:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_EMPTY_HONEYCOMB_FP_WOZZA:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_MUMBO_TOKEN_FP_INSIDE_IGLOO:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_BEHIND_PRESENTS:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_ABOVE_HOUSE_FLIGHT_PAD:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_FP_SIR_SLUSH_WOZZA:
            lambda state:
            (
                    state.has(ITEM_FLIGHT, player) and
                    state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_FP_SIR_SLUSH_ISLAND:
            lambda state:
            (
                    state.has(ITEM_FLIGHT, player) and
                    state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_FP_TOBOGGAN:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or    #required to reach the snowman's scarf
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_LEFT:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_RIGHT:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_UNDER_CHRISTMAS_TREE:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_FP_UNDERWATER:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_MOLEHILL_GV_NEAR_KAZOOIE_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_GV_JINXY:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or   #required to jump across carpets
                    (
                        state.has(ITEM_JUMP, player) and    #some carpets have very strict jumps that need the height
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_GV_GRABBA:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_JIGGY_GV_FLIP_PANELS:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_GV_WATER_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_GV_ANCIENT_ONES:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_GV_RUBEE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player) and
                state.has(ITEM_EGGS, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get the Jiggy
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JIGGY_GV_SANDYBUTT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_GV_GOBI:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
            state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_GV_TRUNKER:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player) #Gobi's jiggy required first
            ) and
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    (
                        state.has(ITEM_CLIMB, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or    #to get on top of Trunker, you can either climb
                            state.has(ITEM_RAT_A_TAT_RAP, player) or    #up a nearby tree and jump across, or...
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        )
                    ) or
                    (
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or  #...get to the flight pad and fly over
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        ) and
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_FLIGHT, player)
                    )
                )
            ),
        LOC_JIGGY_GV_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_GV_BLUE, player) and
                state.has(ITEM_JINJO_GV_GREEN, player) and
                state.has(ITEM_JINJO_GV_ORANGE, player) and
                state.has(ITEM_JINJO_GV_PURPLE, player) and
                state.has(ITEM_JINJO_GV_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_GV_CACTUS:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_GV_GOBI:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ) and
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to get to carpet
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                ) #TODO: require Gobi & Trunker Jiggies
            ),
        LOC_MUMBO_TOKEN_GV_BEHIND_JINXY:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_GV_ABOVE_JINXYS_NOSE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                    )
                ) or
                (
                    state.has(ITEM_JUMP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                        state.has(ITEM_TALON_TROT, player)
                    ) and
                    (
                        state.has(ITEM_FLAP_FLIP, player) or        #required to actually get the token
                        state.has(ITEM_FLIGHT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_GV_INSIDE_JINXY:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                    )
                ) or
                (
                    state.has(ITEM_JUMP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_GV_OUTSIDE_WATER_PYRAMID_FRONT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or  # required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_GV_FLIP_PANEL_PYRAMID:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or  # required to access most of the level
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_GV_MOAT:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or  # required to access most of the level
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) #TODO: require water pyramid Jiggy or other solution
            ),
        LOC_MUMBO_TOKEN_GV_RUBEE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_GV_ATOP_CENTRAL_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_EGGS, player) or #you can either raise the pyramid normally, or...
                    (
                        ( #climb up Jinxy and fly to the token directly
                            state.has(ITEM_FLAP_FLIP, player) and
                            (
                                state.has(ITEM_FEATHERY_FLAP, player) or
                                state.has(ITEM_RAT_A_TAT_RAP, player)  # required to get on top of Jinxy
                            )
                        ) or
                        (
                            state.has(ITEM_JUMP, player) and
                            (
                                state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to get on top of Jinxy
                                state.has(ITEM_TALON_TROT, player)
                            )
                        ) and
                        state.has(ITEM_FLIGHT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_GV_CENTRAL_PYRAMID_POT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_GV_INSIDE_WATER_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_JIGGY_MMM_NAPPER:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_JUMP, player) or         #required to hop along the chairs
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or    #yes, it's possible, and not really that difficult
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_JIGGY_MMM_CELLAR:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MMM_TUMBLAR:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MMM_WELL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and   #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_JIGGY_MMM_FLOWERPOT:
            lambda state:
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MMM_CLOCK_TOWER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_JIGGY_MMM_MOTZAND:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_JIGGY_MMM_LOGGO:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                ) and
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_JIGGY_MMM_STORM_DRAIN:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                    state.has(ITEM_EGGS, player)
                )

            ),
        LOC_JIGGY_MMM_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_MMM_BLUE, player) and
                state.has(ITEM_JINJO_MMM_GREEN, player) and
                state.has(ITEM_JINJO_MMM_ORANGE, player) and
                state.has(ITEM_JINJO_MMM_PURPLE, player) and
                state.has(ITEM_JINJO_MMM_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_MMM_CHURCH_RAFTER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_MMM_FLOORBOARD:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                ) and
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_MMM_FIREPLACE:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and      #you can either climb up the mansion and enter the chimney...
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or       #...or just break down the door and walk in
                    state.has(ITEM_EGGS, player)                #Wonderwing also works
                )
            ),
        LOC_MUMBO_TOKEN_MMM_CELLAR:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_MMM_LOGGO:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                ) and
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_MMM_SINK:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                )
            ),
        LOC_MUMBO_TOKEN_MMM_MAZE:
            lambda state: True,
        LOC_MUMBO_TOKEN_MMM_MAZE_HIDDEN_AREA:
            lambda state:
            (
                (                   #you can either turn into a pumpkin and go in through the small gap in the hedge...
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                ) or
                state.has(ITEM_CLIMB, player) #...or just climb onto the roof and fall onto it, your call:)
            ),
        LOC_MUMBO_TOKEN_MMM_SHACK_ROOF:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_MMM_WELL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and   #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_MMM_BEHIND_GRAVE:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CLOCK_TOWER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CHURCH_CHAIR:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CHURCH_RAFTER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_MMM_NEAR_SHACK:
            lambda state: True,
        LOC_MUMBO_TOKEN_MMM_BEDROOM:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                )
            ),
        LOC_MUMBO_TOKEN_MMM_FOUNTAIN:
            lambda state:
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_MMM_NEAR_FOUNTAIN:
            lambda state: True,
        LOC_JIGGY_RBB_SMOKESTACK:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_JIGGY_RBB_WHISTLE:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or        #to get to the platform
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_RBB_WAREHOUSE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_EGGS, player) and    #to get to the Jiggy, you can either take the toll road...
                        state.has(ITEM_TALON_TROT, player) and
                        state.has(ITEM_BEAK_BUSTER, player)
                    )
                ) or
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or    #...or go in through the submerged door and climb up
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)           #you need this for the last jump regardless
            ),
        LOC_JIGGY_RBB_METAL_CAGE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_BEAK_BARGE, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or        #to get on top of the box
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #going around is never logically unique due to Trot
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JIGGY_RBB_CAPTAINS_ROOM:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or   #to break the window and the wooden door
                    state.has(ITEM_EGGS, player)                #Wonderwing probably works?
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or        #to get the Jiggy
                    state.has(ITEM_BEAK_BUSTER, player)         #not tested but probably works?
                )
            ),
        LOC_JIGGY_RBB_BOSS_BOOM_BOX:
            lambda state:
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or   #to jump on the TNT box above the boss room
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or             #to jump on the other boxes
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                (
                    state.has(ITEM_CLIMB, player) or            #to drop the TNT box
                    state.has(ITEM_BEAK_BARGE, player)          #Beak Barge is enough to beat the boss. Good luck:)
                )
            ),
        LOC_JIGGY_RBB_SNORKEL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_RBB_ENGINE_ROOM:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and       #to hit the switch before entering the engine room
                state.has(ITEM_BEAK_BUSTER, player)     #yes, you really need no other moves to get the Jiggy
            ),
        LOC_JIGGY_RBB_PROPELLER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and           #to hit the switch before entering the engine room
                state.has(ITEM_BEAK_BUSTER, player) and     #yes, you don't need any more moves for this one either
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_RBB_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_RBB_BLUE, player) and
                state.has(ITEM_JINJO_RBB_GREEN, player) and
                state.has(ITEM_JINJO_RBB_ORANGE, player) and
                state.has(ITEM_JINJO_RBB_PURPLE, player) and
                state.has(ITEM_JINJO_RBB_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_RBB_ENGINE_ROOM:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and #I THINK you can fall into the cubbyhole where the empty honeycomb is?
                state.has(ITEM_FLAP_FLIP, player) #I couldn't replicate it myself though
            ),
        LOC_EMPTY_HONEYCOMB_RBB_WAREHOUSE:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_RBB_TOLL_BRIDGE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_RBB_LIFEBOAT:
            lambda state: True,
        LOC_MUMBO_TOKEN_RBB_BEHIND_WITCH_SWITCH_TOWER:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_MUMBO_TOKEN_RBB_BARRACKS:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or   #to break the window
                    state.has(ITEM_EGGS, player)               #Wonderwing works too
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_ENTRY:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_LEFT:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_RIGHT:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_PERISCOPE_STOREROOM:
            lambda state: True,
        LOC_MUMBO_TOKEN_RBB_NAVIGATION_ROOM:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or   #to break the window
                state.has(ITEM_EGGS, player)               #Wonderwing works too
            ),
        LOC_MUMBO_TOKEN_RBB_OVEN:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player) #this is nigh impossible to get without taking damage or Wonderwing
            ),
        LOC_MUMBO_TOKEN_RBB_SMOKESTACK:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_TOXIC_WASTE_DRUM:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_SHIP_BOW:
            lambda state: True,
        LOC_MUMBO_TOKEN_RBB_LEFT_SHIPPING_CRATE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or    #first, you need to get to the crate, either from
                        state.has(ITEM_CLIMB, player)           #the ship's crane...
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and        #...or by going around the perimeter of the level
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or             #then you need to actually be able to get the token
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_RBB_MIDDLE_SHIPPING_CRATE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_CLIMB, player)           #first, you need to get to the crate, either from
                    ) or                                        #the ship's crane...
                    (
                        state.has(ITEM_EGGS, player) and        #...or by going around the perimeter of the level
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player)           #then you need to actually be able to get the token
                )
            ),
        LOC_JIGGY_CCW_TREETOP_ROOM:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break the wooden door at the top
                    state.has(ITEM_BEAK_BARGE, player) or           #Wonderwing works too
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_JIGGY_CCW_TREETOP_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_BEE, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_JIGGY_CCW_ZUBBA:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)         #yes, you can beat the Zubbas with just Beak Buster
            ),
        LOC_JIGGY_CCW_LEAVES:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and   #either route requires this
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or        #you can either jump up the leaves from the bottom...
                    state.has(ITEM_TALON_TROT, player)          #...or climb up and fall onto the platform
                )
            ),
        LOC_JIGGY_CCW_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_JIGGY_CCW_GNAWTY:
            lambda state:
            (
                (
                    state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                    state.has(ITEM_BEAK_BUSTER, player) or          #Wonderwing MIGHT work but probably not
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_CCW_PLANT:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BUSTER, player) and         #needs all Gobi events prior done
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_CCW_NABNUTS:
            lambda state:
            (
                state.has(ITEM_ACORN, player, 6)
            ),
        LOC_JIGGY_CCW_EYRIE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_WORM, player, 15)
            ),
        LOC_JIGGY_CCW_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_CCW_BLUE, player) and
                state.has(ITEM_JINJO_CCW_GREEN, player) and
                state.has(ITEM_JINJO_CCW_ORANGE, player) and
                state.has(ITEM_JINJO_CCW_PURPLE, player) and
                state.has(ITEM_JINJO_CCW_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_CCW_WINTER_NABNUTS:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BOMB, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_CCW_WINTER_GNAWTY:
            lambda state:
            (
                state.has(ITEM_SWIM, player) #May require boulder broken in summer?
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_GARDEN_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_BEEHIVE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_NABNUTS_DRESSER:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_NEAR_EYRIES_NEST:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_THORNS:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_GNAWTY:
            lambda state:
            (
                state.has(ITEM_BEAK_BARGE, player) or  # required to break the boulder
                state.has(ITEM_BEAK_BUSTER, player) or # Wonderwing MIGHT work but probably not
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_GARDEN:
            lambda state: True,
        LOC_MUMBO_TOKEN_CCW_SUMMER_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or   #you can either just climb the ramp...
                (
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    ) and
                    (
                        state.has(ITEM_FLAP_FLIP, player) and        #...or climb the leaves and fall onto the platform
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_LEAVES:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and   #either route requires this
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_AFTER_NABNUTS_HOUSE:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and   #either route requires this
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or        #you can either jump up the leaves from the bottom...
                    state.has(ITEM_TALON_TROT, player)          #...or climb up the ramp
                )
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or   #you can either just climb the ramp...
                (
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    ) and
                    (
                        state.has(ITEM_FLAP_FLIP, player) and        #...or climb the leaves and fall onto the platform
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_LEAVES:
            lambda state:
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or        #you can either jump up the leaves from the bottom...
                    (
                        state.has(ITEM_TALON_TROT, player) and  #...or climb up the ramp and fall down the leaves
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_GARDEN:
            lambda state: True,
        LOC_MUMBO_TOKEN_CCW_WINTER_SIR_SLUSH:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_BEEHIVE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_NEAR_NABNUTS_HOUSE:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_TALON_TROT, player) and
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    ) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_BEHIND_LAKE_PLATFORM:
            lambda state: True,
        # Notes
# Mumbo's Mountain Notes (1-100)
        
        # Bridge (1-7) - Basic access
        LOC_NOTE_MM_BRIDGE_1:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_2:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_3:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_4:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_5:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_6:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_7:
            lambda state: True,
        
        # Slope To Tickers (8-16) - May need basic movement
        LOC_NOTE_MM_SLOPE_TO_TICKERS_1:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_2:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_3:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_4:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_5:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_6:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_7:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_8:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_TICKERS_9:
            lambda state: True,
        
        # Slope To Stonehenge (17-20)
        LOC_NOTE_MM_SLOPE_TO_STONEHENGE_1:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_STONEHENGE_2:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_STONEHENGE_3:
            lambda state: True,
        LOC_NOTE_MM_SLOPE_TO_STONEHENGE_4:
            lambda state: True,
        
        # Stonehenge (21-34) - Stone circle area
        LOC_NOTE_MM_STONEHENGE_1:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_2:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_3:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_4:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_5:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_6:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_7:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_8:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_9:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_10:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_11:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_12:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_13:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_14:
            lambda state: True,
        
        # Conga Upper Right (35-37) - Requires Flap Flip
        LOC_NOTE_MM_CONGA_UPPER_RIGHT_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_CONGA_UPPER_RIGHT_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_CONGA_UPPER_RIGHT_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Conga Upper Left (38-40) - Requires Flap Flip and (Jump or Feathery Flap)
        LOC_NOTE_MM_CONGA_UPPER_LEFT_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_MM_CONGA_UPPER_LEFT_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_MM_CONGA_UPPER_LEFT_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        
        # Conga Middle Right (41-43)
        LOC_NOTE_MM_CONGA_MIDDLE_RIGHT_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_MIDDLE_RIGHT_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_MIDDLE_RIGHT_3:
            lambda state: True,
        
        # Conga Bottom Left (44-46)
        LOC_NOTE_MM_CONGA_BOTTOM_LEFT_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_BOTTOM_LEFT_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_BOTTOM_LEFT_3:
            lambda state: True,
        
        # Conga Middle Left (47-49)
        LOC_NOTE_MM_CONGA_MIDDLE_LEFT_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_MIDDLE_LEFT_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_MIDDLE_LEFT_3:
            lambda state: True,
        
        # Conga Bottom Right (50-52)
        LOC_NOTE_MM_CONGA_BOTTOM_RIGHT_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_BOTTOM_RIGHT_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_BOTTOM_RIGHT_3:
            lambda state: True,
        
        # Conga Bottom (53-55)
        LOC_NOTE_MM_CONGA_BOTTOM_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_BOTTOM_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_BOTTOM_3:
            lambda state: True,
        
        # Mumbo Top Right (56-58)
        LOC_NOTE_MM_MUMBO_TOP_RIGHT_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_TOP_RIGHT_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_TOP_RIGHT_3:
            lambda state: True,
        
        # Mumbo Middle Right (59-61)
        LOC_NOTE_MM_MUMBO_MIDDLE_RIGHT_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_MIDDLE_RIGHT_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_MIDDLE_RIGHT_3:
            lambda state: True,
        
        # Mumbo Middle Left (62-64)
        LOC_NOTE_MM_MUMBO_MIDDLE_LEFT_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_MIDDLE_LEFT_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_MIDDLE_LEFT_3:
            lambda state: True,
        
        # Mumbo Lower Left (65-67)
        LOC_NOTE_MM_MUMBO_LOWER_LEFT_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_LOWER_LEFT_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_LOWER_LEFT_3:
            lambda state: True,
        
        # Mumbo Bottom Middle (68-70)
        LOC_NOTE_MM_MUMBO_BOTTOM_MIDDLE_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_BOTTOM_MIDDLE_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_BOTTOM_MIDDLE_3:
            lambda state: True,
        
        # Mumbo Bottom Right (71-73)
        LOC_NOTE_MM_MUMBO_BOTTOM_RIGHT_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_BOTTOM_RIGHT_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_BOTTOM_RIGHT_3:
            lambda state: True,
        
        # Inside Mumbos Skull (74-77)
        LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_1:
            lambda state: True,
        LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_2:
            lambda state: True,
        LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_3:
            lambda state: True,
        LOC_NOTE_MM_INSIDE_MUMBOS_SKULL_4:
            lambda state: True,
        
        # Totem Pole Hut (78-83)
        LOC_NOTE_MM_TOTEM_POLE_HUT_1:
            lambda state: True,
        LOC_NOTE_MM_TOTEM_POLE_HUT_2:
            lambda state: True,
        LOC_NOTE_MM_TOTEM_POLE_HUT_3:
            lambda state: True,
        LOC_NOTE_MM_TOTEM_POLE_HUT_4:
            lambda state: True,
        LOC_NOTE_MM_TOTEM_POLE_HUT_5:
            lambda state: True,
        LOC_NOTE_MM_TOTEM_POLE_HUT_6:
            lambda state: True,
        
        # Destroy Hut (84-88) - Requires Beak Buster
        LOC_NOTE_MM_DESTROY_HUT_1:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_MM_DESTROY_HUT_2:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_MM_DESTROY_HUT_3:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_MM_DESTROY_HUT_4:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_MM_DESTROY_HUT_5:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        
        # Underwater Left Cave (89-91) - Requires swimming
        LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Underwater Right Cave (92-94) - Requires swimming
        LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Termite Mound Landing (95-100) - Requires Termite Transformation
        LOC_NOTE_MM_TERMITE_MOUND_LANDING_1:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_LANDING_2:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_LANDING_3:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_LANDING_4:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_LANDING_5:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_LANDING_6:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        # TTC Notes
# Treasure Trove Cove Notes (1-100)
        
        # Arrival Platform (1-4) - Immediate access
        LOC_NOTE_TTC_ARRIVAL_PLATFORM_1:
            lambda state: True,
        LOC_NOTE_TTC_ARRIVAL_PLATFORM_2:
            lambda state: True,
        LOC_NOTE_TTC_ARRIVAL_PLATFORM_3:
            lambda state: True,
        LOC_NOTE_TTC_ARRIVAL_PLATFORM_4:
            lambda state: True,
        
        # Blubber's Forward Netting (5-7) - Requires climbing or flight
        LOC_NOTE_TTC_BLUBBERS_FORWARD_NETTING_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_FORWARD_NETTING_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_FORWARD_NETTING_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        
        # Top Sandcastle (8-12) - Requires vertical movement
        LOC_NOTE_TTC_TOP_SANDCASTLE_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_TOP_SANDCASTLE_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_TOP_SANDCASTLE_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_TOP_SANDCASTLE_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_TOP_SANDCASTLE_5:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        
        # Inside Sandcastle (13-16) - Ground level access
        LOC_NOTE_TTC_INSIDE_SANDCASTLE_1:
            lambda state: True,
        LOC_NOTE_TTC_INSIDE_SANDCASTLE_2:
            lambda state: True,
        LOC_NOTE_TTC_INSIDE_SANDCASTLE_3:
            lambda state: True,
        LOC_NOTE_TTC_INSIDE_SANDCASTLE_4:
            lambda state: True,
        
        # Inside Nipper's Shell (17-22) - Requires Rat-a-Tap Rap to defeat Nipper
        LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_5:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_INSIDE_NIPPERS_SHELL_6:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        
        # Upper Stairway Pools (23-26) - Requires movement ability
        LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_UPPER_STAIRWAY_POOLS_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Middle Stairway Pools (27-30) - Easier to reach
        LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_1:
            lambda state: True,
        LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_2:
            lambda state: True,
        LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_3:
            lambda state: True,
        LOC_NOTE_TTC_MIDDLE_STAIRWAY_POOLS_4:
            lambda state: True,
        
        # Lower Stairway Pools (31-34) - Ground level
        LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_1:
            lambda state: True,
        LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_2:
            lambda state: True,
        LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_3:
            lambda state: True,
        LOC_NOTE_TTC_LOWER_STAIRWAY_POOLS_4:
            lambda state: True,
        
        # Raised Pool Crab (35-37) - Elevated pool
        LOC_NOTE_TTC_RAISED_POOL_CRAB_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_RAISED_POOL_CRAB_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_RAISED_POOL_CRAB_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        
        # High Bridge Chest (38-40) - Elevated bridge
        LOC_NOTE_TTC_HIGH_BRIDGE_CHEST_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_CHEST_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_CHEST_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # High Bridge Nipper (41-43)
        LOC_NOTE_TTC_HIGH_BRIDGE_NIPPER_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_NIPPER_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_NIPPER_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # High Bridge Blubbers (44-46)
        LOC_NOTE_TTC_HIGH_BRIDGE_BLUBBERS_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_BLUBBERS_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_BLUBBERS_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # High Bridge Sandcastle (47-49)
        LOC_NOTE_TTC_HIGH_BRIDGE_SANDCASTLE_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_SANDCASTLE_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_HIGH_BRIDGE_SANDCASTLE_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Shock Spring Pillar (50-52) - Requires Shock Spring Jump
        LOC_NOTE_TTC_SHOCK_SPRING_PILLAR_1:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_TTC_SHOCK_SPRING_PILLAR_2:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_TTC_SHOCK_SPRING_PILLAR_3:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        
        # High Platform Treasure Box (53-58) - Very high platform
        LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_5:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_TTC_HIGH_PLATFORM_TREASURE_BOX_6:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        
        # Tree Stern (59-62) - Requires climbing ability
        LOC_NOTE_TTC_TREE_STERN_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_TTC_TREE_STERN_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_TTC_TREE_STERN_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_TTC_TREE_STERN_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        
        # Tree Bow (63-66)
        LOC_NOTE_TTC_TREE_BOW_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_TTC_TREE_BOW_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_TTC_TREE_BOW_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_TTC_TREE_BOW_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        
        # Blubber's Bow Netting (67-69)
        LOC_NOTE_TTC_BLUBBERS_BOW_NETTING_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_BOW_NETTING_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_BOW_NETTING_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        
        # Blubber's Aft Netting (70-74)
        LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_BLUBBERS_AFT_NETTING_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        
        # Blubber's Aft Cargo (75-78)
        LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_1:
            lambda state: True,
        LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_2:
            lambda state: True,
        LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_3:
            lambda state: True,
        LOC_NOTE_TTC_BLUBBERS_AFT_CARGO_4:
            lambda state: True,
        
        # Blubber's Bow Cargo (79-82)
        LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_1:
            lambda state: True,
        LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_2:
            lambda state: True,
        LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_3:
            lambda state: True,
        LOC_NOTE_TTC_BLUBBERS_BOW_CARGO_4:
            lambda state: True,
        
        # Treasure Chest SSS (83-87) - On island, no special requirements
        LOC_NOTE_TTC_TREASURE_CHEST_SSS_1:
            lambda state: True,
        LOC_NOTE_TTC_TREASURE_CHEST_SSS_2:
            lambda state: True,
        LOC_NOTE_TTC_TREASURE_CHEST_SSS_3:
            lambda state: True,
        LOC_NOTE_TTC_TREASURE_CHEST_SSS_4:
            lambda state: True,
        LOC_NOTE_TTC_TREASURE_CHEST_SSS_5:
            lambda state: True,
        
        # Path First Map Pillar (88-91) - High area
        LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_TTC_PATH_FIRST_MAP_PILLAR_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Cave To Lighthouse (92)
        LOC_NOTE_TTC_CAVE_TO_LIGHTHOUSE_1:
            lambda state: True,
        
        # Path To Lighthouse (93-95) - Requires flight
        LOC_NOTE_TTC_PATH_TO_LIGHTHOUSE_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_PATH_TO_LIGHTHOUSE_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_PATH_TO_LIGHTHOUSE_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        
        # Lighthouse Balcony (96-100) - Top of lighthouse
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_5:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        # CC Notes
        
        # Left Pipe Entryway (1-4) - Requires climbing ladder and jumping
        LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_CC_LEFT_PIPE_ENTRYWAY_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        
        # Right Pipe Entryway (5-8) - Same requirements
        LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_NOTE_CC_RIGHT_PIPE_ENTRYWAY_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        
        # Pipe to Clanker (9-14) - Underwater pipes
        LOC_NOTE_CC_PIPE_TO_CLANKER_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PIPE_TO_CLANKER_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PIPE_TO_CLANKER_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PIPE_TO_CLANKER_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PIPE_TO_CLANKER_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PIPE_TO_CLANKER_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Right Floor Pipe (15-21) - Floor pipes in water
        LOC_NOTE_CC_RIGHT_FLOOR_PIPE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_FLOOR_PIPE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_FLOOR_PIPE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_FLOOR_PIPE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_FLOOR_PIPE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_FLOOR_PIPE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_FLOOR_PIPE_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Glowing Room (22-29) - Bottom of room, just needs swim
        LOC_NOTE_CC_GLOWING_ROOM_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Around Anchor (30-37) - Swimming around anchor chain
        LOC_NOTE_CC_AROUND_ANCHOR_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_AROUND_ANCHOR_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_AROUND_ANCHOR_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_AROUND_ANCHOR_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_AROUND_ANCHOR_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_AROUND_ANCHOR_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_AROUND_ANCHOR_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_AROUND_ANCHOR_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Along Spine (38-47) - On Clanker's back after surfacing
        LOC_NOTE_CC_ALONG_SPINE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_9:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CC_ALONG_SPINE_10:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        
        # Raised Pipe Behind (48-57) - Elevated pipe with shock spring
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_9:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RAISED_PIPE_BEHIND_10:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        
        # Platform Blowhole (58-61) - Platform near blowhole
        LOC_NOTE_CC_PLATFORM_BLOWHOLE_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PLATFORM_BLOWHOLE_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PLATFORM_BLOWHOLE_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PLATFORM_BLOWHOLE_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_SWIM, player)
            ),
        
        # Tunnel Starboard Gills (62-66) - Inside gill tunnels
        LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_TUNNEL_STARBOARD_GILLS_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Tunnel Portside Gills (67-69)
        LOC_NOTE_CC_TUNNEL_PORTSIDE_GILLS_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_TUNNEL_PORTSIDE_GILLS_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_TUNNEL_PORTSIDE_GILLS_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Inside Mouth (70-77) - Inside Clanker's mouth
        LOC_NOTE_CC_INSIDE_MOUTH_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_INSIDE_MOUTH_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_INSIDE_MOUTH_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_INSIDE_MOUTH_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_INSIDE_MOUTH_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_INSIDE_MOUTH_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_INSIDE_MOUTH_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_INSIDE_MOUTH_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Blowhole Sawblade (78-83) - 
        LOC_NOTE_CC_BLOWHOLE_SAWBLADE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWBLADE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWBLADE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWBLADE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWBLADE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWBLADE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Right Climbing Pipe (84-87) - Requires climbing
        LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_NOTE_CC_RIGHT_CLIMBING_PIPE_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_JUMP, player) and 
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        
        # Right Angled Duct (88-92) - Accessible through swimming
        LOC_NOTE_CC_RIGHT_ANGLED_DUCT_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_ANGLED_DUCT_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_ANGLED_DUCT_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_ANGLED_DUCT_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_ANGLED_DUCT_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Left Cubbies (93-94) - Elevated alcoves (no flight pad here)
        LOC_NOTE_CC_LEFT_CUBBIES_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player)
                )
            ),
        LOC_NOTE_CC_LEFT_CUBBIES_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_JUMP, player)
                )
            ),
        
        # Aft Sawblade (95-100) - Requires flight
        LOC_NOTE_CC_AFT_SAWBLADE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWBLADE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWBLADE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWBLADE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWBLADE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWBLADE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),

        #BGS Notes
        
# Bubblegloop Swamp Notes (1-100)
        
        # Bridge Entryway (1-5) - Entry area
        LOC_NOTE_BGS_BRIDGE_ENTRYWAY_1:
            lambda state: True,
        LOC_NOTE_BGS_BRIDGE_ENTRYWAY_2:
            lambda state: True,
        LOC_NOTE_BGS_BRIDGE_ENTRYWAY_3:
            lambda state: True,
        LOC_NOTE_BGS_BRIDGE_ENTRYWAY_4:
            lambda state: True,
        LOC_NOTE_BGS_BRIDGE_ENTRYWAY_5:
            lambda state: True,
        
        # Log Jiggy Switch (6-8) - Ground level
        LOC_NOTE_BGS_LOG_JIGGY_SWITCH_1:
            lambda state: True,
        LOC_NOTE_BGS_LOG_JIGGY_SWITCH_2:
            lambda state: True,
        LOC_NOTE_BGS_LOG_JIGGY_SWITCH_3:
            lambda state: True,
        
        # Log Stumps (9-11) - Ground level
        LOC_NOTE_BGS_LOG_STUMPS_1:
            lambda state: True,
        LOC_NOTE_BGS_LOG_STUMPS_2:
            lambda state: True,
        LOC_NOTE_BGS_LOG_STUMPS_3:
            lambda state: True,
        
        # Log Turtle (12-14) - Ground level
        LOC_NOTE_BGS_LOG_TURTLE_1:
            lambda state: True,
        LOC_NOTE_BGS_LOG_TURTLE_2:
            lambda state: True,
        LOC_NOTE_BGS_LOG_TURTLE_3:
            lambda state: True,
        
        # Tanktup's Flippers (15-18) - On top of turtle, needs level access
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_1:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_2:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_3:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_4:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Log Hut Pillars (19-21) - Ground level
        LOC_NOTE_BGS_LOG_HUT_PILLARS_1:
            lambda state: True,
        LOC_NOTE_BGS_LOG_HUT_PILLARS_2:
            lambda state: True,
        LOC_NOTE_BGS_LOG_HUT_PILLARS_3:
            lambda state: True,
        
        # Log Crocodile (22-24) - Ground level
        LOC_NOTE_BGS_LOG_CROCODILE_1:
            lambda state: True,
        LOC_NOTE_BGS_LOG_CROCODILE_2:
            lambda state: True,
        LOC_NOTE_BGS_LOG_CROCODILE_3:
            lambda state: True,
        
        # Crocodile's Snout (25-29) - On top of crocodile head
        LOC_NOTE_BGS_CROCODILES_SNOUT_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Behind Giant Egg (30-34) - In water, requires Stilt Stride
        LOC_NOTE_BGS_BEHIND_GIANT_EGG_1:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_GIANT_EGG_2:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_GIANT_EGG_3:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_GIANT_EGG_4:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_GIANT_EGG_5:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        
        # First Raised Bridge (35-39) - Elevated platform
        LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_FIRST_RAISED_BRIDGE_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Second Raised Bridge (40-43) - Elevated platform
        LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_SECOND_RAISED_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Third Raised Bridge (44-50) - Elevated platform
        LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_THIRD_RAISED_BRIDGE_7:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Fourth Raised Bridge (51-54) - Elevated platform
        LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_BGS_FOURTH_RAISED_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Inside Tanktup's Shell (55-60) - Need level access and Beak Buster to enter
        LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_1:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_2:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_3:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_4:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_5:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUPS_SHELL_6:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        
        # Destroy Hut Grunty (61-65) - Requires level access, Shock Spring Jump, and Beak Buster
        LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_1:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_2:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_3:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_4:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_GRUNTY_5:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        
        # Cattail Blue Jinjo (66-68) - On cattails, requires level access and climb
        LOC_NOTE_BGS_CATTAIL_BLUE_JINJO_1:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_BGS_CATTAIL_BLUE_JINJO_2:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_BGS_CATTAIL_BLUE_JINJO_3:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        
        # Behind Blue Jinjo (69-73) - In water
        LOC_NOTE_BGS_BEHIND_BLUE_JINJO_1:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_BLUE_JINJO_2:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_BLUE_JINJO_3:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_BLUE_JINJO_4:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_BLUE_JINJO_5:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        
        # Wading Boots Maze (74-85) - In water, requires Stilt Stride
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_1:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_2:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_3:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_4:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_5:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_6:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_7:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_8:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_9:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_10:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_11:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_WADING_BOOTS_MAZE_12:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        
        # Crocodile Right Nostril (86-88) - Inside crocodile head
        LOC_NOTE_BGS_CROCODILE_RIGHT_NOSTRIL_1:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_CROCODILE_RIGHT_NOSTRIL_2:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_CROCODILE_RIGHT_NOSTRIL_3:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        
        # Crocodile Left Nostril (89-91) - Inside crocodile head
        LOC_NOTE_BGS_CROCODILE_LEFT_NOSTRIL_1:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_CROCODILE_LEFT_NOSTRIL_2:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_CROCODILE_LEFT_NOSTRIL_3:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        
        # Under Hut Pillar (92-95) - Under water, requires Stilt Stride and Crocodile transformation
        LOC_NOTE_BGS_UNDER_HUT_PILLAR_1:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_UNDER_HUT_PILLAR_2:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_UNDER_HUT_PILLAR_3:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_UNDER_HUT_PILLAR_4:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        
        # Behind Hut Pillars (96-100) - In water
        LOC_NOTE_BGS_BEHIND_HUT_PILLARS_1:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_HUT_PILLARS_2:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_HUT_PILLARS_3:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_HUT_PILLARS_4:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_HUT_PILLARS_5:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),

        #FP Notes
        
        # Upper Boggy Ramp (1-5) - Elevated ramp
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Lower Boggy Ramp (6-9) - Ground level
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_1:
            lambda state: True,
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_2:
            lambda state: True,
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_3:
            lambda state: True,
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_4:
            lambda state: True,
        
        # Behind Tree (10-14) - Ground level
        LOC_NOTE_FP_BEHIND_TREE_1:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_2:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_3:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_4:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_5:
            lambda state: True,
        
        # Stack Presents Purple (15-18) - Elevated stack
        LOC_NOTE_FP_STACK_PRESENTS_PURPLE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_STACK_PRESENTS_PURPLE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_STACK_PRESENTS_PURPLE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_STACK_PRESENTS_PURPLE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Around Present Sir Slush (19-22) - Ground level
        LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_1:
            lambda state: True,
        LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_2:
            lambda state: True,
        LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_3:
            lambda state: True,
        LOC_NOTE_FP_AROUND_PRESENT_SIR_SLUSH_4:
            lambda state: True,
        
        # House Mumbos (23-25) - Ground level
        LOC_NOTE_FP_HOUSE_MUMBOS_1:
            lambda state: True,
        LOC_NOTE_FP_HOUSE_MUMBOS_2:
            lambda state: True,
        LOC_NOTE_FP_HOUSE_MUMBOS_3:
            lambda state: True,
        
        # House Between Slushes (26-28) - Ground level
        LOC_NOTE_FP_HOUSE_BETWEEN_SLUSHES_1:
            lambda state: True,
        LOC_NOTE_FP_HOUSE_BETWEEN_SLUSHES_2:
            lambda state: True,
        LOC_NOTE_FP_HOUSE_BETWEEN_SLUSHES_3:
            lambda state: True,
        
        # Beehive Platform (29-32) - Elevated platform
        LOC_NOTE_FP_BEEHIVE_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_BEEHIVE_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_BEEHIVE_PLATFORM_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_BEEHIVE_PLATFORM_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        
        # Snowman's Left Foot (33-37) - Ground level
        LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_1:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_2:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_3:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_4:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_LEFT_FOOT_5:
            lambda state: True,
        
        # Snowman's Right Foot (38-42) - Ground level
        LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_1:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_2:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_3:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_4:
            lambda state: True,
        LOC_NOTE_FP_SNOWMANS_RIGHT_FOOT_5:
            lambda state: True,
        
        # Inside Tree (43-54) - Requires breaking in and climbing
        LOC_NOTE_FP_INSIDE_TREE_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_5:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_6:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_7:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_8:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_9:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_10:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_11:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_12:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_CLIMB, player)
            ),
        
        # Wozza's Cave Platform (55-58) - Cave area
        LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_1:
            lambda state: True,
        LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_2:
            lambda state: True,
        LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_3:
            lambda state: True,
        LOC_NOTE_FP_WOZZAS_CAVE_PLATFORM_4:
            lambda state: True,
        
        # Up Snowman's Scarf (59-73) - Climbing snowman
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_5:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_6:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_7:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_8:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_9:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_10:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_11:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_12:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_13:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_14:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_UP_SNOWMANS_SCARF_15:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Scarf Around Neck (74-77) - On snowman's neck
        LOC_NOTE_FP_SCARF_AROUND_NECK_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_SCARF_AROUND_NECK_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_SCARF_AROUND_NECK_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_FP_SCARF_AROUND_NECK_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        
        # Top Snowman's Hat (78-85) - Very top, requires flight
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_5:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_6:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_7:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_TOP_SNOWMANS_HAT_8:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        
        # Inside Mumbo's Skull (86-91) - Ground access
        LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_1:
            lambda state: True,
        LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_2:
            lambda state: True,
        LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_3:
            lambda state: True,
        LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_4:
            lambda state: True,
        LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_5:
            lambda state: True,
        LOC_NOTE_FP_INSIDE_MUMBOS_SKULL_6:
            lambda state: True,
        
        # Around Island Mumbos (92-100) - Island area, requires reaching Mumbo's island
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_5:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_6:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_7:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_8:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_NOTE_FP_AROUND_ISLAND_MUMBOS_9:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_STILT_STRIDE, player) or 
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        # GV Notes
# Gobi's Valley Notes (1-100)
        
        # Slope Entryway (1-5) - Entry area
        LOC_NOTE_GV_SLOPE_ENTRYWAY_1:
            lambda state: True,
        LOC_NOTE_GV_SLOPE_ENTRYWAY_2:
            lambda state: True,
        LOC_NOTE_GV_SLOPE_ENTRYWAY_3:
            lambda state: True,
        LOC_NOTE_GV_SLOPE_ENTRYWAY_4:
            lambda state: True,
        LOC_NOTE_GV_SLOPE_ENTRYWAY_5:
            lambda state: True,
        
        # Jinxy's Right Paw (6-8) - Need Talon Trot for level access
        LOC_NOTE_GV_JINXYS_RIGHT_PAW_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_JINXYS_RIGHT_PAW_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_JINXYS_RIGHT_PAW_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Jinxy's Left Paw (9-11)
        LOC_NOTE_GV_JINXYS_LEFT_PAW_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_JINXYS_LEFT_PAW_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_JINXYS_LEFT_PAW_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Magic Carpet Ride (12-16) - Need to jump across carpets
        LOC_NOTE_GV_MAGIC_CARPET_RIDE_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_RIDE_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_RIDE_3:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_RIDE_4:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_RIDE_5:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Stairs Sandybutts Tomb (17-20)
        LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_STAIRS_SANDYBUTTS_TOMB_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Stairs Flip Puzzle (21-24)
        LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_STAIRS_FLIP_PUZZLE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Next Flip Puzzle (25-26)
        LOC_NOTE_GV_NEXT_FLIP_PUZZLE_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_NEXT_FLIP_PUZZLE_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        
        # Flip Puzzle Front (27-30)
        LOC_NOTE_GV_FLIP_PUZZLE_FRONT_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_FLIP_PUZZLE_FRONT_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_FLIP_PUZZLE_FRONT_3:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_FLIP_PUZZLE_FRONT_4:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        
        # Around Sandybutts Tomb (31-39)
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_7:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_8:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_SANDYBUTTS_TOMB_9:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Turbo Trainers Platform (40-41)
        LOC_NOTE_GV_TURBO_TRAINERS_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_TURBO_TRAINERS_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Water Pyramid Race (42-45) - Requires Turbo Talon Trot
        LOC_NOTE_GV_WATER_PYRAMID_RACE_1:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_WATER_PYRAMID_RACE_2:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_WATER_PYRAMID_RACE_3:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_WATER_PYRAMID_RACE_4:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Behind Jinxy (46-53) - Requires Stilt Stride
        LOC_NOTE_GV_BEHIND_JINXY_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_3:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_4:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_5:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_6:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_7:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_8:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        
        # Floor Inside Jinxy (54-57) - Need to get on top of Jinxy
        LOC_NOTE_GV_FLOOR_INSIDE_JINXY_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_NOTE_GV_FLOOR_INSIDE_JINXY_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_NOTE_GV_FLOOR_INSIDE_JINXY_3:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_NOTE_GV_FLOOR_INSIDE_JINXY_4:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        
        # Carpets Inside Jinxy (58-60) - Also need eggs
        LOC_NOTE_GV_CARPETS_INSIDE_JINXY_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_GV_CARPETS_INSIDE_JINXY_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_GV_CARPETS_INSIDE_JINXY_3:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        
        # Around Grabba's Platform (61-71) - Requires Turbo
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_3:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_4:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_5:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_6:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_7:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_8:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_9:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_10:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_AROUND_GRABBAS_PLATFORM_11:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Sandybutts Tomb Entryway (72-74)
        LOC_NOTE_GV_SANDYBUTTS_TOMB_ENTRYWAY_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_ENTRYWAY_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_ENTRYWAY_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Sandybutts Tomb Maze Exit (75-78)
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MAZE_EXIT_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Inside Water Pyramid (79-82) - Requires Turbo
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_1:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_2:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_3:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_4:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Sandybutts Tomb Moat (83-88)
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_SANDYBUTTS_TOMB_MOAT_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        
        # Inside Flip Puzzle (89-92) - Requires Beak Buster
        LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_3:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_INSIDE_FLIP_PUZZLE_4:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        
        # Inside Rubee's Pyramid (93-100) - Need to get on Jinxy, fly, and Beak Bomb
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_1:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_2:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_3:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_4:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_5:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_6:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_7:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_8:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        #MMM Notes
# Mad Monster Mansion Notes (1-100)
        
        # Main Entrance Wall (1-4) - Entry area
        LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_1:
            lambda state: True,
        LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_2:
            lambda state: True,
        LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_3:
            lambda state: True,
        LOC_NOTE_MMM_MAIN_ENTRANCE_WALL_4:
            lambda state: True,
        
        # Hedge Maze (5-10) - Ground level maze
        LOC_NOTE_MMM_HEDGE_MAZE_1:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_2:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_3:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_4:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_5:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_6:
            lambda state: True,
        
        # Foul Fountain (11-14) - Ground accessible
        LOC_NOTE_MMM_FOUL_FOUNTAIN_1:
            lambda state: True,
        LOC_NOTE_MMM_FOUL_FOUNTAIN_2:
            lambda state: True,
        LOC_NOTE_MMM_FOUL_FOUNTAIN_3:
            lambda state: True,
        LOC_NOTE_MMM_FOUL_FOUNTAIN_4:
            lambda state: True,
        
        # Alcove Graveyard (15-17) - Need to open church gate
        LOC_NOTE_MMM_ALCOVE_GRAVEYARD_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_ALCOVE_GRAVEYARD_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_ALCOVE_GRAVEYARD_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        
        # Gutter Drain (18-21) - Pumpkin transformation required
        LOC_NOTE_MMM_GUTTER_DRAIN_1:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_GUTTER_DRAIN_2:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_GUTTER_DRAIN_3:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_GUTTER_DRAIN_4:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        
        # Dining Room Chair (22-29) - Inside mansion via chimney or door
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_1:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_2:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_3:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_4:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_5:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_6:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_7:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_8:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        
        # Upper Gutters (30-33) - Outside mansion roof
        LOC_NOTE_MMM_UPPER_GUTTERS_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_MMM_UPPER_GUTTERS_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_MMM_UPPER_GUTTERS_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_MMM_UPPER_GUTTERS_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        
        # Painting Room (34-42) - Inside mansion via window
        LOC_NOTE_MMM_PAINTING_ROOM_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_5:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_6:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_7:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_8:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_9:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        
        # Bedroom Dresser (43-46) - Climb + shock spring + break window
        LOC_NOTE_MMM_BEDROOM_DRESSER_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_BEDROOM_DRESSER_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_BEDROOM_DRESSER_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_BEDROOM_DRESSER_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        
        # Wine Rack Basement (47-50) - Cellar access
        LOC_NOTE_MMM_WINE_RACK_BASEMENT_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_WINE_RACK_BASEMENT_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_WINE_RACK_BASEMENT_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_WINE_RACK_BASEMENT_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        
        # Graveyard Church Roof (51-60) - Church gate access required
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_5:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_6:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_7:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_8:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_9:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_GRAVEYARD_CHURCH_ROOF_10:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        
        # Atop Clock Tower (61-64) - Clock tower requirements
        LOC_NOTE_MMM_ATOP_CLOCK_TOWER_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_MMM_ATOP_CLOCK_TOWER_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_MMM_ATOP_CLOCK_TOWER_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_MMM_ATOP_CLOCK_TOWER_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_CLIMB, player)
            ),
        
        # On Tumblar's Shack (65-68) - On roof
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_1:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_2:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_3:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_4:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        
        # Church Pew (69-72) - Inside church
        LOC_NOTE_MMM_CHURCH_PEW_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_CHURCH_PEW_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_CHURCH_PEW_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_CHURCH_PEW_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        
        # Church Organ Pedals (73-74) - Motzand location requirements
        LOC_NOTE_MMM_CHURCH_ORGAN_PEDALS_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_CHURCH_ORGAN_PEDALS_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        
        # Church Organ Pipes (75-78) - Same as pedals
        LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_CHURCH_ORGAN_PIPES_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        
        # Ledges Around Well (79-82) - Ground level near well
        LOC_NOTE_MMM_LEDGES_AROUND_WELL_1:
            lambda state: True,
        LOC_NOTE_MMM_LEDGES_AROUND_WELL_2:
            lambda state: True,
        LOC_NOTE_MMM_LEDGES_AROUND_WELL_3:
            lambda state: True,
        LOC_NOTE_MMM_LEDGES_AROUND_WELL_4:
            lambda state: True,
        
        # Inside Well (83-89) - Swimming or pumpkin transformation
        LOC_NOTE_MMM_INSIDE_WELL_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_BEAK_BARGE, player) or
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_BEAK_BARGE, player) or
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_BEAK_BARGE, player) or
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_BEAK_BARGE, player) or
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_BEAK_BARGE, player) or
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_BEAK_BARGE, player) or
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_BEAK_BARGE, player) or
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        
        # Inside Mumbo's Skull (90-91) - Flap Flip to reach
        LOC_NOTE_MMM_INSIDE_MUMBOS_SKULL_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MMM_INSIDE_MUMBOS_SKULL_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Inside Tumblar's Shack (92-95) - Breaking into cellar
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        
        # Inside Gutter Barrel (96-100) - Pumpkin transformation
        LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_1:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_2:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_3:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_4:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_GUTTER_BARREL_5:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),

        #RBB Notes
# Rusty Bucket Bay Notes (1-100)
        
        # Gangplank (1-5) - Entry area
        LOC_NOTE_RBB_GANGPLANK_1:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_2:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_3:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_4:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_5:
            lambda state: True,
        
        # Ramp Aft Deck (6-9) - On ship deck
        LOC_NOTE_RBB_RAMP_AFT_DECK_1:
            lambda state: True,
        LOC_NOTE_RBB_RAMP_AFT_DECK_2:
            lambda state: True,
        LOC_NOTE_RBB_RAMP_AFT_DECK_3:
            lambda state: True,
        LOC_NOTE_RBB_RAMP_AFT_DECK_4:
            lambda state: True,
        
        # Aft Deck (10-15) - Rear deck area
        LOC_NOTE_RBB_AFT_DECK_1:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_2:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_3:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_4:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_5:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_6:
            lambda state: True,
        
        # Fan Switch Room (16-19) - Inside ship
        LOC_NOTE_RBB_FAN_SWITCH_ROOM_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_FAN_SWITCH_ROOM_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_FAN_SWITCH_ROOM_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_FAN_SWITCH_ROOM_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        
        # Kitchen (20-24) - Oven room with Wonderwing requirement
        LOC_NOTE_RBB_KITCHEN_1:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_RBB_KITCHEN_2:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_RBB_KITCHEN_3:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_RBB_KITCHEN_4:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_RBB_KITCHEN_5:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        
        # Storeroom Shelf (25-29) - Basic access
        LOC_NOTE_RBB_STOREROOM_SHELF_1:
            lambda state: True,
        LOC_NOTE_RBB_STOREROOM_SHELF_2:
            lambda state: True,
        LOC_NOTE_RBB_STOREROOM_SHELF_3:
            lambda state: True,
        LOC_NOTE_RBB_STOREROOM_SHELF_4:
            lambda state: True,
        LOC_NOTE_RBB_STOREROOM_SHELF_5:
            lambda state: True,
        
        # Next To Whistles (30-31) - Near whistle platform
        LOC_NOTE_RBB_NEXT_TO_WHISTLES_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_NEXT_TO_WHISTLES_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Lower Bridge Smokestacks (32-35) - Lower smokestack area
        LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_LOWER_BRIDGE_SMOKESTACKS_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        
        # Upper Bridge Smokestacks (36-39) - Top of smokestacks
        LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_RBB_UPPER_BRIDGE_SMOKESTACKS_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        
        # Bunk Room (40-43) - Barracks room, break window
        LOC_NOTE_RBB_BUNK_ROOM_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_BUNK_ROOM_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_BUNK_ROOM_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_BUNK_ROOM_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Navigation Room (44-47) - Break window
        LOC_NOTE_RBB_NAVIGATION_ROOM_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_RBB_NAVIGATION_ROOM_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_RBB_NAVIGATION_ROOM_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_RBB_NAVIGATION_ROOM_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_EGGS, player)
            ),
        
        # Captain's Bedroom (48-50) - Captain's room
        LOC_NOTE_RBB_CAPTAINS_BEDROOM_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_NOTE_RBB_CAPTAINS_BEDROOM_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_NOTE_RBB_CAPTAINS_BEDROOM_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        
        # Engine Room Right (51-54) - Engine room access
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Engine Room Left (55-58)
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Engine Room Center (59-62)
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_EGGS, player)
            ),
        
        # Grate Above Pink Jinjo (63-66) - Requires platforming
        LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_1:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_2:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_3:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_RBB_GRATE_ABOVE_PINK_JINJO_4:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        
        # TNT Crane Catwalk (67-69) - Boss boom box area
        LOC_NOTE_RBB_TNT_CRANE_CATWALK_1:
            lambda state:
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_TNT_CRANE_CATWALK_2:
            lambda state:
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_TNT_CRANE_CATWALK_3:
            lambda state:
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        
        # Flooded Warehouse (70-73) - Underwater warehouse
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        
        # Around Snacker's Pool (74-78) - Toxic water area
        LOC_NOTE_RBB_AROUND_SNACKERS_POOL_1:
            lambda state: True,
        LOC_NOTE_RBB_AROUND_SNACKERS_POOL_2:
            lambda state: True,
        LOC_NOTE_RBB_AROUND_SNACKERS_POOL_3:
            lambda state: True,
        LOC_NOTE_RBB_AROUND_SNACKERS_POOL_4:
            lambda state: True,
        LOC_NOTE_RBB_AROUND_SNACKERS_POOL_5:
            lambda state: True,
        
        # Toxic Waste Barrel (79-81) - Toxic drum area
        LOC_NOTE_RBB_TOXIC_WASTE_BARREL_1:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_RBB_TOXIC_WASTE_BARREL_2:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_RBB_TOXIC_WASTE_BARREL_3:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        
        # Toxic Waste Crane (82-84) - Crane area
        LOC_NOTE_RBB_TOXIC_WASTE_CRANE_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_TOXIC_WASTE_CRANE_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_TOXIC_WASTE_CRANE_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        
        # Warehouse Crate 1 (85-92) - Shipping crates
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_1:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_2:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_3:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_4:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_5:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_6:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_7:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_1_8:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_CLIMB, player)
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        
        # Warehouse Crate 3 (93-96) - Middle crate
        LOC_NOTE_RBB_WAREHOUSE_CRATE_3_1:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_3_2:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_3_3:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_WAREHOUSE_CRATE_3_4:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        
        # Anchor Switch Room (97-100) - Underwater anchor room
        LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_RBB_ANCHOR_SWITCH_ROOM_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),

        #CCW Notes

        # Click Clock Wood Notes

        # Outside Spring Entrance (1-4) - Basic entry area
        LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_1:
            lambda state: True,
        LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_2:
            lambda state: True,
        LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_3:
            lambda state: True,
        LOC_NOTE_CCW_OUTSIDE_SPRING_ENTRANCE_4:
            lambda state: True,

        # Spring Gobi's Garden (1-4) - Ground level
        LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_1:
            lambda state: True,
        LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_2:
            lambda state: True,
        LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_3:
            lambda state: True,
        LOC_NOTE_CCW_SPRING_GOBIS_GARDEN_4:
            lambda state: True,

        # Spring Bridge Gobi's (1-3) - Elevated bridge
        LOC_NOTE_CCW_SPRING_BRIDGE_GOBIS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SPRING_BRIDGE_GOBIS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SPRING_BRIDGE_GOBIS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),

        # Spring Bridge Flooded (1-3) - Same as bridge
        LOC_NOTE_CCW_SPRING_BRIDGE_FLOODED_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SPRING_BRIDGE_FLOODED_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SPRING_BRIDGE_FLOODED_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),

        # Spring High Wall Mumbos (1-3) - Higher walls, need vertical movement
        LOC_NOTE_CCW_SPRING_HIGH_WALL_MUMBOS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_CCW_SPRING_HIGH_WALL_MUMBOS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_CCW_SPRING_HIGH_WALL_MUMBOS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),

        # Spring Low Wall Mumbos (1-3) - Lower walls, easier access
        LOC_NOTE_CCW_SPRING_LOW_WALL_MUMBOS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SPRING_LOW_WALL_MUMBOS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SPRING_LOW_WALL_MUMBOS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),

        # Summer Leaves Entryway (1-2) - On leaves at entry
        LOC_NOTE_CCW_SUMMER_LEAVES_ENTRYWAY_1:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CCW_SUMMER_LEAVES_ENTRYWAY_2:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),

        # Summer Gnawty's Entryway (1-2) - Near Gnawty's area
        LOC_NOTE_CCW_SUMMER_GNAWTYS_ENTRYWAY_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SUMMER_GNAWTYS_ENTRYWAY_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),

        # Summer Bridge Zubbas (1-3) - Bridge near bee hive
        LOC_NOTE_CCW_SUMMER_BRIDGE_ZUBBAS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SUMMER_BRIDGE_ZUBBAS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SUMMER_BRIDGE_ZUBBAS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),

        # Summer Treehouse (1-4) - Inside/around treehouse
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),

        # Summer Unfinished Nabnuts (1-5) - Near Nabnut's unfinished house
        LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_CCW_SUMMER_UNFINISHED_NABNUTS_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),

        # Autumn Snarebear Mumbos (1-3) - Near Snarebear and Mumbo's
        LOC_NOTE_CCW_AUTUMN_SNAREBEAR_MUMBOS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_SNAREBEAR_MUMBOS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_SNAREBEAR_MUMBOS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_WONDERWING, player)
            ),

        # Autumn Lower Path Tree (1-16) - Lower tree paths in Autumn
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_7:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_8:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_9:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_10:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_11:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_12:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_13:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_14:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_15:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_PATH_TREE_16:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),

        # Autumn Inside Mumbos (1-4) - Inside Mumbo's skull
        LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_CCW_AUTUMN_INSIDE_MUMBOS_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),

        # Autumn Behind Gobis (1-5) - Behind Gobi's area
        LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_BEHIND_GOBIS_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),

        # Autumn Snarebear Gobis (1-3) - Near Snarebear and Gobi
        LOC_NOTE_CCW_AUTUMN_SNAREBEAR_GOBIS_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_SNAREBEAR_GOBIS_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_SNAREBEAR_GOBIS_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_WONDERWING, player)
            ),

        # Autumn Gnawty's Shelf (1-2) - Near Gnawty's shelf
        LOC_NOTE_CCW_AUTUMN_GNAWTYS_SHELF_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_CCW_AUTUMN_GNAWTYS_SHELF_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),

        # Autumn Zubba's Hive (1-4) - Inside bee hive
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),

        # Autumn Nabnut's Shelf (1-3) - Near Nabnut's shelf
        LOC_NOTE_CCW_AUTUMN_NABNUTS_SHELF_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_CCW_AUTUMN_NABNUTS_SHELF_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_CCW_AUTUMN_NABNUTS_SHELF_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),

        # Autumn Eyrie's Nest (1-8) - Near/at Eyrie's nest (requires reaching Eyrie)
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_1:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_2:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_3:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_4:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_5:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_6:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_7:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_8:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),

        # Winter Branches Sir Slush (1-4) - On branches, requires flight
        LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_CCW_WINTER_BRANCHES_SIR_SLUSH_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),

        # Winter Treehouse Roof (1-4) - On treehouse roof
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_TALON_TROT, player) and
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    ) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_TALON_TROT, player) and
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    ) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_TALON_TROT, player) and
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    ) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_TALON_TROT, player) and
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    ) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),

        # Winter Platform Sir Slush (1-4) - Platform near Sir Slush
        LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_CCW_WINTER_PLATFORM_SIR_SLUSH_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),

        # Winter Highest Platforms (1-4) - Highest platforms in winter
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_DEFEAT_GRUNTILDA:
            lambda state: True,
    }
