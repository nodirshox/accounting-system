function get_value() {
  // check number: if can't get, then return 0
  function check(x) {
    if (isNaN(x)) { x = 0; return x; }
    return x;
  }
  // Product price
  var product_info = document.getElementById("product_info").value;
  product_price = product_info.split("|")
  price = product_price[1]

  // Quantity
  var quantity = document.getElementById("quantity").value;

  // Calculate product price: => product price = item price * quantity 
  var total_product_price = parseFloat(price) * check(parseFloat(quantity))
  document.getElementById("price").value = total_product_price;

  // Calculate product price in currency: => price in currency =  total price / currency
  var currency = document.getElementById("currency").value;
  var price_in_currency = total_product_price / parseFloat(currency)
  document.getElementById("price_in_currency").value = price_in_currency;

  // Get cash, plastic, bonus values
  var cash = document.getElementById("cash").value;
  var plastic = document.getElementById("plastic").value;
  var bonus = document.getElementById("bonus").value;

  // Calculate total paid money
  var total_money = check(parseFloat(cash)) + check(parseFloat(plastic)) + check(parseFloat(bonus) * parseFloat(currency) * 0.95238 );
  document.getElementById('total_money').value = Math.round((total_money + Number.EPSILON) * 100) / 100;

  // Calculate difference which is should be added
  var difference = Math.round(((total_money - check(parseFloat(total_product_price))) + Number.EPSILON) * 100) / 100;
  document.getElementById('difference').value = difference;

  // Calculate suggestion point
  suggestion = Math.round(((price_in_currency - check(parseFloat(cash))/parseFloat(currency) - check(parseFloat(plastic))/parseFloat(currency)) * 1.05 + Number.EPSILON) * 100) / 100;
  document.getElementById("suggestion_bonus_point").value = suggestion
}