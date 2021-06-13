## RECIPE APP PROJECT FOR CFG PYTHON COURSE

# imports requests module
import requests

# sets app id and app key for API
# sign up at https://developer.edamam.com/edamam-recipe-api for id and key, and insert here
app_id = ''
app_key = ''

# sets out example input that will be accepted in the recipe selection criteria below
example_cuisineReq = ['American', 'British', 'French', ' Middle Eastern', 'Chinese', 'Mexican', 'Caribbean', 'Indian', 'Italian', 'Japanese', 'Mediterranean']
example_dietReq = ['alcohol-free', 'sugar-conscious', 'gluten-free', 'wheat-free', 'vegetarian', 'vegan']
example_dietRegime = ['balanced', 'high-fiber', 'high-protein', 'low-carb', 'low-fat', 'low-sodium']

# defines variables to be used for including API parameters
includeAppId = 'app_id={}'.format(app_id)
includeAppKey = 'app_key={}'.format(app_key)
includeCuisineReq = ''
includeDietReq = ''
includeDietRegime = ''

# asks user to enter ingredient(s)
ingredient = input('Enter one or more ingredients you want to use: ')
# uses split and join functions to enable selection of more than one ingredient
components = ingredient.split()
items = ',+'.join(components) or 'and+'.join(components) or ' +'.join(components)
ingredients = 'ingredients=' + items
includeIngredients = 'q={}'.format(ingredients)

# asks user to enter cuisine preference (if any)
print('Here are the cuisine options: ' + str(example_cuisineReq))
cuisineReq_ask = input('Do you have a preferred cuisine? Y/N: ')
if cuisineReq_ask == 'Y' or cuisineReq_ask == 'y':
    cuisineReq = input('What is your preferred cuisine? (type exactly as shown) ')
    includeCuisineReq = 'cuisineType={}'.format(cuisineReq)
    cuisineReq_flag = 1
elif cuisineReq_ask == 'N' or cuisineReq_ask == 'n':
    cuisineReq_flag = 0

# asks user to enter dietary requirements (if any)
print('Dietary requirement options: ' + str(example_dietReq))
dietReq_ask = input('Do you have a dietary requirement from the above options? Y/N: ')
if dietReq_ask == 'Y' or dietReq_ask == 'y':
    dietReq = input('What is your dietary requirement? (type exactly as shown) ')
    includeDietReq = 'health={}'.format(dietReq)
    dietReq_flag = 1
elif dietReq_ask == 'N' or dietReq_ask == 'n':
    dietReq_flag = 0

# ask user to enter diet regime (if any)
print('Diet regime options: ' + str(example_dietRegime))
dietRegime_ask = input('Do you have any specific diet regime from the above options? Y/N ')
if dietRegime_ask == 'Y' or dietRegime_ask == 'y':
    dietRegime = input('What is your diet regime? (type exactly as shown) ')
    includeDietRegime = 'diet={}'.format(dietRegime)
    dietRegime_flag = 1
elif dietRegime_ask == 'N' or dietRegime_ask == 'n':
    dietRegime_flag = 0

# pulls API parameters into the url based on user choices, and sets relevant print message for each combo
if dietReq_flag == 1 and dietRegime_flag == 1 and cuisineReq_flag == 1:
    url = 'https://api.edamam.com/search?{}&{}&{}&{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey, includeDietReq, includeDietRegime, includeCuisineReq)
    recipeChoices = 'You searched for {}, {} and {} recipe options, using {} '.format(cuisineReq, dietReq, dietRegime, components)
elif dietReq_flag == 1 and dietRegime_flag == 0 and cuisineReq_flag == 1:
    url = 'https://api.edamam.com/search?{}&{}&{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey, includeDietReq, includeCuisineReq)
    recipeChoices = 'You searched for {} and {} recipe options, using {} '.format(cuisineReq, dietReq, components)
elif dietReq_flag == 0 and dietRegime_flag == 1 and cuisineReq_flag == 1:
    url = 'https://api.edamam.com/search?{}&{}&{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey, includeDietRegime, includeCuisineReq)
    recipeChoices = 'You searched for {} and {} recipe options, using {} '.format(cuisineReq, dietRegime, components)
elif dietReq_flag == 0 and dietRegime_flag == 0 and cuisineReq_flag == 1:
    url = 'https://api.edamam.com/search?{}&{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey, includeCuisineReq)
    recipeChoices = 'You searched for {} recipe options, using {} '.format(cuisineReq, components)
elif dietReq_flag == 1 and dietRegime_flag == 1 and cuisineReq_flag == 0:
    url = 'https://api.edamam.com/search?{}&{}&{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey, includeDietReq, includeDietRegime)
    recipeChoices = 'You searched for {} and {} recipe options, using {} '.format(dietReq, dietRegime, components)
elif dietReq_flag == 1 and dietRegime_flag == 0 and cuisineReq_flag == 0:
    url = 'https://api.edamam.com/search?{}&{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey, includeDietReq)
    recipeChoices = 'You searched for {} recipe options, using {} '.format(dietReq, components)
elif dietReq_flag == 0 and dietRegime_flag == 1 and cuisineReq_flag == 0:
    url = 'https://api.edamam.com/search?{}&{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey, includeDietRegime)
    recipeChoices = 'You searched for {} recipe options, using {} '.format(dietRegime, components)
elif dietReq_flag == 0 and dietRegime_flag == 0 and cuisineReq_flag == 0:
    url = 'https://api.edamam.com/search?{}&{}&{}'.format(includeIngredients, includeAppId, includeAppKey)
    recipeChoices = 'You searched for recipe options, using {} '.format(components)

# tests whether the correct url is showing!
print(url)

# asks user if they have a maximum calorie preference
calories_ask = input('Do you have any calorie requirements (per person)? Y/N: ')
if calories_ask == 'Y' or calories_ask == 'y':
    calories_requirement = int(input('Enter the maximum number of calories per person: '))
elif calories_ask == 'N' or calories_ask == 'n':
    calories_requirement = 100000

# requests and extracts recipes from the API, into the 'results' variable, based on user choices above
results = requests.get(url)
data = results.json()
results = data['hits']

# Printing the results
# prints 'You've searched for {cuisineReq}, {dietReq}, {dietRegime} recipes using {ingredient(s)}'
# based on user's choices/input
print('================================================================================')
print(recipeChoices)
# includes/prints calories requirement if specified by user
if calories_ask == 'Y' or calories_ask == 'y':
    print(f'(under {calories_requirement} calories)')
elif calories_ask == 'N' or calories_ask == 'n':
    pass
# loops through results and adds 1 on each iteration (to count how many results found)
count = 0
for result in results:
    recipe = result['recipe']
    if int((recipe['calories']) / recipe['yield']) <= calories_requirement:
        count = count + 1
# if more than 0 results found, prints 'Here are your recipes'
if count > 0:
    print('Here are your recipes: ')
# else, if less than 0 results, prints 'Sorry, no recipes found' and the program ends here
else:
    print('================================================================================')
    print('Sorry, no recipes found!')
# loops through results again, where more than 0 results found...
for result in results:
    recipe = result['recipe']
    if int((recipe['calories']) / recipe['yield']) <= calories_requirement and count > 0:
        # define recipe info variables, i.e. name, web link, servings, nutrition, total time, and ingredients list
        recipeLabel = recipe['label']
        webLink = recipe['url']
        calories = round(int(recipe['calories'] / recipe['yield']))
        fat = recipe['totalNutrients']['FAT']
        fat_quantity = round(int(fat['quantity'] / recipe['yield']))
        protein = recipe['totalNutrients']['PROCNT']
        protein_quantity = round(int(protein['quantity'] / recipe['yield']))
        y = round(int(recipe['yield']))
        ingredList = recipe['ingredientLines']
        time = round(int(recipe['totalTime']))
        # prints recipe name, web link, servings, and nutrition info
        print('================================================================================')
        print(recipeLabel)
        print(webLink)
        print('Makes ' + str(y) + ' servings')
        print('Contains per serving: ' + str(calories) + ' calories, ' + str(fat_quantity) + 'g fat, ' + str(protein_quantity) + 'g protein')
        # not all recipes include total time, so prints this info only if they do (i.e. total time is more than 0 minutes)
        if time > 0:
            print('Total time: approximately ' + str(time) + ' minutes' )
        else:
            pass
    else:
        pass

# if more than one recipe found, asks user to choose a recipe and prints/saves shopping (ingredients) list to a text file
if count > 0:
    print('================================================================================')
    print('================================================================================')
    chosen_recipe = input('Which recipe do you want to cook? (Copy and paste the recipe as it is): ')
    if chosen_recipe == recipeLabel:
        MyFile=open('Shopping list.txt','w')
        MyFile.write(f'Shopping list: {recipeLabel} ({y} servings) ')
        MyFile.write('\n\n')
        for i in range(0, len(ingredList)):
            MyFile.write(ingredList[i])
            MyFile.write('\n')
        MyFile.write(f'\n(Link to recipe: {webLink})')
        MyFile.close()
        # prints final message to user, confirming shopping list file has been saved and asking if they want to open/print it
        print('================================================================================')
        print(f'Your shopping list for {recipeLabel} has been saved.\n')
        print_recipe = input('Would you like to print your shopping list? Y/N: ')
        print('\n')
        if print_recipe == 'Y' or print_recipe == 'y':
            with open('Shopping list.txt', 'r') as text_file:
                contents = text_file.read()
                print(contents)
        else:
            pass
        print('================================================================================')
        print('Happy cooking, and enjoy your meal!')
    else:
        pass
else:
    pass
