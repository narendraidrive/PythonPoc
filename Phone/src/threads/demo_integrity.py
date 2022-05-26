import pdb
stdout= """Controller = 0
Status = Success
Description = Show Drive Information Succeeded.


Drive Information :
=================

-----------------------------------------------------------------------------
EID:Slt DID State DG      Size Intf Med SED PI SeSz Model            Sp Type 
-----------------------------------------------------------------------------
252:0     8 Onln   0 12.732 TB SAS  HDD N   N  512B WUH721414AL5204  U  -    
252:1    11 Onln   0 12.732 TB SAS  HDD N   N  512B WUH721414AL5204  U  -    
252:2     9 Onln   0 12.732 TB SAS  HDD N   N  512B WUH721414AL5204  U  -    
252:3    10 Onln   0 12.732 TB SAS  HDD N   N  512B WUH721414AL5204  U  -    
252:4    12 Onln   0 12.732 TB SAS  HDD N   N  512B WUH721414AL5204  U  -    
252:5    13 Onln   0 12.732 TB SAS  HDD N   N  512B WUH721414AL5204  U  -    
252:6    14 DHS    0 12.732 TB SAS  HDD N   N  512B WUH721414AL5204  D  -    
-----------------------------------------------------------------------------

Predictive Failure Counts 1
4 Predictive Failure Counts
0 Predictive Failure Counts
EID-Enclosure Device ID|Slt-Slot No.|DID-Device ID|DG-DriveGroup
DHS-Dedicated Hot Spare|UGood-Unconfigured Good|GHS-Global Hotspare
UBad-Unconfigured Bad|Onln-Online|Offln-Offline|Intf-Interface
Med-Media Type|SED-Self Encryptive Drive|PI-Protection Info
SeSz-Sector Size|Sp-Spun|U-Up|D-Down|T-Transition|F-Foreign
UGUnsp-Unsupported|UGShld-UnConfigured shielded|HSPShld-Hotspare shielded
CFShld-Configured shielded|Cpybck-CopyBack|CBShld-Copyback Shielded"""

#cmd_output = ['0','Server', 'drives', 'Predictive Failure Counts 5']

cmd_output = stdout.splitlines()
#   
#print(cmd_output)

predictive_failure_counts= []
for item in cmd_output:
    if "Predictive Failure Count" in item and "0" not in item:
        predictive_failure_counts.append(item)
print(predictive_failure_counts)
