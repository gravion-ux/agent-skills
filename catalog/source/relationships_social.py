"""Skills for relationships and social skills."""

from __future__ import annotations

from catalog.source._types import spec

DOMAIN = "relationships-social"

SKILLS = (
    spec(
        "write-a-thoughtful-thank-you",
        summary="Write a thank-you that names the specific thing that mattered to the recipient.",
        when="the user wants to thank someone and the message should feel personal rather than generic",
        steps=(
            "Identify the exact action or gift the person did that the user appreciated.",
            "Say what it changed for the user rather than only describing the action.",
            "Keep the message short enough to read in under a minute.",
            "Match the formality of the relationship rather than the formality of the moment.",
            "Leave the draft editable so the user can add a detail that only they know.",
        ),
        tags=("thanks", "writing", "appreciation"),
        triggers=("write a thoughtful thank you", "thank you message for a specific favour", "how to say thanks properly"),
    ),
    spec(
        "apologise-well",
        summary="Apologise in a way that names the harm, takes responsibility and moves forward.",
        when="the user has done something that needs a real apology rather than an excuse",
        steps=(
            "Name the specific thing that went wrong without softening it into vagueness.",
            "Describe the impact on the other person rather than on the user's intent.",
            "Take responsibility directly, with no condition attached to the apology.",
            "State what will change so the apology is not only words.",
            "Offer to make it right and then let the other person decide.",
        ),
        tags=("apology", "repair", "honesty"),
        triggers=("apologise well", "how to apologise for real", "write an apology that lands properly"),
    ),
    spec(
        "set-a-boundary-with-clarity",
        summary="Set a boundary that is specific, said once and does not invite negotiation.",
        when="the user needs to say no, or to limit what they are willing to keep doing",
        steps=(
            "Write the boundary as one plain sentence with a concrete limit in it.",
            "State it without justifying it at length, because justification invites debate.",
            "Name what the user is willing to do instead, if anything.",
            "Plan the exact moment and channel for saying it.",
            "Decide in advance the repeated response if the boundary is tested again.",
        ),
        tags=("boundaries", "assertion", "communication"),
        triggers=("set a boundary with clarity", "how do I say no without over-explaining", "write a clear limit on what I will do"),
    ),
    spec(
        "have-a-hard-conversation-with-someone-close",
        summary="Prepare for a hard conversation with someone close so it ends in clarity rather than damage.",
        when="the user must raise something difficult with a friend, partner or family member",
        steps=(
            "Write the one point the conversation actually needs to resolve.",
            "Separate the facts from the interpretation and keep only the facts.",
            "Rehearse the opening two sentences, because the start sets the tone for the rest.",
            "Decide what the user is willing to change and what they are not.",
            "Plan how to end the conversation, including when to pause and continue later.",
        ),
        tags=("conversation", "conflict", "preparation"),
        triggers=("hard conversation with someone close", "prepare for a difficult talk with a friend", "how to raise a serious issue without a fight"),
    ),
    spec(
        "keep-a-long-distance-friendship",
        summary="Keep a long-distance friendship alive with small, regular contact instead of rare long calls.",
        when="the user wants to maintain a friendship across distance or a busy period",
        steps=(
            "Agree a contact rhythm that both sides can keep without it feeling like an obligation.",
            "Mix short, frequent messages with occasional longer conversations.",
            "Send something specific from the other person's life rather than only reacting to their posts.",
            "Plan the next visit or shared event early so distance has a visible end point.",
            "Let the rhythm change when life changes, and set a new one rather than letting it fade.",
        ),
        tags=("friendship", "distance", "maintenance"),
        triggers=("keep a long distance friendship", "stay in touch with a distant friend", "maintain a friendship over distance"),
    ),
    spec(
        "make-a-new-friend-as-an-adult",
        summary="Make a new friend as an adult through repeated low-pressure contact.",
        when="the user wants to build a new friendship and is unsure how to start as an adult",
        steps=(
            "Choose a setting where the same people return regularly, such as a class or a club.",
            "Talk to one person briefly about something the setting makes obvious.",
            "Suggest a low-commitment second meeting such as a coffee or a walk.",
            "Keep the conversation going by asking about the thing the other person cares about.",
            "Let the relationship grow through repeated contact rather than trying to fast-track it.",
        ),
        tags=("friendship", "networking", "confidence"),
        triggers=("make a new friend as an adult", "how to meet people as an adult", "start a new friendship later in life"),
    ),
    spec(
        "plan-a-friends-meeting",
        summary="Plan a friends meeting that fits everyone's time and ends with a reason to meet again.",
        when="the user wants to organise a get-together that works for a group of friends",
        steps=(
            "Pick a date range and a place rather than a single fixed option.",
            "Ask each person for their constraint directly instead of inferring it.",
            "Choose the option that most people can reach with the least effort.",
            "Set a start and an end time so the meeting does not stretch indefinitely.",
            "Agree the next meet-up before the current one ends.",
        ),
        tags=("planning", "friends", "group"),
        triggers=("plan a friends meeting", "organise a get together with friends", "arrange a group meet-up that works"),
    ),
    spec(
        "handle-a-friendship-slight",
        summary="Handle a small hurt in a friendship by naming it once and checking what it meant.",
        when="the user feels let down or overlooked by a friend and is deciding whether to raise it",
        steps=(
            "Decide whether the event matters enough to raise or should simply be let go.",
            "Describe the specific action that felt wrong, without characterising the friend's motives.",
            "Ask what the friend saw the situation as, because the gap is usually there.",
            "Agree what each side will do differently if the same situation recurs.",
            "Keep the exchange short and do not reopen every past instance.",
        ),
        tags=("friendship", "conflict", "repair"),
        triggers=("handle a friendship slight", "my friend let me down how do I raise it", "resolve a small betrayal between friends"),
    ),
    spec(
        "talk-to-a-parent-about-something-difficult",
        summary="Talk to a parent about something difficult by giving them context and a clear ask.",
        when="the user needs to raise a sensitive topic with a parent or older relative",
        steps=(
            "Decide how much detail the parent needs and what they can actually act on.",
            "Choose a moment when they are rested and not in the middle of something else.",
            "Start with what the parent has already noticed, so the news does not arrive cold.",
            "Make one specific request and be ready for the answer to be no.",
            "Agree what happens next if they need time to think about it.",
        ),
        tags=("family", "conversation", "sensitivity"),
        triggers=("talk to my parent about something difficult", "how to tell my parents hard news", "raise a sensitive topic with a parent"),
    ),
    spec(
        "support-a-friend-in-crisis",
        summary="Support a friend in crisis by staying present, listening well and connecting them to help.",
        when="the user is worried about a friend who is in emotional or mental distress",
        steps=(
            "Contact the friend soon and keep the contact regular rather than waiting for them to reply.",
            "Listen without fixing, arguing or offering solutions the friend did not ask for.",
            "Ask plainly and directly whether they are thinking about harming themselves.",
            "Help them reach professional support and offer to go with them or make the call.",
            "Agree a check-in plan and involve another trusted person if the risk seems high.",
        ),
        tags=("support", "crisis", "listening"),
        triggers=("support a friend in crisis", "my friend is in distress what do I do", "help a friend who is not okay"),
    ),
    spec(
        "handle-a-social-invitation-you-cannot-accept",
        summary="Decline a social invitation warmly, briefly and without inventing an excuse.",
        when="the user cannot attend an event and wants to decline without damaging the relationship",
        steps=(
            "Reply promptly, even if the answer is still being decided.",
            "Decline directly in the first sentence rather than leaving it ambiguous.",
            "Give a brief reason only if one is genuinely needed, and keep it short.",
            "Offer an alternative way to connect if the relationship matters.",
            "Send a short warm message afterwards so the decline does not feel cold.",
        ),
        tags=("decline", "invitation", "social"),
        triggers=("decline a social invitation", "say no to an invitation without an excuse", "politely refuse an event I cannot attend"),
    ),
)
