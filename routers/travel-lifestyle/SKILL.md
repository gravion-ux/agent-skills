---
name: router-travel-lifestyle
description: Route work in the Travel and lifestyle planning domain to the right leaf skill. Use when a task clearly belongs to travel-lifestyle.
domain: travel-lifestyle
tags: [router, routing, travel-lifestyle]
triggers: ["route a travel-lifestyle task", "which travel-lifestyle skill should I use"]
---

# Travel and lifestyle planning router

## Purpose

List every leaf skill in the travel-lifestyle domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside travel-lifestyle and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a single booking confirmation; use communication instead.

## Inputs required

- The dates, the budget and the travellers
- The origin, destination and the constraints
- The documents, visas and booking status

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

An itinerary with timings, bookings, local logistics and a document checklist.

## Validation checklist

- [ ] Times and transfer windows are feasible
- [ ] Every document requirement is checked
- [ ] The budget covers the booked items

## Safety notes

Never assume visa or entry rules are current; point the traveller to the official source and tell them to verify.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `apply-for-a-travel-visa` | Use when the user needs to apply for a visa for travel to another country. |
| `arrange-travel-for-a-group` | Use when the user is organising travel for several people at once. |
| `book-accommodation-that-fits` | Use when the user wants to choose and book a place to stay. |
| `choose-travel-insurance` | Use when the user wants to buy travel insurance for an upcoming trip. |
| `compare-flight-options` | Use when the user wants to choose between several flight options. |
| `find-local-food-and-markets` | Use when the user wants to find somewhere genuine to eat or shop in a new place. |
| `handle-a-missed-connection` | Use when the user has missed a flight, train or connecting transport. |
| `pack-a-carry-on-bag` | Use when the user wants to pack for a trip using only cabin baggage. |
| `plan-a-budget-travel-route` | Use when the user wants to travel on a tight budget over a longer route. |
| `plan-a-safe-transit-day` | Use when the user wants to get from one place to another across a day in an unfamiliar city. |
| `plan-a-solo-travel-safety-check` | Use when the user is travelling alone and wants to check they are prepared. |
| `plan-a-trip-itinerary` | Use when the user wants a day-by-day plan for a trip they are about to take. |
| `plan-an-accessible-itinerary` | Use when the user needs a trip plan that works for someone with mobility or sensory needs. |
| `prepare-for-a-long-haul-flight` | Use when the user has a flight of several hours or more ahead of them. |
| `rent-a-car-for-a-road-trip` | Use when the user wants to hire a car for a self-drive journey. |
| `travel-overnight-by-train` | Use when the user wants to travel overnight by train and save a night's accommodation. |
| `travel-with-a-newborn` | Use when the user wants to travel with a very young baby. |
| `write-a-travel-postcard-summary` | Use when the user wants to share a short reflection about a trip they just took. |
