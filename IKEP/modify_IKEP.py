import pandas as pd
# Read in the csv files
sheet1 = pd.read_csv("C:/MISC/BAU/Python Script/IKEP/sheet1.csv")
sheet2 = pd.read_csv("C:/MISC/BAU/Python Script/IKEP/sheet2.csv")
sheet1_IPSECP = pd.read_csv("C:/MISC/BAU/Python Script/IPSECP/sheet1_IPSECP.csv")
sheet_Dist_Tep = pd.read_csv("C:/MISC/BAU/Python Script/Distributed_Tep.csv")
sheet_Cent_Tep = pd.read_csv("C:/MISC/BAU/Python Script/Centralised_Tep.csv")

# Create an empty list to store the modified data
modified_data = []
modified_data_IPSECP = []

for i, row in sheet1.iterrows():
 
# Check if "IKEP-3" is present in the $dn column
    if "IKEP-3" in row["$dn"]:

        # Rows to drop
        row = row.drop("$dn",axis = 0) 
# Check if "IKEP-4" is present in the $dn column    
    elif "IKEP-4" in row["$dn"]:
 #       print(i)
#        print(row["remoteTunnelEndpoint"])
        for ind, row_cent in sheet_Cent_Tep.iterrows():
        
            match_tep = sheet_Cent_Tep[sheet_Cent_Tep["Tunnel Group Address"] == row["remoteTunnelEndpoint"]]
        
        if not match_tep.empty:
            
            row["remoteTunnelEndpoint"] = match_tep.iloc[0,5]
            row["userLabel"] = match_tep.iloc[0,6]

# Check if "IKEP-6" is present in the $dn column
    elif "IKEP-6" in row["$dn"]:
        
#        
        substring_IPSECP = row["$dn"][:54]
        for i2, row_IPSECP in sheet1_IPSECP.iterrows():
            print(sheet1_IPSECP.iloc[i2,0][:54])
            match_IPSECP = sheet1_IPSECP.iloc[i2,0][:54] == substring_IPSECP
        #print(match_IPSECP["$dn"])
        
            #print (sheet1_IPSECP["$dn"][:54])
            if not match_IPSECP.empty:
                print ("matched")
            #print (row["$dn"][:54])
            #print (sheet1_IPSECP)
#            for i2, row_IPSECP in sheet1_IPSECP.iterrows():
#                if row_IPSECP.iloc[0][:54] = row["$dn"][:54]
#                    print(row_IPSECP.iloc[0])
#                if row_IPSECP["$dn"] == row
            #print (match_IPSECP.iloc[0,1])
#          
            #dn_IPSECP2_substring = row_IPSECP["$dn"][:54]+"IPSECP-2"   
            #print(dn_IPSECP2_substring)
#            row_IPSECP["$dn"] = dn_IPSECP2_substring
#            row_IPSECP["userLabel"] = "Direct X2 Tunnel"
            #row_IPSECP["remoteTunnelEndpoint"] = match.iloc[0,7]
 #           row["userLabel"] = match.iloc[0,5]
#            row["ikeAuthenticationMethod"] = 2
 #           row["ikeEncryptionMethod"] = 4
##            row["ipsecPerfForwSecEnabled"] = 1
        # Inserting a new_row                
#            new_row_IPSECP = row_IPSECP.copy()
 #           new_row_IPSECP["$dn"] = row_IPSECP["$dn"][:54]+"IPSECP-1"
  #          new_row_IPSECP["authenticationMethod"] = 2
   #         new_row_IPSECP["encryptionMethod"] = 5
    #        new_row_IPSECP["userLabel"] = "BAU Tunnel"
#        modified_data_IPSECP.append(row_IPSECP)
#        modified_data_IPSECP.append(new_row_IPSECP)
#        
        
    

# Check if "IKEP-1" is present in the $dn column          
    elif "IKEP-1" in row["$dn"]:
        
        # Get the first 21 characters of the $dn column
        dn_substring = row["$dn"][:21]

        # Search for a matching MRBTS in sheet2
        match = sheet2[sheet2["MRBTS"] == dn_substring]
        #print(match)
        # If a match is found, update the remoteTunnelEndpoint column
        if not match.empty:

            dn_IKEP3_substring = row["$dn"][:54]+"IKEP-3"    
            row["remoteTunnelEndpoint"] = match.iloc[0,7]
            row["userLabel"] = match.iloc[0,5]
            row["ikeAuthenticationMethod"] = 2
            row["ikeEncryptionMethod"] = 4
            row["ipsecPerfForwSecEnabled"] = 1
            
            # Inserting a new_row                
            new_row = row.copy()
            new_row["$dn"] = dn_IKEP3_substring
           
            new_row["remoteTunnelEndpoint"] = match.iloc[0,10]
            new_row["userLabel"] = match.iloc[0,8]
            
            # Add the modified row to the modified_data list
            modified_data.append(new_row)
    modified_data.append(row)
#    modified_data_IPSECP.append(row_IPSECP)
            
# Convert the modified_data list to a DataFrame
modified_sheet = pd.DataFrame(modified_data)

# Write the modified data to a new csv file
modified_sheet.to_csv("C:/MISC/BAU/Python Script/IKEP/sheet3_modified_IKEP.csv", index=False)

# Convert the modified_data_IPSECP list to a DataFrame
modified_sheet_IPSECP = pd.DataFrame(modified_data_IPSECP)

# Write the modified data to a new csv file
modified_sheet_IPSECP.to_csv("C:/MISC/BAU/Python Script/IPSECP/sheet3_modified_IPSECP.csv", index=False) 
   


print("Congifuration file created !!!!!")