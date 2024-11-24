N = int(input("Masukan ukuran grid (N) = "))
commads = input("Masukan perintah gerakan = ")

# posisi awal robot
x,y = 1,1

# iterasi melalui setiap perintah dalam string 
for commad in commads:
    if commad == "L":
        if y > 1:
            y -= 1
    elif commad == "R":
        if y < N:
            y += 1
    elif commad == "U":
        if x < N:
            x += 1
    elif commad == "D":
        if x > 1:
            x -= 1

# output akhir
print(x,y)
