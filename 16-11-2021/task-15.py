"""
15. napisi program koji ce preko skupova provjeriti je li uneseni string binaran ili nije. primjer binarnog stringa: "0110101", "ababbbabab", "566556" itd.
"""

s = "0110101"
print("binaran je" if len(set(s)) == 2 else "nije binaran")