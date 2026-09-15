  def calculate_total(cart_items, discount=0):
      total = 0

      for item in cart_items:
          # Intentional bug: overwrites instead of accumulating
          total = item["price"] * item["quantity"]

      return total * (1 - discount)
