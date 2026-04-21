# Month Cycle Table Rulebook

This document describes the finished rules used by the current version of the game.

## 1. Overview

Month Cycle Table is a 4-player draw-discard card game built around a 72-card custom deck.

Core flow:

- each player normally holds `5` total cards
- on your turn, you draw to `6`
- if those `6` cards form a legal winning pattern, you may win
- otherwise you discard back to `5`
- other players may claim that discard in priority order
- scoring uses exactly one 6-card winning pattern

The game is built around:

- `Month`: `1` to `12`
- `Color`: `G`, `R`, `Y`, `K`, `B`, `W`
- each card's unique month-color identity

## 2. Components

The deck has `72` unique cards.

Each card has:

- a month from `1` to `12`
- a color: `G`, `R`, `Y`, `K`, `B`, or `W`

Deck structure:

- months repeat every `12` cards
- the first `60` cards use the original five colors: `G`, `R`, `Y`, `K`, `B`
- the final `12` cards are white cards
- each month appears exactly `6` times in the deck
- each color appears exactly `12` times in the deck

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

- shuffle all `72` cards
- deal `5` cards to each player
- the remaining `52` cards become the wall
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

`Pon` is month-based.

Rules:

- you may `pon` only if you already have exactly `3` cards of the same month as the discard across your concealed and open cards
- all of those same-month cards, plus the claimed discard, become open
- after `pon`, you must discard one concealed card

In practice, `pon` creates an open month block of `4` visible cards.

### 8.4 Kan

`Kan` is also month-based.

Rules:

- you may `kan` only if you already have exactly `4` cards of the same month as the discard across your concealed and open cards
- all of those same-month cards, plus the claimed discard, become open
- after `kan`, you must discard one concealed card

In practice, `kan` creates an open month block of `5` visible cards.

### 8.5 Self Kan

On your own turn, you may also declare a `self kan`.

Rules:

- if your concealed hand contains `5` cards of the same month, you may open them immediately as a `kan`
- after `self kan`, you must discard `1` concealed card

In practice, `self kan` converts a concealed 5-card month into an open 5-card month block without needing an opponent discard.

## 9. Winning

There are two win methods:

- `Tsumo`: win on your own draw
- `Ron`: win on another player's discard

A winning hand is always exactly `6` total cards.

If a 6-card hand matches more than one pattern:

- remove any pattern that fails the gear rule
- from the remaining valid patterns, apply any gear-based point reduction
- use the highest-point result after gear is applied

## 10. Gear Rule

Gear is based on the literal number of visible open cards in your open area. Some higher-value sets can still score with lower gear, but they score as a smaller point tier until you have enough open cards.

Current gear requirements:

- `3pt` requires at least `3` open cards
- `6pt` requires at least `2` open cards
  - with exactly `2` open cards, it scores `3pt`
  - with `3` or more open cards, it scores the full `6pt`
- `9pt` requires at least `1` open card
  - with exactly `1` open card, it scores `3pt`
  - with exactly `2` open cards, it scores `6pt`
  - with `3` or more open cards, it scores the full `9pt`
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

## 11. Round Bonus

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

## 12. Settlement

### 12.1 Tsumo

On `tsumo`:

- the winner gains the hand's full value
- the other `3` players each pay one third of that value

Because all legal totals are divisible by `3`, settlement is always clean.

Examples:

- `3pt` tsumo: each opponent pays `1`
- `12pt` tsumo: each opponent pays `4`
- `18pt` tsumo: each opponent pays `6`

### 12.2 Ron

On `ron`:

- the discarder pays the full value
- the winner gains the full value

### 12.3 Multiple Ron

If multiple players `ron` the same discard:

- each winner scores separately
- the discarder pays each winner in full

## 13. Winning Patterns

All patterns below use exactly `6` cards.

### 13.1 3-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Mono | All 6 cards share one color | At least 3 open cards |
| Skip | All 6 cards are all odd months or all even months, all 6 months are different, and all 6 colors are different | At least 3 open cards |
| Run | Six different months in order; if any of those cards are open, the open months must also be consecutive within the run | At least 3 open cards |

### 13.2 6-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Triple Pair | 3 pairs from 3 consecutive months | 2 open cards scores 3pt; 3+ open cards scores 6pt |
| Twin Tone Pairs | 3 pairs from 3 different months, using at most 2 colors total | 2 open cards scores 3pt; 3+ open cards scores 6pt |
| Parity Pairs | 3 pairs from 3 different months, all odd or all even | 2 open cards scores 3pt; 3+ open cards scores 6pt |

### 13.3 9-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Twin Triples | 3 cards of one month and 3 cards of a consecutive month | 1 open card scores 3pt; 2 open cards scores 6pt; 3+ open cards scores 9pt |
| Tri Tone Triples | 3 cards of one month and 3 cards of another month, using at most 3 colors total | 1 open card scores 3pt; 2 open cards scores 6pt; 3+ open cards scores 9pt |
| Parity Triples | 3 cards of one month and 3 cards of another month, all odd or all even | 1 open card scores 3pt; 2 open cards scores 6pt; 3+ open cards scores 9pt |

### 13.4 12-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Crown | 5 of one month plus 1 neighboring month, or 6 of one month, with all 6 colors present | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |
| Escort | 4 of one month plus 2 matching cards from either the previous or next month, with all 6 colors present | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |
| Split Escort | 4 of one month plus 1 previous and 1 next month, with all 6 colors present | 0-3 open cards scores 6pt; 4 open cards scores 9pt; 5 open cards scores 12pt |

### 13.5 15-point patterns

| Pattern | Requirement | Gear |
| --- | --- | --- |
| Mono Skip | All 6 cards share one color and are all odd months or all even months | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |
| Mono Run | Six different months in order, all sharing one color | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |
| Round Crown | All 6 cards are the current round month | 0-3 open cards scores 9pt; 4 open cards scores 12pt; 5 open cards scores 15pt |

Notes on the 15-point patterns:

- `Skip` means all odd months or all even months, with all 6 colors and all 6 months different.
- `Run` means a 6-month consecutive run.
- `Mono Skip` means a `Skip` played in a single color lane.
- `Round Crown` means collecting all 6 cards of the round's target month. In sudden death there is no target month, so this pattern is unavailable.
- Only `Run` requires any open cards inside that pattern to form a consecutive block of months within the completed run.

## 14. End of Hand

A hand ends when:

- a player wins by `tsumo`
- one or more players win by `ron`
- the wall is exhausted

If the wall is exhausted:

- the hand is a draw
- no one scores
- dealer rotates normally unless East had won before the draw, which did not happen

## 15. End of Match

The match ends when one of these happens:

- a player falls to `0` or below
- round `12` ends and one player is alone in first place
- sudden death ends with one player alone in first place

If round `12` ends tied for first:

- no one wins the match yet
- play continues in sudden death rounds until the tie breaks

## 16. Practical Notes

- Odd/even patterns use the card's hidden deck position parity. Each month contains both odd and even cards.
- The month labels are numeric `1` to `12`.
- The color labels are abbreviated: `G`, `R`, `Y`, `K`, `B`, `W`.
- Open-card count matters a lot because of gear. A beautiful hand may still be invalid if it does not meet the required visible open count for its point tier.
