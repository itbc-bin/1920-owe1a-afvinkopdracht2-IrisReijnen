#mRNA van de Pan Paniscus
mrna_pan = """TTTAGCGCGGTGAGTTTGAAACTGCTCGCACTTGGCTTCAAAGCTGGCTCTTGGAAGTTGAGTGGAGAGC
GACGCGGTTGTTGTAGCTGCCGCTGCGGCCGCCGCGGAATAATAAGCCAGGATCTACCATACCCATTGAC
TAACTATGGAAGATTATACCAAAATAGAGAAAATTGGAGAAGGTACCTATGGAGTTGTGTATAAGGGTAG
ACACAAAACTACAGGTCAAGTGGTAGCCATGAAAAAAATCAGACTAGAAAGTGAAGAGGAAGGGGTTCCT
AGTACTGCAATTCGGGAAATTTCTCTATTAAAGGAACTTCGTCATCCAAATATAGTCAGTCTTCAGGATG
TGCTTATGCAGGATTCCAGGTTATATCTCATCTTTGAGTTTCTTTCCATGGATCTGAAGAAATACTTGGA
TTCTATCCCTCCTGGTCAGTACATGGATTCTTCACTTGTTAAGAGTTATTTATACCAAATCCTACAGGGG
ATTGTGTTTTGTCACTCTAGAAGAGTTCTTCACAGAGACTTAAAACCTCAAAATCTCTTGATTGATGACA
AAGGAACAATTAAACTGGCTGATTTTGGCCTTGCCAGAGCTTTTGGAATACCTATTAGAGTATATACACA
TGAGGTAGTAACACTCTGGTACAGATCTCCAGAAGTATTGCTGGGGTCAGCTCGTTACTCAACTCCAGTT
GACATTTGGAGTATAGGCACCATATTTGCTGAACTAGCAACTAAGAAACCACTTTTCCATGGGGATTCAG
AAATTGATCAACTCTTCAGGATTTTCAGAGCTTTGGGCACTCCCAATAATGAAGTGTGGCCAGAAGTGGA
ATCTTTACAGGACTATAAGAATACATTTCCCAAATGGAAACCAGGAAGCCTAGCATCCCATGTCAAAAAC
TTGGATGAAAATGGCTTGGATTTGCTCTCGAAAATGTTAATCTATGATCCAGCCAAACGAATTTCTGGCA
AAATGGCACTGAATCATCCATATTTTAATGATTTGGACAATCAGATTAAGAAGATGTAGCTTTCTGACAA
AAAGTTTCCATATGTTATATCAACAGATAGTTGTGTTTTTATTGTTAACTCTTGTCTATTTTTGTCTTAT
ATATATTTCTTTGTTATCAAACTTCAGCTGTACTTCGTCTTCTAATTTCAAAAATATAACTTAAAAATGT
AAATATTCTATTATGAATTTAAATATAATTCTGTAAATGTGTGTAGGTCTCACTGTAACAACTATTTGTT
ACTATAATAAAACTATAATATTGATGTCAGGAATCAGGAAAAAATTTGAGTTGGCTTAAATCATCTCAGT
CCTTATGGCAGTTTTATTTTCCTGTAGTTGGAACTACTAAAATTTAGGAAAATGCTAAGTTCAAGTTTCG
TAATGCTTTGAAGTATTTTTATGTTCTGAATGTTTAAATGTTCTCATCAGTTTCTTGCCATGTTGTTAAC
TATACAACCTGGCTAAAGATGAATATTTTTCTACTGGTATTTTAATTTTTGACCTAAATGTTTAAGCATT
CGGAATGAGAAAACTATACAGATTTGAGAAATGATGCTAAATTTATAGGAGTTTTCAGTAACTTAAAAAG
CTAACATGAGAGCATGCCAAAATTTGCTAAGTCTTACAAAGATCAAGGGCTGTCCGCAACAGGGAAGAAC
AGTTTTGAAAATTTATGAACTATCTTATTTTTAGGTAGGTTTTGAAAGCTTTTTGTCTAAGTGAATTCTT
ATGCCTTGGTCAGAGTAATAACTGAAGGAGTTGCTTGTCTTGGCTTTCGAGTCTCAGTTTAAAACTACAC
ATTTTGACAGTGTTTATTAGTAGCCATCTAAAAAGGCTCTAATGTATATTTAACTAAAATTACTAGCTTT
GGGAATTAAACTGTTTAACGAATAA"""


#Berekent de lengte van het mRNA van Pan Paniscus zonder enters.
aantal_tot = len(mrna_pan.replace("\n",""))
print("Lengte: ", aantal_tot)


#Telt het aantal C en G
aantal_c = mrna_pan.count("C")
aantal_g = mrna_pan.count("G")
aantal_gc = aantal_c + aantal_g

print("Aantal G: ", aantal_g)
print("Aantal C: ", aantal_c)
print("Aantal G en C: ", aantal_gc)


#GC% berekenen
gc_percentage = aantal_gc / aantal_tot * 100
print("Het GC% van het mRNA van Pan Paniscus is", str(gc_percentage) + "%")
