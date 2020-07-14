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
    document.getElementById("bonus").value = parseFloat(price) * check(parseFloat(quantity)) / parseFloat(currency);
}

function add_item() {
    document.getElementById("form").innerHTML = document.getElementById("form").innerHTML + '<a href="#" class="btn btn-success">AAA</a>';
}
document.getElementById('add_item').addEventListener('click', add_item);

// Get Total


function get_total() {
    function check(x) {
        if (isNaN(x)) {
            x = 0
          return x;
        }
        return x;
      }
    
    var cash = document.getElementById("cash").value;
    var plastic = document.getElementById("plastic").value;
    var bonus = document.getElementById("bonus_point").value;
    var currency = document.getElementById("currency").value;

    document.getElementById('total').value = check(parseFloat(cash)) + check(parseFloat(plastic)) + check(parseFloat(bonus) * parseFloat(currency) * 0.95 );
}
