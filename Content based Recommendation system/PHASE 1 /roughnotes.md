




Today 10:48 AM
explain me what is the error

yes now tell me

 solve the error 

now give me 

the already work but when i run the notebook from first code so this is coming

eyError                                  Traceback (most recent call last)
Cell In[62], line 1
----> 1 movies = movies['crew'].apply(fetch_director)

File /lib/python3.14/site-packages/pandas/core/series.py:959, in Series.__getitem__(self, key)
    954     key = unpack_1tuple(key)
    956 elif key_is_scalar:
    957     # Note: GH#50617 in 3.0 we changed int key to always be treated as
    958     #  a label, matching DataFrame behavior.
--> 959     return self._get_value(key)
    961 # Convert generator to list before going through hashable part
    962 # (We will iterate through the generator there to check for slices)
    963 if is_iterator(key):

File /lib/python3.14/site-packages/pandas/core/series.py:1046, in Series._get_value(self, label, takeable)
   1043     return self._values[label]
   1045 # Similar to Index.get_value, but we do not fall back to positional
-> 1046 loc = self.index.get_loc(label)
   1048 if is_integer(loc):
   1049     return self._values[loc]

File /lib/python3.14/site-packages/pandas/core/indexes/base.py:3648, in Index.get_loc(self, key)
   3643     if isinstance(casted_key, slice) or (
   3644         isinstance(casted_key, abc.Iterable)
   3645         and any(isinstance(x, slice) for x in casted_key)
   3646     ):
   3647         raise InvalidIndexError(key) from err
-> 3648     raise KeyError(key) from err
   3649 except TypeError:
   3650     # If we have a listlike key, _check_indexing_error will raise
   3651     #  InvalidIndexError. Otherwise we fall through and re-raise
   3652     #  the TypeError.
   3653     self._check_indexing_error(key)

KeyError: 'crew'

yError                                  Traceback (most recent call last)
Cell In[91], line 1
----> 1 movies = movies['cast'].apply(convert3)

File /lib/python3.14/site-packages/pandas/core/series.py:959, in Series.__getitem__(self, key)
    954     key = unpack_1tuple(key)
    956 elif key_is_scalar:
    957     # Note: GH#50617 in 3.0 we changed int key to always be treated as
    958     #  a label, matching DataFrame behavior.
--> 959     return self._get_value(key)
    961 # Convert generator to list before going through hashable part
    962 # (We will iterate through the generator there to check for slices)
    963 if is_iterator(key):

File /lib/python3.14/site-packages/pandas/core/series.py:1046, in Series._get_value(self, label, takeable)
   1043     return self._values[label]
   1045 # Similar to Index.get_value, but we do not fall back to positional
-> 1046 loc = self.index.get_loc(label)
   1048 if is_integer(loc):
   1049     return self._values[loc]

File /lib/python3.14/site-packages/pandas/core/indexes/base.py:3648, in Index.get_loc(self, key)
   3643     if isinstance(casted_key, slice) or (
   3644         isinstance(casted_key, abc.Iterable)
   3645         and any(isinstance(x, slice) for x in casted_key)
   3646     ):
   3647         raise InvalidIndexError(key) from err
-> 3648     raise KeyError(key) from err
   3649 except TypeError:
   3650     # If we have a listlike key, _check_indexing_error will raise
   3651     #  InvalidIndexError. Otherwise we fall through and re-raise
   3652     #  the TypeError.
   3653     self._check_indexing_error(key)

KeyError: 'cast'?


it is working and this happen now

The error tells us exactly what's wrong.

AttributeError: 'list' object has no attribute 'lower'
What does this mean?
Python is trying to do this:

['Action', 'Adventure', 'Fantasy'].lower()
But lower() only works on strings, not on lists.

Step 1: Check your data type
Run this:

type(new_df['tags'].iloc[0])
You'll most likely get:

<class 'list'>
For example, your first row probably looks like:

new_df['tags'].iloc[0]
Output:

['Action', 'Adventure', 'Fantasy', 'future', 'alien']
Since it's a list, .lower() cannot be used.

Step 2: Convert the list into a string
Run:

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
Now check again:

type(new_df['tags'].iloc[0])
Output:

<class 'str'>
Now one row looks like:

"Action Adventure Fantasy future alien"
Step 3: Convert to lowercase
Now this will work:

new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())
Output:

"action adventure fantasy future alien"
Why did this happen?
Your preprocessing pipeline should be:

Original data
        │
        ▼
overview.split()
        │
        ▼
['A', 'marine', 'alien']          ← list
        │
        ▼
Combine with genres, cast, crew
        │
        ▼
['A','marine','Action','Adventure']  ← list
        │
        ▼
" ".join(x)
        │
        ▼
"A marine Action Adventure"       ← string
        │
        ▼
.lower()
        │
        ▼
"a marine action adventure"
You are trying to do:

list
 │
 ▼
.lower()   ❌
instead of:

list
 │
 ▼
join()
 │
 ▼
string
 │
 ▼
lower()   ✅
One thing to verify
Please run these two commands and paste their output:

type(new_df['tags'].iloc[0])
and

new_df['tags'].iloc[0]
This will tell us exactly what is inside your tags column, and we can identify why it is still a list instead of a string.


Screenshot 2026-07-21 at 3.18.41 PM.png
it is still showing me the list i had convert into the string

Stopped thinking
I can see the screenshot. The important clue is this:

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
Then you displayed:

new_df.head(1)
and the tags column looks like:

[In, the, 22nd, century,, a, paraplegic, Marin...]
At first glance that looks like a list, but in a Pandas DataFrame display it can be misleading. Let's verify the actual data type.

Step 1: Check the type
Run these two lines:

print(type(new_df['tags'].iloc[0]))
print(new_df['tags'].iloc[0])
If you get
<class 'str'>
then your join() worked correctly.

The output might be:

In the 22nd century a paraplegic Marine ...
If you get
<class 'list'>
then the assignment didn't actually change the column.

Step 2: Check if you're looking at the correct DataFrame
Run:

print(type(movies['tags'].iloc[0]))
print(type(new_df['tags'].iloc[0]))
Sometimes people accidentally modify movies and inspect new_df, or vice versa.

Step 3: Check whether the assignment really happened
Run:

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

print(type(new_df['tags'].iloc[0]))
print(new_df['tags'].iloc[0])
I suspect one more thing
From your screenshot, the displayed value starts with:

[In, the, 22nd, century,, a, paraplegic...
Normally, after join(), it should look like:

In the 22nd century a paraplegic Marine...
without the square brackets.

So I'd like to see the exact value.

Please run these three commands and paste the output:
print(type(new_df['tags'].iloc[0]))
print(repr(new_df['tags'].iloc[0]))
print(new_df['tags'].iloc[0])
The repr() output is especially useful because it will tell us whether the value is:

a Python list,

a Python string, or

something else.

Once you paste those three outputs, I'll be able to tell you the exact cause in one step.


just tell me i have run the exact code to convert list into string then why it is not converting

The most likely reason is not that join() failed. It's that Jupyter notebooks don't automatically refresh outputs from previous cells.

Here are the most common possibilities:

1. You are looking at an old output (most likely)
You ran:

new_df.head(1)
before converting the column. That output stays on the screen even after you run other cells.

Run this again after the join() line:

new_df.head(1)
2. new_df['tags'] is already a string
Sometimes Pandas displays long strings in a way that looks like a list because the text starts with [ or is truncated.

Check with:

type(new_df['tags'].iloc[0])
This is the only reliable way to know.

3. You overwrote new_df later
If you ran something like:

new_df = movies[['movie_id', 'title', 'tags']]
again after the join(), then new_df got recreated from movies, losing the changes.

4. You are modifying one DataFrame and viewing another
For example:

movies['tags'] = ...
but displaying:

new_df.head()
or vice versa.

Since you're following the TMDB recommendation tutorial, the correct order is:
new_df = movies[['movie_id', 'title', 'tags']]

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

new_df.head()
If it is still not working
Then there is only one explanation:

Some earlier cell recreated new_df or tags after you converted it.

Jupyter notebooks execute cells independently, so if you run cells out of order, variables can easily be overwritten.

To find the exact cause, I need only one thing:
Please share the 5–10 cells before this one (or the notebook from where you create tags until lower()). I can then point to the exact line that's resetting your data.



# 🎬 **Movie Recommendation System**  
**End-to-End Detailed Notes**  
*Content-Based Recommendation System using Python & Pandas*

---

## 📊 **Dataflow Diagram**
Data → Preprocessing → Model
↓
Website
↑
Deploy
text**Approach:**
- `movies.csv` | `title` | `tag` | `overview` | `cast` | `crew` | `genres`

---

## 🛠️ **Step 1: Merging Two DataFrames**

```python
movies = movies.merge(credits, on='title')
# Check shape
movies = movies.merge(credits, on='title').shape
movies.head()

🔍 Step 2: Selecting Particular Columns
Pythonmovies = movies[['genres', 'title', 'movie_id', 'cast', 'crew']]

🧹 Step 3: Handling Missing & Duplicate Data
Python# Check missing data
movies.isnull().sum()

# Remove missing data
movies.dropna(inplace=True)

# Check duplicate data
movies.duplicated().sum()

# Remove duplicate data
movies.drop_duplicates()

📍 Step 4: Selecting Special Row & Columns by Index
Pythonmovies.loc[0].genres

🔄 Step 5: Converting List of Dictionaries into List
Example Input:
Python# [{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}]
Desired Output:
Python["Action", "Adventure", "SciFi"]
Helper Function:
Pythonimport ast

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
Apply to DataFrame:
Pythonmovies['genres'] = movies['genres'].apply(convert)

🎭 Step 6: Applying Convert to Keywords & Cast
Pythonmovies['keywords'] = movies['keywords'].apply(convert)

# For Cast - Only Top 3
def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L

movies['cast'] = movies['cast'].apply(convert3)

🧼 Step 7: Cleaning Overview Column
Python# Split into list of words
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Example
text = "I love python"
text.split()  # → ['I', 'love', 'python']

✨ Step 8: Removing Spaces (Important for Vectorization)
Python# Remove spaces from genres, keywords, cast, crew
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])
Why? Spaces can confuse the machine learning model.

🔗 Step 9: Consolidating Columns
Python# Create tags by combining
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

🔗 Step 10: Converting List Back to String
Python# Join list into single string
new_df = movies[['movie_id', 'title', 'tags']]

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
Example of join():
Pythonwords = ['I', 'love', 'Python']
" ".join(words)  # → "I love Python"

🚀 Next Steps (Not in PDF but Logical Continuation)

Vectorization using CountVectorizer or TF-IDF
Cosine Similarity for recommendations
Deploy as Streamlit/Flask web app


🎉 Notes Compiled Faithfully from Provided PDF
No content changed — only organized into clean, eye-catching Markdown with code blocks, diagrams, and highlights.
Tip: Copy this into a .md file or use Obsidian/Typora for best viewing with themes!
text---

**📁 To save as Markdown file:**  
Copy the entire content above into a new file named `movie_recommendation_notes.md` 

**For Graphics/Animations (in supported viewers like Obsidian or GitHub):**
- Use emoji for visual appeal ✨
- Code blocks for readability
- Headings for structure

Let me know if you want a **PDF version**, **PowerPoint**, or **enhanced version with images**! 🎥