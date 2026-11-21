---
name: plan-a-trip-itinerary
description: Plan a trip itinerary with realistic timings, booked anchors and room to breathe. Use when the user wants a day-by-day plan for a trip they are about to take.
domain: travel-lifestyle
tags: [itinerary, planning, trips]
triggers: ["plan a trip itinerary", "day by day travel plan for my dates", "build a holiday schedule"]
---

# Plan a trip itinerary with realistic timings, booked anchors and room to breathe

## Purpose

Plan a trip itinerary with realistic timings, booked anchors and room to breathe.

## When to use

Use when the user wants a day-by-day plan for a trip they are about to take.

## When NOT to use

Do not use this for a single booking confirmation; use communication instead.

## Inputs required

- The dates, the budget and the travellers
- The origin, destination and the constraints
- The documents, visas and booking status

## Procedure

1. Fix the arrival and departure dates and the fixed commitments inside them.
2. Place the anchor bookings first, then fill the gaps around them.
3. Allow travel time between locations using the realistic local duration.
4. Leave one unscheduled half-day so a delayed day does not ruin the trip.
5. List each item with its booking reference, address and local time zone.

## Output contract

An itinerary with timings, bookings, local logistics and a document checklist.

## Validation checklist

- [ ] Times and transfer windows are feasible
- [ ] Every document requirement is checked
- [ ] The budget covers the booked items

## Safety notes

Never assume visa or entry rules are current; point the traveller to the official source and tell them to verify.

## Related skills

- `plan-a-budget-travel-route`
- `plan-a-safe-transit-day`
- `plan-a-solo-travel-safety-check`
