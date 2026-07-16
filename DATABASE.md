# Database Design — SPX Cafe

This document describes the full database that supports the application, covering **both** components:

- **Menu component** — `menus`, `courses`, `meals` *(already built)*
- **Customer & Orders component** — `customers`, `orders`, `orderItems` *(to be added)*

It doubles as the **Database Schema & Data Dictionary** deliverable for the portfolio.

---

## 1. Schema Overview (Entity Relationships)

```
menus (1) ────< (many) courses (1) ────< (many) meals
                                                   │
                                                   │ referenced by
                                                   ▼
customers (1) ────< (many) orders (1) ────< (many) orderItems
```

**How to read the relationships:**

- One **menu** has many **courses**; one **course** has many **meals**.
- One **customer** places many **orders**; one **order** contains many **orderItems** (the individual dishes on that order).
- Each **orderItem** points back to the **meal** that was ordered.

---

## 2. Data Dictionary

### Existing tables (Menu component)

#### `menus`
| Field | Type | Key | Rules | Description |
|---|---|---|---|---|
| menuId | INTEGER | PK | Auto-increment | Unique menu identifier |
| menuName | TEXT(20) | | NOT NULL | e.g. Breakfast, Lunch, Dinner |

#### `courses`
| Field | Type | Key | Rules | Description |
|---|---|---|---|---|
| courseId | INTEGER | PK | Auto-increment | Unique course identifier |
| courseName | TEXT(20) | | NOT NULL | e.g. Entree, Main, Dessert |
| menuId | INTEGER | FK → menus | NOT NULL | The menu this course belongs to |

#### `meals`
| Field | Type | Key | Rules | Description |
|---|---|---|---|---|
| mealId | INTEGER | PK | Auto-increment | Unique meal identifier |
| mealName | TEXT(20) | | NOT NULL | e.g. soup, pizza, cake |
| mealPrice | REAL(6,2) | | NOT NULL, default 0 | Current price of the dish |
| courseId | INTEGER | FK → courses | NOT NULL | The course this meal belongs to |

### New tables (Customer & Orders component)

#### `customers`
| Field | Type | Key | Rules | Description |
|---|---|---|---|---|
| username | TEXT | PK | NOT NULL, unique | The customer's login name |
| password | TEXT | | NOT NULL | The customer's password |
| firstName | TEXT | | NOT NULL | Typed in to preserve spelling |
| lastName | TEXT | | NOT NULL | Typed in to preserve spelling |

> **Why username is the primary key:** the task says orders are stored *"for a particular customer username"*, so username is the natural unique identifier customers log in with.

#### `orders`
| Field | Type | Key | Rules | Description |
|---|---|---|---|---|
| orderId | INTEGER | PK | Auto-increment | Unique order identifier (the "order number") |
| username | TEXT | FK → customers | NOT NULL | Which customer placed the order |
| orderDate | TEXT | | NOT NULL | Date/time the order was placed |
| total | REAL(8,2) | | NOT NULL, default 0 | Total cost of the whole order |

#### `orderItems`
| Field | Type | Key | Rules | Description |
|---|---|---|---|---|
| orderItemId | INTEGER | PK | Auto-increment | Unique line-item identifier |
| orderId | INTEGER | FK → orders | NOT NULL | Which order this line belongs to |
| mealId | INTEGER | FK → meals | NOT NULL | Which meal was ordered |
| quantity | INTEGER | | NOT NULL, default 1 | Number of servings |
| priceAtTime | REAL(6,2) | | NOT NULL | Price of the meal **when ordered** |

> **Why `priceAtTime` exists:** the task requires showing *"the Meals ordered and their prices at that point in time"*. If we relied on `meals.mealPrice`, changing a price later would rewrite old receipts. Copying the price into the order line "freezes" it, so history stays accurate.

---

## 3. SQL to Create the New Tables

Run these once to add the Customer & Orders tables (the menu tables already exist):

```sql
CREATE TABLE customers (
    username  TEXT PRIMARY KEY NOT NULL,
    password  TEXT NOT NULL,
    firstName TEXT NOT NULL,
    lastName  TEXT NOT NULL
);

CREATE TABLE orders (
    orderId   INTEGER PRIMARY KEY AUTOINCREMENT,
    username  TEXT NOT NULL,
    orderDate TEXT NOT NULL,
    total     REAL (8, 2) NOT NULL DEFAULT (0),
    FOREIGN KEY (username) REFERENCES customers (username)
        ON DELETE RESTRICT ON UPDATE RESTRICT
);

CREATE TABLE orderItems (
    orderItemId INTEGER PRIMARY KEY AUTOINCREMENT,
    orderId     INTEGER NOT NULL,
    mealId      INTEGER NOT NULL,
    quantity    INTEGER NOT NULL DEFAULT (1),
    priceAtTime REAL (6, 2) NOT NULL,
    FOREIGN KEY (orderId) REFERENCES orders (orderId)
        ON DELETE RESTRICT ON UPDATE RESTRICT,
    FOREIGN KEY (mealId) REFERENCES meals (mealId)
        ON DELETE RESTRICT ON UPDATE RESTRICT
);
```

---

## 4. Sample Data (values to populate)

### Menu data (already in the database)

```sql
-- menus
INSERT INTO menus (menuName) VALUES ('Breakfast'), ('Lunch'), ('Dinner');

-- courses (menuId 3 = Dinner)
INSERT INTO courses (courseName, menuId) VALUES
    ('Entree', 3), ('Main', 3), ('Dessert', 3),
    ('Breakfast', 1), ('Lunch Specials', 2);

-- meals
INSERT INTO meals (mealName, mealPrice, courseId) VALUES
    ('soup', 5.00, 1), ('bread', 2.00, 1),
    ('pizza', 17.00, 2), ('steak', 30.00, 2),
    ('cake', 7.00, 3), ('ice cream', 7.00, 3);
```

> **Note:** the Breakfast and Lunch menus currently have courses but **no meals**. You should add meals to those so every menu shows dishes (see suggested extra data below).

### Suggested extra menu data (to fill the empty courses)

```sql
INSERT INTO meals (mealName, mealPrice, courseId) VALUES
    ('pancakes', 9.00, 4), ('omelette', 11.00, 4),   -- Breakfast course
    ('burger', 14.00, 5), ('salad', 10.00, 5);       -- Lunch Specials course
```

### Sample customers (for testing login)

```sql
INSERT INTO customers (username, password, firstName, lastName) VALUES
    ('jsmith', 'pass123', 'John',  'Smith'),
    ('agarcia', 'hello99', 'Ana',  'Garcia');
```

### Sample order (shows how the three tables link)

```sql
-- 1. The order header (total = 17 + 30 + 2*5 = 57.00)
INSERT INTO orders (username, orderDate, total)
    VALUES ('jsmith', '2026-07-16', 57.00);

-- 2. The dishes on that order (orderId 1), with prices frozen at order time
INSERT INTO orderItems (orderId, mealId, quantity, priceAtTime) VALUES
    (1, 3, 1, 17.00),   -- 1 x pizza  @ 17.00
    (1, 4, 1, 30.00),   -- 1 x steak  @ 30.00
    (1, 1, 2, 5.00);    -- 2 x soup   @ 5.00 each
```

> This demonstrates the **minimum 3 different dishes** rule from the task: the order has three distinct meals (pizza, steak, soup).

---

## 5. How this maps to the requirements

| Requirement | Satisfied by |
|---|---|
| Identify customer (username/password/name) | `customers` table |
| Store orders per customer with order numbers & date | `orders` table (`orderId`, `username`, `orderDate`) |
| Record dishes, quantities and prices at time of order | `orderItems` (`mealId`, `quantity`, `priceAtTime`) |
| Total order value | `orders.total` |
| Menus / courses / meals with prices | `menus`, `courses`, `meals` |
| Persist across sessions | All data stored in `SPXCafeDB.db` (SQLite) |
