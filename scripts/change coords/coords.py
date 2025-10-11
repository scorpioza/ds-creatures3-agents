#setv game "mapeditortmp" addm 97120 19535 1200 800 "waterfall-room-v3a"
#setv game "toxic_tmp" addm 2 6701 1320 856 "PG_toxic03"
LEFT = 97120
TOP = 19535
WIDTH = 1200
RIGHT = LEFT+WIDTH

LEFT2 = 2
TOP2 = 6701

LEFT_OFFSET = -68 + LEFT - LEFT2
TOP_OFFSET = 543 + TOP - TOP2
TOP_LIMIT = 790 + TOP

DEBUG = False

if DEBUG:
    print(TOP_OFFSET)
    print(TOP_LIMIT)
    print(" ================== ")

def main():

    content = ""
    try:
        with open('coords.txt', 'r') as file:
            content = file.read()
            if not content:
                return
    except FileNotFoundError:
        print("Error: The file 'coords.txt' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    lines = content.splitlines()
    num = -1
    for line in lines:
        num += 1
        s = " ".join(line.replace("\t", "\s").split()).strip()
        sx = s.split()
        # 'setv va00 addr game "toxic_tmp" 942 1032 7071 7071 7172 7161'
        if sx[0] == "setv" and sx[1] == "va00" and sx[-1].isdigit() and sx[-2].isdigit() \
        and sx[-3].isdigit() and sx[-4].isdigit() and sx[-5].isdigit() and sx[-6].isdigit():
            for x in range(-6, -4):
                sx[x] = int(sx[x]) + LEFT_OFFSET
            if sx[-6] < LEFT:
                sx[-6] = LEFT
                if DEBUG:    
                    print("@L sx[-6] = %d" % sx[-6])
            if sx[-5] > RIGHT:
                sx[-5] = RIGHT  
                print("@L sx[-5] = %d" % sx[-5])
            if sx[-6] > sx[-5]:
                if DEBUG:   
                    print("\n\n! WARNING: LEFT > RIGHT\n%s\n\n" % s)   
                continue   
            for x in range(-4, 0):
                sx[x] = int(sx[x]) + TOP_OFFSET
                if sx[x]< TOP_LIMIT:
                    sx[x] = TOP_LIMIT
                    if DEBUG:
                        print("@T sx[%d] = %d" % (x, sx[x]))

            if sx[-1] == TOP_LIMIT and sx[-2] == TOP_LIMIT:
                if DEBUG:
                    print("\n\n! WARNING: TOP < TOP_LIMIT\n%s\n\n" % s)   
                continue  

            for x in range(-6, -0):
                sx[x] = str(sx[x])

            s = " ".join(sx)
            lines[num]=s
        #rmsc 1033 7403 ""
        elif sx[0] == "rmsc" and sx[1].isdigit() and sx[2].isdigit():
            sx[1] = int(sx[1]) + LEFT_OFFSET
            if sx[1] <= LEFT:
                sx[1] = LEFT+1
            if sx[1] >= RIGHT:
                sx[1] = RIGHT-1
            sx[2] = int(sx[2]) + TOP_OFFSET
            if sx[2] <= TOP_LIMIT:
                sx[2] = TOP_LIMIT+1

            sx[1] = str(sx[1])
            sx[2] = str(sx[2])
            
            s = " ".join(sx)
            lines[num]=s

    print("\n".join(lines))

if __name__ == '__main__':
    main()

