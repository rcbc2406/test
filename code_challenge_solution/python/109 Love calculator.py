print("Love Calculator")
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

combined_name = name1 + name2

lower_combined_name = combined_name.lower()

true_count = 0
for letter in "true":
    true_count += lower_combined_name.count(letter)

love_count = 0
for letter in "love":
    love_count += lower_combined_name.count(letter)

percentage = (true_count + love_count) * 10

print("Love Percentage: " + str(percentage) + "%")