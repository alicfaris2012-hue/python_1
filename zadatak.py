zadaci = ["domaci", "ucenje", "pospremanje"]
print("Pocetna lista:", zadaci)

zadaci.append("trening")
print("nakon dodavanja:", zadaci)

zadaci.insert(1, "kupovina")
print("nakon ubacivanja:", zadaci)

zadaci.remove("ucenje")
print("nakon izbacivanja:", zadaci)

zadaci[0] = "domaci iz matematike"
print("nakon promjene:", zadaci)