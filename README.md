# Times Ten Dictionary Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that creates a dictionary mapping integers within a specified range to their values multiplied by ten. This solution demonstrates fundamental dictionary creation, range iteration, and key-value pair mapping concepts.

---

## 📖 Problem Description

Write a function `times_ten(start_index: int, end_index: int)` that creates and returns a new dictionary. The keys should be numbers between `start_index` and `end_index` (inclusive), and each value should be the corresponding key multiplied by ten.

### Requirements
- Create a dictionary with integer keys in the specified range
- Map each key to its value times ten
- Include both start_index and end_index in the range (inclusive)
- Return the completed dictionary

### Example Transformation
```python
times_ten(3, 6)
# Returns: {3: 30, 4: 40, 5: 50, 6: 60}
```

---

## 💻 Code Implementation

```python
def times_ten(start_index: int, end_index: int):
    numbers = {}
    
    for num in range(start_index, end_index + 1):
        numbers[num] = num * 10
    
    return numbers

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
```

**Output:**
```
{3: 30, 4: 40, 5: 50, 6: 60}
```

---

## 🧠 Algorithm Explanation

### **The Dictionary Building Strategy**
```python
for num in range(start_index, end_index + 1):
    numbers[num] = num * 10
```

**Key Insights:**
- **Range Function**: `range(start_index, end_index + 1)` ensures inclusive bounds
- **Dictionary Assignment**: `numbers[num] = num * 10` creates key-value pairs
- **Direct Mapping**: Each number becomes both the key and the basis for its value

**Step-by-Step Process:**
1. **Initialize**: Create empty dictionary `numbers = {}`
2. **Iterate**: Loop through range from start_index to end_index (inclusive)
3. **Map**: For each number, assign `number * 10` as the value
4. **Return**: Send back the completed dictionary

**Time Complexity:** O(n) - where n is the range size (end_index - start_index + 1)  
**Space Complexity:** O(n) - dictionary stores n key-value pairs

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 times_ten.py
```

Or import the function in your own code:

```python
from times_ten import times_ten

# Create dictionary for range 1-5
result = times_ten(1, 5)
print("Range 1-5:", result)

# Create dictionary for range 10-12
result = times_ten(10, 12)
print("Range 10-12:", result)
```

---

## 🧪 Test Cases

```python
# Test case 1: Small positive range
print("Test 1 - Range 3-6:")
print(times_ten(3, 6))
# Expected: {3: 30, 4: 40, 5: 50, 6: 60}

# Test case 2: Single number range
print("\nTest 2 - Single number:")
print(times_ten(5, 5))
# Expected: {5: 50}

# Test case 3: Starting from 1
print("\nTest 3 - Range 1-4:")
print(times_ten(1, 4))
# Expected: {1: 10, 2: 20, 3: 30, 4: 40}

# Test case 4: Larger range
print("\nTest 4 - Range 8-12:")
print(times_ten(8, 12))
# Expected: {8: 80, 9: 90, 10: 100, 11: 110, 12: 120}

# Test case 5: Starting from 0
print("\nTest 5 - Range 0-3:")
print(times_ten(0, 3))
# Expected: {0: 0, 1: 10, 2: 20, 3: 30}

# Test case 6: Negative numbers
print("\nTest 6 - Range -2 to 2:")
print(times_ten(-2, 2))
# Expected: {-2: -20, -1: -10, 0: 0, 1: 10, 2: 20}
```

---

## ✨ Key Learning Highlights

This problem focuses on **fundamental Python dictionary operations** and demonstrates several important concepts:

### **Dictionary Creation Patterns**
```python
# Method used in solution - Direct assignment
numbers = {}
for num in range(start, end + 1):
    numbers[num] = num * 10
```

### **Range Function Mastery**
- `range(start, end + 1)` creates inclusive bounds
- Understanding why `+ 1` is necessary for inclusive end
- Range works with negative numbers and zero

### **Key-Value Relationship**
- **Keys**: The numbers in the specified range
- **Values**: Each key multiplied by 10
- **Direct mathematical relationship** between key and value

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Simplicity**: Straightforward loop-based dictionary building
2. **Clarity**: Clear relationship between input range and output dictionary
3. **Flexibility**: Works with any integer range (positive, negative, or mixed)
4. **Efficiency**: Single pass through the range creates the complete dictionary

### **Clean Code Principles Applied**
- **Descriptive Names**: `numbers` dictionary and `num` loop variable
- **Single Purpose**: Function does one thing - create the times-ten mapping
- **Clear Logic Flow**: Initialize → Iterate → Assign → Return

---

## 🔄 Problem-Solving Process

### **Initial Understanding**
The problem requires:
1. Taking a range of numbers (inclusive)
2. Creating dictionary keys from these numbers
3. Setting values as keys multiplied by ten

### **Implementation Strategy**
```python
def times_ten(start_index: int, end_index: int):
    numbers = {}  # Start with empty dictionary
    
    for num in range(start_index, end_index + 1):  # Inclusive range
        numbers[num] = num * 10  # Key = num, Value = num * 10
    
    return numbers  # Return completed dictionary
```

### **Key Insight Moments**
- **Inclusive Range**: Remembering to use `end_index + 1` in range()
- **Key-Value Assignment**: Understanding that `numbers[num] = num * 10` creates the mapping
- **Dictionary Initialization**: Starting with empty `{}` to build upon

---

## 🎓 Learning Outcomes

* **Dictionary Operations**: Creating and populating dictionaries programmatically
* **Range Function**: Using range() with inclusive bounds
* **Loop-Based Building**: Constructing data structures through iteration
* **Mathematical Mapping**: Creating relationships between keys and values
* **Function Design**: Writing functions that return new data structures
* **Parameter Usage**: Working with start and end index parameters

---

## 💡 Developer Reflection

> *"I had no trouble with this one other than mixing up the keys and the values but other than that it was smooth sailing."*

### **Learning Insights from the Experience**

**What Went Well:**
- Quick grasp of the overall problem structure
- Understanding of dictionary creation concept
- Smooth implementation once the key-value relationship was clear

**Minor Challenge:**
- **Key-Value Confusion**: Initially mixed up which should be the key and which should be the value
- **Quick Recovery**: Easily corrected once the relationship was clarified

**Key Takeaway:**
Sometimes the simplest problems teach the most fundamental concepts. This exercise reinforced:
- Dictionary syntax and operations
- The importance of clearly understanding problem requirements
- How small mistakes (like key-value confusion) are normal and easily corrected

### **Programming Fundamentals**
This solution demonstrates that valuable learning comes from:
- Mastering fundamental data structures
- Getting comfortable with basic operations
- Building confidence through successful implementations

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
