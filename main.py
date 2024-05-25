import requests
from bs4 import BeautifulSoup

# RECIPE NUMBERS
starting_number = 10222
ending_number = 10224

# IF YOU WANT TO SCRAPE A SINGLE RECIPE, SET STARTING_NUMBER AND ENDING_NUMBER TO THE SAME VALUE
urls = []

for num in range(starting_number, ending_number + 1):
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
    print("\nRecipe name:", recipe_name)

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