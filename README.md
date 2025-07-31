### Python Lists

---

### ✅ **Built-in Functions (Used with Lists)**

* `len()` – Get the number of elements
* `max()` – Get the largest element
* `min()` – Get the smallest element
* `sum()` – Get the sum of all elements (only numeric lists)
* `sorted()` – Return a new sorted list
* `type()` – Return the type of the object
* `list()` – Convert iterable to a list

---

### ✅ **List Methods**

* `append(x)` – Add item to the end
* `insert(i, x)` – Insert item at index `i`
* `extend(iterable)` – Add multiple items
* `remove(x)` – Remove first occurrence of `x`
* `pop([i])` – Remove and return item at index `i` (or last)
* `clear()` – Remove all items from the list
* `index(x)` – Return index of first occurrence of `x`
* `count(x)` – Count how many times `x` appears
* `sort()` – Sort the list (in-place)
* `reverse()` – Reverse the list (in-place)
* `copy()` – Return a shallow copy of the list

---


### 🆚 `sorted()` vs `sort()`

| Feature           | `sorted()`                       | `sort()`                    |
| ----------------- | -------------------------------- | --------------------------- |
| **Type**          | Built-in **function**            | **Method** of list objects  |
| **Returns**       | A **new sorted list**            | Sorts the list **in-place** |
| **Original List** | Unchanged                        | Modified                    |
| **Works on**      | Any iterable (list, tuple, etc.) | Only on lists               |
| **Chainable**     | ✅ Yes (returns a value)          | ❌ No (returns `None`)       |

---

### ✅ Example Comparison:

```python
# sorted()
nums = [3, 1, 2]
sorted_nums = sorted(nums)
print(nums)        # [3, 1, 2]
print(sorted_nums) # [1, 2, 3]

# sort()
nums.sort()
print(nums)        # [1, 2, 3]
```

---

### 📌 Use When:

* Use **`sorted()`** when:

  * You don’t want to modify the original list
  * You’re sorting something that isn’t a list (e.g. a tuple or string)

* Use **`sort()`** when:

  * You’re okay with changing the original list
  * You want slightly better performance (since it doesn't create a copy)

---

