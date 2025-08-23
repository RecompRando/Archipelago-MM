known_logic_tricks = {
    # General tricks

    'Earlygame Hard Combat': {
        'name'    : 'logic_hard_combat',
        'tooltip' : '''\
                    Allows killing the Dodongo and Peahat grottos
                    with only Deku Sticks. An experienced player
                    can do this, but it's not free.
                    '''},
    'Stock Pot Inn at Night with Nothing': {
        'name'    : 'logic_stockpot_night',
        'tooltip' : '''\
                    Allows entering Stock Pot Inn at night without 
                    Room Key or Deku Mask. This can be done with a
                    variety of clever jumps or by just playing the
                    Song of Double Time on the upper ledge.
                    '''},
    'Powder Keg as Explosive': {
        'name'    : 'logic_keg_everywhere',
        'tooltip' : '''\
                    Allows using the Powder Keg as a substitute for
                    normal explosives in a variety of mundane situations.
                    This can be very tedious.
                    '''},
    'Postman Game with Nothing': {
        'name'    : 'logic_postman_nobunny',
        'tooltip' : '''\
                    Allows completing the Postman's counting
                    minigame without Bunny Hood. Count 19
                    quarter-turns of the Z-target cursor.
                    '''},
    'Bank Checks without Wallets': {
        'name'    : 'logic_early_bank',
        'tooltip' : '''\
                    Allows checking the items at 500 and
                    1000 rupees in the bank without Wallet
                    upgrades. This is tedious but easy.
                    '''},
    'Goron Pound to Swamp Tour Roof': {
        'name'    : 'logic_goron_swamp_roof',
        'tooltip' : '''\
                    Allows using a Goron ground pound to reach the
                    roof of the Swamp Tour building without the
                    nearby Deku Flower/Land Title Deed.
                    '''},
    'Cross Poisoned Swamp as Goron or Zora': {
        'name'    : 'logic_talltransform_swamp',
        'tooltip' : '''\
                    Allows running through the poisoned swamp as
                    Goron or Zora to reach Swamp Spider House. As
                    specifically Zora, this also allows access to
                    the nearby grotto. This requires taking damage
                    so should not be used with OHKO.
                    '''},
    'Climb Mountain Village Wall with Nothing': {
        'name'    : 'logic_blind_climb',
        'tooltip' : '''\
                    Allows climbing the wall in Mountain Village
                    without the Lens of Truth. This will not grant
                    access to the vanilla Goron Mask check, but it
                    can allow for Hot Spring Water access.
                    '''},
    'Fewer Lens Requirements': {
        'name'    : 'logic_fewer_lens',
        'tooltip' : '''\
                    Removes several minor Lens of Truth requirements
                    from Path to Snowhead, Snowhead Temple, Ikana
                    Graveyard, and the Ancient Castle of Ikana.
                    '''},
    'Snowhead Temple Final Key Skip': {
        'name'    : 'logic_snowhead_void',
        'tooltip' : '''\
                    Allows skipping the last locked door in Snowhead
                    Temple. This requires either dropping to the bottom
                    and intentionally voiding out as Deku or Zora or,
                    in the worst case, dropping and reclimbing after
                    breaking the pillar. Some pillarless nonsense
                    could work too but is harder than this trick
                    demands.
                    '''},
    'Hot Spring Water on Snowhead Temple 1f': {
        'name'    : 'logic_snowhead_hsw',
        'tooltip' : '''\
                    Allows bringing Hot Spring Water into Snowhead
                    Temple to reach two chests on 1f without Fire
                    Arrows. This is not very fun but not very hard.
                    '''},
    'Pinnacle Rock without Seahorse': {
        'name'    : 'logic_no_seahorse',
        'tooltip' : '''\
                    Allows reaching Pinnacle Rock without following the
                    seahorse. This is actually pretty easy.
                    '''},
    'Zora Hall as Human': {
        'name'    : 'logic_human_zora_hall',
        'tooltip' : '''\
                    Allows swimming to Zora Hall as human. Damage is
                    unavoidable so don't use this with OHKO.
                    '''},
    'Goron Bomb Jumps': {
        'name'    : 'logic_goron_bomb_jump',
        'tooltip' : '''\
                    Allows using the Goron's ground pound and a bomb
                    to jump over short fences. This allows reaching
                    Great Bay and Ikana Graveyard without Epona,
                    entering Oceanside Spider House without Hookshot,
                    and reaching the Astral Observatory without Deku
                    or a projectile.
                    '''},
    'Brute Force Oceanside Spider House Code': {
        'name'    : 'logic_OSH_code',
        'tooltip' : '''\
                    Allows solving the Oceanside Spider House mask
                    code without Captain's Hat.
                    '''},
    'Goron Pound in Zora Hall': {
        'name'    : 'logic_goron_zora_hall',
        'tooltip' : '''\
                    Allows using a Goron ground pound to reach the
                    item in Mikau\'s room without the Mountain
                    Title Deed.
                    '''},
    'Great Bay Temple Skip Frog Miniboss': {
        'name'    : 'logic_gbt_miniboss',
        'tooltip' : '''\
                    Allows some clever Ice Arrows platforming to skip
                    fighting the frog miniboss, removing a Fire Arrows
                    requirement.
                    '''},
    'Climb Ikana Canyon without Ice Arrows': {
        'name'    : 'logic_iceless_ikana',
        'tooltip' : '''\
                    Allows a precise Hookshot usage to ascend Ikana
                    Canyon without Ice Arrows.
                    '''},
    'One Mask Stone Tower Climb': {
        'name'    : 'logic_onemask_stonetower',
        'tooltip' : '''\
                    Allows using Elegy of Emptiness and Hookshot in
                    smart ways to climb Stone Tower with only Goron
                    or Zora Mask, not necessarily both.
                    '''},
    'Inverted Stone Tower Temple Deku Spin to Boss Key Area': {
        'name'    : 'logic_istt_deku',
        'tooltip' : '''\
                    Allows using a Deku spin at a good angle to skip most of
                    Inverted Stone Tower Temple and reach the miniboss from
                    the second room.
                    '''},
    'Inverted Stone Tower Temple Early Eyegore': {
        'name'    : 'logic_istt_eyegore',
        'tooltip' : '''\
                    Allows some very precise Light Arrow and Hookshot usage to
                    defeat the ISTT Eyegore and Hookshot to the chest defeating
                    it spawns from the area near the miniboss.
                    '''},


}

normalized_name_tricks = {trick.casefold(): info for (trick, info) in known_logic_tricks.items()}
