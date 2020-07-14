function get_value() {
    function check(x) {
        if (isNaN(x)) {
            x = 0
          return x;
        }
        return x;
      }
    var price = document.getElementById("products").value;
    var quantity = document.getElementById("quantity").value;
    var currency = document.getElementById("currency").value;
    document.getElementById("price").value = parseFloat(price) * check(parseFloat(quantity));
    var bonus = parseFloat(price) * check(parseFloat(quantity)) / parseFloat(currency)
    document.getElementById("bonus").value = bonus;

    var cash = document.getElementById("cash").value;
    var plastic = document.getElementById("plastic").value;
    var bonus_point = document.getElementById("bonus_point").value;
    var all = check(parseFloat(cash)) + check(parseFloat(plastic)) + check(parseFloat(bonus_point) * parseFloat(currency) * 0.95238 );
    document.getElementById('total').value = all;

    
    var total_price = document.getElementById('price').value;
    document.getElementById('difference').value = all - check(parseFloat(total_price));

    document.getElementById("suggestion_bonus_point").value = bonus * 1.05;
}
/*
function add_item() {
    document.getElementById("form").innerHTML = document.getElementById("form").innerHTML + '<a href="#" class="btn btn-success">AAA</a>';
}
document.getElementById('add_item').addEventListener('click', add_item);
*/