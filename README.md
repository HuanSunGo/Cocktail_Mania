# Cocktail_Mania

For everyone who favors the taste and passionate about cocktail like me, here I created this cocktail information API wrapper, based on **TheCocktailDB**, which is an authorization free API that collects the information for the cocktail. The features involve name, ingredient, description, alcoholic type, latest, popular, etc., in altogether 618 available cocktails.

Supporters can pay $2 each month for better user experience to have access to the upgrade version of API which allows multiple ingredient filters and get special lookups for Popular and Recent cocktails. There's a request limitation for at most 100 per time without the subscription.

Hope you enjoy the usage and get the information you'd want!

API documentation: https://www.thecocktaildb.com/api.php

Base URL:http://www.thecocktaildb.com/api/json/


## Installation

```bash
$ pip install Cocktail_Mania
```

## Usage

`from Cocktail_Mania import Cocktail_Mania`

####  _Get the ID of the Cocktail._
`get_idDrink('Gin')`

####  _Get the ABV (alcohol by volume) of the certain cocktail._
`check_ABV('vodka')`

####  _Get the ingredients with the ID of the Cocktail_
`get_drink_ingredients(178358)`

####  _Choose the right cocktail with the desired ingredient._
`find_all('Tequila', "Gin", "Vodka")`

####  _Return the recommended cocktail with the preferred flavor._
`find_drinks_by_tag('Classic')`


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`Cocktail_Mania` was created by Huan Sun. It is licensed under the terms of the MIT license.

## Credits

`Cocktail_Mania` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
