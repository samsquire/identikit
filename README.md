# identikit

Identikit is a format for succinctly representing a collection of stances or part of someone's identity on an arbitrary list of matters.

# Format

Each stance is represented as a hash, a community name followed by colon and stance.

Someone who believes government and taxes should be minimal might have the following identikit:

```
#PoliticalSide:Left_wing #Government:Small #Taxes:Small #VoluntaryCollectivism:Yes
```

# Rules

The ordering of the compact answer format should not matter.

# Obfuscation

If desired and someone wants to keep their opinions obfuscated, there is a protocol to create an identikit hash.

1. Split the communities into subcommunities.
1. Sort the subcommunities.
1. SHA256 hash the subcommunities.
1. Join with a colon character

The above identikit is represented as:

```
59715ab7c5237a668345917b79b86c35baddabb153317cd40dac4a652feccf0c:8702c16ac706e3433cc6ddd9103560054def65db7feecb7b70ca0ee74bb6dddb:35f5cf7a186a76e295b1ab4aeae5b9554d1a132c414a2c6d5b5868ceec4279fa:b2e4240a467c09bb6b84fa8e05a3b6b479a3c10b6fb220ff441bda16dcaaaae6
```

See obfuscate.py for some Python3 code for creating an obfuscated string.
