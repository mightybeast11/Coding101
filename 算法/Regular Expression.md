# Regular expression

Remember to use double backslash for special characters (`\n`) or character classes (`\d`). The first \ is to escape the second \, so we get a valid character class in string by typing `\\d`.

-   Group `(...)`: can be named and reused.
-   Non-capturing group `(?:...)`: this part will be **parsed**, but **not captured** for further use. Check this [page](https://stackoverflow.com/questions/3512471/what-is-a-non-capturing-group-in-regular-expressions) for detailed explanation.