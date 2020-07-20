function get_value() {
    function check(x) {
        if (isNaN(x)) {
            x = 0
          return x;
        }
        return x;
      }
    var price = document.getElementById("products").value;
    real_price = price.split("|")
    price = real_price[1]
    
    var quantity = document.getElementById("quantity").value;
    var currency = document.getElementById("currency").value;
    document.getElementById("price").value = parseFloat(price) * check(parseFloat(quantity));
    var bonus = parseFloat(price) * check(parseFloat(quantity)) / parseFloat(currency)
    document.getElementById("bonus").value = bonus;

    var cash = document.getElementById("cash").value;
    var plastic = document.getElementById("plastic").value;
    var bonus_point = document.getElementById("bonus_point").value;
    var all = check(parseFloat(cash)) + check(parseFloat(plastic)) + check(parseFloat(bonus_point) * parseFloat(currency) * 0.95238 );
    document.getElementById('total').value = Math.round((all + Number.EPSILON) * 100) / 100;

    
    var total_price = document.getElementById('price').value;
    document.getElementById('difference').value = Math.round(((all - check(parseFloat(total_price))) + Number.EPSILON) * 100) / 100;

    document.getElementById("suggestion_bonus_point").value = Math.round(((bonus - check(parseFloat(cash))/parseFloat(currency) - check(parseFloat(plastic))/parseFloat(currency)) * 1.05 + Number.EPSILON) * 100) / 100;
}
/*
function add_item() {
    document.getElementById("form").innerHTML = document.getElementById("form").innerHTML + '<a href="#" class="btn btn-success">AAA</a>';
}
document.getElementById('add_item').addEventListener('click', add_item);
*/