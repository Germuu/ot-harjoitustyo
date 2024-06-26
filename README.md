# RecipeGeneratorApp
This application aims to simplify the often tedious task of deciding what to cook. Users can create and manage their recipe collections, making meal planning more efficient and enjoyable.

## DOCUMENTATION
[Manual](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/manual.md)

[Requirement specification](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/requirement_specification.md)

[Tuntikirjanpito](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/tuntikirjanpito.md)

[Changelog](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/changelog.md)

[Testing](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/testing.md)

[Architecture](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/architecture.md)

[Final release](https://github.com/Germuu/ot-harjoitustyo/releases/tag/final_release)

## USE

1. Install dependencies using the following command:
   ```bash
   poetry install

2. Initialize database using following command:
   ```bash
   poetry run invoke build

3. Start the login window
   ```bash
   poetry run invoke start

**Note : When creating a recipe, ingredients must be comma separated**
   

## TESTING
   ```bash
   poetry run invoke test
   ```

## COVERAGE
  ```bash
   poetry run invoke coverage-report
  ```
## PYLINT
  ```bash
   poetry run invoke lint
  ```





 






