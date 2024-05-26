import requests
from bs4 import BeautifulSoup

# RECIPE NUMBERS
starting_number = 10300
ending_number = 10300
my_numbers = [10303, 10400]
# IF YOU WANT TO SCRAPE A SINGLE RECIPE, SET STARTING_NUMBER AND ENDING_NUMBER TO THE SAME VALUE,
# IF YOU WANT TO SCRAPE MULTIPLE RECIPES NOT IN ORDER INSERT THEM IN MY_NUMBERS THEN SET IN_ORDER TO FALSE
in_order = False
urls = []

if in_order:
    for num in range(starting_number, ending_number + 1):
        url = f"https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/{num}"
        if url not in urls:
            urls.append(url)
else:
    for num in my_numbers:
        url = f"https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/{num}"
        if url not in urls:
            urls.append(url)


for url in urls:
    response = requests.get(url)
    html_content = response.content

    # INIT
    soup = BeautifulSoup(html_content, "html.parser")

    # RECIPE NAME
    recipe_name = soup.find("h3").text.strip()
    print("\nURL:", url)
    print("Recipe name:", recipe_name)

    # NUTRIENTS
    nutrient_table = soup.find("table", {"class": "highlight striped"})
    if nutrient_table:
        nutrient_rows = nutrient_table.find_all("tr")
        for row in nutrient_rows[1:]:
            nutrient_name = row.find_all("td")[0].text.strip()
            nutrient_value = row.find_all("td")[1].text.strip()
            print(f"{nutrient_name}: {nutrient_value}")

    # INGREDIENTS
    ingredient_table = soup.find("div", {"id": "ingredient_nutri"})
    if ingredient_table:
        ingredient_rows = ingredient_table.find("table").find_all("tr")
        for row in ingredient_rows[1:]:
            ingredient_name = row.find_all("td")[0].text.strip()
            ingredient_quantity = row.find_all("td")[1].text.strip()
            ingredient_unit = row.find_all("td")[2].text.strip()
            ingredient_state = row.find_all("td")[3].text.strip()
            ingredient_energy = row.find_all("td")[4].text.strip()
            ingredient_carb = row.find_all("td")[5].text.strip()
            ingredient_protein = row.find_all("td")[6].text.strip()
            ingredient_lipids = row.find_all("td")[7].text.strip()

            print(f"Ingredient: {ingredient_name}, Quantity: {ingredient_quantity}, Unit: {ingredient_unit}, State: {ingredient_state}, Energy: {ingredient_energy}, Carb: {ingredient_carb}, Protein: {ingredient_protein}, Lipids: {ingredient_lipids}")