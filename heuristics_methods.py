import heuristics
import random

max_delta = 0.5
def print_heuristics():
    print(heuristics.h0)
    print(heuristics.h1)
    print(heuristics.h2)
    print(heuristics.h3)
    print(heuristics.h4)
    print(heuristics.h5)
    print(heuristics.h6)
    print(heuristics.h7)
    print(heuristics.h8)
    print(heuristics.h9)
    print(heuristics.h10)
    print(heuristics.h11)
    print(heuristics.h12)
    print(heuristics.h13)
    print(heuristics.h14)
    print(heuristics.h15)
    print(heuristics.h16)
    print(heuristics.h17)
    print(heuristics.h18)
    print(heuristics.h19)
    print(heuristics.h20)
    print(heuristics.h21)
    print(heuristics.h22)
    print(heuristics.h23)
    print(heuristics.h24)
    print(heuristics.h25)
    print(heuristics.h26)
    print(heuristics.h27)
    print(heuristics.h28)
    print(heuristics.h29)
    print(heuristics.h30)
    print(heuristics.h31)
    print(heuristics.h32)
    print(heuristics.h33)
    print(heuristics.h34)
    print(heuristics.h35)
    print(heuristics.h36)
    print(heuristics.h37)
    print(heuristics.h38)
    print(heuristics.h39)
    print(heuristics.h40)
    print(heuristics.h41)
    print(heuristics.h42)
    print(heuristics.h43)
    print(heuristics.h44)
    print(heuristics.h45)
    print(heuristics.h46)
    print(heuristics.h47)
    print(heuristics.h48)
    print(heuristics.h49)
    print(heuristics.h50)
    print(heuristics.h51)
    print(heuristics.h52)
    print(heuristics.h53)
    print(heuristics.h54)
    print(heuristics.h55)
    print(heuristics.h56)
    print(heuristics.h57)
    print(heuristics.h58)
    print(heuristics.h59)
    print(heuristics.h60)
    print(heuristics.h61)
    print(heuristics.h62)
    print(heuristics.h63)
    print(heuristics.h64)
    print(heuristics.h65)
    print(heuristics.h66)
    print(heuristics.h67)
    print(heuristics.h68)
    print(heuristics.h69)
    print(heuristics.h70)
    print(heuristics.h71)
    print(heuristics.h72)
    print(heuristics.h73)
    print(heuristics.h74)
    print(heuristics.h75)
    print(heuristics.h76)
    print(heuristics.h78)
    print(heuristics.h79)
    print(heuristics.h80)
    print(heuristics.h81)
    print(heuristics.h82)
    print(heuristics.h83)
    print(heuristics.h84)
def write_heuristics():
    f = open("heuristics.py", "w")
    f.write("""
h0 = """ + str(heuristics.h0) + """
h1 = """ + str(heuristics.h1) + """
h2 = """ + str(heuristics.h2) + """
h3 = """ + str(heuristics.h3) + """
h4 =  """ + str(heuristics.h4) + """
h5 =  """ + str(heuristics.h5) + """
h6 =  """ + str(heuristics.h6) + """
h7 =  """ + str(heuristics.h7) + """
h8 =  """ + str(heuristics.h8) + """
h9 =  """ + str(heuristics.h9) + """
h10 =  """ + str(heuristics.h10) + """
h11 =  """ + str(heuristics.h11) + """
h12 =  """ + str(heuristics.h12) + """
h13 =  """ + str(heuristics.h13) + """
h14 =  """ + str(heuristics.h14) + """
h15 =  """ + str(heuristics.h15) + """
h16 =  """ + str(heuristics.h16) + """
h17 =  """ + str(heuristics.h17) + """
h18 =  """ + str(heuristics.h18) + """
h19 =  """ + str(heuristics.h19) + """
h20 =  """ + str(heuristics.h20) + """
h21 =  """ + str(heuristics.h21) + """
h22 =  """ + str(heuristics.h22) + """
h23 =  """ + str(heuristics.h23) + """
h24 =  """ + str(heuristics.h24) + """
h25 =  """ + str(heuristics.h25) + """
h26 =  """ + str(heuristics.h26) + """
h27 =  """ + str(heuristics.h27) + """
h28 =  """ + str(heuristics.h28) + """
h29 =  """ + str(heuristics.h29) + """
h30 =  """ + str(heuristics.h30) + """
h31 =  """ + str(heuristics.h31) + """
h32 =  """ + str(heuristics.h32) + """
h33 =  """ + str(heuristics.h33) + """
h34 =  """ + str(heuristics.h34) + """
h35 =  """ + str(heuristics.h35) + """
h36 =  """ + str(heuristics.h36) + """
h37 =  """ + str(heuristics.h37) + """
h38 =  """ + str(heuristics.h38) + """
h39 =  """ + str(heuristics.h39) + """
h40 =  """ + str(heuristics.h40) + """
h41 =  """ + str(heuristics.h41) + """
h42 =  """ + str(heuristics.h42) + """
h43 =  """ + str(heuristics.h43) + """
h44 =  """ + str(heuristics.h44) + """
h45 =  """ + str(heuristics.h45) + """
h46 =  """ + str(heuristics.h46) + """
h47 =  """ + str(heuristics.h47) + """
h48 =  """ + str(heuristics.h48) + """
h49 =  """ + str(heuristics.h49) + """
h50 =  """ + str(heuristics.h50) + """
h51 =  """ + str(heuristics.h51) + """
h52 =  """ + str(heuristics.h52) + """
h53 =  """ + str(heuristics.h53) + """
h54 =  """ + str(heuristics.h54) + """
h55 =  """ + str(heuristics.h55) + """
h56 =  """ + str(heuristics.h56) + """
h57 =  """ + str(heuristics.h57) + """
h58 =  """ + str(heuristics.h58) + """
h59 =  """ + str(heuristics.h59) + """
h60 =  """ + str(heuristics.h60) + """
h61 =  """ + str(heuristics.h61) + """
h62 =  """ + str(heuristics.h62) + """
h63 =  """ + str(heuristics.h63) + """
h64 =  """ + str(heuristics.h64) + """
h65 =  """ + str(heuristics.h65) + """
h66 =  """ + str(heuristics.h66) + """
h67 =  """ + str(heuristics.h67) + """
h68 =  """ + str(heuristics.h68) + """
h69 =  """ + str(heuristics.h69) + """
h70 =  """ + str(heuristics.h70) + """
h71 =  """ + str(heuristics.h71) + """
h72 =  """ + str(heuristics.h72) + """
h73 =  """ + str(heuristics.h73) + """
h74 =  """ + str(heuristics.h74) + """
h75 =  """ + str(heuristics.h75) + """
h76 =  """ + str(heuristics.h76) + """
h78 =  """ + str(heuristics.h78) + """
h79 =  """ + str(heuristics.h79) + """
h80 =  """ + str(heuristics.h80) + """
h81 =  """ + str(heuristics.h81) + """
h82 =  """ + str(heuristics.h82) + """
h83 =  """ + str(heuristics.h83) + """
h84 =  """ + str(heuristics.h84) + """""")
    f.close()
    
def randomize_heuristics():
    heuristics.h0 += random.uniform(-1,1) * max_delta
    heuristics.h1 += random.uniform(-1,1) * max_delta
    heuristics.h2 += random.uniform(-1,1) * max_delta
    heuristics.h3 += random.uniform(-1,1) * max_delta
    heuristics.h4 += random.uniform(-1,1) * max_delta
    heuristics.h5 += random.uniform(-1,1) * max_delta
    heuristics.h6 += random.uniform(-1,1) * max_delta
    heuristics.h7 += random.uniform(-1,1) * max_delta
    heuristics.h8 += random.uniform(-1,1) * max_delta
    heuristics.h9 += random.uniform(-1,1) * max_delta
    heuristics.h10 += random.uniform(-1,1) * max_delta
    heuristics.h11 += random.uniform(-1,1) * max_delta
    heuristics.h12 += random.uniform(-1,1) * max_delta
    heuristics.h13 += random.uniform(-1,1) * max_delta
    heuristics.h14 += random.uniform(-1,1) * max_delta
    heuristics.h15 += random.uniform(-1,1) * max_delta
    heuristics.h16 += random.uniform(-1,1) * max_delta
    heuristics.h17 += random.uniform(-1,1) * max_delta
    heuristics.h18 += random.uniform(-1,1) * max_delta
    heuristics.h19 += random.uniform(-1,1) * max_delta
    heuristics.h20 += random.uniform(-1,1) * max_delta
    heuristics.h21 += random.uniform(-1,1) * max_delta
    heuristics.h22 += random.uniform(-1,1) * max_delta
    heuristics.h23 += random.uniform(-1,1) * max_delta
    heuristics.h24 += random.uniform(-1,1) * max_delta
    heuristics.h25 += random.uniform(-1,1) * max_delta
    heuristics.h26 += random.uniform(-1,1) * max_delta
    heuristics.h27 += random.uniform(-1,1) * max_delta
    heuristics.h28 += random.uniform(-1,1) * max_delta
    heuristics.h29 += random.uniform(-1,1) * max_delta
    heuristics.h30 += random.uniform(-1,1) * max_delta
    heuristics.h31 += random.uniform(-1,1) * max_delta
    heuristics.h32 += random.uniform(-1,1) * max_delta
    heuristics.h33 += random.uniform(-1,1) * max_delta
    heuristics.h34 += random.uniform(-1,1) * max_delta
    heuristics.h35 += random.uniform(-1,1) * max_delta
    heuristics.h36 += random.uniform(-1,1) * max_delta
    heuristics.h37 += random.uniform(-1,1) * max_delta
    heuristics.h38 += random.uniform(-1,1) * max_delta
    heuristics.h39 += random.uniform(-1,1) * max_delta
    heuristics.h40 += random.uniform(-1,1) * max_delta
    heuristics.h41 += random.uniform(-1,1) * max_delta
    heuristics.h42 += random.uniform(-1,1) * max_delta
    heuristics.h43 += random.uniform(-1,1) * max_delta
    heuristics.h44 += random.uniform(-1,1) * max_delta
    heuristics.h45 += random.uniform(-1,1) * max_delta
    heuristics.h46 += random.uniform(-1,1) * max_delta
    heuristics.h47 += random.uniform(-1,1) * max_delta
    heuristics.h48 += random.uniform(-1,1) * max_delta
    heuristics.h49 += random.uniform(-1,1) * max_delta
    heuristics.h50 += random.uniform(-1,1) * max_delta
    heuristics.h51 += random.uniform(-1,1) * max_delta
    heuristics.h52 += random.uniform(-1,1) * max_delta
    heuristics.h53 += random.uniform(-1,1) * max_delta
    heuristics.h54 += random.uniform(-1,1) * max_delta
    heuristics.h55 += random.uniform(-1,1) * max_delta
    heuristics.h56 += random.uniform(-1,1) * max_delta
    heuristics.h57 += random.uniform(-1,1) * max_delta
    heuristics.h58 += random.uniform(-1,1) * max_delta
    heuristics.h59 += random.uniform(-1,1) * max_delta
    heuristics.h60 += random.uniform(-1,1) * max_delta
    heuristics.h61 += random.uniform(-1,1) * max_delta
    heuristics.h62 += random.uniform(-1,1) * max_delta
    heuristics.h63 += random.uniform(-1,1) * max_delta
    heuristics.h64 += random.uniform(-1,1) * max_delta
    heuristics.h65 += random.uniform(-1,1) * max_delta
    heuristics.h66 += random.uniform(-1,1) * max_delta
    heuristics.h67 += random.uniform(-1,1) * max_delta
    heuristics.h68 += random.uniform(-1,1) * max_delta
    heuristics.h69 += random.uniform(-1,1) * max_delta
    heuristics.h70 += random.uniform(-1,1) * max_delta
    heuristics.h71 += random.uniform(-1,1) * max_delta
    heuristics.h72 += random.uniform(-1,1) * max_delta
    heuristics.h73 += random.uniform(-1,1) * max_delta
    heuristics.h74 += random.uniform(-1,1) * max_delta
    heuristics.h75 += random.uniform(-1,1) * max_delta
    heuristics.h76 += random.uniform(-1,1) * max_delta
    heuristics.h78 += random.uniform(-1,1) * max_delta
    heuristics.h79 += random.uniform(-1,1) * max_delta
    heuristics.h80 += random.uniform(-1,1) * max_delta
    heuristics.h81 += random.uniform(-1,1) * max_delta
    heuristics.h82 += random.uniform(-1,1) * max_delta
    heuristics.h83 += random.uniform(-1,1) * max_delta
    heuristics.h84 += random.uniform(-1,1) * max_delta