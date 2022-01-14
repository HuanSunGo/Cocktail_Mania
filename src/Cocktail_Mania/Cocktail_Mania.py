import pandas as pd
import requests
import os
import re
import json 

def get_idDrink(key_words):
    
    '''
    This function return the unique cocktail ID that supports further query.

    Parameters
    ----------
    key_words: String type key words that contains part of the name of the cocktail.

    Returns
    -------------
    return_table: One dataframe containing the name, strDrink, Category, Alcoholic, Glass, Instructions and Picture.

    Example:
    -------------
    >>>get_idDrink('Mango')
    >>>[OUT]
        strDrink	            strDrinkThumb	                                   idDrink	Alcoholic
    360	Mango Mojito	        https://www.thecocktaildb.com/images/media/dri...	178358	True
    31	Lassi-Mango	            https://www.thecocktaildb.com/images/media/dri...	12698	False
    37	Mango Orange Smoothie	https://www.thecocktaildb.com/images/media/dri...	12716	False
    '''
    
    # Get the full list of drinks by using the alcoholic/non-alcoholic filter
    alcoholic_drinks = requests.get('http://www.thecocktaildb.com/api/json/v2/9973533/filter.php?a=Alcoholic').json()
    non_alcoholic_drinks = requests.get('http://www.thecocktaildb.com/api/json/v2/9973533/filter.php?a=Non_Alcoholic').json()
    
    alcoholic_drinks_df = pd.DataFrame(alcoholic_drinks['drinks'])
    alcoholic_drinks_df['Alcoholic']=True
    non_alcoholic_drinks_df = pd.DataFrame(non_alcoholic_drinks['drinks'])
    non_alcoholic_drinks_df['Alcoholic']=False
    all_drinks_df = pd.concat([alcoholic_drinks_df, non_alcoholic_drinks_df])
    all_drinks_df
    
    #Slice the dataframe that contains the entered key words, return a df with the idDrink information.
    return_table=all_drinks_df[all_drinks_df['strDrink'].str.contains(f'{key_words}')]
    
    return return_table

def check_ABV(name):    
    """
    A function to get the ABV (alcohol by volume) given the name of the cocktail.
    
    Parameters
    ----------
    name: The name of the cocktail in string format.
    
    Returns
    ----------
    abv: The alcohol by volume for the designited cocktail.
    
    Examples
    ----------
    >>> check_ABV('vodka')
    [OUT] '40'
    """
    base_url='http://www.thecocktaildb.com/api/json/v2/9973533/search.php?'
    url=base_url+f'i={name}'
    
    try:
        r = requests.get(url).json()    
        # If the response was successful, no Exception will be raised
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        pass
    
    abv=r['ingredients'][0]['strABV']
    
    return abv

def get_drink_ingredients(idDrink):
    """
    A function to get all the ingredients of a cocktail given the idDrink.
    
    Parameters
    ----------
    idDrink: The unique cocktail ID that can conduct query properly.
    
    Returns
    ----------
    ingredients: A list of all the ingredients of this cocktail.
    
    Examples
    ----------
    >>> get_drink_ingredients(178358)
    [OUT] ['Lime','Mango','Mint','White Rum','Ice','Soda Water','Mango']
    """
    
    def get_drink(idDrink):
        url = f'http://www.thecocktaildb.com/api/json/v2/9973533/lookup.php?i={idDrink}'
        response=requests.get(url).json()
        return response
        
    drink_json = get_drink(idDrink)['drinks'][0]
    ingredients = []
    for i in range(1,16):
        ingredient = drink_json[f"strIngredient{i}"]
        if ingredient:
            ingredients.append(ingredient)
            
    return ingredients

def find_all(*ingredients):
    """
    A function to get the information of cocktails with the desired ingredients.
    
    Parameters
    ----------
    *ingredients: Input should have at least one ingredient.
    
    Returns
    ----------
    drinks: A Dataframe that exhibits all the possible drinks that has the listed ingredients.
    
    Examples
    ----------
    >>> find_all('Tequila', "Gin", "Vodka")
    [OUT]   strDrink	                       idDrink
        0	3-Mile Long Island Iced Tea	        15300
        1	Cherry Electric Lemonade	        17,174
        2	Long Island Iced Tea	            17204
        3	Long Island Tea                     11002
        4	Radioactive Long Island Iced Tea	16,984
    """
    
    url=f"http://www.thecocktaildb.com/api/json/v2/9973533/filter.php?i={','.join(ingredients)}" 
    response=requests.get(url).json()
    if not isinstance(response['drinks'], list):
        return pd.DataFrame()
    drinks=pd.DataFrame(response['drinks']).drop(columns='strDrinkThumb')
    
    return drinks

def find_drinks_by_tag(flavor):
    """
    A function to get all the ingredients of a cocktail given the idDrink.
    
    Parameters
    ----------
    flavor: The desired flavor in the string format.
    
    Returns
    ----------
    recommend_with_flavor: A Dataframe with the full information of the recommended cocktail according to the provided flavor.
    
    """
    flavor = flavor.lower()
    popular_drinks=requests.get('http://www.thecocktaildb.com/api/json/v2/9973533/popular.php').json()['drinks']
    matching_drinks = []
    for drink in popular_drinks:
        if not drink['strTags']:
            continue?
        if flavor in drink['strTags'].lower():
            matching_drinks.append(drink)
    
    recommend_with_flavor=pd.DataFrame(matching_drinks)
    
    return recommend_with_flavor