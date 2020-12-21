// FUNCTION TO CHECK IF TRONLINK IS AVAILABLE IN BROWSER
function getTronlink(){
    
    let tronlink = window.tronWeb && window.tronWeb.defaultAddress.base58 // VARIABLE TO TAKE IN WALLET ADDRESS

    if(tronlink){
        $("#trontest").html(tronlink); 
    } else {
        $("#trontest").html(`<p>Please sign in to Tronlink and reload page.</p>`);
    }
}

// FUNCTION TO SUBMIT A PAYMENT USING GOOGLE CHROME TRONLINK EXTENSION
// FROM: https://developers.tron.network/docs/tronlink-integration
function payment(){    
    var obj = setInterval(async ()=>{
        if (window.tronWeb && window.tronWeb.defaultAddress.base58) {
            clearInterval(obj)
            var tronweb = window.tronWeb
            var wallet = window.tronWeb && window.tronWeb.defaultAddress.base58
            // sendTrx(to, amount sun, from, options)
            var tx = await tronweb.transactionBuilder.sendTrx('TWFEaFsLiC7EDfgCqjnZKx8gbfNiZftPwT', 10000000, wallet)
            var signedTx = await tronweb.trx.sign(tx)
            var broastTx = await tronweb.trx.sendRawTransaction(signedTx)
            console.log(broastTx)
        }
    }, 10)
}