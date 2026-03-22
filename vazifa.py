import asyncio

async def savol1():
    try:
        matn = "sa1lo2m3"
        i = 0
        natija = ""
        while i < len(matn):
            if not matn[i].isdigit():
                natija += matn[i]
            i += 1
            await asyncio.sleep(0)
        print("1:", natija)
    except Exception as e:
        print("1-xatolik:", e)


async def savol2():
    try:
        matn = "abcdefghijklmnop"
        i = 0
        natija = ""
        while i < len(matn) and i < 10:
            natija += matn[i]
            i += 1
            await asyncio.sleep(0)
        print("2:", natija)
    except Exception as e:
        print("2-xatolik:", e)


async def savol3():
    try:
        ism = "Ali123"
        i = 0
        natija = ""
        while i < len(ism):
            if not ism[i].isdigit():
                natija += ism[i]
            i += 1
            await asyncio.sleep(0)
        print("3:", natija)
    except Exception as e:
        print("3-xatolik:", e)


async def savol4():
    try:
        matn = "Sa Lo M"
        i = 0
        natija = ""
        while i < len(matn):
            if matn[i] != " ":
                natija += matn[i].lower()
            i += 1
            await asyncio.sleep(0)
        print("4:", natija)
    except Exception as e:
        print("4-xatolik:", e)


async def savol5():
    try:
        matn = "salom"
        unlilar = "aeiouAEIOU"
        i = 0
        natija = ""
        while i < len(matn):
            if matn[i] in unlilar:
                natija += matn[i]
            i += 1
            await asyncio.sleep(0)
        print("5:", natija)
    except Exception as e:
        print("5-xatolik:", e)


async def savol6():
    try:
        soz = "abbaab"
        i = 0
        natija = ""
        while i < len(soz):
            if i < len(soz)-1 and soz[i] == "a" and soz[i+1] == "b":
                natija += "#"
                i += 2
            else:
                natija += soz[i]
                i += 1
            await asyncio.sleep(0)
        print("6:", natija)
    except Exception as e:
        print("6-xatolik:", e)


async def savol7():
    try:
        matn = "12345"
        i = 0
        faqat_raqam = True
        while i < len(matn):
            if not matn[i].isdigit():
                faqat_raqam = False
                break
            i += 1
            await asyncio.sleep(0)

        if faqat_raqam:
            print("7:", matn[::-1])
        else:
            print("7: faqat raqam emas")
    except Exception as e:
        print("7-xatolik:", e)


async def savol8():
    try:
        soz = "salom"
        i = 0
        natija = ""
        while i < len(soz):
            if i != len(soz)//2:
                natija += soz[i]
            i += 1
            await asyncio.sleep(0)
        print("8:", natija)
    except Exception as e:
        print("8-xatolik:", e)


async def savol9():
    try:
        ism = "Madina"
        if ism.endswith("a"):
            i = 0
            natija = ""
            while i < len(ism):
                natija += ism[i].lower()
                i += 1
                await asyncio.sleep(0)
            print("9:", natija)
        else:
            print("9:", ism)
    except Exception as e:
        print("9-xatolik:", e)


async def savol10():
    try:
        matn = "banana"
        i = 0
        natija = ""
        while i < len(matn):
            if matn[i] not in natija:
                natija += matn[i]
            i += 1
            await asyncio.sleep(0)
        print("10:", natija)
    except Exception as e:
        print("10-xatolik:", e)


async def main():
    try:
        await asyncio.gather(
            savol1(),
            savol2(),
            savol3(),
            savol4(),
            savol5(),
            savol6(),
            savol7(),
            savol8(),
            savol9(),
            savol10()
        )
    except Exception as e:
        print("Main xatolik:", e)


asyncio.run(main())
