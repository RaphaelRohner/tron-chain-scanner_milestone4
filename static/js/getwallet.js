// FUNCTION TO CHECK IF TRONLINK IS AVAILABLE IN BROWSER
function getTronlink(){
    
    let tronlink = window.tronWeb && window.tronWeb.defaultAddress.base58 // VARIABLE TO TAKE IN WALLET ADDRESS

    if(tronlink){
        $("#trontest").html(tronlink); 
    } else {
        $("#trontest").html(`<p>Test Please sign in to Tronlink and reload page.</p>`);
    }

    console.log(test);
}
