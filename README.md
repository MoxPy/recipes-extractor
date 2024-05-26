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

    Update the starting_number and ending_number variables in the script to the desired range of recipe IDs or add your recipe's IDs to my_numbers.

    Choose your scraping mode by setting in_order to True or False.

    Run the script. The script will extract nutrients and ingredients for each recipe in urls.



# Define the starting and ending numbers
    starting_number = 10222
    ending_number = 10224

# Or define your numbers
    my_numbers = [10303, 10400]

# Set in_order to choose your scraping mode
You can choose to use a range of numbers (starting_number and ending_number) or a list of defined numbers (my_numbers) by setting in_order variable to True or False

    in_order = False

# Generate and append new URLs based on the given range
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

Example

If you set starting_number = 10222 and ending_number = 10224, the script will generate and print the following list of URLs:

    [
        "https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/10222",
        "https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/10223",
        "https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/10224"
    ]

# Run the script

The script will extract nutrients and ingredients for each recipe in urls.

    URL: https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/10303
    Recipe name: Provincial Tomatoes
    Protein (g): 23.0334
    Energy (kCal): 442.246
    Carbohydrates (g): 50.0753
    Total fats (g): 17.719
    Fatty acids, total saturated 20:0 (g): 0.0559
    Fatty acids, total saturated 18:3 undifferentiated (g): 0.1936
    Fatty acids, total polyunsaturated 17:1 (g): 0.0169
    Fatty acids, total trans-monoenoic (g): 0.0000
    Fatty acids, total saturated 20:4 undifferentiated (g): 0.0000
    Fatty acids, total saturated 4:0 (g): 0.0648
    Fatty acids, total trans (g): 0.0000
    Riboflavin (mg): 0.2054
    Tocopherol, beta (mg): 0.0620
    Lactose (g): 0.0000
    Fatty acids, total saturated 22:5 n-3 (DPA) (g): 0.0000
    Fatty acids, total polyunsaturated 24:1 c (g): 0.0000
    Fatty acids, total saturated 18:4 (g): 0.0000
    Fatty acids, total saturated 18:0 (g): 0.6810
    Tocopherol, delta (mg): 0.0486
    Arginine (g): 0.2347
    Proline (g): 0.4396
    Fatty acids, total polyunsaturated 18:1 t (g): 0.0000
    Campesterol (mg): 0.0000
    Glucose (dextrose) (g): 5.0414
    Adjusted Protein (g): 0.0000
    Cystine (g): 0.1090
    Tocotrienol, beta (mg): 0.0000
    Selenium, Se (g): 24.1316
    Copper, Cu (mg): 0.3029
    Maltose (g): 0.5184
    Zinc, Zn (mg): 2.2916
    Total lipid (fat) (g): 17.7190
    Vitamin K (phylloquinone) (g): 163.4650
    Cholesterol (mg): 8.0000
    Fatty acids, total saturated 22:1 undifferentiated (g): 0.0000
    Fatty acids, total trans-polyenoic 18:3 n-3 c,c,c (ALA) (g): 0.0000
    Menaquinone-4 (g): 0.0000
    Phytosterols (mg): 57.8550
    Folate, total (g): 105.0420
    Fatty acids, total trans-polyenoic 20:3 n-6 (g): 0.0000
    Vitamin A, IU (IU): 3732.7440
    Energy (kcal): 442.2460
    Fatty acids, total saturated 16:1 undifferentiated (g): 0.2184
    Fatty acids, total saturated 14:1 (g): 0.0000
    Vitamin D2 (ergocalciferol) (g): 0.0000
    Methionine (g): 0.0876
    Fatty acids, total saturated 20:5 n-3 (EPA) (g): 0.0000
    Sugars, total (g): 11.9118
    Folic acid (g): 22.1400
    Tocotrienol, alpha (mg): 0.0391
    Vitamin C, total ascorbic acid (mg): 59.9760
    Lutein + zeaxanthin (g): 870.3560
    Fatty acids, total saturated 22:6 n-3 (DHA) (g): 0.0000
    Vitamin B-12, added (g): 0.0000
    Valine (g): 0.2406
    Fatty acids, total trans-polyenoic 18:1-11 t (18:1t n-7) (g): 0.0000
    Fatty acids, total polyunsaturated 22:1 c (g): 0.0000
    Magnesium, Mg (mg): 71.4500
    Fatty acids, total saturated 16:0 (g): 2.3065
    Carbohydrate, by difference (g): 50.0753
    Vitamin D (IU): 0.0000
    Fructose (g): 5.6510
    Fluoride, F (g): 8.3720
    Aspartic acid (g): 0.7205
    Tyrosine (g): 0.1647
    Potassium, K (mg): 1197.8390
    Fatty acids, total saturated 12:0 (g): 0.0560
    Vitamin A, RAE (g): 200.8760
    Serine (g): 0.2836
    Fatty acids, total trans-polyenoic 21:5 (g): 0.0000
    Phenylalanine (g): 0.2862
    Fatty acids, total trans-polyenoic 22:4 (g): 0.0000
    Alcohol, ethyl (g): 0.0000
    Fatty acids, total polyunsaturated 24:0 (g): 0.0000
    Fatty acids, total saturated 22:0 (g): 0.0174
    Fatty acids, total saturated 14:0 (g): 0.2014
    Histidine (g): 0.1355
    Isoleucine (g): 0.2214
    Fatty acids, total polyunsaturated 18:2 CLAs (g): 0.0000
    Niacin (mg): 4.1332
    Water (g): 355.9165
    Fatty acids, total saturated 8:0 (g): 0.0224
    Tocotrienol, delta (mg): 0.0000
    Theobromine (mg): 0.0000
    Fatty acids, total polyunsaturated 20:2 n-6 c,c (g): 0.0000
    Carotene, beta (g): 2023.6640
    Sodium, Na (mg): 680.3660
    Iron, Fe (mg): 4.8337
    Energy (kJ): 1845.7110
    Ash (g): 5.3221
    Caffeine (mg): 0.0000
    Glycine (g): 0.2120
    Fatty acids, total trans-polyenoic (g): 0.0000
    Fatty acids, total polyunsaturated 18:3 n-6 c,c,c (g): 0.0000
    Fatty acids, total saturated 18:2 undifferentiated (g): 2.1690
    Fatty acids, total polyunsaturated (g): 2.3627
    Vitamin E (alpha-tocopherol) (mg): 3.9974
    Sucrose (g): 0.0000
    Vitamin B-6 (mg): 0.3707
    Fatty acids, total trans-polyenoic 13:0 (g): 0.0000
    Fatty acids, total saturated 6:0 (g): 0.0384
    Vitamin D (D2 + D3) (g): 0.0000
    Vitamin D3 (cholecalciferol) (g): 0.0000
    Lysine (g): 0.2282
    Beta-sitosterol (mg): 0.0000
    Fatty acids, total polyunsaturated 20:3 undifferentiated (g): 0.0000
    Fatty acids, total trans-polyenoic 15:1 (g): 0.0000
    Lycopene (g): 9365.7200
    Starch (g): 16.1082
    Pantothenic acid (mg): 0.5034
    Fatty acids, total trans-polyenoic 20:4 n-6 (g): 0.0000
    Fatty acids, total polyunsaturated 18:2 t,t (g): 0.0000
    Fatty acids, total polyunsaturated 15:0 (g): 0.0000
    Fatty acids, total trans-polyenoic 18:3i (g): 0.0000
    Thiamin (mg): 0.4223
    Folate, food (g): 82.9020
    Fatty acids, total saturated 20:1 (g): 0.0724
    Fatty acids, total monounsaturated (g): 10.8395
    Stigmasterol (mg): 0.0000
    Fatty acids, total polyunsaturated 18:2 n-6 c,c (g): 0.0000
    Fatty acids, total polyunsaturated 16:1 t (g): 0.0000
    Fatty acids, total polyunsaturated 17:0 (g): 0.0030
    Fatty acids, total polyunsaturated 18:2 i (g): 0.0000
    Hydroxyproline (g): 0.0000
    Dihydrophylloquinone (g): 0.2970
    Choline, total (mg): 35.5033
    Fatty acids, total polyunsaturated 16:1 c (g): 0.0000
    Fatty acids, total saturated (g): 3.5448
    Vitamin B-12 (g): 0.5345
    Calcium, Ca (mg): 416.4330
    Fatty acids, total saturated 10:0 (g): 0.0504
    Galactose (g): 0.0000
    Tocotrienol, gamma (mg): 0.2808
    Alanine (g): 0.2435
    Glutamic acid (g): 2.7009
    Fatty acids, total trans-polyenoic 20:3 n-3 (g): 0.0000
    Carotene, alpha (g): 367.6400
    Vitamin E, added (mg): 0.0000
    Retinol (g): 15.6000
    Leucine (g): 0.3665
    Folate, DFE (g): 120.4320
    Fatty acids, total polyunsaturated 22:1 t (g): 0.0000
    Fatty acids, total polyunsaturated 18:2 t not further defined (g): 0.0000
    Fiber, total dietary (g): 5.8338
    Tryptophan (g): 0.0689
    Threonine (g): 0.2229
    Fatty acids, total polyunsaturated 18:1 c (g): 0.0000
    Manganese, Mn (mg): 0.6753
    Protein (g): 23.0334
    Cryptoxanthin, beta (g): 0.0000
    Fatty acids, total saturated 18:1 undifferentiated (g): 10.5309
    Betaine (mg): 0.3775
    Phosphorus, P (mg): 416.3180
    Tocopherol, gamma (mg): 0.7943
    Ingredient: tomato, Quantity: 2, Unit: , State: cut, Energy: 65.52, Carb: 14.1596, Protein: 3.2032, Lipids: 0.728
    Ingredient: salt pepper, Quantity: to taste, Unit: , State: , Energy: -, Carb: -, Protein: -, Lipids: -
    Ingredient: olive oil, Quantity: 1, Unit: tablespoon, State: , Energy: 119.34, Carb: 0.0, Protein: 0.0, Lipids: 13.5
    Ingredient: parmesan cheese, Quantity: 1/2, Unit: cup, State: grated, Energy: 148.0, Carb: 16.0, Protein: 16.0, Lipids: 2.0
    Ingredient: asiago cheese, Quantity: 1/4, Unit: cup, State: grated, Energy: -, Carb: -, Protein: -, Lipids: -
    Ingredient: bread crumb, Quantity: 1/4, Unit: cup, State: , Energy: 106.65, Carb: 19.4346, Protein: 3.6045, Lipids: 1.431
    Ingredient: parsley, Quantity: 2, Unit: tablespoons, State: , Energy: 2.736, Carb: 0.4811, Protein: 0.2257, Lipids: 0.06

## Disclaimer

This tool is provided for educational and informational purposes only. The creator of this tool does not take any responsibility for any misuse or damage caused by the use of this tool. Users are solely responsible for ensuring that their use of this tool complies with all applicable laws and regulations.

Web scraping can be against the terms of service of some websites. It is your responsibility to check the terms of service of any website you intend to scrape and to comply with them. The creator of this tool is not liable for any legal consequences arising from the use of this tool.

By using this tool, you agree to indemnify and hold harmless the creator from any claims, damages, or expenses resulting from your use of the tool.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the  GPL-3.0 License. See the LICENSE file for details.
