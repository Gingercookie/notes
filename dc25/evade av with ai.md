# Evade Next-Gen AV with AI

### AI Mutations
Bus + Noise = Ostrict
PE Malware + Changed Bytes =
    At worst = Not a PE anymore
    At best = Not the intended malware anymore

We need to make sure that whatever changes happen preserver two things
- Still a PE
- Still the malware we intended

OpenAI
Download Atari breakout
We are going to modify the game.
Instead of rewarding individual actions, we can distribute the reward amongst
a _sequence of actions_.

We can then define a large set of action sequences - which are known to preserve our two requirements, and the AI can choose those as it wishes.

The _State_ of the PE (Input to AI)
* General file info
* Header info
* session characteristics
* import/export functions
* strings
* file byte and entropy histograms

The _Actions_ available to AI
    (Sequences of actions defined earlier)

#### Sources
https://www.github.com/endgameinc/gym-malware
