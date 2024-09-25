

var updateBtns = document.querySelectorAll("#update-cart");

updateBtns.forEach(function(btn) {
    btn.addEventListener("click", function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;
        const data = {
            product_id: productId,
            action: action,
        };
        if (user === 'AnonymousUser') {
            addCookieItem(productId, action);
        } else {
            updateCart(data);
            console.log(action, productId);
        }
    });
});

function addCookieItem(productId, action) {
    if (action === 'add') {
        if (cart[productId] == null) {
            cart[productId] = { 'quantity': 1 };
        } else {
            cart[productId]['quantity'] += 1;
        }
    }

    if (action === 'remove') {
        cart[productId]['quantity'] -= 1;
        if (cart[productId]['quantity'] <= 0) {
            delete cart[productId];
        }
    }

    if (action === 'delete') {
            delete cart[productId];
        }

    document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
    location.reload();

    console.log('Updated cart:', cart);
}

function updateCart(data) {
    fetch("/updateCart/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            console.log(data);
            location.reload();
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}

// Add event listener for quantity input change on enter or blur
var quantityInputs = document.querySelectorAll(".quantity-input");
quantityInputs.forEach(function(input) {
    input.addEventListener("keypress", function(event) {
        if (event.key === 'Enter') {
            updateQuantityInput(this);
        }
    });

    input.addEventListener("blur", function() {
        updateQuantityInput(this);
    });
});

function updateQuantityInput(input) {
    const productId = input.dataset.product;
    let quantity = parseInt(input.value);

    // Error check for empty or invalid quantity
    if (isNaN(quantity) || quantity <= 0) {
        quantity = 1;
        input.value = quantity;
    }

    const data = {
        product_id: productId,
        quantity: quantity
    };

    if (user === 'AnonymousUser') {
        updateCookieItem(productId, quantity);
    } else {
        updateQuantity(data);
        console.log('update', productId, quantity);
    }
}

function updateQuantity(data) {
    fetch("/update_quantity/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            console.log(data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}

function updateCookieItem(productId, quantity) {
    if (cart[productId] == null) {
        cart[productId] = { 'quantity': quantity };
    } else {
        cart[productId]['quantity'] = quantity;
    }

    document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
    location.reload();

    console.log('Updated cart:', cart);
}

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "100%";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "gray";
}

function showPayment() {
    var pay_section = document.getElementById("pay-section");
    if (pay_section.className === "pay-section") {
        pay_section.className += " active";
    }
}

var eL = document.querySelectorAll(".product");
for (var i = 0; i <= eL.length; i++) {
    if (i >= 5) {
        eL[i].classList.add('reveal');
    } else {
        eL[i].classList.remove('reveal');
    }
}

var newsForm = document.getElementById('nwsletter');
newsForm.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log('email save');
});
