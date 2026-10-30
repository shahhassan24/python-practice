# # if else

# # age = 8

# # if age <= 18:
# #     print("You are an adult")
# #     print("You can vote")
# # elif age > 12:
# #     print("You are a teenager")
# # else:
# #     print("You are a child")


# # practice problem

# # total = 200
# # city = "Islamabad"

# # if total > 10000:
# #     print("order too much")
# # elif total >= 5000 and city == "Lahore":
# #     print("Free Delivery")
# # elif total >= 5000 or city == "Islamabad":
# #     print("fee is 250")
# # else:
# #     print("Charges are 350")


# # double and or
# orders = [
#     {"id": "A101", "total": 4500, "status": "delivered"},
#     {"id": "A102", "total": 12800, "status": "pending"},
#     {"id": "A103", "total": 2300, "status": "pending"},
# ]

# # pending_count = 0

# # for order in orders:
# #     if order["status"] == "pending":
# #         pending_count += 1
# #         print(f"Pending: {order['id']}")

# # print(f"{pending_count} order(s) pending")


# ## for Loop using range

# # arr = [1, 2, 3, 4, 5]

# # for j in range(5):
# #     print(j, "Ashfaq")


## problem

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]
delievered_revenue = 0

for order in orders:
    if order["status"] == "delivered":
        # delievered_revenue += order["total"]

        delievered_revenue = delievered_revenue + order["total"]
        # print(f"Total delievered revenue: {delievered_revenue}")

print(order["total"])
print(delievered_revenue)
