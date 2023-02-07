import pandas as pd
# Read in the csv files
sheet1 = pd.read_csv("C:/MISC/BAU/Python Script/IPSECP/sheet1_IPSECP.csv")
sheet2 = pd.read_csv("C:/MISC/BAU/Python Script/IKEP/sheet3_modified_IKEP.csv")
#sheet_Dist_Tep = pd.read_csv("C:/MISC/BAU/Python Script/Distributed_Tep.csv")
#sheet_Cent_Tep = pd.read_csv("C:/MISC/BAU/Python Script/Centralised_Tep.csv")

# Create an empty list to store the modified data
modified_data = []
# For 4G only
substr = "PLMN-PLMN/MRBTS-17450"
#sheet1["$dn"][:21]
print(substr)
print(sheet1.iloc[2,0][:21])