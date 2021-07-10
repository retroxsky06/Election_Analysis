# counties = ["Arapahope", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1]

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("oooh you cold boo")

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(counties_dict.get(county))

# for key,  value in dictionary_name.items():
#     print(key, value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}] 

# for county_dict in voting_data:
#     print(county_dict)


# range() function to iterate over the list of dictionaries and print the counties in voting_data
for county in range(len(voting_data)):
      print(voting_data[county]['county'])