import pandas as pd
print("Creating config files...............")
# Read in the csv files
sheet1 = pd.read_csv("C:/MISC/BAU/Python Script/IKEP/sheet1.csv")
sheet2 = pd.read_csv("C:/MISC/BAU/Python Script/IKEP/sheet2.csv")
sheet1_IPSECP = pd.read_csv("C:/MISC/BAU/Python Script/IPSECP/sheet1_IPSECP.csv")
sheet1_SECPOL = pd.read_csv("C:/MISC/BAU/Python Script/SECPOL/Sheet1_SECPOL.csv")
sheet1_TWAMP = pd.read_csv("C:/MISC/BAU/Python Script/TWAMP/sheet1_TWAMP.csv")
sheet_Dist_Tep = pd.read_csv("C:/MISC/BAU/Python Script/Distributed_Tep.csv")
sheet_Cent_Tep = pd.read_csv("C:/MISC/BAU/Python Script/Centralised_Tep.csv")



# Create an empty list to store the modified data
modified_data = []
modified_data_IPSECP = []
modified_data_TWAMP = []
modified_data_SECPOL = []

for i, row in sheet1.iterrows():
 
# Check if "IKEP-3" is present in the $dn column
    if "IKEP-3" in row["$dn"]:

        # Rows to drop
        row = row.drop(row.index)
     
# Check if "IKEP-4" is present in the $dn column    
    elif "IKEP-4" in row["$dn"]:

        for ind, row_cent in sheet_Cent_Tep.iterrows():
        
            match_tep = sheet_Cent_Tep[sheet_Cent_Tep["Tunnel Group Address"] == row["remoteTunnelEndpoint"]]
        
        if not match_tep.empty:
            
            row["remoteTunnelEndpoint"] = match_tep.iloc[0,5]
            row["userLabel"] = match_tep.iloc[0,6]

# Check if "IKEP-6" is present in the $dn column
    elif "IKEP-6" in row["$dn"]:
          
        substring_IKEP = row["$dn"][:54]

        for i2, row_IPSECP in sheet1_IPSECP.iterrows():
            
            substring_IPSECP = sheet1_IPSECP.iloc[i2,0][:54]
                 
            if substring_IPSECP == substring_IKEP:
            
                if "IPSECP-2" in row_IPSECP["$dn"]:
                    # Rows to drop
                    row_IPSECP = row_IPSECP.drop(row_IPSECP.index)
                elif "IPSECP-1" in row_IPSECP["$dn"]:
                    dn_IPSECP2_substring = row_IPSECP["$dn"][:54]+"IPSECP-2"
                    row_IPSECP["$dn"] = dn_IPSECP2_substring
                    #print(row_IPSECP["$dn"])
                    row_IPSECP["userLabel"] = "Direct X2 Tunnel"
                    row_IPSECP["authenticationMethod"] = 1
                    row_IPSECP["encryptionMethod"] = 1
                    row_IPSECP["pfsDiffHellGrp"] = 1

                modified_data_IPSECP.append(row_IPSECP)
                
                
        #for i_secpol, row_SECPOL in sheet1_SECPOL.iterrows():
        
         #   substring_SECPOL = sheet1_SECPOL.iloc[i_secpol,0][:54]
            
          #  if substring_SECPOL == substring_IKEP: 
            
           #     if "IKEP-1" in row_SECPOL["ikePDN"]: 
            #        substring_protgrp = row_SECPOL["ikePDN"][:44]+"IKEPROTGRP-1"
             #       row_SECPOL["ikePDN"] = substring_protgrp
                    
              #  elif "IKEP-6" in row_SECPOL["ikePDN"]:
               #     substring_protgrp = row_SECPOL["ipSecPDN"][:44]+"IPSECP-2"
                #    row_SECPOL["ipSecPDN"] = substring_protgrp
                
                #modified_data_SECPOL.append(row_SECPOL)

# Check if "IKEP-1" is present in the $dn column          
    elif "IKEP-1" in row["$dn"]:
        
        # Get the first 21 characters of the $dn column
        dn_substring = row["$dn"][:21]
        substring_IKEP = row["$dn"][:54]

        # Search for a matching MRBTS in sheet2
        match = sheet2[sheet2["MRBTS"] == dn_substring]

        # If a match is found, update the remoteTunnelEndpoint column
        if not match.empty:

            dn_IKEP3_substring = row["$dn"][:54]+"IKEP-3"    
            row["remoteTunnelEndpoint"] = match.iloc[0,7]
            row["userLabel"] = match.iloc[0,5]
            row["ikeAuthenticationMethod"] = 2
            row["ikeEncryptionMethod"] = 4
            row["ipsecPerfForwSecEnabled"] = 1
            row["ikeDiffHellGrp"] = 1
            
            # Inserting a new_row for IKEP-3                
            new_row = row.copy()
            new_row["$dn"] = dn_IKEP3_substring
           
            new_row["remoteTunnelEndpoint"] = match.iloc[0,10]
            new_row["userLabel"] = match.iloc[0,8]
            
            # Add the modified row to the modified_data list
            modified_data.append(new_row)
        for i_twamp, row_TWAMP in sheet1_TWAMP.iterrows():
            substring_TWAMP = sheet1_TWAMP.iloc[i_twamp,0][:21]
            #print(substring_TWAMP)
            #print(dn_substring)
            if substring_TWAMP == dn_substring:
            #if not match_twamp.empty():
            
                for i_d, row_dist in sheet_Dist_Tep.iterrows():
                    if row_dist["Tunnel End Point"] == match.iloc[0,7]:
                        row_TWAMP["destIpAddress"] = row_dist["TWAMP Reflector"]
                        #print(i_d," ",row_dist["TWAMP Reflector"])
                        modified_data_TWAMP.append(row_TWAMP)            
            
            
        #print(substring_IKEP)
        for i2, row_IPSECP in sheet1_IPSECP.iterrows():
            substring_IPSECP = sheet1_IPSECP.iloc[i2,0][:54]
                      
            if substring_IPSECP == substring_IKEP:
                if "IPSECP-1" in row_IPSECP["$dn"]:
                    row_IPSECP["authenticationMethod"] = 2
                    row_IPSECP["encryptionMethod"] = 5
                    row_IPSECP["pfsDiffHellGrp"] = 1
                    row_IPSECP["userLabel"] = "BAU Tunnel"
             
                    modified_data_IPSECP.append(row_IPSECP) 
        
        for i_secpol, row_SECPOL in sheet1_SECPOL.iterrows():
        
            substring_SECPOL = sheet1_SECPOL.iloc[i_secpol,0][:54]
            
            if substring_SECPOL == substring_IKEP: 
            
                if "IKEP-1" in row_SECPOL["ikePDN"]: 
                    substring_protgrp = row_SECPOL["ikePDN"][:44]+"IKEPROTGRP-1"
                    row_SECPOL["ikePDN"] = substring_protgrp
                    
                elif "IKEP-6" in row_SECPOL["ikePDN"]:
                    substring_protgrp = row_SECPOL["ipSecPDN"][:44]+"IPSECP-2"
                    row_SECPOL["ipSecPDN"] = substring_protgrp
                
                modified_data_SECPOL.append(row_SECPOL)        
                    
                    
        
    modified_data.append(row)

        
# Convert the modified_data list to a DataFrame
modified_sheet = pd.DataFrame(modified_data)

# Write the modified data to a new csv file
modified_sheet.to_csv("C:/MISC/BAU/Python Script/IKEP/sheet3_modified_IKEP.csv", index=False)

# Convert the modified_data_IPSECP list to a DataFrame
modified_sheet_IPSECP = pd.DataFrame(modified_data_IPSECP)

# Write the modified data to a new csv file
modified_sheet_IPSECP.to_csv("C:/MISC/BAU/Python Script/IPSECP/sheet3_modified_IPSECP.csv", index=False) 

# Convert the modified_data_TWAMP list to a DataFrame
modified_sheet_TWAMP = pd.DataFrame(modified_data_TWAMP)

# Write the modified data to a new csv file
modified_sheet_TWAMP.to_csv("C:/MISC/BAU/Python Script/TWAMP/sheet3_modified_TWAMP.csv", index=False)    

# Convert the modified_data_SECPOL list to a DataFrame
modified_sheet_SECPOL = pd.DataFrame(modified_data_SECPOL)

# Write the modified data to a new csv file
modified_sheet_SECPOL.to_csv("C:/MISC/BAU/Python Script/SECPOL/sheet3_modified_SECPOL.csv", index=False)  


print("Congifuration file created !!!!!")