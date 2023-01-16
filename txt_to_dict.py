'''
tsv to dict

-- result sample --
{'2020':{'rs1':'0', 'rs2':'1', 'rs3':'2', 'rs4':0},
'2021':{'rs1':'0','rs2':'0','rs3':'0','rs4':'0'},
'2022':{'rs1':'0','rs2':'0','rs3':'0','rs4':'1'},
'2023':{'rs1':'0','rs2':'0','rs3':'0','rs4':'0'},
'2024':{'rs1':'','rs2':'2','rs3':'1','rs4':'1'},
'2025':{'rs1':'1','rs2':'0','rs3':'0','rs4':'0'},
'2026':{'rs1':'0','rs2':'0','rs3':'0','rs4':'0'}}
'''

result = {}

with open('./test.raw', 'r') as f:
    header = f.readline().strip().split("\t")
    del header[0]
    del header[1:5]
    rs_cols = header[1:5]
    
    for line in f:
        fields = line.strip().split('\t')
        del fields[0]
        del fields[1:5]
        
        key = fields[0]
        values = fields[1:]
        
        result[key] = {}
        for i in range(len(rs_cols)):
            result[key][rs_cols[i]] = values[i]

print(result)
