from PIL import Image

def returnMonthName(monthNumber):
    return {
        1 : 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }.get(monthNumber,'Doesnt exist')

def createImage(firstImage, secondImage, pathToSave, diff):
    firstImage = Image.open(firstImage)  # type: Image.Image
    secondImage = Image.open(secondImage)  # type: Image.Image
    size = 520, 1126
    firstImage.thumbnail(size, Image.ANTIALIAS)
    secondImage.thumbnail(size, Image.ANTIALIAS)
    mask = Image.open('background.png')  # type: Image.Image
    blankImage = Image.new('RGBA', (1200, 1200), (255, 255, 255, 255))  # type: Image.Image

    blankImage.paste(firstImage, (40, 40))
    blankImage.paste(secondImage, (640, 40))
    blankImage.paste(mask, (0, 0), mask)
    blankImage.save(pathToSave+ f'/content{diff}.png')
