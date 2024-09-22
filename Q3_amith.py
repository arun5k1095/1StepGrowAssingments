# Q3
# Task:
# Add a new city "San Francisco" with a population of 883305 and country "USA".
# Update the population of "Chicago" to 2800000.
# Remove the city "Phoenix" from the dictionary.
# Add a new key "Mayor" with the value "Bill de Blasio" to the "New York" dictionary.
# Nested dictionary containing city details
city_details = {"New York": {"Population": 8419000, "Country": "USA"},
                "Los Angeles": {"Population": 3980000, "Country": "USA"},
                "Chicago": {"Population": 2716000, "Country": "USA"},
                "Houston": {"Population": 2328000, "Country": "USA"},
                "Phoenix": {"Population": 1690000, "Country": "USA"}}

# 1. Add a new city "San Francisco"
city_details["San Francisco"] = {"Population": 883305, "Country": "USA"}

# 2. Update the population of "Chicago" to 2800000
city_details["Chicago"]["Population"] = 2800000

# 3. Remove the city "Phoenix"
city_details.pop("Phoenix")

# 4. Add a new key "Mayor" to "New York"
city_details["New York"]["Mayor"] = "Bill de Blasio"

# Print the updated city details
print("Updated city details:", city_details)
# Explanation:
# We add a new entry for "San Francisco" to the dictionary.
# We update the population for "Chicago" by accessing the "Population" key.
# We remove "Phoenix" from the dictionary using the pop() method.
# Finally, we add a new "Mayor" key to the "New York" dictionary and print the updated dictionary.

import java.util.HashMap;
import java.util.Map;

# public class CityDetails {
#     public static void main(String[] args) {
#         // Creating a HashMap to store city details
#         Map<String, Map<String, Object>> cityDetails = new HashMap<>();
#
#         // Populating the HashMap
#         cityDetails.put("New York", new HashMap<>(Map.of("Population", 8419000, "Country", "USA")));
#         cityDetails.put("Los Angeles", new HashMap<>(Map.of("Population", 3980000, "Country", "USA")));
#         cityDetails.put("Chicago", new HashMap<>(Map.of("Population", 2716000, "Country", "USA")));
#         cityDetails.put("Houston", new HashMap<>(Map.of("Population", 2328000, "Country", "USA")));
#         cityDetails.put("Phoenix", new HashMap<>(Map.of("Population", 1690000, "Country", "USA")));
#
#         // 1. Add a new city "San Francisco"
#         cityDetails.put("San Francisco", new HashMap<>(Map.of("Population", 883305, "Country", "USA")));
#
#         // 2. Update the population of "Chicago" to 2800000
#         cityDetails.get("Chicago").put("Population", 2800000);
#
#         // 3. Remove the city "Phoenix"
#         cityDetails.remove("Phoenix");
#
#         // 4. Add a new key "Mayor" to "New York" city
#         cityDetails.get("New York").put("Mayor", "Bill de Blasio");
#
#         // Print the updated city details
#         System.out.println("Updated city details: " + cityDetails);
#     }
# }
