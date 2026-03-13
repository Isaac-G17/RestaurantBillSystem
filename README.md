# 🍽️RestaurantBillSystem
A Python program that calculates a restaurant bill based on the dish price, drink price, and quantity ordered. The program computes the subtotal, applies tax, and prints an invoice.

---

## 📌 Features

 - ✅ Calculates the subtotal of the order.
 - ✅ Applies a 10% tax to the subtotal.
 - ✅ Generates a simple restaurant invoice.
 - ✅ Uses functions to organize the logic.

---

## ⚙️ Technologies Used

- 🐍Python 3

---

## 📦 Installation (Local)

### 1️⃣ Clone this repository

```bash
git clone https://github.com/Isaac-G17/RestaurantBillSystem.git
```

### 2️⃣ Open the project folder

```bash
cd RestaurantBillSystem
```

### 3️⃣ Run the program

```bash
python3 main.py
```

---

## ⚠️ Requisitos

To run this program, you need to have Python 3 installed on your computer.

You can download it from the official website:

[Download Python](https://www.python.org/downloads/) 

---

## 🧠 Program logic

The program follows a simple sequence of steps to generate the restaurant bill:

1. **User Input**
- The program asks the user to enter:
    - Dish name
    - Dish price
    - Drink name
    - Drink price
    - Quantity of orders

2. **Calculate Subtotal**
- The function `calculate_consumption()` calculates the subtotal using the formula:
    
    ```python
    subtotal = (dish_price + drink_price) * quantity
    ```
3. **Apply Tax**
- The function `apply_tax()` calculates a **10% tax** on the subtotal:
    
    ```python
    tax = subtotal * 0.10
    total = subtotal + tax
    ```

4. **Generate Invoice**
- The function `print_invoice()` prints the restaurant bill showing:
    - Dish
    - Drink
    - Quantity
    - Subtotal
    - Tax
    - Total amount to pay

5. **Final Output**
- The program displays a formatted invoice with the final amount the customer needs to pay.

---

## 🖥️ Example Execution

```
Enter dish name: Burger
Enter dish price $10
Enter drink name: Soda
Enter drink price $3
Enter quantity: 2

----Restaurant Bill----
Dish: Burger
Drink: Soda
Quantity: 2
Subtotal: $ 26
Tax: $ 2.6
Total: $ 28.6
-----------------------
```
---

## 📂 Project Structure

```
RestaurantBillSystem
│
├── restaurant_bill.py
└── README.md
``` 

---

## 👨‍💻 Autor

This project was created by **[Isaac Guzmán Mora](https://github.com/Isaac-G17)**.
