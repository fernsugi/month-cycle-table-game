# Month Cycle Table Rulebook

This document describes the finished rules used by the current version of the game.

## 1. Overview

Month Cycle Table is a 4-player draw-discard card game built around a 96-card custom deck.

Core flow:

- each player normally holds `5` total cards
- on your turn, you draw to `6`
- if those `6` cards form at least one legal winning pattern, you may win
- otherwise you discard back to `5`
- other players may claim that discard in priority order
- scoring can combine multiple valid 6-card winning patterns

The game is built around:

- `Month`: `1` to `12`
- `Color`: `G`, `R`, `Y`, `K`, `B`, `W`
- `Wind`: `N`, `S`, `E`, `W`
- each month-color card has a unique month-color identity
- each wind-color card has a unique wind-color identity and no month

## 2. Components

The deck has `96` unique cards.

### 2.1 Month Cards (72 cards)

Each month card has:

- a month from `1` to `12`
- a color: `G`, `R`, `Y`, `K`, `B`, or `W`

Month order is linear and does not wrap. Month `12` and month `1` are not neighboring or consecutive.

Deck structure:

- months repeat every `12` cards
- the `72` month cards cover all `12` months across all `6` colors: `G`, `R`, `Y`, `K`, `B`, `W`
- each month appears exactly `6` times in the deck
- each color appears exactly `12` times among month cards

### 2.2 Wind Cards (24 cards)

Each wind card has:

- a wind: `N` (North), `S` (South), `E` (East), or `W` (West)
- a color: `G`, `R`, `Y`, `K`, `B`, or `W`
- **no month**

Wind cards participate in color-based requirements but cannot satisfy month-based requirements.

## 3. Players, Seats, and Dealer

The game uses exactly `4` players:

- East
- South
- West
- North

At the start of a new match:

- all players begin with `18` points
- a random dealer is chosen
- that dealer becomes `East`

**Seat wind (home wind):**

- East player's home wind is `E`
- South player's home wind is `S`
- West player's home wind is `W`
- North player's home wind is `N`

Dealer rule:

- if East wins the hand, East remains dealer for the next hand
- otherwise dealer passes to the next player

East starts each hand, but East does not receive a special scoring bonus.

## 4. Match Structure

A match lasts up to `12` rounds.

Round flow:

- rounds are numbered `1` through `12`
- after round `12`, if one player leads, the match ends
- if round `12` ends in a tie for first, the game enters sudden death
- sudden death continues until the tie breaks

Early match end:

- if any player falls to `0` points or below, the match ends immediately

## 5. Hand Setup

At the start of each hand:

- shuffle all `96` cards
- deal `5` cards to each player
- the remaining `76` cards become the wall
- East takes the first turn

## 6. Hand Structure

Each player has:

- a concealed hand
- an open area

For win checking, a player's total hand is:

- concealed cards + open cards

Important:

- only concealed cards may be discarded
- open cards stay face-up and locked for the rest of the hand
- before drawing or claiming, a player should normally have `5` total cards
- after drawing or claiming, they temporarily have `6`

## 7. Turn Flow

On your turn:

1. Draw `1` card from the wall.
2. You now have `6` total cards.
3. If the 6-card hand forms a legal winning pattern, you may declare `tsumo`.
4. If you do not win, discard `1` concealed card.
5. Other players may respond to that discard.
6. If no claim succeeds, the next player takes a turn.

A player may pass a legal `tsumo` and keep playing.

## 8. Claims

After a discard, claims are checked in this order:

1. `ron`
2. `kan`
3. `pon`
4. `chi`

If a higher-priority claim succeeds, lower-priority claims do not happen.

### 8.1 Ron

`Ron` means winning on another player's discard.

Rules:

- if adding the discarded card to your current total hand creates a legal winning 6-card pattern, you may `ron`
- multiple players may `ron` the same discard
- each `ron` winner is paid separately by the discarder

### 8.2 Chi

`Chi` is not a sequence claim in this game.

Rules:

- only the next player in turn order may `chi`
- no sequence is required
- `chi` simply takes the discarded card and places it into your open area
- after `chi`, you must discard one concealed card

Because `chi` opens exactly one visible card, it is the smallest way to build gear.

### 8.3 Pon

`Pon` is month-based for month cards and wind-based for wind cards.

Rules for month cards:

- you may `pon` only if you already have exactly `3` cards of the same month as the discard across your concealed and open cards
- all of those same-month cards, plus the claimed discard, become open
- after `pon`, you must discard one concealed card

Rules for wind cards:

- you may `pon` only if you already have exactly `3` cards of the same wind as the discard across your concealed and open cards
- all of those same-wind cards, plus the claimed discard, become open
- after `pon`, you must discard one concealed card

In practice, `pon` creates an open block of `4` visible cards.

### 8.4 Kan

`Kan` is also month-based for month cards and wind-based for wind cards.

Rules for month cards:

- you may `kan` only if you already have exactly `4` cards of the same month as the discard across your concealed and open cards
- all of those same-month cards, plus the claimed discard, become open
- after `kan`, you must discard one concealed card

Rules for wind cards:

- you may `kan` only if you already have exactly `4` cards of the same wind as the discard across your concealed and open cards
- all of those same-wind cards, plus the claimed discard, become open
- after `kan`, you must discard one concealed card

In practice, `kan` creates an open block of `5` visible cards.

### 8.5 Self Kan

On your own turn, you may also declare a `self kan`.

Rules for month cards:

- if your concealed hand contains `5` cards of the same month, you may open them immediately as a `kan`
- after `self kan`, you must discard `1` concealed card

Rules for wind cards:

- if your concealed hand contains `5` cards of the same wind, you may open them immediately as a `kan`
- after `self kan`, you must discard `1` concealed card

In practice, `self kan` converts a concealed 5-card block into an open 5-card block without needing an opponent discard.

## 9. Wind Discard Rules

### 9.1 Home Wind Discard

When you discard your **home wind** (the wind matching your seat):

- `ron` is checked first
- if no player wins by `ron`, you **may** choose to move one concealed card from your hand to your open area
- if you do, that opened card is placed face-up before `kan`, `pon`, or `chi` respond to the discarded wind
- opponents may claim the discarded wind card via `ron`, `kan`, `pon`, or `chi`
- opponents **may not** claim the card you just opened
- if you have no concealed cards other than the wind you are discarding, you may skip the optional open

### 9.2 Matching Card Discard

When you discard a card and still have another concealed card with the same group:

- same group means the same month number for month cards
- same group means the same wind for wind cards
- `ron` is checked first
- if no player wins by `ron`, you **may** choose to move one matching concealed card from your hand to your open area
- only a matching concealed card may be opened this way
- the opened matching card is placed face-up before `kan`, `pon`, or `chi` respond to the discarded card
- opponents may claim the discarded card via `ron`, `kan`, `pon`, or `chi`
- opponents **may not** claim the card you just opened

Examples:

- if you discard a month `7` and still hold another month `7`, you may open one held month `7`
- if you discard `N` and still hold another `N`, you may open one held `N`
- if you discard a month `7`, you may not open a month `5`

### 9.3 Guest Wind Discard

When you discard a wind card that is **not** your home wind:

- the discard proceeds normally
- no additional effects apply

## 10. Winning

There are two win methods:

- `Tsumo`: win on your own draw
- `Ron`: win on another player's discard

A winning hand is always exactly `6` total cards.

If a 6-card hand matches more than one pattern:

- remove any pattern that fails the gear rule
- each remaining valid pattern contributes its low-gear/base scoring value
- apply the gear upgrade from the strongest remaining pattern once
- add round month, home wind, `Rainbow`, `Prism`, `Overture`, `Finale`, and `tsumo` bonuses after pattern scoring

Low-gear/base scoring value means:

- `3pt` patterns contribute `3pt`
- `6pt` patterns contribute `3pt`
- `9pt` patterns contribute `3pt`
- `12pt` patterns contribute `6pt`
- `15pt` patterns contribute `9pt`

Named upgrade patterns suppress their component versions when they describe the same hand, such as `Mono Compass` suppressing `Mono` and `Compass`.

### 10.1 Wind Card Pattern Restrictions

Wind cards have **no month**. Therefore, wind cards cannot be used in any pattern that requires month properties, including:

- Skip
- Run
- Triple Pair
- Parity Pairs
- Twin Triples
- Parity Triples
- Escort
- Split Escort
- Mono Skip
- Mono Run

Wind cards **can** be used in `Mono` (all same color), `Cross`, `Twin Tone Pairs`, `Tri Tone Triples`, `Axis`, `Grand Axis`, `Tempest`, `Grand Tempest`, and all wind-specific patterns listed in Section 16.

### 10.2 Exhaustive Draw: Full Gear

`Full Gear` is checked only when the hand ends in an exhaustive draw.

A player is eligible for `Full Gear` if:

- they have exactly `5` open cards

Settlement:

- each non-eligible player pays each eligible player `1pt`
- if no players are eligible, no one pays
- if all players are eligible, the hand is a normal draw and no one pays

## 11. Gear Rule

Gear is based on the literal number of visible open cards in your open area. Some higher-value sets can still score with lower gear, but they score as a smaller point tier until you have enough open cards.

Current gear requirements:

- `3pt` requires at least `3` open cards
- `6pt` requires at least `3` open cards
  - with exactly `3` open cards, it scores `3pt`
  - with `4` or more open cards, it scores the full `6pt`
- `9pt` requires at least `3` open cards
  - with exactly `3` open cards, it scores `3pt`
  - with exactly `4` open cards, it scores `6pt`
  - with `5` open cards, it scores the full `9pt`
- `12pt` is always valid, but gear changes the score
  - with `0` to `3` open cards, it scores `6pt`
  - with exactly `4` open cards, it scores `9pt`
  - with `5` open cards, it scores the full `12pt`
- `15pt` is always valid, but gear changes the score
  - with `0` to `3` open cards, it scores `9pt`
  - with exactly `4` open cards, it scores `12pt`
  - with `5` open cards, it scores the full `15pt`

This applies to both:

- `tsumo`
- `ron`

Examples:

- one `chi` gives `1` open card
- two `chi` claims give `2` open cards
- one `pon` usually gives `4` open cards
- one `kan` usually gives `5` open cards
- a home wind discard with optional open gives `1` open card
- a matching-card discard with optional open gives `1` open card

## 12. Round Bonus

Each round has a target month equal to the round number.

Examples:

- round `1` targets month `1`
- round `5` targets month `5`
- round `12` targets month `12`

Bonus rule:

- if you win in round `N`
- and your final winning 6-card hand contains month `N`
- you gain `+3` points once

Important:

- the bonus applies only once per winning hand
- it applies to both `tsumo` and `ron`
- it can raise a `15pt` hand to `18pt`
- sudden death rounds do not have a numbered month target

## 13. Home Wind Bonus

If your winning 6-card hand contains your **home wind** (the wind matching your seat), you gain `+3` points once.

Important:

- the bonus applies only once per winning hand
- it applies to both `tsumo` and `ron`
- it stacks with the round month bonus
- a `15pt` hand with both bonuses scores `21pt`

## 14. Additional Winning Bonuses

### 14.1 Rainbow

`Rainbow` is a `+3pt` winning bonus.

You gain `Rainbow` when:

- you win by `tsumo`
- your final winning 6-card hand contains all `6` colors
- all `6` final cards have different month/wind identities

### 14.2 Prism

`Prism` is a `+3pt` winning bonus.

You gain `Prism` when:

- you have exactly `5` open cards
- your final winning 6-card hand contains all `6` colors
- all `6` final cards have different month/wind identities

Important:

- `Rainbow` and `Prism` can stack with each other
- both stack with `tsumo`, round month, and home wind bonuses
- they are bonuses, not winning patterns

### 14.3 Overture

`Overture` is a `+3pt` winning bonus.

You gain `Overture` when:

- you win by `tsumo`
- the winning hand is your initial hand plus your first draw
- you have not discarded yet this hand
- you have no open cards

Because `Overture` happens before your first discard, it is always a `tsumo` bonus.

### 14.4 Finale

`Finale`is a `+3pt` winning bonus.

You gain `Finale` when:

- the wall has exactly `0` cards at the moment of winning
- this may be a `tsumo` on the last draw
- or it may be a `ron` on the discard made after the last draw

Important:

- `Overture` and `Finale` stack with other winning bonuses
- they are bonuses, not winning patterns

## 15. Settlement

### 15.1 Tsumo

On `tsumo`:

- the hand gains a `+3pt` `tsumo` bonus
- the winner gains the hand's full value
- the other `3` players each pay one third of that value

Because all legal totals are divisible by `3`, settlement is always clean.

Examples:

- `3pt` hand by tsumo: total `6pt`; each opponent pays `2`
- `12pt` hand by tsumo: total `15pt`; each opponent pays `5`
- `18pt` hand by tsumo: total `21pt`; each opponent pays `7`
- `21pt` hand by tsumo: total `24pt`; each opponent pays `8`

### 15.2 Ron

On `ron`:

- the discarder pays the full value
- the winner gains the full value

### 15.3 Multiple Ron

If multiple players `ron` the same discard:

- each winner scores separately
- the discarder pays each winner in full

## 16. Winning Patterns

All patterns below use exactly `6` cards.

### 16.1 3-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Mono | All 6 cards share one color | At least 3 open cards |
| Skip | All 6 cards are all odd months or all even months, all 6 months are different, and all 6 colors are different | At least 3 open cards |
| Run | Six consecutive months, all in different colors | At least 3 open cards |
| Wind | All 6 cards are wind cards, with all 6 colors present | At least 3 open cards |
| Cross | Month 1, month 12, and all four winds N, S, E, W, with all 6 colors present | At least 3 open cards |

### 16.2 6-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Triple Pair | 3 pairs from 3 consecutive months | 3 open cards scores 3pt; 4+ open cards scores 6pt |
| Wind Pairs | 3 pairs from 3 different winds | 3 open cards scores 3pt; 4+ open cards scores 6pt |
| Axis | Either: 2 of your seat wind plus 4 of the current round month; or 4 of your seat wind plus 2 of the current round month | 3 open cards scores 3pt; 4+ open cards scores 6pt |
| Twin Tone Pairs | 3 pairs from 3 different month or wind identities, using at most 2 colors total | 3 open cards scores 3pt; 4+ open cards scores 6pt |
| Parity Pairs | 3 pairs from 3 different months, all odd or all even | 3 open cards scores 3pt; 4+ open cards scores 6pt |

### 16.3 9-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Twin Triples | 3 cards of one month and 3 cards of a consecutive month | 3 open cards scores 3pt; 4 open cards scores 6pt; 5 open cards scores 9pt |
| Wind Triples | 3 cards of one wind and 3 cards of another wind | 3 open cards scores 3pt; 4 open cards scores 6pt; 5 open cards scores 9pt |
| Grand Axis | 3 of your seat wind plus 3 of the current round month | 3 open cards scores 3pt; 4 open cards scores 6pt; 5 open cards scores 9pt |
| Tri Tone Triples | 3 cards of one month or wind identity and 3 cards of another month or wind identity, using at most 3 colors total | 3 open cards scores 3pt; 4 open cards scores 6pt; 5 open cards scores 9pt |
| Parity Triples | 3 cards of one month and 3 cards of another month, all odd or all even | 3 open cards scores 3pt; 4 open cards scores 6pt; 5 open cards scores 9pt |

### 16.4 12-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Crown | Either: 5 of one month plus 1 neighboring month with all 6 colors present; or 6 of one month with all 6 colors present | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |
| Tempest | All 6 cards are the same wind, as long as it is not your seat wind | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |
| Escort | 4 of one month plus 2 matching cards from either the previous or next month, with all 6 colors present | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |
| Split Escort | 4 of one month plus 1 previous and 1 next month, with all 6 colors present | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |
| Compass | Either: four same-color N, S, E, W plus any month pair or 2-card month sequence; or four same-color consecutive months plus 2 same-color winds | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |

### 16.5 15-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Mono Skip | All 6 cards share one color and are all odd months or all even months | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |
| Mono Run | Six different months in order, all sharing one color | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |
| Grand Crown | All 6 cards are the current round month | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |
| Grand Tempest | All 6 cards are your seat wind | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |
| Mono Compass | Either compass shape, with all 6 cards sharing one color | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |

Notes on the 15-point patterns:

- `Skip` means all odd months or all even months, with all 6 colors and all 6 months different.
- `Run` means a 6-month consecutive run with all 6 colors present.
- `Mono Skip` means a `Skip` played in a single color lane.
- `Grand Crown` means collecting all 6 cards of the round's target month. In sudden death there is no target month, so `Grand Crown` is unavailable.
- `Axis` means mixing your seat wind with the round's target month in a `2+4` or `4+2` split.
- `Grand Axis` means a `3+3` split between your seat wind and the round's target month.
- `Tempest` means all 6 cards are the same wind, as long as it is not your seat wind.
- `Grand Tempest` means all 6 cards are your seat wind.
- `Compass` has two shapes. Wind Compass uses all four winds in one color plus either any month pair or any 2-month sequence. Month Compass uses four consecutive months in one color plus 2 winds that share a color.
- `Mono Compass` uses either Compass shape, but all 6 cards must share one color.

## 17. End of Hand

A hand ends when:

- a player wins by `tsumo`
- one or more players win by `ron`
- the wall is exhausted

If the wall is exhausted:

- the hand is a draw
- no one scores
- dealer rotates normally unless East had won before the draw, which did not happen

## 18. End of Match

The match ends when one of these happens:

- a player falls to `0` or below
- round `12` ends and one player is alone in first place
- sudden death ends with one player alone in first place

If round `12` ends tied for first:

- no one wins the match yet
- play continues in sudden death rounds until the tie breaks

## 19. Practical Notes

- Odd/even patterns use the visible month number parity.
- The month labels are numeric `1` to `12`.
- Month order does not wrap; month `12` and month `1` are not neighbors.
- The color labels are abbreviated: `G`, `R`, `Y`, `K`, `B`, `W`.
- The wind labels are abbreviated: `N`, `S`, `E`, `W`.
- Open-card count matters a lot because of gear. A beautiful hand may still be invalid if it does not meet the required visible open count for its point tier.
- Wind cards have no month and therefore cannot satisfy requirements for month sequence, month consecutiveness, or month parity.
