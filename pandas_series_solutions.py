"""Pandas Series practice: solutions for 30 lab questions."""

import pandas as pd

def show_question(number, title):
    print("\n" + "=" * 68)
    print(f"Question {number}: {title}")
    print("=" * 68)

# Section A - Easy

show_question(1, "Create a Pandas Series named sales containing the values 120, 150, 180 and 210.")
sales = pd.Series([120, 150, 180, 210], name="sales")
print(sales)

# Note: A Series is created with the default index 0, 1, 2 and 3.

show_question(2, "For the Series below, display only the stored data values.")
marks = pd.Series([72, 81, 69, 90])
print(marks.values)

# Note: The values attribute returns the data without the index labels.

show_question(3, "For the same Series marks, display its index.")
marks = pd.Series([72, 81, 69, 90])
print(marks.index)

# Note: The index attribute shows the labels of the Series.

show_question(4, "Create a Series of temperatures 28, 31, 30 and 29 using the index labels Mon, Tue, Wed and Thu.")
temperatures = pd.Series([28, 31, 30, 29], index=["Mon", "Tue", "Wed", "Thu"])
print(temperatures)

# Note: The day names are used as the index labels.

show_question(5, "Retrieve the population value for Jaipur from the given Series.")
population = pd.Series([35, 42, 31], index=["Delhi", "Mumbai", "Jaipur"])
print(population["Jaipur"])

# Note: A value can be selected by writing its index label inside square brackets.

show_question(6, "Display only the values greater than 50 from the Series score.")
score = pd.Series([35, 68, 44, 79, 52])
print(score[score > 50])

# Note: The condition creates a Boolean mask, which is used to filter the Series.

show_question(7, "Check whether the label Chemistry is present in the index of subjects.")
subjects = pd.Series([76, 83, 91], index=["Physics", "Chemistry", "Maths"])
print("Chemistry" in subjects.index)

# Note: Using `in` with the index checks for a label, not a stored value.

show_question(8, "Write the Series method that converts a Series into a Python dictionary.")
values = pd.Series([25, 40, 18], index=["Item1", "Item2", "Item3"])
print(values.to_dict())

# Note: The method is `to_dict()`.

show_question(9, "Convert the given prices dictionary into a Pandas Series named price_series.")
prices = {"Pen": 10, "Notebook": 55, "Bag": 700}
price_series = pd.Series(prices, name="price_series")
print(price_series)

# Note: The dictionary keys become the Series index.

show_question(10, "When a dictionary is converted into a Series without separately specifying an index, what becomes the Series index?")
prices = {"Pen": 10, "Notebook": 55, "Bag": 700}
price_series = pd.Series(prices)
print(price_series.index)

# Note: The dictionary keys become the index labels.

show_question(11, "Identify the label that will have a missing value in the following Series.")
data = {"A": 10, "B": 20, "C": 30}
s = pd.Series(data, index=["A", "B", "C", "D"])
print(s)
print("Missing label:", s[s.isna()].index.tolist())

# Note: D is not present in the dictionary, so its value becomes NaN.

show_question(12, "Use isnull to identify missing values in a Series named s.")
s = pd.Series([10, None, 30])
print(pd.isnull(s))

# Note: `pd.isnull(s)` returns True wherever a value is missing.

show_question(13, "Use notnull to identify non-missing values in a Series named s.")
s = pd.Series([10, None, 30])
print(pd.notnull(s))

# Note: `pd.notnull(s)` returns True wherever a value is present.

show_question(14, "Assign the name Monthly Sales to a Series named sales.")
sales = pd.Series([120, 150, 180, 210])
sales.name = "Monthly Sales"
print(sales.name)

# Note: The name property stores the Series name.

show_question(15, "Assign the name Month to the index of a Series named sales.")
sales = pd.Series([120, 150, 180], index=["Jan", "Feb", "Mar"])
sales.index.name = "Month"
print(sales)

# Note: The index.name property assigns a name to the index.

# Section B - Medium

show_question(16, "Predict which labelled entries are returned by s[s > 30].")
s = pd.Series([18, 45, 27, 61], index=["P", "Q", "R", "S"])
print(s[s > 30])

# Note: Only Q (45) and S (61) are greater than 30.

show_question(17, "Predict both membership tests. Membership is checked against the Series index.")
s = pd.Series([500, 600, 700], index=["East", "West", "North"])
print("West" in s)
print(500 in s)

# Note: West is an index label, so the first result is True. 500 is a value, not a label, so the second result is False.

show_question(18, "Create a Series from city_data using the ordered index Delhi, Kochi, Pune, Chennai. Identify the label that receives NaN.")
city_data = {"Delhi": 80, "Pune": 65, "Kochi": 70}
city_series = pd.Series(city_data, index=["Delhi", "Kochi", "Pune", "Chennai"])
print(city_series)

# Note: Chennai receives NaN because it is not a key in the dictionary.

show_question(19, "Show the Boolean output of pd.isnull(s) for W, X, Y and Z.")
s = pd.Series({"W": 5, "X": 10, "Y": 15}, index=["W", "X", "Y", "Z"])
print(pd.isnull(s))

# Note: The output is False for W, X and Y, and True for Z.

show_question(20, "Show the Boolean output of pd.notnull(s) for W, X, Y and Z.")
s = pd.Series({"W": 5, "X": 10, "Y": 15}, index=["W", "X", "Y", "Z"])
print(pd.notnull(s))

# Note: The output is True for W, X and Y, and False for Z.

show_question(21, "Predict the result of adding s1 and s2. Show the result for labels A, B and C.")
s1 = pd.Series([10, 20, 30], index=["A", "B", "C"])
s2 = pd.Series([1, 2, 3], index=["C", "A", "B"])
print(s1 + s2)

# Note: Pandas matches the labels before adding: A = 10 + 2, B = 20 + 3 and C = 30 + 1.

show_question(22, "Explain why adding these Series produces missing values for some labels.")
s1 = pd.Series({"A": 12, "B": 18})
s2 = pd.Series({"B": 5, "C": 9})
print(s1 + s2)

# Note: Pandas aligns by index. A is missing from s2 and C is missing from s1, so both results are NaN. Only B has values in both Series.

show_question(23, "Convert stock to a dictionary named stock_dict and then create a new Series named stock2 from it.")
stock = pd.Series([25, 40, 18], index=["Item1", "Item2", "Item3"])
stock_dict = stock.to_dict()
stock2 = pd.Series(stock_dict, name="stock2")
print(stock_dict)
print(stock2)

# Note: The dictionary keeps the labels as keys, so stock2 is rebuilt with the same labelled values.

show_question(24, "Create a Series from marks using the index order History, English, Science, Maths. Display only values greater than 70.")
marks_data = {"Maths": 88, "Science": 74, "English": 69, "History": 81}
subject_marks = pd.Series(marks_data, index=["History", "English", "Science", "Maths"])
print(subject_marks[subject_marks > 70])

# Note: History (81), Science (74) and Maths (88) are greater than 70.

show_question(25, "Assign Revenue as the Series name and Branch as the index name for a Series object called rev.")
rev = pd.Series([450, 620, 510], index=["North", "South", "East"])
rev.name = "Revenue"
rev.index.name = "Branch"
print(rev)

# Note: The two assignments are `rev.name = "Revenue"` and `rev.index.name = "Branch"`.

# Section C - Hard

show_question(26, "Find the result of total for every label and explain how index alignment determines each value.")
north = pd.Series({"Jan": 40, "Feb": 55, "Mar": 60})
south = pd.Series({"Feb": 20, "Mar": 25, "Apr": 30})
total = north + south
print(total)

# Note: The combined index contains Jan, Feb, Mar and Apr. Feb = 55 + 20 = 75 and Mar = 60 + 25 = 85. Jan and Apr are NaN because one Series has no value for each of those labels.

show_question(27, "Answer all parts: identify the label with NaN, its isnull result, why it is missing, and which labels have numeric values.")
d = {"Red": 12, "Blue": 18, "Green": 24}
labels = ["Green", "Red", "Yellow", "Blue"]
result = pd.Series(d, index=labels)
print(result)
print(pd.isnull(result))

# Note: Yellow contains NaN. `pd.isnull(result)` is True for Yellow because it is not a key in d. Green, Red and Blue retain numeric values.

show_question(28, "Trace the transformation and state the index and values of s2. Do s and s2 represent the same labelled data?")
s = pd.Series([90, 75, 82], index=["Ravi", "Aman", "Neha"])
d = s.to_dict()
s2 = pd.Series(d)
print("Dictionary:", d)
print("s2:")
print(s2)
print("Same labelled data:", s.equals(s2))

# Note: s2 has index Ravi, Aman, Neha and values 90, 75, 82. It represents the same labelled data as s.

show_question(29, "Write a short program for four products and sales. Display values and index, select one label, filter sales above 500, check a label and convert the Series to a dictionary.")
product_sales = pd.Series(
    [750, 320, 620, 450],
    index=["Laptop", "Mouse", "Keyboard", "Headphones"]
)

print("Values:", product_sales.values)
print("Index:", product_sales.index)
print("Laptop sales:", product_sales["Laptop"])
print("Sales above 500:")
print(product_sales[product_sales > 500])
print("Is Mouse present?", "Mouse" in product_sales.index)
sales_dict = product_sales.to_dict()
print("Dictionary:", sales_dict)

# Note: This example uses label selection, Boolean filtering, index membership and to_dict().

show_question(30, "Answer all parts: index order, NaN label, result of s[s > 20], pd.notnull(s), Series name and index name.")
data = {"A": 15, "B": 35, "C": 25}
s = pd.Series(data, index=["C", "A", "D", "B"])
s.name = "Observations"
s.index.name = "Category"

print(s)
print("Values greater than 20:")
print(s[s > 20])
print("Non-missing values:")
print(pd.notnull(s))
print("Series name:", s.name)
print("Index name:", s.index.name)

# Note: The index order is C, A, D, B. D contains NaN. The filter returns C (25) and B (35). notnull is True for C, A and B, and False for D. The Series name is Observations and the index name is Category.
