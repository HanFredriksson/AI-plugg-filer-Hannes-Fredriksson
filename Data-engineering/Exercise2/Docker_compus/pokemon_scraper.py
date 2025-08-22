import pandas as pd


tabel_names = pd.read_html("https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon")
tabel_gen = pd.read_html("https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon")


poke__name_tabel = tabel_names[1]
poke__name_tabel.drop(columns="Japanskt namn", inplace=True)
poke__name_tabel.to_csv(f"data/Poke-list", index=False)

poke_gen_tabel = tabel_gen[2]
poke_gen_tabel.columns = poke_gen_tabel.columns.droplevel(0)
poke_gen_tabel["Gen"] = None  

generation = 1

for i in range(len(poke_gen_tabel)):
    dex = poke_gen_tabel.loc[i, ('Dex #')]
    
    if "Gen" in str(dex):
        generation += 1
    
    poke_gen_tabel.loc[i, "Gen"] = generation

# Identify the columns
dex_cols  = [c for c in poke_gen_tabel.columns if "Dex" in c]
name_cols = [c for c in poke_gen_tabel.columns if "Name" in c]

# Create an empty dataframe to collect results
long_df = pd.DataFrame(columns=["Dex #", "Name", "Gen"])

# Loop through each Dex/Name column pair
for d, n in zip(dex_cols, name_cols):
    tmp = poke_gen_tabel[[d, n, "Gen"]].rename(columns={d: "Dex #", n: "Name"})
    long_df = pd.concat([long_df, tmp], ignore_index=True)

# Drop empty rows (NaN)
long_df = long_df.dropna(subset=["Dex #", "Name"]).reset_index(drop=True)

# Remove rows with Name and Generation values
mask = long_df["Dex #"].astype(str).str.contains("Gen|Name")
long_df = long_df[~mask] 

# Save each genration to a CSV file
for gen in range(1, long_df["Gen"].max()+1):
    mask = long_df["Gen"].astype(str).str.contains(str(gen))
    tmp = long_df[mask]
    tmp.to_csv(f"data/Generation {gen}", index=False)