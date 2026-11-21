---
name: compare-flight-options
description: Compare flight options on total journey time and total cost rather than the headline fare. Use when the user wants to choose between several flight options.
domain: travel-lifestyle
tags: [flights, comparison, journey]
triggers: ["compare flight options", "which flight is actually faster or cheaper", "layover versus direct flight comparison"]
---

# Compare flight options on total journey time and total cost rather than the headline fare

## Purpose

Compare flight options on total journey time and total cost rather than the headline fare.

## When to use

Use when the user wants to choose between several flight options.

## When NOT to use

Do not use this for a single booking confirmation; use communication instead.

## Inputs required

- The dates, the budget and the travellers
- The origin, destination and the constraints
- The documents, visas and booking status

## Procedure

1. List each option with its departure and arrival times in local time.
2. Add the layover duration for every itinerary that has one.
3. Compute the door-to-door travel time for each option, not just the flight duration.
4. Add bags, seats and transport to and from the airports to the fare.
5. Rank the options by the user's priority, either time, cost or number of stops.

## Output contract

An itinerary with timings, bookings, local logistics and a document checklist.

## Validation checklist

- [ ] Times and transfer windows are feasible
- [ ] Every document requirement is checked
- [ ] The budget covers the booked items

## Safety notes

Never assume visa or entry rules are current; point the traveller to the official source and tell them to verify.

## Related skills

- `prepare-for-a-long-haul-flight`
- `apply-for-a-travel-visa`
- `arrange-travel-for-a-group`
