# Regex Searches on JSONB Columns

## PostgreSQL: Basic Regex on a JSONB Key

Extract the value with `->>`  then apply the `~` operator:

```sql
-- Case-sensitive
SELECT * FROM table WHERE data->>'key' ~ 'pattern';

-- Case-insensitive
SELECT * FROM table WHERE data->>'key' ~* 'pattern';
```

Using `jsonb_path_exists` with `like_regex` (PostgreSQL 12+):

```sql
SELECT * FROM table WHERE jsonb_path_exists(data, '$.key like_regex "pattern"');

-- Case-insensitive flag
SELECT * FROM table WHERE jsonb_path_exists(data, '$.key like_regex "pattern" flag "i"');
```

---

## Django ORM Equivalents

```python
# Case-sensitive regex
MyModel.objects.filter(data__key__regex=r'pattern')

# Case-insensitive regex
MyModel.objects.filter(data__key__iregex=r'pattern')

# Nested keys
MyModel.objects.filter(data__nested__key__iregex=r'pattern')
```

Using `jsonb_path_exists` via `RawSQL`:

```python
from django.db.models.expressions import RawSQL

MyModel.objects.filter(
    RawSQL("jsonb_path_exists(data, '$.key like_regex %s')", ('pattern',))
)
```

---

## Functional Indexes for Regex Performance

Define in `Meta.indexes` to speed up queries on extracted JSONB values:

```python
from django.db import models
from django.db.models.expressions import RawSQL

class MyModel(models.Model):
    data = models.JSONField()

    class Meta:
        indexes = [
            models.Index(
                RawSQL("((data->>'key'))", []),
                name='idx_mymodel_data_key',
            ),
        ]
```

The double parentheses `((data->>'key'))` are required by PostgreSQL to mark it as an expression index.

> **Note:** `__regex` on a JSONB path won't use a GIN index. A functional index on the extracted text value is needed for performance.

---

## Matching Against JSONB Array Values

**Exact match on any array element:**

```python
MyModel.objects.filter(data__key__contains=['value'])
```

**Regex on any array element using `jsonb_path_exists`:**

```python
MyModel.objects.filter(
    RawSQL(
        "jsonb_path_exists(data, '$.key[*] like_regex %s')",
        ('pattern',)
    )
)
```

**Nested array of objects:**

```python
MyModel.objects.filter(
    RawSQL(
        "jsonb_path_exists(data, '$.items[*].name like_regex %s')",
        ('pattern',)
    )
)
```

**Case-insensitive:**

```python
"jsonb_path_exists(data, '$.key[*] like_regex %s flag \"i\"')"
```

> `__contains` is index-friendly (GIN) but exact-match only. `jsonb_path_exists` supports regex but won't use an index efficiently on large tables.

---

## Matching User Input Against a Stored Regex Pattern

Use case: a user enters a code (e.g. `J1234`) and records store a regex pattern in a JSONB field (e.g. `{"code": "J\\d\\d\\d\\d"}`). Find the record whose stored pattern matches the input.

The `~` operator works with the pattern on either side:

```sql
-- user input on left, stored pattern on right
SELECT * FROM project WHERE 'J1234' ~ (data->>'code');
```

**In Django:**

```python
from django.db.models.expressions import RawSQL

user_code = 'J1234'

# Case-sensitive
Project.objects.filter(
    RawSQL("%s ~ (data->>'code')", [user_code])
)

# Case-insensitive
Project.objects.filter(
    RawSQL("%s ~* (data->>'code')", [user_code])
)
```

Passing `user_code` as a parameterised value (not string-interpolated) prevents SQL injection.

> **Warning:** If users can write the stored patterns, validate them before saving — an invalid regex will raise a PostgreSQL error at query time.
