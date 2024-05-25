# Recipe Nutrients and Ingredients Extractor

This Python script extracts the nutrients and ingredients of selected recipes from the given range of URLs.

## Dependencies

This script requires the following Python libraries:
- `requests`
- `beautifulsoup4`

## Installation

You can install the required dependencies using `pip`. Run the following commands:


    pip install requests
    pip install beautifulsoup4

Usage

    Clone this repository or download the script to your local machine.

    Make sure you have Python installed (preferably version 3.6 or higher).

    Install the required dependencies as mentioned in the Installation section.

    Update the starting_number and ending_number variables in the script to the desired range of recipe IDs.

    Run the script. The script will extract nutrients and ingredients for each recipe in urls.



# Define the starting and ending numbers
    starting_number = 10222
    ending_number = 10224

# Generate and append new URLs based on the given range
    for num in range(starting_number, ending_number + 1):
        url = f"https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/{num}"
        if url not in urls:
            urls.append(url)

Example

If you set starting_number = 10222 and ending_number = 10224, the script will generate and print the following list of URLs:

    [
        "https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/10222",
        "https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/10223",
        "https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/10224"
    ]

# Run the script

The script will extract nutrients and ingredients for each recipe in urls.

    Recipe name: Rosemary Tomato Leek Soup
    Protein (g): 18.9595
    Energy (kCal): 512.6146
    Carbohydrates (g): 52.5794
    Total fats (g): 30.6928
    Fatty acids, total saturated 20:0 (g): 0.0000
    Fatty acids, total saturated 18:3 undifferentiated (g): 0.2487
    Fatty acids, total polyunsaturated 17:1 (g): 0.0000
    Fatty acids, total trans-monoenoic (g): 0.0000
    Fatty acids, total saturated 20:4 undifferentiated (g): 0.0000
    Fatty acids, total saturated 4:0 (g): 0.0000
    Fatty acids, total trans (g): 0.0000
    Riboflavin (mg): 0.4861
    Tocopherol, beta (mg): 0.0894
    Lactose (g): 0.0000
    Fatty acids, total saturated 22:5 n-3 (DPA) (g): 0.0000
    Fatty acids, total polyunsaturated 24:1 c (g): 0.0000
    Fatty acids, total saturated 18:4 (g): 0.0000
    Fatty acids, total saturated 18:0 (g): 1.2851
    Tocopherol, delta (mg): 0.0000
    Arginine (g): 1.8077
    Proline (g): 0.6274
    Fatty acids, total polyunsaturated 18:1 t (g): 0.0000
    Campesterol (mg): 0.0000
    Glucose (dextrose) (g): 11.1694
    Adjusted Protein (g): 0.0000
    Cystine (g): 0.3000
    Tocotrienol, beta (mg): 0.0000
    Selenium, Se (g): 0.8348
    Copper, Cu (mg): 1.5164
    Maltose (g): 0.0000
    Zinc, Zn (mg): 4.3792
    Total lipid (fat) (g): 30.6928
    Vitamin K (phylloquinone) (g): 71.0473
    Cholesterol (mg): 0.0000
    Fatty acids, total saturated 22:1 undifferentiated (g): 0.0000
    Fatty acids, total trans-polyenoic 18:3 n-3 c,c,c (ALA) (g): 0.0000
    Menaquinone-4 (g): 0.0000
    Phytosterols (mg): 62.9222
    Folate, total (g): 193.4780
    Fatty acids, total trans-polyenoic 20:3 n-6 (g): 0.0000
    Vitamin A, IU (IU): 7671.2474
    Energy (kcal): 512.6146
    Fatty acids, total saturated 16:1 undifferentiated (g): 0.0964
    Fatty acids, total saturated 14:1 (g): 0.0000
    Vitamin D2 (ergocalciferol) (g): 0.0000
    Methionine (g): 0.4107
    Fatty acids, total saturated 20:5 n-3 (EPA) (g): 0.0000
    Sugars, total (g): 23.6029
    Folic acid (g): 0.0000
    Tocotrienol, alpha (mg): 0.0894
    Vitamin C, total ascorbic acid (mg): 124.5078
    Lutein + zeaxanthin (g): 1159.1730
    Fatty acids, total saturated 22:6 n-3 (DHA) (g): 0.0000
    Vitamin B-12, added (g): 0.0000
    Valine (g): 0.7741
    Fatty acids, total trans-polyenoic 18:1-11 t (18:1t n-7) (g): 0.0000
    Fatty acids, total polyunsaturated 22:1 c (g): 0.0000
    Magnesium, Mg (mg): 157.9749
    Fatty acids, total saturated 16:0 (g): 2.7694
    Carbohydrate, by difference (g): 52.5794
    Vitamin D (IU): 0.0000
    Fructose (g): 12.2417
    Fluoride, F (g): 20.5517
    Aspartic acid (g): 2.2255
    Tyrosine (g): 0.5772
    Potassium, K (mg): 2397.6401
    Fatty acids, total saturated 12:0 (g): 0.0001
    Vitamin A, RAE (g): 386.4569
    Serine (g): 0.8255
    Fatty acids, total trans-polyenoic 21:5 (g): 0.0000
    Phenylalanine (g): 0.8179
    Fatty acids, total trans-polyenoic 22:4 (g): 0.0000
    Alcohol, ethyl (g): 0.0000
    Fatty acids, total polyunsaturated 24:0 (g): 0.0000
    Fatty acids, total saturated 22:0 (g): 0.0000
    Fatty acids, total saturated 14:0 (g): 0.0724
    Histidine (g): 0.4458
    Isoleucine (g): 0.6326
    Fatty acids, total polyunsaturated 18:2 CLAs (g): 0.0000
    Niacin (mg): 8.9411
    Water (g): 849.7032
    Fatty acids, total saturated 8:0 (g): 0.0000
    Tocotrienol, delta (mg): 0.0000
    Theobromine (mg): 0.0000
    Fatty acids, total polyunsaturated 20:2 n-6 c,c (g): 0.0000
    Carotene, beta (g): 4110.6140
    Sodium, Na (mg): 90.1647
    Iron, Fe (mg): 4.0489
    Energy (kJ): 2133.1069
    Ash (g): 7.5790
    Caffeine (mg): 0.0000
    Glycine (g): 0.9130
    Fatty acids, total trans-polyenoic (g): 0.0000
    Fatty acids, total polyunsaturated 18:3 n-6 c,c,c (g): 0.0000
    Fatty acids, total saturated 18:2 undifferentiated (g): 13.1547
    Fatty acids, total polyunsaturated (g): 13.4166
    Vitamin E (alpha-tocopherol) (mg): 4.9639
    Sucrose (g): 0.0000
    Vitamin B-6 (mg): 0.8844
    Fatty acids, total trans-polyenoic 13:0 (g): 0.0000
    Fatty acids, total saturated 6:0 (g): 0.0000
    Vitamin D (D2 + D3) (g): 0.0000
    Vitamin D3 (cholecalciferol) (g): 0.0000
    Lysine (g): 0.5992
    Beta-sitosterol (mg): 0.0000
    Fatty acids, total polyunsaturated 20:3 undifferentiated (g): 0.0000
    Fatty acids, total trans-polyenoic 15:1 (g): 0.0000
    Lycopene (g): 22991.1244
    Starch (g): 0.0000
    Pantothenic acid (mg): 1.2451
    Fatty acids, total trans-polyenoic 20:4 n-6 (g): 0.0000
    Fatty acids, total polyunsaturated 18:2 t,t (g): 0.0000
    Fatty acids, total polyunsaturated 15:0 (g): 0.0000
    Fatty acids, total trans-polyenoic 18:3i (g): 0.0000
    Thiamin (mg): 1.1131
    Folate, food (g): 193.4780
    Fatty acids, total saturated 20:1 (g): 0.0402
    Fatty acids, total monounsaturated (g): 11.1662
    Stigmasterol (mg): 0.0000
    Fatty acids, total polyunsaturated 18:2 n-6 c,c (g): 0.0000
    Fatty acids, total polyunsaturated 16:1 t (g): 0.0000
    Fatty acids, total polyunsaturated 17:0 (g): 0.0000
    Fatty acids, total polyunsaturated 18:2 i (g): 0.0000
    Hydroxyproline (g): 0.0000
    Dihydrophylloquinone (g): 0.0000
    Choline, total (mg): 61.3991
    Fatty acids, total polyunsaturated 16:1 c (g): 0.0000
    Fatty acids, total saturated (g): 4.3031
    Vitamin B-12 (g): 0.0000
    Calcium, Ca (mg): 352.1573
    Fatty acids, total saturated 10:0 (g): 0.0002
    Galactose (g): 0.0000
    Tocotrienol, gamma (mg): 0.0000
    Alanine (g): 0.8073
    Glutamic acid (g): 6.2795
    Fatty acids, total trans-polyenoic 20:3 n-3 (g): 0.0000
    Carotene, alpha (g): 902.4888
    Vitamin E, added (mg): 0.0000
    Retinol (g): 0.0000
    Leucine (g): 1.0590
    Folate, DFE (g): 193.4780
    Fatty acids, total polyunsaturated 22:1 t (g): 0.0000
    Fatty acids, total polyunsaturated 18:2 t not further defined (g): 0.0000
    Fiber, total dietary (g): 16.5426
    Tryptophan (g): 0.2913
    Threonine (g): 0.6935
    Fatty acids, total polyunsaturated 18:1 c (g): 0.0000
    Manganese, Mn (mg): 1.9955
    Protein (g): 18.9595
    Cryptoxanthin, beta (g): 28.1340
    Fatty acids, total saturated 18:1 undifferentiated (g): 11.0182
    Betaine (mg): 0.8936
    Phosphorus, P (mg): 675.5393
    Tocopherol, gamma (mg): 1.0723
    Ingredient: butter, Quantity: 1/4, Unit: cup, State: , Energy: 342.0, Carb: 15.714, Protein: 10.686, Lipids: 28.8
    Ingredient: leek lengthwise, Quantity: 1, Unit: , State: cut washed trimmed sliced, Energy: -, Carb: -, Protein: -, Lipids: -
    Ingredient: rosemary, Quantity: 3, Unit: sprigs, State: stripped, Energy: -, Carb: -, Protein: -, Lipids: -
    Ingredient: garlic, Quantity: 2, Unit: teaspoons, State: minced, Energy: 8.344, Carb: 1.8514, Protein: 0.3562, Lipids: 0.027999999999999997
    Ingredient: tomato, Quantity: 4, Unit: cans, State: diced, Energy: 160.8396, Carb: 34.7592, Protein: 7.8633, Lipids: 1.7871
    Ingredient: cayenne pepper, Quantity: 1/4, Unit: teaspoon, State: , Energy: 1.431, Carb: 0.2548, Protein: 0.054000000000000006, Lipids: 0.0777
    Ingredient: leaf basil, Quantity: 10, Unit: , State: minced, Energy: -, Carb: -, Protein: -, Lipids: -
    Ingredient: heavy whipping cream, Quantity: , Unit: , State: , Energy: -, Carb: -, Protein: -, Lipids: -
    Ingredient: salt black pepper, Quantity: to taste, Unit: , State: ground, Energy: -, Carb: -, Protein: -, Lipids: -

Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

License

This project is licensed under the  GPL-3.0 License. See the LICENSE file for details.
