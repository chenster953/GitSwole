print('Hello. My names Danny Bolivia. Dbol for short. \nI will be here '
      'to guide you to the body of your dreams.\nFirst, '
      'a couple of questions to establish a baseline.')
NAME = input('What is your name?: ')
print('Welcome,', NAME)

while True:
    GOAL = input('Is your current goal to gain weight, lose weight, or eat healthier?: ').lower()
    if GOAL == 'gain weight':
        print('Great! let the bulk begin!')
        break
    elif GOAL == 'lose weight':
        print('Great! Let the shreds begin!')
        break
    elif GOAL == 'eat healthier':
        print('Great! You are what you eat!')
        break
    else:
        print('Please choose an option listed above.')
        continue

# GAIN WEIGHT CODE BLOCK

if GOAL == 'gain weight':
    print('let\'s find out your FFMI to see how quickly you should gain weight. '
    '\nFor this, we will need your height, weight and estimated body fat percentage.')
    while True:
        HEIGHT = (input('Please enter your height in inches: '))
        if HEIGHT.isdigit():
            HEIGHT = float(HEIGHT)
            break
        else:
            print('Please enter a number. ')
            continue
    while True:
        WEIGHT = (input('Please enter your weight in pounds: '))
        if WEIGHT.isdigit():
            WEIGHT = float(WEIGHT)
            break
        else:
            print('Please enter a number. ')
            continue
    while True:
        BF = (input('Please enter your body fat percentage as a whole number: '))
        if BF.isdigit():
            BF = float(BF)
            break
        else:
            print('Please enter a whole number without a percentage sign. ')
            continue
    FFMI = ((WEIGHT * ((100 - BF)/100))/2.2) / (HEIGHT * 0.0254) ** 2
    rounded_FFMI = round(FFMI, 2)
    print('Your FFMI is', str(rounded_FFMI))
    print('Now that we know your FFMI, we will refer to the FFMI scale\n'
          'to see if losing weight is for you.')

    SEX = input('Please enter your sex: (male/female) ').lower()
    while SEX != 'male' and SEX != 'female':
        SEX = input('Please choose either male or female: ) ').lower()
    if SEX == 'male':
        if FFMI < 18 and 10 < BF < 18:
            print('You are skinny, buiking is perfect!')
        elif 18 < FFMI < 20 and 20 < BF < 27:
            print('You are average, bulking is safe!')
        elif 19 < FFMI < 21 and 25 < BF < 40:
            print('You are fat, bulking is not for you.')
        elif 20 < FFMI < 21 and 10 < BF < 18:
            print('You are an moderately lean, bulking is safe!')
        elif 22 < FFMI < 23 and 6 < BF < 12:
            print('You are an extremely lean, bulking is recommended!')
        elif 24 < FFMI < 25 and 8 < BF < 20:
            print('You are nearing your genetic ceiling, bulking is not recommended.')
        else:
            print('Your specific body measurements are not\n'
                  'catagorized on the FFMI scale, as a general \n'
                  'rule, if you are over 20% body fat, we recommend \n'
                  'you do not bulk.')
    if SEX == 'female':
        if FFMI < 15 and 20 < BF < 25:
            print('You are skinny, buiking is perfect!')
        elif 15 < FFMI < 17 and 22 < BF < 35:
            print('You are average, bulking is safe!')
        elif 15 < FFMI < 18 and 30 < BF < 45:
            print('You are fat, bulking is not for you.')
        elif 16 < FFMI < 17 and 18 < BF < 25:
            print('You are an moderately lean, bulking is safe!')
        elif 18 < FFMI < 20 and 15 < BF < 22:
            print('You are an extremely lean, bulking is recommended!')
        elif 19 < FFMI < 21 and 15 < BF < 30:
            print('You are basically at your genetic ceiling, bulk if it fits your goals!')
        else:
            print('Your specific body measurements are not\n'
                  'catagorized on the FFMI scale, as a general \n'
                  'rule, if you are over 25% body fat, we recommend \n'
                  'you do not bulk.')

    print('If bulking is the right choice for you, we will move on \n'
            'to calculating daily caloric intake. For this, we will be \n'
            'using the Katch-McArdle Formula to find basal metabolic rate (BMR) \n'
            'and determine the surplus from there. If all that seems complicated \n'
            'do not worry, we will walk you through step by step.')

    BMR = 370 + 21.6 * (100 - BF)
    print('Your BMR is', str(BMR)+'.')
    print('For calculating maintainence calorie intake, we will multiply BMR \n'
          'by PAL (physical activity level). The PAL scale ranges from 1.2 to 2.4. \n'
          '1.2 ==> little or no exercise \n'
          '1.4 ==> light exercise (1-2 times/week) \n'
          '1.6 ==> moderate exercise (2-3 times/week) \n'
          '1.75 ==> hard exercise (3-5 times/week) \n'
          '2.0 ==> physical job or hard exercise (6-7 times/week) \n'
          '2.4 ==> professional athlete')
    while True:
        PAL = input('Please enter a number that best describes your weekly PAL \n'
        'from the options above: ')
        PAL_OPTIONS = ['1.2', '1.4', '1.6', '1.75', '2.0', '2.4']
        if PAL not in PAL_OPTIONS:
            print('Please select a number from the options listed above.')
            continue
        else:
            break

    MAINTAINENCE_CALORIES = float(BMR) * float(PAL)
    rounded_maintainence = round((float(BMR) * float(PAL)), 0)
    print('Your maintainence calories are', str(rounded_maintainence) + '.')
    SURPLUS10 = round((rounded_maintainence * 1.1), 0)
    SURPLUS20 = round((rounded_maintainence * 1.2), 0)
    print('You should begin with a 10% surplus and increase it to 20% if needed.')
    print('Your 10% surplus is', str(SURPLUS10), 'and your 20% surplus is', str(SURPLUS20), ' calories.')

    print('Best of luck on your journey to gettin swole!')
    QUIT = input('To exit, type \'quit\': ')
    if QUIT == 'quit':
        quit()
    else:
        print('You spelled quit wrong.')

# LOSE WEIGHT CODE BLOCK
    
elif GOAL == 'lose weight':
    print('let\'s find out your FFMI to see how quickly you should lose weight.'
          '\nFor this, we will need your height, weight and estimated body fat percentage.')
    while True:
        HEIGHT = (input('Please enter your height in inches: '))
        if HEIGHT.isdigit():
            HEIGHT = float(HEIGHT)
            break
        else:
            print('Please enter a number. ')
            continue
    while True:
        WEIGHT = (input('Please enter your weight in pounds: '))
        if WEIGHT.isdigit():
            WEIGHT = float(WEIGHT)
            break
        else:
            print('Please enter a number. ')
            continue
    while True:
        BF = (input('Please enter your body fat percentage as a whole number: '))
        if BF.isdigit():
            BF = float(BF)
            break
        else:
            print('Please enter a whole number without a percentage sign. ')
            continue
    FFMI = ((WEIGHT * ((100 - BF) / 100)) / 2.2) / (HEIGHT * 0.0254) ** 2
    rounded_FFMI = round(FFMI, 2)
    print('Your FFMI is', str(rounded_FFMI))
    print('Now that we know your FFMI, we will refer to the FFMI scale\n'
          'to see if losing weight is for you.')

    SEX = input('Please enter your sex: (male/female) ').lower()
    while SEX != 'male' and SEX != 'female':
        SEX = input('Please choose either male or female: ) ').lower()
    if SEX == 'male':
        if FFMI < 18 and 10 < BF < 18:
            print('You are skinny, cutting is not recommended.')
        elif 18 < FFMI < 20 and 20 < BF < 27:
            print('You are average, cutting is safe!')
        elif 19 < FFMI < 21 and 25 < BF < 40:
            print('You are fat, cutting is recommended!')
        elif 20 < FFMI < 21 and 10 < BF < 18:
            print('You are an moderately lean, cutting is safe!')
        elif 22 < FFMI < 23 and 6 < BF < 12:
            print('You are an extremely lean, cutting is not recommended.')
        elif 24 < FFMI < 25 and 8 < BF < 20:
            print('You are basically at your genetic ceiling, cut if it fits your goals!')
        else:
            print('Your specific body measurements are not\n'
                  'catagorized on the FFMI scale, as a general \n'
                  'rule, if you are under 12% body fat, we recommend \n'
                  'you do not cut.')
    if SEX == 'female':
        if FFMI < 15 and 20 < BF < 25:
            print('You are skinny, cutting is not recommended.')
        elif 15 < FFMI < 17 and 22 < BF < 35:
            print('You are average, cutting is safe!')
        elif 15 < FFMI < 18 and 30 < BF < 45:
            print('You are fat, cutting perfect!')
        elif 16 < FFMI < 17 and 18 < BF < 25:
            print('You are an moderately lean, cutting is safe!')
        elif 18 < FFMI < 20 and 15 < BF < 22:
            print('You are an extremely lean, cutting is not recommended.')
        elif 19 < FFMI < 21 and 15 < BF < 30:
            print('You are basically at your genetic ceiling, cut if it fits your goals!')
        else:
            print('Your specific body measurements are not\n'
                  'catagorized on the FFMI scale, as a general \n'
                  'rule, if you are under 15% body fat, we recommend \n'
                  'you do not cut.')

    print('If cutting is the right choice for you, we will move on \n'
          'to calculating daily caloric intake. For this, we will be \n'
          'using the Katch-McArdle Formula to find basal metabolic rate (BMR) \n'
          'and determine the deficit from there. If all that seems complicated \n'
          'do not worry, we will walk you through step by step.')

    BMR = 370 + 21.6 * (100 - BF)
    print('Your BMR is', str(BMR) + '.')
    print('For calculating maintenance calorie intake, we will multiply BMR \n'
          'by PAL (physical activity level). The PAL scale ranges from 1.2 to 2.4. \n'
          '1.2 ==> little or no exercise \n'
          '1.4 ==> light exercise (1-2 times/week) \n'
          '1.6 ==> moderate exercise (2-3 times/week) \n'
          '1.75 ==> hard exercise (3-5 times/week) \n'
          '2.0 ==> physical job or hard exercise (6-7 times/week) \n'
          '2.4 ==> professional athlete')
    while True:
        PAL = input('Please enter a number that best describes your weekly PAL \n'
                    'from the options above: ')
        PAL_OPTIONS = ['1.2', '1.4', '1.6', '1.75', '2.0', '2.4']
        if PAL not in PAL_OPTIONS:
            print('Please select a number from the options listed above.')
            continue
        else:
            break

    MAINTENANCE_CALORIES = float(BMR) * float(PAL)
    rounded_maintenance = round((float(BMR) * float(PAL)), 0)
    print('Your maintainence calories are', str(rounded_maintenance) + '.')
    DEF10 = round((rounded_maintenance * 0.9), 0)
    DEF20 = round((rounded_maintenance * 0.8), 0)
    print('You should begin with a 10% surplus and increase it to 20% if needed.')
    print('Your 10% deficit is', str(DEF10), 'and your 20% deficit is', str(DEF20), ' calories.')

    print('Best of luck on your journey to gettin shredded!')
    QUIT = input('To exit, type \'quit\': ')
    if QUIT == 'quit':
        quit()
    else:
        print('You spelled quit wrong.')

# EAT HEALTHIER CODE BLOCK

elif GOAL == 'eat healthier':
    print('Since you are choosing to eat healthier, we want to keep your weight at maintenance.')
    print('let\'s find out your FFMI to determine how many calories you should eat daily.'
          '\nFor this, we will need your height, weight and estimated body fat percentage.')
    while True:
        HEIGHT = (input('Please enter your height in inches: '))
        if HEIGHT.isdigit():
            HEIGHT = float(HEIGHT)
            break
        else:
            print('Please enter a number. ')
            continue
    while True:
        WEIGHT = (input('Please enter your weight in pounds: '))
        if WEIGHT.isdigit():
            WEIGHT = float(WEIGHT)
            break
        else:
            print('Please enter a number. ')
            continue
    while True:
        BF = (input('Please enter your body fat percentage as a whole number: '))
        if BF.isdigit():
            BF = float(BF)
            break
        else:
            print('Please enter a whole number without a percentage sign. ')
            continue
    FFMI = ((WEIGHT * ((100 - BF) / 100)) / 2.2) / (HEIGHT * 0.0254) ** 2
    BMR = 370 + 21.6 * (100 - BF)
    print('Your BMR is', str(BMR) + '.')
    rounded_FFMI = round(FFMI, 2)
    print('Your FFMI is', str(rounded_FFMI))
    print('For calculating maintenance calorie intake, we will multiply BMR \n'
          'by PAL (physical activity level). The PAL scale ranges from 1.2 to 2.4. \n'
          '1.2 ==> little or no exercise \n'
          '1.4 ==> light exercise (1-2 times/week) \n'
          '1.6 ==> moderate exercise (2-3 times/week) \n'
          '1.75 ==> hard exercise (3-5 times/week) \n'
          '2.0 ==> physical job or hard exercise (6-7 times/week) \n'
          '2.4 ==> professional athlete')
    while True:
        PAL = input('Please enter a number that best describes your weekly PAL \n'
                    'from the options above: ')
        PAL_OPTIONS = ['1.2', '1.4', '1.6', '1.75', '2.0', '2.4']
        if PAL not in PAL_OPTIONS:
            print('Please select a number from the options listed above.')
            continue
        else:
            break

    MAINTENANCE_CALORIES = float(BMR) * float(PAL)
    rounded_maintenance = round((float(BMR) * float(PAL)), 0)
    print('Your maintainence calories are', str(rounded_maintenance) + '.')
    PROTEIN_MACROS = rounded_maintenance * 0.2
    FATS_MACROS = rounded_maintenance * 0.2
    CARBS_MACROS = rounded_maintenance * 0.6
    print(str(PROTEIN_MACROS), 'calories should come from protein sources,\n',
    str(FATS_MACROS), 'calories should come from fat sources, \n'
    'and', str(CARBS_MACROS), 'calories should come from carbohydrate sources.')


    PROTEIN_SOURCES = {'Chicken': 141, 'Steak': 158, 'Turkey': 135,
        'Lamb': 172, 'Pork': 122,'Ham': 139, 'Egg': 71, 'Salmon' : 155,
        'Tuna': 99, 'Shrimp' : 101, 'Lobster': 76, 'Scallops': 375,
        'Pinto Beans': 197, 'Adzuki Beans':147, 'Lentils': 101, 'Edamame': 95}

    FAT_SOURCES = {'Avocado': 45, 'Almonds': 45, 'cashews': 45, 'peanuts': 45,
        'pecans': 45,  'walnuts': 45, 'Margarine': 45, 'Mayonnaise': 45, 'Pesto sauce': 45,
        'Salad dressing':45, 'sour cream': 45, 'butter': 45}

    CARB_SOURCES = {'Cereal': 80, 'oatmeal': 80, 'cream of wheat': 80,
        'White Rice': 80, 'brown rice': 80, 'Pasta': 80, 'Bean sprouts': 50,
        'Beets': 50, 'Broccoli': 50, 'Brussels sprouts': 50, 'Cabbage': 50,
        'Carrots': 50, 'Cauliflower': 50, 'Celery': 50, 'Cucumber': 50,
        'Eggplant': 50, 'Greens': 50, 'Lettuce': 50, 'Mushrooms': 50, 'Okra': 50,
        'Onion': 50, 'Pea pods': 50, 'Peppers': 50, 'Radishes': 50, 'Spinach': 50,}

    print('To generate a list of healthy choices for each group of foods, type either\n'
          'protein, carbs, or fats. A list will appear with the name of the food\n'
          'followed by the calories per serving. Use this list to build your own\n'
          'nutrition plan according to the macronutrients. ')
    SEARCH = input('search for proteins, carbs or fats, or quit to exit: ').lower()
    while SEARCH != 'proteins' and SEARCH != 'carbs' and SEARCH != 'fats' and SEARCH != 'quit':
        SEARCH = input('please search for proteins, carbs, or fats or quit to exit. ')
    while True:
        if SEARCH == 'proteins':
            print(PROTEIN_SOURCES)
            SEARCH = input('please search for proteins, carbs, or fats or quit to exit. ')
        elif SEARCH == 'fats':
            print(FAT_SOURCES)
            SEARCH = input('please search for proteins, carbs, or fats or quit to exit. ')
        elif SEARCH == 'carbs':
            print(CARB_SOURCES)
            SEARCH = input('please search for proteins, carbs, or fats or quit to exit. ')
        else:
            quit()
