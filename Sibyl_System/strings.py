on_string = """
  **I'm Edith, How Are You! Sir**
**Welcome** ⭐⭐⭐
**Name** - `{name}`
**Rank** - `{Enforcer}`
__You are an authorized user__
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
$SCAN
Cymatic Scan request!
**Enforcer:** {enforcer}
**User scanned:** {spammer}
**Reason:** `{reason}`
**Scan Source:** {chat}
**Target Message:** `{message}`
"""
forced_scan_string = """
$FORCED
**Inspector:** {ins}
**Target:** {spammer}
**Reason:** `{reason}`
**Scan Source:** {chat}
**Target Message:** `{message}`
"""

reject_string = """
$REJECTED
**Crime Coefficient:** `Under 100`
Not a target for enforcement action.
The trigger of Dominator will be locked.
"""

proof_string = """
**Case file for** - {proof_id} :
┣━**Reason**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""

scan_approved_string = """
#LethalEliminator
**Target User:** {scam}
**Crime Coefficient:** `Over 300`
**Reason:** `{reason}`
**Enforcer:** `{enforcer}`
**Case Number:** `{proof_id}`
"""

bot_gban_string = """
#DestroyDecomposer
**Enforcer:** `{enforcer}`
**Target User:** {scam}
**Reason:** `{reason}`
"""

ban_codes_string = """
HERE ARE THE BAN CODES FOR EDITH -X :

• `ED-X_01` - RAID PARTICIPANT
• `ED-X_02` - RAID/SPAM INFLAMMER
• `ED-X_03` - SCAMMER
• `ED-X_04` - SPAM ADDING MEMBER
• `ED-X_05` - ABUSE SPAM 
• `ED-X_06` - NSFW SPAMMER
• `ED-X_07` - IMPERSONATION
• `ED-X_08` - MD/BTC SCAM
• `ED-X_09` - ADDING SPAMBOTS
• `ED-X_10` - ILLEGAL
• `ED-X_11` - PHISHING
• `ED-X_12` - FRAUD PROMOTION  (ANY KIND)
• `ED-X_13` - CYBER THREATENING/CYBER BULLY 
• `ED-X_14` - CHILD ABUSE 
• `ED-X_15` - BAN EVASION 
• `ED-X_16` - SPAMBOT
• `ED-X_17` - RAID INITIALIZOR
• `ED-X_18` - CRIMINAL ACT


THIS SCANNER BANS ONLY APPLY TO YOUR GROUP IF U ARE USING ANY ONE OF THE BOTS IN [THIS LIST](https://t.me/EdithXinfo/12)
"""

# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator
