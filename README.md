# AS2113-Coursework
A Python program to manage insurance policyholders and claims, and analyse claim data.
# Insurance Policy & Claims Manager

This is my coursework project for AS2113. It's a command-line program in Python that keeps track of insurance policyholders and their claims, and also does some basic analysis on the claims data. No libraries, just plain Python.


## What it does

**Policyholders**
- Look up a policyholder by policy number
- Add new ones (it checks everything so you can't put in garbage):
  - policy number has to look like `P1234567` and can't already exist
  - names can only be letters, and it auto-capitalises them
  - age is `Young` (under 30) or `Old` (30+), gender is `Male`/`Female`, area is `North`/`Central`/`South`
- Asks you to confirm before saving, and you can export everything to a CSV

**Claims**
- View all claims
- Add a claim (format `C01234`). The claim number has to be unique, and the policy number has to actually exist in the policyholder data
- Edit a claim that's already there
- Export claims to a CSV

**Analysis**

Pick a group by age, gender and area and it gives you:
- how many policyholders are in the group
- how many claims they made
- claim frequency (claims per policyholder)
- smallest and largest claim
- mean claim and standard deviation

Make sure `policyholders.csv` and `claims.csv` are in the same folder as the script.

### File formats

`policyholders.csv`
```
Policy Number,First Name,Surname,Age,Gender,Area
P0000001,Ruby,Jane,Young,Female,North
```

`claims.csv`
```
Claim Number,Policy Number,Claim Amount
C00001,P0000001,1500
```

## Using it

It starts at a main menu and you just type a number:

```
Main Menu:
1. Policyholder Management
2. Claims Management
3. Analysis
4. Exit
```

Every sub-menu walks you through step by step, and if you type something wrong it tells you and lets you try again instead of crashing.

## What's in the repo

.
├── AS2113 CW2 Final.py   # the whole program
├── policyholders.csv     # policyholder data
├── claims.csv            # claims data
└── README.md
