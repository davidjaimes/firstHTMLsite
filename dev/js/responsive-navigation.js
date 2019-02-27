function myFunction() {
                var x = document.getElementById("topnav");
                if (x.className === "header") {
                    x.className += " responsive";
                } else {
                    x.className = "header";
                }
                var y = document.getElementById("ptext");
                if (y.innerHTML === 'Menu <i class="fas fa-ellipsis-v"></i>') {
                    y.innerHTML = 'Close <i class="fas fa-times"></i>'
                } else {
                    y.innerHTML = 'Menu <i class="fas fa-ellipsis-v"></i>'
                }
            }